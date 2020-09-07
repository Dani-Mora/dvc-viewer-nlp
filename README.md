# DVC UI playground

I have used this repository as a playgroiund for the DVC Viewer beta.

## Requirements

- Python >= 3.7
- Conda >= 4.8.4

## Set up

Data is extracted from Kaggle using Kaggle API. Make sure your credentials are properly persisted in your system (you can follow instructions from [here](https://github.com/Kaggle/kaggle-api).

In order to execute any of the stages, install and activate the environment by typing:

```bash
conda env create -f environment.yml
conda activate kaggle
```

Then you can train the baseline by typing:

```
dvc repro training
```
