
import streamlit as st
import pandas as pd
import plotly.express as px

from data_loader import load_financial_data
from financial_metrics import calculate_financial_metrics
from anomaly_detector import detect_anomalies
from report_generator import (
    generate_excel_report,
    generate_pdf_report,
)


# --------------------------------------------------
# 1. Page configuration and typography
# --------------------------------------------------

st.set_page_config(
    page_title="LedgerIQ | Financial Intelligence",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <style>
    /* Use the AccessGuard-style font */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: "DejaVu Sans", Arial, sans-serif !important;
    }

    [data-testid="stAppViewContainer"] h1,
    [data-testid="stAppViewContainer"] h2,
    [data-testid="stAppViewContainer"] h3,
    [data-testid="stAppViewContainer"] p,
    [data-testid="stAppViewContainer"] label,
    [data-testid="stMetricValue"],
    [data-testid="stMetricLabel"] {
        font-family: "DejaVu Sans", Arial, sans-serif !important;
    }

    /* Reduce the unused space above the application heading */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 2rem !important;
    }

    /* Keep the heading close to the top */
    h1 {
        margin-top: 0.5rem !important;
        padding-top: 0.25rem !important;
    }

    /* Slightly tighten vertical spacing between components */
    [data-testid="stVerticalBlock"] {
        gap: 0.8rem;
    }

    /* Financial overview KPI cards */
    [data-testid="stMetric"] {
        background: linear-gradient(145deg, #171D29, #11151E);
        border: 1px solid #303B4D;
        border-radius: 12px;
        padding: 20px 22px;
        min-height: 135px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.18);
        transition: border-color 0.2s ease, transform 0.2s ease;
    }

    /* Subtle highlight on hover */
    [data-testid="stMetric"]:hover {
        border-color: #4F8BF9;
        transform: translateY(-2px);
    }
    /* KPI labels */
    [data-testid="stMetricLabel"] {
        color: #AAB6C8 !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
    }
    /* KPI values */
    [data-testid="stMetricValue"] {
        color: #F4F7FC !important;
        font-size: 2rem !important;
        font-weight: 650 !important;
        line-height: 1.4 !important;
    }
    /* Space around the overview cards */
    [data-testid="stHorizontalBlock"] {
        gap: 16px;
    }
    
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# 2. Formatting helpers
# --------------------------------------------------

def format_inr(value):
    """Format a numeric amount using Indian rupee grouping."""

    if pd.isna(value):
        return "N/A"

    amount = int(round(float(value)))
    sign = "-" if amount < 0 else ""
    digits = str(abs(amount))

    if len(digits) <= 3:
        formatted = digits
    else:
        last_three = digits[-3:]
        remaining = digits[:-3]

        groups = []
        while remaining:
            groups.insert(0, remaining[-2:])
            remaining = remaining[:-2]

        formatted = ",".join(groups) + "," + last_three

    return f"{sign}₹{formatted}"


def format_rupee_columns(df, columns):
    """Return a display-only copy with monetary columns formatted."""

    display_df = df.copy()

    for column in columns:
        if column in display_df.columns:
            display_df[column] = display_df[column].map(format_inr)

    return display_df


# --------------------------------------------------
# 3. Application header
# --------------------------------------------------

st.title("LedgerIQ")
st.caption("Financial Statement Analysis")

st.markdown(
    "Understand financial performance, compare reporting periods, "
    "and identify unusual movements using transparent screening rules."
)

st.caption("Currency display: Indian Rupee (INR · ₹)")


# --------------------------------------------------
# 4. Upload financial data
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload a financial statement CSV",
    type=["csv"],
    help="Upload a CSV containing the required financial statement columns.",
)

if uploaded_file is None:
    st.info(
        "Upload your financial statement CSV to begin."
    )

