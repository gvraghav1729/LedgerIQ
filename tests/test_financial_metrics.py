
import pandas as pd
import pytest

from financial_metrics import calculate_financial_metrics


@pytest.fixture
def sample_data():
    return pd.DataFrame([
        {
            "period": "2024",
            "revenue": 1000,
            "cost_of_sales": 600,
            "operating_expenses": 200,
            "total_assets": 1500,
            "current_assets": 500,
            "current_liabilities": 250,
            "total_liabilities": 700,
            "equity": 800,
            "net_income": 100,
        },
        {
            "period": "2025",
            "revenue": 1200,
            "cost_of_sales": 700,
            "operating_expenses": 230,
            "total_assets": 1700,
            "current_assets": 600,
            "current_liabilities": 300,
            "total_liabilities": 750,
            "equity": 950,
            "net_income": 150,
        },
    ])


def test_gross_profit_calculation(sample_data):
    result = calculate_financial_metrics(sample_data)

    assert result.loc[0, "gross_profit"] == 400
    assert result.loc[1, "gross_profit"] == 500


def test_net_profit_margin(sample_data):
    result = calculate_financial_metrics(sample_data)

    assert result.loc[0, "net_profit_margin_pct"] == pytest.approx(10.0)
    assert result.loc[1, "net_profit_margin_pct"] == pytest.approx(12.5)


def test_current_ratio(sample_data):
    result = calculate_financial_metrics(sample_data)

    assert result.loc[0, "current_ratio"] == pytest.approx(2.0)
    assert result.loc[1, "current_ratio"] == pytest.approx(2.0)


def test_revenue_growth(sample_data):
    result = calculate_financial_metrics(sample_data)

    assert pd.isna(result.loc[0, "revenue_growth_pct"])
    assert result.loc[1, "revenue_growth_pct"] == pytest.approx(20.0)


def test_net_income_growth(sample_data):
    result = calculate_financial_metrics(sample_data)

    assert pd.isna(result.loc[0, "net_income_growth_pct"])
    assert result.loc[1, "net_income_growth_pct"] == pytest.approx(50.0)
