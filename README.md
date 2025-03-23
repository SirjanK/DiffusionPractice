# DiffusionPractice
Practice implementing VAEs and Diffusion models on CIFAR-10.

## Setup
Use `python3.11`
1. Download CIFAR-10 from https://www.cs.toronto.edu/~kriz/cifar.html and place under `data/` folder.
2. `tar -xvf data/cifar-10-python.tar -C data/`

## Classifier
We build a simple CIFAR-10 CNN classifier to use for generative metric computation (see below). We could have taken an already available model,
but for extra practice and a warm-up we go through the whole train-validate-eval cycle for this classifier to get one that performs decently.

### Model Architecture
TODO

### Training Procedure
TODO

### Evaluation
TODO

#### Current Best Results
TODO

## Evaluator Notebook
`Evaluator.ipynb` allows you to generate a metrics dashboard for trained generative models along with displaying 9 sampled images for each model.

This allows us to compare performance and evaluate models against each other.

### Metrics
We report FID (Frechet Inception Distance), KID (Kernel Inception Distance), IS (Inception Score) for each generative model.
Furthermore, we break it down by FID, KID, and IS with the traditional definitions that use Inception V3 projected embeddings (for FID, KID) and
ImageNet classes (for IS) along with a custom implementation with a custom network trained on CIFAR-10.
We describe these below. Useful paper to read more: https://proceedings.neurips.cc/paper_files/paper/2018/file/f7696a9b362ac5a51c3dc8f098b73923-Paper.pdf.

#### FID
TODO

#### KID
TODO

#### IS
TODO

#### Details on CIFAR-{FID, KID, IS}
TODO

## Review of VAE Theory
### ELBO
TODO

### VAE
TODO

### Hierarchical VAE
TODO

## Review of Diffusion Theory
TODO

## Model Implementation Details
### Common
TODO

### VAE
TODO

### Hierarchical VAE
TODO

### Diffusion
TODO

## Results
TODO
