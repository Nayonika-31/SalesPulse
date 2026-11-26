# SalesPulse

A sales dashboard built with Python, Streamlit, Pandas, and Plotly.

Spreadsheets make it tough to see which deals are actually moving and which ones are stuck. I built SalesPulse to keep track of revenue, spot stalled deals, and see which accounts need a follow-up right away.

## What is inside

Overview shows total won revenue, open pipeline, win rate, and monthly sales trends, along with breakdowns by product and region.

Lead Intelligence helps find the best accounts to contact next. It compares engagement against deal size, lets you filter by buying signals like pricing page visits or new funding, and gives a quick follow-up tip for each lead.

Pipeline and Velocity breaks down open deals by industry and sales stage, compares rep performance, and flags deals that have had no activity for over 21 days.

Use the sidebar filters to sort everything by region, industry, sales owner, or product.

## How to run it

Clone the repo, install the libraries, and run Streamlit:

```
git clone [https://github.com/Nayonika-31/SalesPulse.git](https://github.com/Nayonika-31/SalesPulse.git)
cd SalesPulse
python -m pip install -r requirements.txt
python -m streamlit run app.py

```

Open http://localhost:8501 in your browser once it starts.

## About the data

`data/sales_leads.csv` has 800 sample B2B sales records made for this project. Priority scores are calculated using simple rules based on engagement, buying signals, and recent activity. SQL versions of the main queries are in `sql/analysis_queries.sql`.