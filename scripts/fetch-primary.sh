#!/usr/bin/env bash
# Fetch the ORIGINAL facsimiles and labelled full-text transcriptions in sources/downloads.tsv.
# Requires bash, curl, sha256sum. Files stay local under papers/; modern books are excluded.
set -euo pipefail

usage() {
  printf 'Usage: %s [core|all]\n' "$0" >&2
  printf 'core includes Leibniz 1691 original volume (~87 MB); all includes large additional scans.\n' >&2
  exit 2
}
mode="${1:-core}"
[[ $# -le 1 ]] || usage
[[ "$mode" == core || "$mode" == all ]] || usage

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_list="$repo_root/sources/downloads.tsv"
output_dir="$repo_root/papers"
mkdir -p "$output_dir"

while IFS=$'\t' read -r tier filename url edition; do
  [[ -n "$tier" && "$tier" != \#* ]] || continue
  [[ "$tier" == core || "$tier" == all ]] || { echo "Invalid tier: $tier" >&2; exit 1; }
  [[ "$mode" == all || "$tier" == core ]] || continue
  [[ "$filename" =~ ^[A-Za-z0-9._-]+[.]pdf$ ]] || { echo "Unsafe filename: $filename" >&2; exit 1; }
  [[ "$url" == https://* ]] || { echo "Unsupported URL: $url" >&2; exit 1; }
  case "$edition" in
    original-facsimile|modern-transcription|critical-edition|historical-English-translation|author-article-based-on-2018-colloquium) ;;
    *) echo "Unknown edition type: $edition" >&2; exit 1 ;;
  esac

  target="$output_dir/$filename"
  if [[ -f "$target" && "$(head -c 5 "$target")" == '%PDF-' ]]; then
    printf 'Existing PDF: %s\n' "$filename"
  else
    part="$target.part"
    rm -f -- "$part"
    printf 'Fetching [%s] %s\n' "$edition" "$filename"
    curl --fail --location --silent --show-error --retry 3 --retry-delay 2 --connect-timeout 30 --max-time 900 --output "$part" "$url"
    if [[ "$(head -c 5 "$part")" != '%PDF-' ]]; then
      rm -f -- "$part"
      printf 'Not a valid PDF header: %s (%s)\n' "$filename" "$url" >&2
      exit 1
    fi
    mv -f -- "$part" "$target"
  fi
  printf 'type\t%s\nsource\t%s\n' "$edition" "$url" > "$target.source"
done < "$source_list"

(
  cd "$output_dir"
  sha256sum -- *.pdf > SHA256SUMS
)
printf '\nSaved PDFs, source receipts and SHA256SUMS under %s\n' "$output_dir"
