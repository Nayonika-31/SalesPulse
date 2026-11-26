-- SalesPulse: example SQL analysis queries
-- These queries illustrate how the CSV dataset could be analysed in a SQL database.
-- The Streamlit app currently reads the CSV directly with Pandas.

-- 1. Pipeline value by stage
SELECT
    stage,
    COUNT(*) AS opportunity_count,
    SUM(deal_value_usd) AS pipeline_value_usd
FROM sales_leads
WHERE stage NOT IN ('Closed Won', 'Closed Lost')
GROUP BY stage
ORDER BY pipeline_value_usd DESC;

-- 2. Lead source performance
SELECT
    lead_source,
    COUNT(*) AS total_leads,
    SUM(CASE WHEN stage = 'Closed Won' THEN deal_value_usd ELSE 0 END) AS won_revenue_usd,
    SUM(CASE WHEN stage IN ('Closed Won', 'Closed Lost') THEN 1 ELSE 0 END) AS closed_deals
FROM sales_leads
GROUP BY lead_source
ORDER BY won_revenue_usd DESC;

-- 3. Accounts to prioritise for follow-up
SELECT
    company,
    lead_name,
    industry,
    stage,
    engagement_score,
    intent_signal,
    days_since_last_activity,
    priority_score
FROM sales_leads
WHERE priority_score >= 70
ORDER BY priority_score DESC, engagement_score DESC;
