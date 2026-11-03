# Nonlinear Regression: China GDP

This project fits a sigmoid curve to historical China GDP data using Python. It reads the included CSV, displays the observed values, estimates the sigmoid parameters with SciPy, prints those parameters, and plots the fitted curve alongside the data.

## Project files

- `none_linear.py` — script that loads the data, fits the model, and displays the plots.
- `china_gdp.csv` — GDP observations with `Year` and `Value` columns. The included data covers 1960–2014.

## Requirements

Python 3 and the following packages are required:

- NumPy
- pandas
- Matplotlib
- SciPy

Install them with pip:

```bash
python -m pip install numpy pandas matplotlib scipy
```

## Run

Run the script from the project directory so it can find `china_gdp.csv`:

```bash
python none_linear.py
```

The script opens a plot of the GDP observations, fits a two-parameter sigmoid to normalized year and GDP values, prints the estimated `beta_1` and `beta_2`, and opens a second plot comparing the data with the fitted curve. A graphical environment is needed to display the plots.

The model used is:

```text
f(x) = 1 / (1 + exp(-beta_1 * (x - beta_2)))
```

Both the observed years and GDP values are divided by their respective maxima before fitting. The fitted parameters therefore apply to the normalized inputs used by the script.
