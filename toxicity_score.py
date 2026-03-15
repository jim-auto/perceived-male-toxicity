"""Core scoring engine for perceived male toxicity."""

from dataclasses import dataclass, field

from features import Feature, get_feature

BASE_SCORE: int = 50
MIN_SCORE: int = 0
MAX_SCORE: int = 100

DOMINANCE_LEVELS: list[tuple[int, str]] = [
    (80, "very high"),
    (65, "high"),
    (45, "moderate"),
    (25, "low"),
    (0, "very low"),
]


@dataclass
class ScoringResult:
    """Container for a full scoring breakdown."""

    score: int
    dominance_level: str
    matched_features: list[Feature] = field(default_factory=list)
    unknown_inputs: list[str] = field(default_factory=list)


def classify_dominance(score: int) -> str:
    """Map a numeric score to a human-readable dominance level."""
    for threshold, label in DOMINANCE_LEVELS:
        if score >= threshold:
            return label
    return "very low"


def compute_score(input_features: list[str]) -> ScoringResult:
    """Compute perceived toxicity score from a list of feature names.

    Args:
        input_features: List of feature name strings (e.g. ["black_clothing", "leather_jacket"]).

    Returns:
        A ScoringResult with the clamped score, dominance level, and breakdown.
    """
    matched: list[Feature] = []
    unknown: list[str] = []

    for name in input_features:
        feature = get_feature(name)
        if feature is not None:
            matched.append(feature)
        else:
            unknown.append(name)

    raw_score = BASE_SCORE + sum(f.weight for f in matched)
    clamped_score = max(MIN_SCORE, min(MAX_SCORE, raw_score))

    return ScoringResult(
        score=clamped_score,
        dominance_level=classify_dominance(clamped_score),
        matched_features=matched,
        unknown_inputs=unknown,
    )


def format_result(result: ScoringResult) -> str:
    """Format a ScoringResult into a human-readable string."""
    lines: list[str] = []
    lines.append(f"Perceived Toxicity Score: {result.score}")
    lines.append(f"Dominance level: {result.dominance_level}")
    lines.append("")

    if result.matched_features:
        lines.append("Factors:")
        for f in sorted(result.matched_features, key=lambda x: x.weight, reverse=True):
            sign = "+" if f.weight >= 0 else ""
            lines.append(f"  {sign}{f.weight:>3}  {f.description}")

    if result.unknown_inputs:
        lines.append("")
        lines.append("Unknown features (ignored):")
        for name in result.unknown_inputs:
            lines.append(f"  - {name}")

    return "\n".join(lines)
