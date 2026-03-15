"""Feature definitions and weights for perceived male toxicity scoring."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Feature:
    """A single outfit feature with its scoring metadata."""

    name: str
    weight: int
    description: str
    category: str


# Core feature registry
FEATURES: dict[str, Feature] = {
    "black_clothing": Feature(
        name="black_clothing",
        weight=10,
        description="Black clothing dominance",
        category="color",
    ),
    "leather_jacket": Feature(
        name="leather_jacket",
        weight=15,
        description="Leather jacket edge",
        category="outerwear",
    ),
    "rolled_sleeves": Feature(
        name="rolled_sleeves",
        weight=8,
        description="Visible forearm / rolled sleeves",
        category="fit",
    ),
    "muscular_fit": Feature(
        name="muscular_fit",
        weight=12,
        description="Tight / muscular-fit clothing",
        category="fit",
    ),
    "silver_chain": Feature(
        name="silver_chain",
        weight=6,
        description="Chain accessory",
        category="accessory",
    ),
    "tattoo": Feature(
        name="tattoo",
        weight=10,
        description="Visible tattoo",
        category="body",
    ),
    "sunglasses": Feature(
        name="sunglasses",
        weight=5,
        description="Dark sunglasses",
        category="accessory",
    ),
    "rings": Feature(
        name="rings",
        weight=4,
        description="Rings on fingers",
        category="accessory",
    ),
    "boots": Feature(
        name="boots",
        weight=7,
        description="Combat or Chelsea boots",
        category="footwear",
    ),
    "stubble": Feature(
        name="stubble",
        weight=6,
        description="Stubble or short beard",
        category="grooming",
    ),
    "slicked_back_hair": Feature(
        name="slicked_back_hair",
        weight=5,
        description="Slicked-back hairstyle",
        category="grooming",
    ),
    "oversized_clothing": Feature(
        name="oversized_clothing",
        weight=-10,
        description="Oversized / baggy clothing",
        category="fit",
    ),
    "formal_suit": Feature(
        name="formal_suit",
        weight=-5,
        description="Traditional formal suit",
        category="outerwear",
    ),
    "minimal_style": Feature(
        name="minimal_style",
        weight=-3,
        description="Minimal / clean aesthetic",
        category="style",
    ),
    "bright_colors": Feature(
        name="bright_colors",
        weight=-8,
        description="Bright or pastel colors",
        category="color",
    ),
    "sneakers": Feature(
        name="sneakers",
        weight=-2,
        description="Casual sneakers",
        category="footwear",
    ),
}


def get_feature(name: str) -> Feature | None:
    """Look up a feature by name."""
    return FEATURES.get(name)


def list_features() -> list[Feature]:
    """Return all registered features sorted by weight descending."""
    return sorted(FEATURES.values(), key=lambda f: f.weight, reverse=True)
