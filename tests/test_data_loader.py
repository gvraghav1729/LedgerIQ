
from io import BytesIO

from data_loader import load_financial_data


VALID_CSV = b"""period,revenue,cost_of_sales,operating_expenses,total_assets,current_assets,current_liabilities,total_liabilities,equity,net_income
2024,1000,600,200,1500,500,250,700,800,100
2025,1200,700,230,1700,600,300,750,950,150
"""


def test_valid_csv_loads_successfully():
    df, error = load_financial_data(BytesIO(VALID_CSV))

    assert error is None
    assert df is not None
    assert len(df) == 2


def test_missing_column_is_rejected():
    csv_data = (
        b"period,revenue\n"
        b"2024,1000\n"
    )

    df, error = load_financial_data(BytesIO(csv_data))

    assert df is None
    assert "Missing required columns" in error


def test_non_numeric_financial_value_is_rejected():
    csv_data = VALID_CSV.replace(b"1000,600", b"invalid,600")

    df, error = load_financial_data(BytesIO(csv_data))

    assert df is None
    assert "non-numeric" in error


def test_duplicate_periods_are_rejected():
    csv_data = VALID_CSV.replace(
        b"2025,1200",
        b"2024,1200",
    )

    df, error = load_financial_data(BytesIO(csv_data))

    assert df is None
    assert "Duplicate reporting periods" in error
