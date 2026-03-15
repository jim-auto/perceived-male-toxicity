#!/usr/bin/env python3
"""CLI demo for perceived male toxicity scoring.

Usage:
    python demo.py black_clothing rolled_sleeves leather_jacket
    python demo.py --list
"""

from __future__ import annotations

import argparse
import sys

from features import list_features
from toxicity_score import compute_score, format_result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Estimate perceived male 'toxicity' (edgy/dominant vibe) from outfit features.",
    )
    parser.add_argument(
        "features",
        nargs="*",
        help="Outfit feature names (e.g. black_clothing leather_jacket rolled_sleeves)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available features and their weights",
    )
    return parser


def print_feature_list() -> None:
    """Display every registered feature with its weight."""
    print("Available features:\n")
    print(f"  {'Feature':<25} {'Weight':>6}  Description")
    print(f"  {'-'*25} {'-'*6}  {'-'*30}")
    for f in list_features():
        sign = "+" if f.weight >= 0 else ""
        print(f"  {f.name:<25} {sign}{f.weight:>5}  {f.description}")


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list:
        print_feature_list()
        return

    if not args.features:
        parser.print_help()
        sys.exit(1)

    result = compute_score(args.features)
    print(format_result(result))


if __name__ == "__main__":
    main()
