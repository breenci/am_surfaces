# AM_surfaces

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

This project investigates the effect of surface defects on the optical properties of Additively Manufactured (AM) mirrors.

In particular, it focuses on the characterization of pores on the surface of AM mirrors and their contribution to scattering performace. The code in this repository implements workflows to identify and measure pores from different datasets, and uses scattering models to estimate their contribution to the overall Bidirectional Reflectance Distribution Function (BRDF) of the mirror surface.

## Project Organization

The project structure is adapted from the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) template, and is organized as follows:

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         amsurf and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── amsurf   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes amsurf a Python module
    │
    ├── BRDF.py               <- BRDF calculation functions
    │
    └── segment.py                <- Image segmentation functions
```

## Environment Setup

The required packages for this project are listed in the `environment.yml` file. If you have make and conda installed, you can create the correct environment by running:

```bash
make create_environment
```

in the root directory of the project. This will create a conda environment name `am_surfaces` with the required packages installed (including the `amsurf` package itself in editable mode). If packages are added or updated, you can update the environment with:

```bash
make requirements
```

Alternatively, you can create the conda environment manually with:

```
conda env create -f environment.yml
```

otherwise, you can install the required packages individually using pip.

## Example Workflow

A workflow for analyzing pores in microscope data and calculating their contribution to BRDF is implemented in the notebook `workflow-01_crb_LISA-microscope-workflow.ipynb`. This notebook demonstrates the following steps:

1. Measure mirror surface with using LISA microscope

2. Use image segmentation to identify and extract surface pores

3. Analyze extracted pores to calculate shape, area, distribution etc.

4. Use Peterson model to calculate BRDF contribution from the pores

--------

