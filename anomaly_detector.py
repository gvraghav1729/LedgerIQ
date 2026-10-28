
import pandas as pd


def detect_anomalies(df):
    """
    Flag unusual financial movements using transparent,
    rule-based screening checks.
    """

    findings = []

    if len(df) < 2:
        return pd.DataFrame(
            columns=[
                "period",
                "severity",
                "finding",
                "explanation",
                "value",
            ]
        )

    data = df.copy()
    data["period"] = data["period"].astype(str)

    # Sort annual periods chronologically where possible.
    data = data.sort_values("period").reset_index(drop=True)

    for i in range(1, len(data)):
        previous = data.iloc[i - 1]
        current = data.iloc[i]

        period = current["period"]

        # Rule 1: Significant revenue decline.
        if previous["revenue"] > 0:
            revenue_change = (
                (current["revenue"] - previous["revenue"])
                / previous["revenue"]
            ) * 100

            if revenue_change <= -10:
                findings.append({
                    "period": period,
                    "severity": "High",
                    "finding": "Significant revenue decline",
                    "explanation": (
                        f"Revenue fell by {abs(revenue_change):.2f}% "
                        f"compared with {previous['period']}."
                    ),
                    "value": round(revenue_change, 2),
                })

        # Rule 2: Significant net income decline.
        if previous["net_income"] > 0:
            income_change = (
                (current["net_income"] - previous["net_income"])
                / previous["net_income"]
            ) * 100

            if income_change <= -20:
                findings.append({
                    "period": period,
                    "severity": "High",
                    "finding": "Significant net income decline",
                    "explanation": (
                        f"Net income fell by {abs(income_change):.2f}% "
                        f"compared with {previous['period']}."
                    ),
                    "value": round(income_change, 2),
                })

        # Rule 3: Sharp drop in net profit margin.
        if previous["revenue"] > 0 and current["revenue"] > 0:
            previous_margin = (
                previous["net_income"] / previous["revenue"]
            ) * 100

            current_margin = (
                current["net_income"] / current["revenue"]
            ) * 100

            margin_change = current_margin - previous_margin

            if margin_change <= -5:
                findings.append({
                    "period": period,
                    "severity": "Medium",
                    "finding": "Net profit margin deterioration",
                    "explanation": (
                        f"Net profit margin dropped by "
                        f"{abs(margin_change):.2f} percentage points "
                        f"compared with {previous['period']}."
                    ),
                    "value": round(margin_change, 2),
                })

    return pd.DataFrame(
        findings,
        columns=[
            "period",
            "severity",
            "finding",
            "explanation",
            "value",
        ],
    )
