
import pandas as pd
import numpy as np


REQUIRED_COLUMNS = [
    "period",
    "revenue",
    "cost_of_sales",
    "operating_expenses",
    "total_assets",
    "current_assets",
    "current_liabilities",
    "total_liabilities",
    "equity",
    "net_income",
]


NUMERIC_COLUMNS = [
    column for column in REQUIRED_COLUMNS if column != "period"
]


def load_financial_data(uploaded_file):
    """Load and validate a financial statement CSV."""

    try:
        df = pd.read_csv(uploaded_file)
    except Exception as exc:
        return None, f"Could not read the CSV file: {exc}"

    # Standardise column names.
    df.columns = df.columns.astype(str).str.strip().str.lower()

    # Check required columns.
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        return None, (
            "Missing required columns: "
            + ", ".join(missing_columns)
        )

    if df.empty:
        return None, "The uploaded file contains no data rows."

    # Keep only the columns the application currently understands.
    df = df[REQUIRED_COLUMNS].copy()

    # Validate reporting periods.
    df["period"] = df["period"].astype("string").str.strip()

    if df["period"].isna().any() or df["period"].eq("").any():
        return None, "Every row must have a reporting period."

    if df["period"].duplicated().any():
        return None, (
            "Duplicate reporting periods were found. "
            "Please use one row per period."
        )

    # Convert financial columns to numbers.
    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    if df[NUMERIC_COLUMNS].isna().any().any():
        return None, (
            "Some financial values are missing or non-numeric. "
            "Please check the uploaded CSV."
        )

    # Reject infinite values.
    if not np.isfinite(df[NUMERIC_COLUMNS].to_numpy()).all():
        return None, "Infinite financial values are not allowed."

    # Reject impossible negative balance-sheet amounts.
    # Net income, cost of sales, and operating expenses can be negative
    # in some datasets, so those are not rejected automatically.
    nonnegative_columns = [
        "total_assets",
        "current_assets",
        "current_liabilities",
        "total_liabilities",
    ]

    for column in nonnegative_columns:
        if (df[column] < 0).any():
            return None, (
                f"Negative values were found in '{column}'. "
                "Please verify the source data."
            )

    # Equity can be negative in real financial statements.
    # Net income and expenses may also be negative.

    return df, None
