#!/usr/bin/env python3
"""Recompute one historical ring series; keep modern comparisons separate.

Source: Buchwald and Feingold (2013), Table 2.1, p. 91, first diameter 45.
This is a published transcription, NOT an independently checked autograph.
See sources/newton-discrepant-measurements.md for the source chain and limits.
Python 3.9+; standard library only. No downloads or changes to source data.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys
import unittest

DATA = Path(__file__).resolve().parents[1] / "data" / "newton-rings-1671.csv"
RECORDED_MEAN = Fraction(1944)
RECORDED_MISMATCH = Fraction(81)


@dataclass(frozen=True)
class Reading:
    ring: int
    diameter: Fraction
    square: Fraction
    next_difference: Fraction | None


def read_series(path: Path = DATA) -> tuple[Reading, ...]:
    """Read all five reported values; reject damaged or inconsistent input."""
    with path.open(encoding="utf-8", newline="") as stream:
        rows = tuple(
            Reading(
                int(row["ring"]),
                Fraction(row["diameter_hundredth_inch"]),
                Fraction(row["recorded_square"]),
                Fraction(row["recorded_next_difference"])
                if row["recorded_next_difference"] else None,
            )
            for row in csv.DictReader(stream)
        )
    if len(rows) != 5 or [row.ring for row in rows] != list(range(1, 6)):
        raise ValueError("Expected the complete, ordered five-ring series.")
    for row in rows:
        if row.diameter <= 0 or row.diameter ** 2 != row.square:
            raise ValueError(f"Ring {row.ring}: diameter/square mismatch.")
    for left, right in zip(rows, rows[1:]):
        if right.square - left.square != left.next_difference:
            raise ValueError(f"Ring {left.ring}: recorded difference mismatch.")
    if rows[-1].next_difference is not None:
        raise ValueError("No sixth observation is present in this series.")
    return rows


def mean_difference(squares: tuple[Fraction, ...]) -> Fraction:
    if len(squares) < 2:
        raise ValueError("At least two squares are needed.")
    return sum(b - a for a, b in zip(squares, squares[1:])) / (len(squares) - 1)


def least_squares_line(squares: tuple[Fraction, ...]) -> tuple[Fraction, Fraction]:
    """Modern comparison only: minimize squared residuals in squared diameter."""
    if len(squares) < 2:
        raise ValueError("At least two squares are needed.")
    orders = tuple(Fraction(n) for n in range(1, len(squares) + 1))
    mean_order = sum(orders) / len(orders)
    mean_square = sum(squares) / len(squares)
    slope = sum((n - mean_order) * (s - mean_square)
                for n, s in zip(orders, squares)) / sum(
                    (n - mean_order) ** 2 for n in orders)
    return mean_square - slope * mean_order, slope


def residuals(squares: tuple[Fraction, ...], offset: Fraction,
              slope: Fraction) -> tuple[Fraction, ...]:
    return tuple(s - offset - n * slope for n, s in enumerate(squares, 1))


class ReconstructionChecks(unittest.TestCase):
    def setUp(self) -> None:
        self.rows = read_series()
        self.squares = tuple(row.square for row in self.rows)

    def test_01_reported_diameters(self) -> None:
        self.assertEqual(tuple(row.diameter for row in self.rows), (45, 62, 77, 89, 99))

    def test_02_reported_squares(self) -> None:
        self.assertEqual(self.squares, (2025, 3844, 5929, 7921, 9801))

    def test_03_reported_differences(self) -> None:
        self.assertEqual(tuple(row.next_difference for row in self.rows[:-1]),
                         (1819, 2085, 1992, 1880))

    def test_04_recorded_mean_and_mismatch(self) -> None:
        mean = mean_difference(self.squares)
        self.assertEqual(mean, RECORDED_MEAN)
        self.assertEqual(self.squares[0] - mean, RECORDED_MISMATCH)

    def test_05_endpoint_residuals(self) -> None:
        self.assertEqual(residuals(self.squares, RECORDED_MISMATCH, RECORDED_MEAN),
                         (0, -125, 16, 64, 0))

    def test_06_modern_least_squares(self) -> None:
        self.assertEqual(least_squares_line(self.squares),
                         (Fraction(153, 10), Fraction(19629, 10)))

    def test_07_normal_equations(self) -> None:
        errors = residuals(self.squares, *least_squares_line(self.squares))
        self.assertEqual(sum(errors), 0)
        self.assertEqual(sum(n * e for n, e in enumerate(errors, 1)), 0)

    def test_08_residual_sums_of_squares(self) -> None:
        endpoint = residuals(self.squares, RECORDED_MISMATCH, RECORDED_MEAN)
        fitted = residuals(self.squares, *least_squares_line(self.squares))
        self.assertEqual(sum(e * e for e in endpoint), 19977)
        self.assertEqual(sum(e * e for e in fitted), Fraction(159999, 10))

    def test_09_interior_perturbation_telescopes(self) -> None:
        # Synthetic sensitivity test, not a historical observation.
        altered = tuple(s + (100 if n == 2 else 0)
                        for n, s in enumerate(self.squares, 1))
        self.assertEqual(mean_difference(altered), RECORDED_MEAN)
        self.assertEqual(least_squares_line(altered)[1], Fraction(19529, 10))

    def test_10_constant_squared_offset(self) -> None:
        # Cancellation holds for offsets in squared diameter, not all biases.
        altered = tuple(s + 100 for s in self.squares)
        self.assertEqual(mean_difference(altered), RECORDED_MEAN)
        self.assertEqual(altered[0] - mean_difference(altered), 181)

    def test_11_constant_diameter_offset_does_not_cancel(self) -> None:
        altered = tuple((row.diameter + 1) ** 2 for row in self.rows)
        self.assertEqual(mean_difference(altered), 1971)

    def test_12_reject_short_series(self) -> None:
        for series in ((), (Fraction(1),)):
            with self.assertRaises(ValueError):
                mean_difference(series)
            with self.assertRaises(ValueError):
                least_squares_line(series)


def report(rows: tuple[Reading, ...]) -> None:
    squares = tuple(row.square for row in rows)
    spacing = mean_difference(squares)
    offset = squares[0] - spacing
    fitted_offset, fitted_spacing = least_squares_line(squares)
    print("Evidence: published transcription; autograph not independently checked.")
    print("Historical mean of successive squared-diameter differences:", spacing)
    print("Historical first-square minus mean:", offset)
    print("Modern endpoint line: square =", offset, "+", spacing, "* ring")
    print("Modern least-squares line: square =", fitted_offset, "+", fitted_spacing, "* ring")
    print("ring | diameter | recorded square | endpoint residual | least-squares residual")
    for row, endpoint, fitted in zip(
            rows, residuals(squares, offset, spacing),
            residuals(squares, fitted_offset, fitted_spacing)):
        print(row.ring, row.diameter, row.square, endpoint, fitted, sep=" | ")
    print("Diameters: hundredths of an inch. Squares/residuals: 1/10000 square inch.")
    print("The two fitted lines above are modern comparisons, not Newton's stated algorithm.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="run 12 exact-arithmetic checks")
    args = parser.parse_args()
    try:
        rows = read_series()
        if args.check:
            tests = unittest.defaultTestLoader.loadTestsFromTestCase(ReconstructionChecks)
            if not unittest.TextTestRunner(verbosity=2).run(tests).wasSuccessful():
                return 1
        report(rows)
        return 0
    except (OSError, ValueError, KeyError, ZeroDivisionError) as error:
        print(f"Reconstruction failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
