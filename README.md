```markdown
# SalesPulse

A sales pipeline and revenue dashboard built with Python, Streamlit, Pandas, and Plotly.

I built this to solve a common problem for small B2B sales teams: figuring out which deals are actually moving, which ones are stalling, and where reps should focus their follow-ups without digging through messy spreadsheets.

## What's inside

* **Overview:** Tracks closed-won revenue, open pipeline, weighted forecast, and win rate. Includes monthly vs. cumulative revenue pacing, product-line revenue share, a regional and product heatmap, and channel performance.
* **Lead Intelligence:** Plots account engagement against deal size so high-value active leads stand out immediately. Lets you filter by intent signal (pricing page visits, funding announcements, hiring growth), export filtered CSVs, and pull up a quick follow-up brief for any account.
* **Pipeline & Velocity:** Breaks down open deals by industry and funnel stage, shows deal-size distributions, compares rep performance, and flags opportunities that have gone quiet for 21+ days.
* **Sidebar Filters:** Slice the entire dashboard live by region, industry, sales owner, and product line.

## Project structure

```text
SalesPulse/
├── .streamlit/
│   └── config.toml          # Theme colors and typography
├── data/
│   └── sales_leads.csv      # 800 synthetic B2B prospect records
├── sql/
│   └── analysis_queries.sql # SQL equivalents for the core pipeline metrics
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies
└── README.md

```

## Running it locally

```bash
git clone [https://github.com/Nayonika-31/SalesPulse.git](https://github.com/Nayonika-31/SalesPulse.git)
cd SalesPulse
python -m pip install -r requirements.txt
python -m streamlit run app.py

```

Open `http://localhost:8501` in your browser once Streamlit starts.

## Notes on the data

* Everything in `data/sales_leads.csv` (800 accounts, deal values, contacts, and activity dates) is synthetic data generated for this project.
* Priority scores are rule-based, calculated from engagement score, recent intent signals, and days since last touch, rather than a black-box ML model.

```

```