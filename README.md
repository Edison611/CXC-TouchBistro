# CxC TouchBistro Challenge

A machine learning solution built for the **(CxC) x TouchBistro 2025** case competition. This project predicts restaurant transaction volume using historical point-of-sale data, helping restaurants anticipate demand and plan staffing, inventory, and operations more effectively.

## Overview

Restaurants need to forecast customer traffic to make informed decisions about staffing, inventory, and marketing. This project trains a regression model to **predict the number of transactions (bills)** a venue will process based on contextual features such as time of day, day of week, and restaurant concept/type.

## Project Structure

```
CXC-TouchBistro/
└── TouchBistroChallenge/
    └── touchbistro_model/
        ├── model.ipynb              # Main notebook: data prep, training, evaluation
        ├── touchbistro_model.py      # Script for running predictions with the trained model
        ├── feature_importance.py    # Visualizes which features drive model predictions
        ├── model.pkl                # Serialized (trained) Random Forest model
        ├── data/                    # Local dataset directory (gitignored, NDA-protected)
        ├── scripts/                 # Exploratory analysis and data-prep utilities
        │   ├── merge.py              # Joins raw source tables on venue ID
        │   ├── MonthyUS.py / MonthyCA.py     # Monthly revenue trend analysis (US/Canada)
        │   ├── HolidaysUS.py / HolidaysCA.py # Holiday-period revenue analysis (US/Canada)
        │   ├── week_data.ipynb        # Day-of-week trend exploration
        │   ├── histograms.ipynb       # Distribution analysis of key metrics
        │   └── user_input_city.ipynb  # Interactive city/concept-based exploration
        ├── devtools/
        │   ├── requirements.txt      # Python dependencies
        │   └── Dockerfile            # Containerized environment setup
        └── Documents/                # Final report and presentation slides
```

## Approach

1. **Data Ingestion & Cleaning** — Raw transaction and venue records are merged on a shared venue identifier and cleaned (null removal, type coercion).
2. **Feature Engineering** — Timestamps are decomposed into hour, day-of-week, and date components. Transactions are aggregated per venue, day, and hour to produce a transaction count target.
3. **Encoding** — Categorical fields (e.g., restaurant concept) are one-hot encoded.
4. **Modeling** — A `RandomForestRegressor` (scikit-learn) is trained on an 80/20 train-test split to predict transaction counts.
5. **Evaluation** — Model performance is measured with Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
6. **Interpretability** — `feature_importance.py` surfaces which features most influence predictions.
7. **Inference** — `touchbistro_model.py` demonstrates loading the saved model and scoring new, unseen inputs (e.g., a given concept, date, and hour).

## Tech Stack

- **Python 3.13**
- **pandas / numpy** — data wrangling
- **scikit-learn** — model training and evaluation (Random Forest Regression)
- **matplotlib** — exploratory visualization and feature importance plots
- **joblib** — model serialization
- **Docker** — reproducible environment setup

## Getting Started

### Prerequisites
- Python 3.13 (or a compatible conda environment)
- The TouchBistro dataset files, placed locally under `TouchBistroChallenge/touchbistro_model/data/` (not provided in this repo — see NDA notice above)

### Setup

```bash
cd TouchBistroChallenge/touchbistro_model
pip install -r devtools/requirements.txt
```

Or using Docker:

```bash
cd TouchBistroChallenge/touchbistro_model
docker build -f devtools/Dockerfile -t touchbistro-model .
```

### Running the Model

Train and evaluate the model by running `model.ipynb` end-to-end (requires the dataset in `data/`).

Run predictions on new inputs with the trained model:

```bash
python touchbistro_model.py
```

Inspect which features matter most to the model:

```bash
python feature_importance.py
```

## Data & Confidentiality

All source data provided by TouchBistro is confidential

## Deliverables

Final write-up and presentation slides summarizing findings and methodology are available under `TouchBistroChallenge/touchbistro_model/Documents/`.
