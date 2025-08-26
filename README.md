# AM_surfaces

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Investigate the effect of surface defects on the optical properties of Additively Manufactured (AM) mirrors.

## Project Organization

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

--------

