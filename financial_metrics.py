
import pandas as pd


def calculate_financial_metrics(df):
    """Calculate financial ratios for each reporting period."""

    result = df.copy()

    # Profitability ratios
    result["gross_profit"] = (
        result["revenue"] - result["cost_of_sales"]
    )

    result["gross_profit_margin_pct"] = (
        result["gross_profit"] / result["revenue"].replace(0, float("nan"))
    ) * 100

    result["net_profit_margin_pct"] = (
        result["net_income"] / result["revenue"].replace(0, float("nan"))
    ) * 100

    result["return_on_assets_pct"] = (
        result["net_income"] / result["total_assets"].replace(0, float("nan"))
    ) * 100

    # Liquidity ratio
    result["current_ratio"] = (
        result["current_assets"]
        / result["current_liabilities"].replace(0, float("nan"))
    )

    # Leverage ratio
    result["debt_to_equity_ratio"] = (
        result["total_liabilities"]
        / result["equity"].replace(0, float("nan"))
    )

    # Efficiency ratio
    result["asset_turnover_ratio"] = (
        result["revenue"] / result["total_assets"].replace(0, float("nan"))
    )

    # Year-over-year revenue growth
    result["revenue_growth_pct"] = (
        result["revenue"].pct_change() * 100
    )

    # Year-over-year net income growth
    result["net_income_growth_pct"] = (
        result["net_income"].pct_change() * 100
    )

    return result