# perceived-male-toxicity

https://jim-auto.github.io/perceived-male-toxicity/

Estimate **perceived male "toxicity" in fashion** — the *perceived dangerous / dominant / edgy attractiveness* of a male outfit.

## What is "perceived toxicity"?

In this project, **toxicity does NOT mean harmful behavior**.

It refers to the **perceived edgy or dangerous vibe** sometimes associated with attractiveness in dating psychology — think leather jackets, dark clothing, visible tattoos, and sharp accessories. This is a subjective, cultural perception, not a moral judgement.

The score (0–100) reflects how "dominant / edgy" an outfit *appears*, based on common fashion psychology heuristics.

## Quick Start

```bash
# Score an outfit
python demo.py black_clothing rolled_sleeves leather_jacket silver_chain

# List all available features
python demo.py --list
```

### Example Output

```
Perceived Toxicity Score: 89
Dominance level: very high

Factors:
  +15  Leather jacket edge
  +10  Black clothing dominance
   +8  Visible forearm / rolled sleeves
   +6  Chain accessory
```

## Project Structure

```
perceived-male-toxicity/
├── README.md
├── features.py          # Feature definitions & weights
├── toxicity_score.py    # Scoring engine
├── demo.py              # CLI entry point
├── data/                # Future: datasets
└── examples/            # Future: example outfits
```

## Features & Weights

| Feature             | Weight | Description                    |
|---------------------|-------:|--------------------------------|
| leather_jacket      |    +15 | Leather jacket edge            |
| muscular_fit        |    +12 | Tight / muscular-fit clothing  |
| black_clothing      |    +10 | Black clothing dominance       |
| tattoo              |    +10 | Visible tattoo                 |
| rolled_sleeves      |     +8 | Visible forearm                |
| boots               |     +7 | Combat or Chelsea boots        |
| silver_chain        |     +6 | Chain accessory                |
| stubble             |     +6 | Stubble or short beard         |
| sunglasses          |     +5 | Dark sunglasses                |
| slicked_back_hair   |     +5 | Slicked-back hairstyle         |
| rings               |     +4 | Rings on fingers               |
| sneakers            |     -2 | Casual sneakers                |
| minimal_style       |     -3 | Minimal / clean aesthetic      |
| formal_suit         |     -5 | Traditional formal suit        |
| bright_colors       |     -8 | Bright or pastel colors        |
| oversized_clothing  |    -10 | Oversized / baggy clothing     |

## How It Works

```
score = clamp(50 + sum(feature_weights), 0, 100)
```

Base score is **50** (neutral). Features push it up (edgy) or down (soft).

## Future Work

- **Image-based outfit detection** — feed a photo, auto-detect features via CV
- **Dataset of human ratings** — collect subjective ratings to calibrate weights
- **PCA analysis** — decompose perceived dominance / trust / attractiveness into orthogonal axes
- **Web demo** — interactive UI to build outfits and see scores in real time
- **ML model** — train on rated outfit images to replace the rule-based engine

## License

MIT
