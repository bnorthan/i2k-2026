# Exercise 1 — Find the pollen

Can a generalist Cellpose model find all the pollen, with no training?

## Start AI Lab on pollen

From notebook 30 switch DATASET to 'pollen_count'

From the `pixi` folder of the repo:

```sh
cd i2k-2026/pixi
pixi run pollen
```

Needs notebook 12 run first, for the data.

## Segment

On the **Segment** tab, pick a Cellpose segmenter and click
**Segment Current Image**.

Things to try:

- **Cellpose 3 or Cellpose 4.** Same image, different model.
- **diameter.** Roughly the size of a pollen grain, in pixels. Too small
  splits grains, too big merges them.
- **flow_threshold.** Default 0.4. Higher keeps more, odder shapes.
- **cellprob_threshold.** Default 0. Lower finds fainter grains, higher
  drops them.
- **niter.** Default 200. More iterations can help large or long objects.

## Check the rest

When settings work for one image, click **Process Sequence** and step
through the others. Do the same settings hold up?
