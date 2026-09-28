# Exercise 2 — Find the bees

Medium. Can you train a model that finds the bees?

## Start AI Lab on bees

```sh
cd i2k-2026/pixi/i2k2026_lite    # or i2k2026_microsam
pixi run bees
```

## Annotations → Labels → Patches

- **Annotations:** what you draw, on the full image. Can be unfinished.
  - **napari brush/fill:** draw on **Labels (Persistent)**, not Working.
  - **SAM:** the result appears on **Labels (Working)**. Commit it to keep it.
  - Only **Labels (Persistent)** is saved.
- **Label box:** marks "this part is done".
- **Labels:** the annotations inside a label box. Only these train.
- **Patches:** labels, augmented. The training set.

**SAVE before you augment. Augment before you train.**

## Label

- Draw labels on some bees.
- Draw a label box around what you labelled.
- Watch out: the honeycomb cells are not bees.

## Train

- Augment, then train.
- Predict, and look at the results.
- Fix the mistakes, add labels, retrain.

Training can take a while. Keep going at home if you need to.