else:
    df, error = load_financial_data(uploaded_file)

    if error:
        st.error(error)

    else:
        df["period"] = df["period"].astype(str).str.strip()
        df = df.sort_values("period").reset_index(drop=True)

        metrics = calculate_financial_metrics(df)
        findings = detect_anomalies(df)

        st.success(
            f"Successfully processed {len(df)} reporting periods."
        )

        # --------------------------------------------------
        # 5. Financial overview
        # --------------------------------------------------

        st.header("Financial overview")

        latest = metrics.iloc[-1]

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Latest revenue",
                format_inr(latest["revenue"]),
            )

        with col2:
            st.metric(
                "Latest net income",
                format_inr(latest["net_income"]),
            )

        with col3:
            margin = latest["net_profit_margin_pct"]

            st.metric(
                "Net profit margin",
                f"{margin:.2f}%"
                if pd.notna(margin)
                else "N/A",
            )

        with col4:
            current_ratio = latest["current_ratio"]

            st.metric(
                "Current ratio",
                f"{current_ratio:.2f}x"
                if pd.notna(current_ratio)
                else "N/A",
            )

        st.caption(
            f"Overview for reporting period {latest['period']}. "
        )

        # --------------------------------------------------
        # 6. Financial performance charts
        # --------------------------------------------------

        st.header("Financial performance")

        tab1, tab2 = st.tabs(
            ["Revenue & income", "Profitability"]
        )

        with tab1:
            st.subheader("Revenue vs net income")

            fig = px.line(
                metrics,
                x="period",
                y=["revenue", "net_income"],
                markers=True,
                labels={
                    "period": "Reporting period",
                    "value": "Amount (INR)",
                    "variable": "Financial metric",
                },
                color_discrete_sequence=["#4F8BF9", "#2DBE8C"],
            )

            fig.update_layout(
                font=dict(
                    family="DejaVu Sans, Arial, sans-serif",
                    size=12,
                ),
                legend_title_text="",
                hovermode="x unified",
                margin=dict(l=10, r=10, t=20, b=10),
            )

            fig.update_yaxes(
                tickprefix="₹",
                tickformat=",",
                title_text="Amount (INR)",
                separatethousands=True,
            )

            st.plotly_chart(fig, use_container_width=True)

            st.caption(
                "Compare revenue and net income across reporting periods. "
                "The currency values represent the units supplied in your CSV."
            )

        with tab2:
            st.subheader("Net profit margin")

            fig_margin = px.line(
                metrics,
                x="period",
                y="net_profit_margin_pct",
                markers=True,
                labels={
                    "period": "Reporting period",
                    "net_profit_margin_pct": "Net profit margin (%)",
                },
                color_discrete_sequence=["#2DBE8C"],
            )

            fig_margin.update_layout(
                font=dict(
                    family="DejaVu Sans, Arial, sans-serif",
                    size=12,
                ),
                showlegend=False,
                margin=dict(l=10, r=10, t=20, b=10),
            )

            fig_margin.update_yaxes(
                ticksuffix="%",
                title_text="Net profit margin (%)",
            )

            st.plotly_chart(
                fig_margin,
                use_container_width=True,
            )

            st.caption(
                "Net profit margin is net income divided by revenue, "
                "expressed as a percentage."
            )

        # --------------------------------------------------
        # 7. Financial ratio analysis
        # --------------------------------------------------

        st.header("Financial ratio analysis")

        ratio_descriptions = {
            "gross_profit_margin_pct": "Gross profit margin (%)",
            "net_profit_margin_pct": "Net profit margin (%)",
            "return_on_assets_pct": "Return on assets (%)",
            "current_ratio": "Current ratio (x)",
            "debt_to_equity_ratio": "Liabilities-to-equity ratio (x)",
            "asset_turnover_ratio": "Asset turnover (x)",
            "revenue_growth_pct": "Revenue growth (%)",
            "net_income_growth_pct": "Net income growth (%)",
        }

        ratio_columns = [
            "period",
            *ratio_descriptions.keys(),
        ]

        ratio_table = metrics[ratio_columns].rename(
            columns=ratio_descriptions
        )

        st.dataframe(
            ratio_table.round(2),
            use_container_width=True,
            hide_index=True,
        )

        with st.expander("How to interpret these ratios"):
            st.markdown(
                """
                - **Gross profit margin:** gross profit as a percentage of revenue.
                - **Net profit margin:** net income as a percentage of revenue.
                - **Return on assets:** net income relative to total assets.
                - **Current ratio:** current assets divided by current liabilities.
                - **Liabilities-to-equity ratio:** total liabilities divided by equity.
                - **Asset turnover:** revenue divided by total assets.
                - **Growth rates:** percentage change from the previous reporting period.
                """
            )

            st.caption(
                "Ratios should be interpreted in context. Industry, accounting "
                "policies, seasonality, and one-off events can affect comparisons."
            )

        # --------------------------------------------------
        # 8. Unusual financial movements
        # --------------------------------------------------

        st.header("Unusual financial movements")

        if findings.empty:
            st.success(
                "No movements crossed the current screening thresholds."
            )

        else:
            high_count = int(
                (findings["severity"] == "High").sum()
            )

            medium_count = int(
                (findings["severity"] == "Medium").sum()
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total findings", len(findings))

            with col2:
                st.metric("High severity", high_count)

            with col3:
                st.metric("Medium severity", medium_count)

            st.warning(
                "These are screening alerts for further review, "
                "not proof of fraud, error, or financial distress."
            )

            severity_filter = st.selectbox(
                "Filter findings by severity",
                ["All", "High", "Medium"],
            )

            displayed_findings = findings.copy()

            if severity_filter != "All":
                displayed_findings = displayed_findings[
                    displayed_findings["severity"] == severity_filter
                ]

            st.dataframe(
                displayed_findings,
                use_container_width=True,
                hide_index=True,
            )

        # --------------------------------------------------
        # 9. Downloadable reports
        # --------------------------------------------------

        st.header("Export your analysis")

        excel_report = generate_excel_report(metrics, findings)
        pdf_report = generate_pdf_report(metrics, findings)

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                label="Download Excel report",
                data=excel_report,
                file_name="LedgerIQ_Financial_Report.xlsx",
                mime=(
                    "application/vnd.openxmlformats-officedocument."
                    "spreadsheetml.sheet"
                ),
                use_container_width=True,
            )

        with col2:
            st.download_button(
                label="Download PDF report",
                data=pdf_report,
                file_name="LedgerIQ_Financial_Report.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

        # --------------------------------------------------
        # 10. Detailed financial data
        # --------------------------------------------------

        with st.expander(
            "View original data and all calculated metrics"
        ):
            monetary_columns = [
                "revenue",
                "cost_of_sales",
                "operating_expenses",
                "total_assets",
                "current_assets",
                "current_liabilities",
                "total_liabilities",
                "equity",
                "net_income",
                "gross_profit",
            ]

            display_metrics = format_rupee_columns(
                metrics,
                monetary_columns,
            )

            st.dataframe(
                display_metrics,
                use_container_width=True,
                hide_index=True,
            )

        st.divider()

        st.caption(
            "LedgerIQ V1.0 | Rule-based financial analysis. "
            "Not a formal audit opinion or investment recommendation."
        )
