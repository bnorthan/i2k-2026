# 32 — Project organization

An AI Lab project is a folder of images. AI Lab adds its own folders beside
them as you work. This is the bees project after some labelling and one
training run.

![The bees project folder](images/32_project_organization.png)

## The images

- `comb_01.png` ... `comb_07.png` are the images.
- AI Lab reads them. It never changes them.

## The folders

**annotations**

- The labels you draw in AI Lab, one `.tif` per image.
- They are in `annotations/Labels (Persistent)/`.
- They can be partial. Annotate some objects now, more later.

**labels**

- The parts of the annotations marked with a label box.
- `input0/` holds the image crops, `truth0/` the matching label crops.
- `boxes.csv` records where each box is.
- Only these are used for training.

**patches**

- The training set, made from the labels by augmentation.
- `input0/` holds the image patches, `ground_truth0/` the matching labels.
- This is what the training reads.

**models**

- The models you train, one per training run.
- Each has a `_history.csv` with the loss for each epoch.

**embeddings**

- SAM's embeddings, one folder per image.
- Computing one takes 20-60 seconds. After that it is saved here, so the next
  click on that image is fast.
- Safe to delete. They are made again when needed.

## The order

images → annotations → labels → patches → models
