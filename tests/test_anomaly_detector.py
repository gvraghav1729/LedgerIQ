
import pandas as pd

from anomaly_detector import detect_anomalies


def make_sample_data():
    return pd.DataFrame([
        {
            "period": "2023",
            "revenue": 1000,
            "net_income": 100,
        },
        {
            "period": "2024",
            "revenue": 850,
            "net_income": 70,
        },
    ])


def test_detects_revenue_decline():
    findings = detect_anomalies(make_sample_data())

    revenue_findings = findings[
        findings["finding"] == "Significant revenue decline"
    ]

    assert len(revenue_findings) == 1
    assert revenue_findings.iloc[0]["period"] == "2024"
    assert revenue_findings.iloc[0]["severity"] == "High"
    assert revenue_findings.iloc[0]["value"] == -15.0


def test_detects_net_income_decline():
    findings = detect_anomalies(make_sample_data())

    income_findings = findings[
        findings["finding"] == "Significant net income decline"
    ]

    assert len(income_findings) == 1
    assert income_findings.iloc[0]["value"] == -30.0


def test_returns_empty_findings_for_one_period():
    data = make_sample_data().iloc[[0]]

    findings = detect_anomalies(data)

    assert findings.empty


def test_no_alert_when_changes_are_small():
    data = pd.DataFrame([
        {"period": "2023", "revenue": 1000, "net_income": 100},
        {"period": "2024", "revenue": 990, "net_income": 95},
    ])

    findings = detect_anomalies(data)

    assert findings.empty
