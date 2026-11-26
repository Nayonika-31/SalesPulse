# SalesPulse — Sales Intelligence Workspace

A portfolio project built with Streamlit, Python, Pandas and Plotly. SalesPulse helps a sales team review revenue performance, explore its pipeline, prioritise accounts and decide where follow-up may be useful.

## Features

- Revenue overview: closed-won revenue, open pipeline, weighted pipeline, win rate and average deal size.
- Pipeline analysis: opportunity value by stage and industry, stage distribution and inactive opportunities.
- Lead intelligence: searchable account/contact table, filters for region/industry/owner, intent signal filters and a rule-based priority score.
- Account brief: a simple suggested follow-up based on the account's latest signal and activity recency.
- CSV export of the filtered lead list.

## Run locally

1. Extract the project folder.
2. Open a terminal in the `SalesPulse` folder (the folder containing `app.py` and `requirements.txt`).
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Launch:

   ```bash
   python -m streamlit run app.py
   ```

5. Open the local URL printed in the terminal (usually http://localhost:8501).

## Data and limitations

- `data/sales_leads.csv` contains 800 fictional prospect/opportunity records generated with a fixed random seed.
- All company names, contacts, revenue figures, deal values and activity signals are synthetic.
- Priority score is an explainable, rule-based score using engagement, intent signal and days since last activity. It is not machine learning or an AI prediction.
- The app does not connect to a live CRM, enrich contacts from external providers, send emails or automate outreach.
- The SQL file contains example analysis queries; the running dashboard reads the included CSV using Pandas and does not connect to a SQL database.

## How to explain it

"SalesPulse is a sales analytics dashboard I built to help a team understand its pipeline and decide which accounts to follow up with. I created a synthetic dataset of 800 prospects and opportunities, used Python and Pandas to analyse revenue, deal stages, lead sources and engagement signals, and built an interactive Streamlit dashboard. It includes a rule-based priority score so users can filter accounts by potential interest and review suggested follow-up actions. The goal is to make sales performance and account prioritisation easier to understand."

## Suggested resume bullets

- Built an interactive sales intelligence dashboard using Python, Pandas and Streamlit to track revenue, pipeline performance and lead engagement.
- Analysed 800 synthetic prospect records to segment accounts, compare lead sources and prioritise follow-ups using rule-based scoring.

**Tech Stack:** Python, Pandas, Streamlit, Plotly, SQL (example analysis queries)
