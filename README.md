# perceived-male-toxicity

https://jim-auto.github.io/perceived-male-toxicity/

男性ファッションにおける**"毒性（Toxicity）"スコア**を推定するプロトタイプです。
ここでの"毒性"とは、**危険・支配的・エッジの効いた魅力**（いわゆる"悪い男"感）を指します。

## "Perceived Toxicity" とは？

本プロジェクトにおける**Toxicity は有害な行動を意味しません**。

恋愛心理学で語られる「危険な雰囲気」「エッジの効いたオーラ」のことです。
レザージャケット、黒い服、タトゥー、シルバーアクセなどが典型例です。

スコア（0〜100）は、服装がどれだけ「支配的 / エッジが効いている」かをルールベースで推定します。

## クイックスタート

```bash
# スコアを計算
python demo.py black_clothing rolled_sleeves leather_jacket silver_chain

# 利用可能なfeature一覧を表示
python demo.py --list
```

### 出力例

```
Perceived Toxicity Score: 89
Dominance level: very high

Factors:
  +15  Leather jacket edge
  +10  Black clothing dominance
   +8  Visible forearm / rolled sleeves
   +6  Chain accessory
```

## プロジェクト構成

```
perceived-male-toxicity/
├── README.md
├── features.py          # Feature定義と重み
├── toxicity_score.py    # スコアリングエンジン
├── demo.py              # CLIエントリーポイント
├── data/                # 将来: データセット
└── examples/            # 将来: 服装例
```

## Feature一覧と重み

| Feature             | 重み | 説明                           |
|---------------------|-----:|--------------------------------|
| leather_jacket      |  +15 | レザージャケットのエッジ感     |
| muscular_fit        |  +12 | タイトフィット / 筋肉質な着こなし |
| black_clothing      |  +10 | 黒い服の支配感                 |
| tattoo              |  +10 | 見えるタトゥー                 |
| rolled_sleeves      |   +8 | 袖まくり / 前腕の露出          |
| boots               |   +7 | コンバットブーツ / チェルシーブーツ |
| silver_chain        |   +6 | チェーンアクセサリー           |
| stubble             |   +6 | 無精ひげ / 短いヒゲ            |
| sunglasses          |   +5 | ダークサングラス               |
| slicked_back_hair   |   +5 | オールバック                   |
| rings               |   +4 | 指輪                           |
| sneakers            |   -2 | カジュアルスニーカー           |
| minimal_style       |   -3 | ミニマル / クリーンな美学      |
| formal_suit         |   -5 | トラディショナルなスーツ       |
| bright_colors       |   -8 | 明るい色 / パステルカラー      |
| oversized_clothing  |  -10 | オーバーサイズ / ダボダボ      |

## スコアの仕組み

```
score = clamp(50 + sum(feature_weights), 0, 100)
```

ベーススコアは **50**（ニュートラル）。各featureの重みで上下します。

## 今後の展望

- **画像ベースの服装検出** — 写真からfeatureを自動検出（CV）
- **人間による評価データセット** — 主観的評価を収集して重みを調整
- **PCA分析** — 支配性 / 信頼性 / 魅力を直交軸に分解
- **Webデモ** — インタラクティブUIでリアルタイムにスコア表示
- **MLモデル** — ルールベースからモデルベースへの移行

## ライセンス

MIT
