# 📊 Financial Report Automation
### Python · Pandas · openpyxl · yfinance · Power BI

An end-to-end automated pipeline that extracts real-time stock market data, processes financial metrics, and delivers a formatted multi-sheet Excel report — ready to share with stakeholders or feed into a Power BI dashboard.

---

## 🚀 What it does

| Step | Tool | Description |
|------|------|-------------|
| **Extract** | yfinance + curl_cffi | Pulls 12 months of closing prices for 8 S&P 500 tickers |
| **Process** | Pandas | Calculates returns, volatility, rankings and correlation |
| **Report** | openpyxl + matplotlib | Generates a formatted Excel report with charts |
| **Dashboard** | Power BI | Interactive dashboard connected to the CSV output |

---

## 📁 Project Structure

```
financial-reporting-automation/
│
├── Scripts/
│   ├── main.py               ← Orchestrator — runs the full pipeline
│   ├── extractor.py          ← Data extraction via yfinance
│   ├── processor.py          ← Metrics calculation via Pandas
│   └── report_generator.py  ← Excel report generation via openpyxl
│
├── output/                   ← Generated files (git-ignored)
│   ├── financial_report.xlsx
│   └── portfolio_data.csv    ← Power BI data source
│
├── assets/                   ← Generated chart images (git-ignored)
│   ├── performance_chart.png
│   └── correlation_heatmap.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📈 Output — Excel Report

The pipeline generates a 4-sheet Excel workbook:

- **Raw Data** — Daily closing prices for all tickers, formatted as a structured table
- **KPI Summary** — One row per asset: initial price, final price, cumulative return, annualized volatility, best/worst day. Conditional formatting highlights positive returns in green and negative in red
- **Performance Chart** — Line chart showing cumulative return evolution for all assets over the period
- **Correlation Heatmap** — Visual matrix showing correlation between all assets

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/financial-reporting-automation.git
cd financial-reporting-automation

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python Scripts/main.py
```

The pipeline runs in sequence and prints progress to the terminal:

```
============================================================
  Financial Report Automation
============================================================

📥  STEP 1 — Data extraction (yfinance)
------------------------------------------------------------
[Extractor] Downloading last 12 months of data...
[Extractor] Tickers: AAPL, MSFT, GOOGL, AMZN, TSLA, META, NVDA, JPM
[Extractor] 252 trading days — 8/8 tickers ✓

⚙️   STEP 2 — Processing (pandas)
------------------------------------------------------------

📊  STEP 3 — Report generation (openpyxl + matplotlib)
------------------------------------------------------------

✅  Pipeline completed in 18.4s
============================================================
```

Output files are saved to the `output/` folder.

---

## 📊 Tickers Tracked

| Ticker | Company |
|--------|---------|
| AAPL | Apple |
| MSFT | Microsoft |
| GOOGL | Alphabet (Google) |
| AMZN | Amazon |
| TSLA | Tesla |
| META | Meta Platforms |
| NVDA | NVIDIA |
| JPM | JPMorgan Chase |

To change the tickers, edit the `TICKERS` list in `Scripts/extractor.py`.

---

## 🔌 Power BI Integration

After running the pipeline, connect Power BI to the generated CSV:

1. Open Power BI Desktop
2. **Get Data** → **Text/CSV**
3. Select `output/portfolio_data.csv`
4. Build your visuals — the CSV contains all processed metrics per ticker per day

To refresh the data, simply re-run `main.py` and click **Refresh** in Power BI.

---

## 📦 Dependencies

```
yfinance
pandas
openpyxl
matplotlib
curl_cffi
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 👤 About

Built by **Rafael Narciso** — FP&A Analyst at Cushman & Wakefield (Fortune 500), responsible for financial dashboards across South America.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/rafael-narciso-875a40188/)
