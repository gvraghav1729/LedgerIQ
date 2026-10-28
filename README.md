# LedgerIQ

### Financial Statement Analysis & Intelligence

**LedgerIQ** is a Python-based financial analysis dashboard built with Streamlit. It helps users analyse financial statements, calculate key financial ratios, visualise financial performance over time, and identify unusual financial movements through transparent, rule-based screening.

The project combines financial analysis, data validation, interactive visualisation, automated testing, and downloadable reporting in one application.

> **Version:** 1.0.0  
> **Status:** Initial release  
> **Currency display:** Indian Rupee (INR, ₹)  
> **Application type:** Interactive web dashboard

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Using LedgerIQ](#using-ledgeriq)
- [Input Data Requirements](#input-data-requirements)
- [Financial Metrics](#financial-metrics)
- [Anomaly Detection](#anomaly-detection)
- [Exporting Reports](#exporting-reports)
- [Running Automated Tests](#running-automated-tests)
- [Data Handling and Security](#data-handling-and-security)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Disclaimer](#disclaimer)

---

## Overview

Financial statements contain valuable information about an organisation's profitability, liquidity, leverage, and operational performance. However, extracting meaningful insights often requires manual calculations and comparisons across reporting periods.

LedgerIQ aims to simplify this process by providing an interactive interface for financial statement analysis.

Users can upload a CSV file containing financial data and receive:

- A financial overview of the latest reporting period.
- Key financial ratios and growth calculations.
- Charts showing revenue, income, and profitability trends.
- Rule-based alerts for unusual financial movements.
- Downloadable Excel and PDF reports.

LedgerIQ is designed as an educational and analytical project demonstrating Python programming, financial analysis, data processing, and dashboard development.

## Key Features

### 1. Financial Statement Import and Validation

- Upload financial statements in CSV format.
- Validate required columns and numeric financial values.
- Identify missing or non-numeric data.
- Detect duplicate reporting periods.
- Reject non-finite numeric values.
- Apply basic validation to selected balance-sheet amounts.

### 2. Financial Overview

The dashboard presents four headline indicators for the latest reporting period:

- **Revenue:** Total reported revenue.
- **Net income:** Reported profit or loss after expenses.
- **Net profit margin:** Net income as a percentage of revenue.
- **Current ratio:** Current assets relative to current liabilities.

Monetary figures are displayed using the Indian rupee symbol and Indian-style comma grouping, for example `₹12,00,000`.

### 3. Interactive Financial Visualisation

LedgerIQ provides charts for examining:

- Revenue and net income over time.
- Net profit margin across reporting periods.

These visualisations help users explore changes in financial performance and identify periods that may require closer examination.

### 4. Financial Ratio Analysis

The dashboard calculates profitability, liquidity, leverage, efficiency, and growth metrics for each reporting period.

### 5. Rule-Based Anomaly Detection

LedgerIQ screens financial data for unusual movements, including:

- Significant revenue declines.
- Significant net income declines.
- Deterioration in net profit margin.

Each finding includes the reporting period, severity, description, and explanation.

### 6. Downloadable Reports

Users can export their analysis in two formats:

- **Excel (`.xlsx`):** Financial analysis and anomaly findings in separate worksheets.
- **PDF (`.pdf`):** A formatted financial report containing a summary, financial metrics table, unusual-movement findings, and a disclaimer.

### 7. Automated Testing

The project includes pytest tests covering financial calculations, anomaly detection, input validation, and report generation.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web dashboard |
| Pandas | Data loading, processing, and financial calculations |
| Plotly | Interactive financial charts |
| OpenPyXL | Excel workbook generation and formatting |
| ReportLab | PDF report generation |
| Pytest | Automated testing |
| pypdf | Reading generated PDFs during tests |
| Git and GitHub | Version control and source-code hosting |

---

## Project Structure

The project is organised into separate modules so that the dashboard, financial calculations, anomaly rules, and report generation can be maintained independently.

```text
LedgerIQ/
│
├── app.py
├── data_loader.py
├── financial_metrics.py
├── anomaly_detector.py
├── report_generator.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── sample_financials.csv
│
├── tests/
│   ├── test_financial_metrics.py
│   ├── test_anomaly_detector.py
│   ├── test_data_loader.py
│   └── test_report_generator.py
│
└── .venv/                 # Local virtual environment; not committed
```

### Module responsibilities

| File | Responsibility |
|---|---|
| `app.py` | Dashboard layout, CSV upload, metrics display, charts, filters, and report downloads |
| `data_loader.py` | CSV import and input validation |
| `financial_metrics.py` | Financial ratio and growth calculations |
| `anomaly_detector.py` | Rule-based screening for unusual financial movements |
| `report_generator.py` | Excel and PDF report generation |
| `requirements.txt` | Python package dependencies |
| `data/sample_financials.csv` | Fictional sample financial statements |
| `tests/` | Automated tests for core functionality |

---

## Installation

### Prerequisites

Before installing LedgerIQ, ensure that you have:

- Python 3.10 or a compatible later version.
- Git, if cloning the repository.
- A web browser.
- A terminal or command prompt.

### 1. Clone the repository

```bash
git clone https://github.com/gvraghav1729/LedgerIQ.git
cd LedgerIQ
```

### 2. Create a virtual environment

A virtual environment keeps LedgerIQ's dependencies separate from other Python projects.

On Windows:

```bat
python -m venv .venv
```

Activate it:

```bat
.venv\Scripts\activate.bat
```

After activation, the terminal should display `(.venv)` at the beginning of the prompt.

### 3. Install dependencies

```bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The requirements file contains the libraries needed to run the dashboard, calculate metrics, generate reports, and execute tests.

---

## Running the Application

From the project directory, with the virtual environment activated, run:

```bat
python -m streamlit run app.py
```

Streamlit will start a local web server and provide a URL, usually:

```text
http://localhost:8501
```

Open the displayed URL in your browser.

To stop the application, return to the terminal and press `Ctrl + C`.

---

## Using LedgerIQ

### Step 1 — Upload a financial statement

Open the dashboard and use the CSV uploader to select your financial statement file.

For an initial demonstration, use:

```text
data/sample_financials.csv
```

The sample dataset contains ten fictional annual reporting periods from 2016 through 2025.

### Step 2 — Review the financial overview

The dashboard displays revenue, net income, net profit margin, and current ratio for the latest reporting period in the uploaded data.

Monetary figures are formatted in INR for display. The input data itself should contain numeric amounts without currency symbols.

### Step 3 — Examine financial trends

Use the financial performance charts to compare revenue with net income and review net profit margin over time.

Look for changes that may warrant additional investigation.

### Step 4 — Review financial ratios

The ratio analysis table presents the calculated metrics for each reporting period.

Use the explanatory section in the dashboard to understand the purpose of each ratio.

### Step 5 — Investigate unusual financial movements

The anomaly detection section lists movements that cross the configured screening thresholds.

You can filter the findings by severity to focus on High- or Medium-severity alerts.

These findings are indicators for further review, not conclusions about the cause of a financial change.

### Step 6 — Export the results

Use the report download buttons to obtain:

- An Excel workbook for further analysis.
- A PDF report for review or presentation.

The PDF is structured as a two-page report for the standard sample dataset: financial summary and metrics on page one, and unusual financial movements on page two. Longer datasets or larger numbers of findings may require additional pages.

---

## Input Data Requirements

LedgerIQ expects a CSV containing one row per reporting period and the following columns.

| Column | Description |
|---|---|
| `period` | Reporting period, such as `2024` |
| `revenue` | Reported revenue |
| `cost_of_sales` | Cost of sales |
| `operating_expenses` | Operating expenses |
| `total_assets` | Total assets |
| `current_assets` | Current assets |
| `current_liabilities` | Current liabilities |
| `total_liabilities` | Total liabilities |
| `equity` | Reported equity |
| `net_income` | Net income or loss |

Column names are case-normalised by the loader, and extra columns are ignored by the current implementation.

### Example CSV

```csv
period,revenue,cost_of_sales,operating_expenses,total_assets,current_assets,current_liabilities,total_liabilities,equity,net_income
2024,1000000,600000,200000,1500000,500000,250000,700000,800000,100000
2025,1200000,700000,230000,1700000,600000,280000,750000,950000,150000
```

### Input guidelines

- Include every required column.
- Use numeric values for financial amounts.
- Do not include currency symbols or thousands separators inside numeric fields.
- Use a unique reporting period for each row.
- Avoid missing or infinite numeric values.
- Ensure that financial amounts use a consistent unit and currency throughout the dataset.

Negative net income and negative equity can occur in real financial statements and are not automatically rejected by the current loader. The loader does, however, reject negative values for selected asset and liability fields.

---

## Financial Metrics

LedgerIQ calculates the following metrics.

| Metric | Formula | Purpose |
|---|---|---|
| Gross profit | Revenue − Cost of sales | Measures profit remaining after cost of sales |
| Gross profit margin | Gross profit ÷ Revenue × 100 | Measures gross profitability |
| Net profit margin | Net income ÷ Revenue × 100 | Measures net profitability |
| Return on assets | Net income ÷ Total assets × 100 | Measures earnings relative to assets |
| Current ratio | Current assets ÷ Current liabilities | Assesses short-term liquidity |
| Liabilities-to-equity ratio | Total liabilities ÷ Equity | Examines financial leverage |
| Asset turnover | Revenue ÷ Total assets | Measures revenue relative to assets |
| Revenue growth | Percentage change in revenue | Tracks revenue movement between periods |
| Net income growth | Percentage change in net income | Tracks changes in net income between periods |

Growth calculations compare each row with the preceding reporting period in the dataset.

If the denominator is zero, the relevant ratio may be unavailable. Growth calculations for the first reporting period are unavailable because no previous period exists.

**Interpretation matters:** these ratios should be evaluated in context, including industry, accounting policies, seasonality, and one-off events. A higher ratio is not automatically better in every circumstance.

---

## Anomaly Detection

LedgerIQ uses transparent, rule-based checks to flag selected unusual financial movements.

| Rule | Trigger | Severity |
|---|---|---|
| Significant revenue decline | Revenue decreases by 10% or more compared with the preceding period | High |
| Significant net income decline | Net income decreases by 20% or more, when the preceding period's net income is positive | High |
| Net profit margin deterioration | Net profit margin decreases by 5 percentage points or more | Medium |

Each finding contains:

- Reporting period.
- Severity.
- Finding description.
- Explanation of the movement.
- Numeric change associated with the rule.

### Example

If revenue decreases from 1,000,000 to 850,000, the percentage change is:

\[
\frac{850{,}000-1{,}000{,}000}{1{,}000{,}000}\times100=-15\%
\]

This crosses the 10% revenue-decline threshold and generates a High-severity finding.

### Important behaviour

The current implementation has limitations when comparing loss-making periods, zero or negative denominators, and non-standard reporting periods. The screening thresholds are configurable design choices, not universal definitions of financial distress.

The alerts do not establish fraud, accounting errors, or misconduct.

---

## Exporting Reports

### Excel report

The Excel workbook contains two worksheets:

1. **Financial Analysis** — original financial data and calculated metrics.
2. **Anomaly Findings** — the detected unusual financial movements.

The workbook includes formatted headers, column sizing, and filters to make the data easier to review.

### PDF report

The PDF report contains:

**Page 1**
- Report title.
- Latest reporting period.
- Revenue, net income, and net profit margin summary.
- Financial metrics by period.

**Page 2**
- Unusual financial movements.
- Severity and explanatory text for each finding.
- Disclaimer describing the scope of the report.

The report generator may produce additional pages if the content exceeds the available page space.

---

## Running Automated Tests

LedgerIQ uses pytest to check the behaviour of its core modules.

With the virtual environment activated, run:

```bat
python -m pytest -v
```

The test suite covers:

- Financial metric calculations.
- Revenue and net income anomaly detection.
- CSV validation.
- Excel workbook creation and contents.
- PDF generation and expected report sections.

The initial test suite was designed around 17 tests. Run the command to verify the actual result for your current checkout before publishing or releasing changes.

A passing test suite provides evidence that the tested cases work as expected; it does not guarantee that every possible input or financial scenario is handled correctly.

---

## Data Handling and Security

LedgerIQ is currently a local Streamlit application.

- Uploaded data is processed by the running application.
- The current project does not implement a dedicated database for uploaded statements.
- Excel and PDF reports are generated when requested.
- The sample dataset is fictional and intended for demonstration.
- The `.gitignore` file excludes the local virtual environment and selected private-data and generated-report directories.

Do not commit confidential financial statements, credentials, `.env` files, or generated reports containing sensitive information to a public repository.

The `.gitignore` rules reduce the risk of accidental commits but do not guarantee that every sensitive file is excluded. Review `git status` and staged files before committing.

---

## Limitations

LedgerIQ V1.0 is an initial release with a deliberately limited scope.

- It supports CSV input rather than direct integration with accounting systems.
- The required schema is fixed.
- Anomaly detection is rule-based, not machine-learning-based.
- The thresholds are not industry-specific.
- The current implementation does not perform a complete accounting reconciliation.
- Ratio calculations depend on the definitions and quality of the supplied data.
- The dashboard's INR formatting is for display; input amounts are not automatically converted from another currency.
- The tool does not independently verify the accuracy of financial statements.
- Report formatting and behaviour should be tested with different data sizes and edge cases.

These limitations should be considered when interpreting the results.

---

## Future Improvements

Potential improvements for future versions include:

- More robust validation of dates, reporting periods, and accounting relationships.
- Better handling of negative earnings, negative equity, and zero denominators.
- Additional ratios, including operating margin and return on equity.
- Configurable anomaly thresholds.
- More advanced period-over-period comparisons.
- Improved report formatting and configurable reporting currency.
- Support for additional input formats.
- Expanded automated tests and continuous integration.
- Additional data visualisations and report customisation.

These are possible future enhancements, not features guaranteed to be present in V1.0.

---

## Disclaimer

LedgerIQ is an educational financial analysis project. It is intended to assist with exploring financial statements and identifying movements that may warrant further investigation.

It is **not** a substitute for professional accounting advice, an independent audit, forensic investigation, or investment advice. Financial calculations and screening alerts should be independently reviewed before being used to support business or financial decisions.

The included sample financial data is fictional and should not be interpreted as the financial performance of any real organisation.

---

## Author

Developed as a Python and Streamlit project focused on financial statement analysis, data validation, financial ratios, and rule-based anomaly detection.

**GitHub:** [gvraghav1729](https://github.com/gvraghav1729)

---

*LedgerIQ V1.0 — Financial Statement Analysis & Intelligence.*
