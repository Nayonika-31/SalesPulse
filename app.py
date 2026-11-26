import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="SalesPulse | Revenue Intelligence",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_PATH = Path(__file__).parent / "data" / "sales_leads.csv"

# ---------- Google Material 3 Visual System ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

:root {
    --bg-canvas: #F8FAFD;
    --surface: #FFFFFF;
    --surface-tonal: #EEF3FC;
    --ink-primary: #202124;
    --ink-secondary: #5F6368;
    --ink-muted: #80868B;
    --border-hairline: #E8EAED;
    --google-blue: #1A73E8;
    --google-green: #1E8E3E;
    --google-amber: #F9AB00;
    --google-red: #D93025;
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--ink-primary);
}

.stApp {
    background-color: var(--bg-canvas);
}

header[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] {
    display: none !important;
}

.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1500px;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid var(--border-hairline);
}

[data-testid="stSidebar"] [data-baseweb="tag"] {
    background-color: #E8F0FE !important;
    color: #1967D2 !important;
    border: none !important;
    border-radius: 999px !important;
    padding: 2px 10px !important;
    font-weight: 500 !important;
}

[data-testid="stSidebar"] [data-baseweb="tag"] span {
    color: #1967D2 !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: #F8FAFD !important;
    border: 1px solid #DADCE0 !important;
    border-radius: 12px !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] > div:hover {
    border-color: #1A73E8 !important;
}

h1, h2, h3, h4 {
    font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
    letter-spacing: -0.025em;
    color: var(--ink-primary);
}

p, label {
    color: var(--ink-secondary);
}

/* Google Workspace Header Banner */
.g-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #FFFFFF;
    border: 1px solid #E8EAED;
    border-radius: 20px;
    padding: 18px 24px;
    margin-bottom: 18px;
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.06);
}

.g-brand-wrap {
    display: flex;
    align-items: center;
    gap: 14px;
}

.g-logo-badge {
    width: 44px;
    height: 44px;
    border-radius: 14px;
    background: linear-gradient(135deg, #1A73E8 0%, #4285F4 60%, #34A853 100%);
    color: #FFFFFF;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: 800;
    box-shadow: 0 3px 10px rgba(26, 115, 232, 0.24);
}

.g-eyebrow {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #1A73E8;
    margin-bottom: 2px;
}

.g-hero-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 23px;
    font-weight: 800;
    color: #202124;
    line-height: 1.2;
}

.g-hero-sub {
    font-size: 13.5px;
    color: #5F6368;
    margin-top: 2px;
}

.g-status-chip {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: #E8F0FE;
    color: #1967D2;
    font-size: 12px;
    font-weight: 600;
    padding: 7px 14px;
    border-radius: 999px;
}

.g-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #1E8E3E;
    display: inline-block;
}

/* KPI Metric Cards */
.g-kpi-card {
    background: #FFFFFF;
    border: 1px solid #E8EAED;
    border-radius: 18px;
    padding: 18px 20px;
    min-height: 124px;
    transition: all 0.18s cubic-bezier(0.2, 0, 0, 1);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.04);
    position: relative;
    overflow: hidden;
}

.g-kpi-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(60, 64, 67, 0.09);
    border-color: #D2E3FC;
}

.g-kpi-accent {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3.5px;
}

.g-kpi-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
}

.g-kpi-label {
    font-size: 12px;
    font-weight: 600;
    color: #5F6368;
}

.g-kpi-pill {
    font-size: 11px;
    font-weight: 600;
    padding: 3px 9px;
    border-radius: 999px;
}

.g-kpi-value {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 29px;
    font-weight: 800;
    color: #202124;
    letter-spacing: -0.03em;
    line-height: 1.15;
}

.g-kpi-note {
    font-size: 12px;
    color: #80868B;
    margin-top: 6px;
}

/* Chart & Section Containers */
.g-card {
    background: #FFFFFF;
    border: 1px solid #E8EAED;
    border-radius: 18px;
    padding: 20px 22px;
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.04);
    margin-bottom: 16px;
}

.g-card-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 8px;
}

.g-card-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 16px;
    font-weight: 700;
    color: #202124;
    margin-bottom: 2px;
}

.g-card-sub {
    font-size: 12.5px;
    color: #5F6368;
    margin-bottom: 10px;
}

.g-badge-mini {
    font-size: 11px;
    font-weight: 600;
    background: #F1F3F4;
    color: #3C4043;
    padding: 3px 10px;
    border-radius: 999px;
}

/* Tonal Next-Step Callout */
.g-action-banner {
    background: linear-gradient(135deg, #EEF3FC 0%, #F4F8FE 100%);
    border: 1px solid #D2E3FC;
    border-radius: 16px;
    padding: 18px 20px;
    margin-top: 12px;
}

.g-action-tag {
    display: inline-block;
    background: #1A73E8;
    color: #FFFFFF;
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 999px;
    margin-bottom: 8px;
}

.g-action-text {
    font-size: 14.5px;
    font-weight: 600;
    color: #174EA6;
    line-height: 1.45;
}

/* Material 3 Segmented Pill Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: #FFFFFF;
    padding: 6px;
    border-radius: 999px;
    border: 1px solid #E8EAED;
    width: fit-content;
    margin-bottom: 16px;
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.04);
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border-radius: 999px !important;
    padding: 8px 20px !important;
    font-weight: 600 !important;
    font-size: 13.5px !important;
    color: #5F6368 !important;
    border: none !important;
    transition: all 0.15s ease;
}

.stTabs [data-baseweb="tab"]:hover {
    background-color: #F1F3F4 !important;
    color: #202124 !important;
}

.stTabs [aria-selected="true"] {
    background-color: #E8F0FE !important;
    color: #1967D2 !important;
    border-bottom: none !important;
}

.stTabs [data-baseweb="tab-highlight"] {
    display: none !important;
}

/* DataFrames & Inputs */
div[data-testid="stDataFrame"] {
    border: 1px solid #E8EAED;
    border-radius: 14px;
    overflow: hidden;
    background: #FFFFFF;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    border-radius: 12px !important;
    border-color: #DADCE0 !important;
    background-color: #FFFFFF !important;
}

.stButton button, .stDownloadButton button {
    border-radius: 999px !important;
    border: 1px solid #DADCE0 !important;
    background-color: #FFFFFF !important;
    color: #1A73E8 !important;
    font-weight: 600 !important;
    padding: 0.45rem 1.2rem !important;
    transition: all 0.15s ease;
}

.stButton button:hover, .stDownloadButton button:hover {
    background-color: #F1F6FE !important;
    border-color: #1A73E8 !important;
}

hr {
    border-color: #E8EAED;
    margin: 1.4rem 0;
}
</style>
""", unsafe_allow_html=True)

# ---------- Color Palettes (Google Material 3) ----------
GOOGLE_PALETTE = ["#1A73E8", "#1E8E3E", "#F9AB00", "#D93025", "#9334E6", "#007B83", "#E8710A", "#3F51B5"]
STAGE_COLORS = {
    "New": "#8AB4F8",
    "Qualified": "#4285F4",
    "Meeting Scheduled": "#1A73E8",
    "Proposal": "#F9AB00",
    "Negotiation": "#1E8E3E",
    "Closed Won": "#137333",
    "Closed Lost": "#D93025",
}
STAGE_ORDER_OPEN = ["New", "Qualified", "Meeting Scheduled", "Proposal", "Negotiation"]
STAGE_ORDER_ALL = ["New", "Qualified", "Meeting Scheduled", "Proposal", "Negotiation", "Closed Won", "Closed Lost"]


@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)
    data["created_date"] = pd.to_datetime(data["created_date"])
    data["expected_close_date"] = pd.to_datetime(data["expected_close_date"])
    return data


df = load_data()


def money(value):
    if value >= 1_000_000:
        return f"${value/1_000_000:.2f}M"
    if value >= 1000:
        return f"${value/1000:.0f}K"
    return f"${value:,.0f}"


def kpi_card(label, value, note, badge_text, accent_color="#1A73E8", badge_bg="#E8F0FE", badge_fg="#1967D2"):
    st.markdown(f"""
    <div class="g-kpi-card">
        <div class="g-kpi-accent" style="background:{accent_color};"></div>
        <div class="g-kpi-header">
            <span class="g-kpi-label">{label}</span>
            <span class="g-kpi-pill" style="background:{badge_bg}; color:{badge_fg};">{badge_text}</span>
        </div>
        <div class="g-kpi-value">{value}</div>
        <div class="g-kpi-note">{note}</div>
    </div>
    """, unsafe_allow_html=True)


def style_plotly(fig, height=340, show_legend=True):
    fig.update_layout(
        height=height,
        margin=dict(l=10, r=16, t=28, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color="#5F6368", size=12),
        hoverlabel=dict(
            bgcolor="#202124",
            font_size=12,
            font_family="Inter, sans-serif",
            font_color="#FFFFFF",
            bordercolor="#202124",
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            linecolor="#E8EAED",
            tickfont=dict(color="#5F6368", size=11),
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="#F1F3F4",
            zeroline=False,
            tickfont=dict(color="#5F6368", size=11),
        ),
        showlegend=show_legend,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            font=dict(size=11.5, color="#3C4043"),
        ),
    )
    return fig


# ---------- Sidebar Controls ----------
with st.sidebar:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:11px;padding:6px 0 12px 0;">
        <div class="g-logo-badge" style="width:36px;height:36px;border-radius:11px;font-size:16px;">✦</div>
        <div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:17px;color:#202124;">SalesPulse</div>
            <div style="font-size:11px;font-weight:600;color:#5F6368;">Revenue Intelligence</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("#### Workspace Filters")

    all_regions = sorted(df["region"].unique())
    all_industries = sorted(df["industry"].unique())
    all_owners = sorted(df["sales_owner"].unique())
    all_products = sorted(df["product_interest"].unique())

    regions = st.multiselect("Region", all_regions, default=all_regions)
    industries = st.multiselect("Industry", all_industries, default=all_industries)
    owners = st.multiselect("Sales Owner", all_owners, default=all_owners)
    products = st.multiselect("Product Line", all_products, default=all_products)

    if st.button("Reset all filters", use_container_width=True):
        st.rerun()

    st.markdown("---")
    st.markdown("""
    <div style="background:#F8FAFD;border:1px solid #E8EAED;border-radius:14px;padding:12px 14px;">
        <div style="font-size:10.5px;font-weight:700;letter-spacing:0.08em;color:#1A73E8;text-transform:uppercase;">Dataset Snapshot</div>
        <div style="font-size:12.5px;font-weight:600;color:#202124;margin-top:4px;">800 B2B Prospect Records</div>
        <div style="font-size:11.5px;color:#5F6368;margin-top:2px;">Currency: USD · Synthetic CRM Feed</div>
    </div>
    """, unsafe_allow_html=True)

# Apply filters safely
mask = (
    df["region"].isin(regions if regions else all_regions)
    & df["industry"].isin(industries if industries else all_industries)
    & df["sales_owner"].isin(owners if owners else all_owners)
    & df["product_interest"].isin(products if products else all_products)
)

filtered = df[mask].copy()
open_deals = filtered[~filtered["stage"].isin(["Closed Won", "Closed Lost"])]
won = filtered[filtered["stage"] == "Closed Won"]
closed = filtered[filtered["stage"].isin(["Closed Won", "Closed Lost"])]

won_revenue = won["deal_value_usd"].sum()
pipeline = open_deals["deal_value_usd"].sum()
weighted_pipeline = (open_deals["deal_value_usd"] * open_deals["stage_probability"]).sum()
win_rate = (len(won) / len(closed) * 100) if len(closed) else 0
avg_deal = filtered["deal_value_usd"].mean() if len(filtered) else 0
capture_ratio = (weighted_pipeline / pipeline * 100) if pipeline else 0

# ---------- Top Hero Header ----------
st.markdown(f"""
<div class="g-topbar">
    <div class="g-brand-wrap">
        <div class="g-logo-badge">✦</div>
        <div>
            <div class="g-eyebrow">Go-To-Market Intelligence</div>
            <div class="g-hero-title">Good morning. Here's your sales pulse.</div>
            <div class="g-hero-sub">Interactive revenue analytics, multi-dimensional pipeline visualisations, and account intent signals across {len(filtered):,} accounts.</div>
        </div>
    </div>
    <div class="g-status-chip">
        <span class="g-dot"></span>
        <span>{len(open_deals):,} Active Deals Tracked</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- KPI Strip ----------
m1, m2, m3, m4 = st.columns(4)
with m1:
    kpi_card(
        "Closed-Won Revenue",
        money(won_revenue),
        f"Across {len(won):,} won opportunities",
        f"{len(won):,} Won",
        accent_color="#1E8E3E",
        badge_bg="#E6F4EA",
        badge_fg="#137333",
    )
with m2:
    kpi_card(
        "Open Pipeline",
        money(pipeline),
        f"{len(open_deals):,} active opportunities in flight",
        "Active Funnel",
        accent_color="#1A73E8",
        badge_bg="#E8F0FE",
        badge_fg="#1967D2",
    )
with m3:
    kpi_card(
        "Weighted Forecast",
        money(weighted_pipeline),
        "Adjusted by stage win probability",
        f"{capture_ratio:.0f}% Yield",
        accent_color="#F9AB00",
        badge_bg="#FEF7E0",
        badge_fg="#B06000",
    )
with m4:
    kpi_card(
        "Overall Win Rate",
        f"{win_rate:.1f}%",
        f"Avg. deal size {money(avg_deal)}",
        f"{len(closed):,} Closed",
        accent_color="#9334E6",
        badge_bg="#F3E8FD",
        badge_fg="#7627BB",
    )

st.write("")

# ---------- Main Navigation Tabs ----------
tab_overview, tab_leads, tab_pipeline = st.tabs([
    "Executive Overview",
    "Lead Intelligence",
    "Pipeline & Velocity",
])

# ==================== TAB 1: EXECUTIVE OVERVIEW ====================
with tab_overview:
    # Row 1: Cumulative Revenue & Forecast Combo Chart + Product Line Donut
    r1_left, r1_right = st.columns([1.6, 1.0], gap="medium")

    with r1_left:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-header">
                <div>
                    <div class="g-card-title">Monthly Revenue & Weighted Forecast Trajectory</div>
                    <div class="g-card-sub">Monthly Closed-Won bars overlaid with Weighted Open Pipeline spline & cumulative pacing</div>
                </div>
                <span class="g-badge-mini">Combo Chart</span>
            </div>
        """, unsafe_allow_html=True)

        view_mode = st.radio(
            "Trajectory View",
            ["Monthly Breakdown", "Cumulative Pacing"],
            horizontal=True,
            label_visibility="collapsed",
        )

        won_m = won.copy()
        open_m = open_deals.copy()
        if not won_m.empty or not open_m.empty:
            won_m["month"] = won_m["expected_close_date"].dt.to_period("M").astype(str)
            open_m["month"] = open_m["expected_close_date"].dt.to_period("M").astype(str)
            open_m["weighted_val"] = open_m["deal_value_usd"] * open_m["stage_probability"]

            w_grp = won_m.groupby("month", as_index=False)["deal_value_usd"].sum().rename(columns={"deal_value_usd": "Closed Won"})
            o_grp = open_m.groupby("month", as_index=False)["weighted_val"].sum().rename(columns={"weighted_val": "Weighted Pipeline"})
            merged_trend = pd.merge(w_grp, o_grp, on="month", how="outer").fillna(0).sort_values("month")

            if view_mode == "Cumulative Pacing":
                merged_trend["Closed Won"] = merged_trend["Closed Won"].cumsum()
                merged_trend["Weighted Pipeline"] = merged_trend["Weighted Pipeline"].cumsum()

            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=merged_trend["month"],
                y=merged_trend["Closed Won"],
                name="Closed-Won Revenue",
                marker_color="#1A73E8",
                opacity=0.88,
                hovertemplate="<b>%{x}</b><br>Closed Won: $%{y:,.0f}<extra></extra>",
            ))
            fig.add_trace(go.Scatter(
                x=merged_trend["month"],
                y=merged_trend["Weighted Pipeline"],
                name="Weighted Open Forecast",
                mode="lines+markers",
                line=dict(color="#1E8E3E", width=3, shape="spline"),
                marker=dict(size=7, color="#1E8E3E", line=dict(width=2, color="#FFFFFF")),
                fill="tozeroy",
                fillcolor="rgba(30, 142, 62, 0.08)",
                hovertemplate="<b>%{x}</b><br>Weighted Forecast: $%{y:,.0f}<extra></extra>",
            ))
            fig.update_layout(barmode="overlay", hovermode="x unified")
            fig.update_yaxes(tickprefix="$", tickformat="~s", title="")
            fig.update_xaxes(title="")
            st.plotly_chart(style_plotly(fig, 310, show_legend=True), use_container_width=True)
        else:
            st.info("No deals available for the selected filter combination.")
        st.markdown("</div>", unsafe_allow_html=True)

    with r1_right:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-header">
                <div>
                    <div class="g-card-title">Revenue Mix by Product Line</div>
                    <div class="g-card-sub">Share of total Closed-Won bookings across product suites</div>
                </div>
                <span class="g-badge-mini">Donut</span>
            </div>
        """, unsafe_allow_html=True)

        prod_df = won.groupby("product_interest", as_index=False)["deal_value_usd"].sum().sort_values("deal_value_usd", ascending=False)
        if not prod_df.empty:
            fig_donut = px.pie(
                prod_df,
                names="product_interest",
                values="deal_value_usd",
                hole=0.62,
                color_discrete_sequence=["#1A73E8", "#1E8E3E", "#F9AB00", "#9334E6"],
            )
            fig_donut.update_traces(
                textposition="inside",
                textinfo="percent",
                marker=dict(line=dict(color="#FFFFFF", width=2.5)),
                hovertemplate="<b>%{label}</b><br>Revenue: $%{value:,.0f}<br>Share: %{percent}<extra></extra>",
            )
            fig_donut.update_traces(domain=dict(x=[0.05, 0.95], y=[0.24, 0.98]))
            fig_donut.add_annotation(
                text=f"<b>{money(won_revenue)}</b><br><span style='font-size:11px;color:#5F6368'>Total Won</span>",
                x=0.5, y=0.61, font_size=16, showarrow=False, font_color="#202124"
            )
            fig_donut = style_plotly(fig_donut, 375, show_legend=True)
            fig_donut.update_layout(
                margin=dict(l=10, r=10, t=12, b=24),
                legend=dict(
                    orientation="h",
                    yanchor="top",
                    y=0.14,
                    xanchor="center",
                    x=0.5,
                    font=dict(size=11.5, color="#3C4043"),
                )
            )
            st.plotly_chart(fig_donut, use_container_width=True)
        else:
            st.info("No closed-won product data in selected filters.")
        st.markdown("</div>", unsafe_allow_html=True)

    # Row 2: Regional x Product Heatmap + Channel Efficiency Quadrant
    r2_left, r2_right = st.columns([1.15, 1.15], gap="medium")

    with r2_left:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-header">
                <div>
                    <div class="g-card-title">Regional × Product Pipeline Heatmap</div>
                    <div class="g-card-sub">Open pipeline concentration across territories and product lines</div>
                </div>
                <span class="g-badge-mini">Matrix</span>
            </div>
        """, unsafe_allow_html=True)

        if not open_deals.empty:
            piv = open_deals.pivot_table(
                index="region",
                columns="product_interest",
                values="deal_value_usd",
                aggfunc="sum",
                fill_value=0,
            )
            text_matrix = [[money(val) for val in row] for row in piv.values]
            fig_heat = go.Figure(data=go.Heatmap(
                z=piv.values,
                x=piv.columns.tolist(),
                y=piv.index.tolist(),
                text=text_matrix,
                texttemplate="%{text}",
                textfont=dict(size=11.5, family="Inter"),
                colorscale=[[0, "#F8FAFD"], [0.4, "#D2E3FC"], [0.75, "#4285F4"], [1, "#174EA6"]],
                showscale=False,
                hovertemplate="<b>%{y} · %{x}</b><br>Open Pipeline: $%{z:,.0f}<extra></extra>",
            ))
            fig_heat = style_plotly(fig_heat, 315, show_legend=False)
            fig_heat.update_xaxes(side="top", showgrid=False)
            fig_heat.update_yaxes(showgrid=False, autorange="reversed")
            st.plotly_chart(fig_heat, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with r2_right:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-header">
                <div>
                    <div class="g-card-title">Acquisition Channel Matrix</div>
                    <div class="g-card-sub">Lead volume vs. Closed-Won revenue (bubble size = avg. deal size)</div>
                </div>
                <span class="g-badge-mini">Bubble Scatter</span>
            </div>
        """, unsafe_allow_html=True)

        src = filtered.groupby("lead_source", as_index=False).agg(
            leads=("company", "count"),
            avg_val=("deal_value_usd", "mean"),
            won_rev=("deal_value_usd", lambda s: s[filtered.loc[s.index, "stage"].eq("Closed Won")].sum()),
        )
        if not src.empty:
            fig_src = px.scatter(
                src,
                x="leads",
                y="won_rev",
                size="avg_val",
                color="lead_source",
                text="lead_source",
                color_discrete_sequence=GOOGLE_PALETTE,
                size_max=44,
            )
            fig_src.add_hline(y=src["won_rev"].mean(), line_dash="dot", line_color="#DADCE0")
            fig_src.add_vline(x=src["leads"].mean(), line_dash="dot", line_color="#DADCE0")
            fig_src.update_traces(
                textposition="top center",
                marker=dict(opacity=0.88, line=dict(width=1.5, color="#FFFFFF")),
                hovertemplate="<b>%{text}</b><br>Leads: %{x}<br>Closed-Won: $%{y:,.0f}<br>Avg Deal: $%{marker.size:,.0f}<extra></extra>",
            )
            fig_src.update_xaxes(title="Total Leads", showgrid=True, gridcolor="#F1F3F4")
            fig_src.update_yaxes(title="Closed-Won Revenue", tickprefix="$", tickformat="~s")
            st.plotly_chart(style_plotly(fig_src, 315, show_legend=False), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Row 3: Priority Accounts Table
    st.markdown("""
    <div class="g-card">
        <div class="g-card-header">
            <div>
                <div class="g-card-title">Top Priority Accounts to Review</div>
                <div class="g-card-sub">Highest-scoring active opportunities ranked by intent & engagement</div>
            </div>
            <span class="g-badge-mini">Live Action Queue</span>
        </div>
    """, unsafe_allow_html=True)

    priority = open_deals.sort_values(["priority_score", "engagement_score"], ascending=False).head(8)
    show = priority[["company", "industry", "product_interest", "stage", "priority_score", "engagement_score", "deal_value_usd", "intent_signal", "sales_owner"]].rename(
        columns={
            "company": "Account",
            "industry": "Industry",
            "product_interest": "Product",
            "stage": "Stage",
            "priority_score": "Priority",
            "engagement_score": "Engagement",
            "deal_value_usd": "Deal Value",
            "intent_signal": "Intent Signal",
            "sales_owner": "Owner",
        }
    )
    st.dataframe(
        show,
        use_container_width=True,
        hide_index=True,
        height=300,
        column_config={
            "Priority": st.column_config.ProgressColumn("Priority", format="%d", min_value=0, max_value=100),
            "Engagement": st.column_config.ProgressColumn("Engagement", format="%d", min_value=0, max_value=100),
            "Deal Value": st.column_config.NumberColumn("Deal Value", format="$%d"),
        },
    )
    st.markdown("</div>", unsafe_allow_html=True)


# ==================== TAB 2: LEAD INTELLIGENCE ====================
with tab_leads:
    # Top Visual Row in Lead Intelligence: Opportunity Quadrant + Intent Signal Lift
    l1, l2 = st.columns([1.35, 1.0], gap="medium")

    with l1:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-header">
                <div>
                    <div class="g-card-title">Account Prioritisation Quadrant</div>
                    <div class="g-card-sub">Engagement Score vs. Deal Value across open deals (sized by Priority Score)</div>
                </div>
                <span class="g-badge-mini">Interactive Scatter</span>
            </div>
        """, unsafe_allow_html=True)

        if not open_deals.empty:
            fig_quad = px.scatter(
                open_deals,
                x="engagement_score",
                y="deal_value_usd",
                color="intent_signal",
                size="priority_score",
                hover_name="company",
                hover_data={"sales_owner": True, "stage": True, "priority_score": True, "deal_value_usd": ":$,.0f"},
                color_discrete_sequence=GOOGLE_PALETTE,
                size_max=18,
            )
            fig_quad.add_vline(x=50, line_dash="dash", line_color="#DADCE0")
            fig_quad.add_hline(y=open_deals["deal_value_usd"].median(), line_dash="dash", line_color="#DADCE0")
            fig_quad.update_traces(marker=dict(opacity=0.82, line=dict(width=1, color="#FFFFFF")))
            fig_quad.update_xaxes(title="Engagement Score (0–100)", showgrid=True, gridcolor="#F1F3F4")
            fig_quad.update_yaxes(title="Deal Value (USD)", tickprefix="$", tickformat="~s")
            st.plotly_chart(style_plotly(fig_quad, 330, show_legend=True), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with l2:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-header">
                <div>
                    <div class="g-card-title">Win Rate & Volume by Intent Signal</div>
                    <div class="g-card-sub">How buyer signals correlate with deal conversion</div>
                </div>
                <span class="g-badge-mini">Signal Lift</span>
            </div>
        """, unsafe_allow_html=True)

        sig_rows = []
        for sig, grp in filtered.groupby("intent_signal"):
            c_cnt = grp["stage"].isin(["Closed Won", "Closed Lost"]).sum()
            w_cnt = (grp["stage"] == "Closed Won").sum()
            wr = (w_cnt / c_cnt * 100) if c_cnt else 0
            sig_rows.append({"Signal": sig, "Win Rate": wr, "Accounts": len(grp)})
        sig_df = pd.DataFrame(sig_rows).sort_values("Win Rate", ascending=True)

        if not sig_df.empty:
            fig_sig = px.bar(
                sig_df,
                x="Win Rate",
                y="Signal",
                orientation="h",
                color="Win Rate",
                color_continuous_scale=["#AECBFA", "#1A73E8", "#1E8E3E"],
                text=sig_df["Win Rate"].apply(lambda v: f"{v:.1f}%"),
                custom_data=["Accounts"],
            )
            fig_sig.update_traces(
                textposition="outside",
                cliponaxis=False,
                hovertemplate="<b>%{y}</b><br>Win Rate: %{x:.1f}%<br>Total Accounts: %{customdata[0]}<extra></extra>",
            )
            fig_sig.update_layout(coloraxis_showscale=False)
            fig_sig.update_xaxes(title="Win Rate (%)", ticksuffix="%", range=[0, max(sig_df["Win Rate"].max() * 1.2, 10)])
            fig_sig.update_yaxes(title="", showgrid=False)
            st.plotly_chart(style_plotly(fig_sig, 330, show_legend=False), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Interactive Lead Explorer Table
    st.markdown("""
    <div class="g-card">
        <div class="g-card-title">Interactive Account & Signal Explorer</div>
        <div class="g-card-sub">Filter by intent signal, priority threshold, or account name to surface high-conversion opportunities</div>
    """, unsafe_allow_html=True)

    f1, f2, f3, f4 = st.columns([1.4, 1, 1, 1])
    with f1:
        search = st.text_input("Search account or contact", placeholder="e.g. Atlas, Aisha...")
    with f2:
        min_score = st.slider("Min. priority score", 0, 100, 40)
    with f3:
        signal_filter = st.selectbox("Intent signal", ["All signals"] + sorted(filtered["intent_signal"].unique().tolist()))
    with f4:
        stage_filter = st.selectbox("Funnel stage", ["All stages"] + sorted(filtered["stage"].unique().tolist()))

    leads = filtered[filtered["priority_score"] >= min_score].copy()
    if search:
        leads = leads[
            leads["company"].str.contains(search, case=False, na=False)
            | leads["lead_name"].str.contains(search, case=False, na=False)
        ]
    if signal_filter != "All signals":
        leads = leads[leads["intent_signal"] == signal_filter]
    if stage_filter != "All stages":
        leads = leads[leads["stage"] == stage_filter]

    leads = leads.sort_values(["priority_score", "engagement_score"], ascending=False)

    lead_view = leads[[
        "lead_name", "company", "industry", "stage", "deal_value_usd",
        "priority_score", "engagement_score", "intent_signal", "days_since_last_activity", "sales_owner"
    ]].rename(columns={
        "lead_name": "Contact",
        "company": "Account",
        "industry": "Industry",
        "stage": "Stage",
        "deal_value_usd": "Deal Value",
        "priority_score": "Priority",
        "engagement_score": "Engagement",
        "intent_signal": "Latest Signal",
        "days_since_last_activity": "Inactive (Days)",
        "sales_owner": "Owner",
    })

    st.dataframe(
        lead_view,
        use_container_width=True,
        hide_index=True,
        height=340,
        column_config={
            "Deal Value": st.column_config.NumberColumn("Deal Value", format="$%d"),
            "Priority": st.column_config.ProgressColumn("Priority", format="%d", min_value=0, max_value=100),
            "Engagement": st.column_config.ProgressColumn("Engagement", format="%d", min_value=0, max_value=100),
        },
    )

    dl_col, info_col = st.columns([1, 3])
    with dl_col:
        st.download_button(
            "⬇ Export Filtered CSV",
            data=leads.to_csv(index=False).encode("utf-8"),
            file_name="salespulse_filtered_leads.csv",
            mime="text/csv",
        )
    with info_col:
        st.caption(f"Showing {len(leads):,} matching accounts · Priority scores are rule-based indicators.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Account Deep-Dive Brief
    st.markdown("""
    <div class="g-card">
        <div class="g-card-title">Account Deep-Dive Brief</div>
        <div class="g-card-sub">Select an account below to inspect deal health and recommended next best action</div>
    """, unsafe_allow_html=True)

    if len(leads):
        selected = st.selectbox("Inspect Account", leads["company"].tolist(), label_visibility="collapsed")
        row = leads[leads["company"] == selected].iloc[0]

        a, b, c, d = st.columns(4)
        with a:
            kpi_card("Priority Score", f"{row['priority_score']}/100", f"Contact: {row['lead_name']}", "Score", "#1A73E8", "#E8F0FE", "#1967D2")
        with b:
            kpi_card("Deal Value", money(row["deal_value_usd"]), f"Stage: {row['stage']}", f"{int(row['stage_probability']*100)}% Prob.", "#1E8E3E", "#E6F4EA", "#137333")
        with c:
            kpi_card("Engagement", f"{row['engagement_score']}/100", row["intent_signal"], "Intent", "#F9AB00", "#FEF7E0", "#B06000")
        with d:
            kpi_card("Last Touch", f"{row['days_since_last_activity']}d ago", f"Owner: {row['sales_owner']}", row["region"], "#9334E6", "#F3E8FD", "#7627BB")

        if row["days_since_last_activity"] > 14:
            next_step = f"Re-engage {row['lead_name']} at {row['company']}: account activity has been quiet for {row['days_since_last_activity']} days."
        elif row["intent_signal"] == "Pricing page visit":
            next_step = f"Share a tailored pricing breakdown or ROI calculator with {row['lead_name']} following their recent pricing page visit."
        elif row["intent_signal"] == "Funding announcement":
            next_step = f"Congratulate {row['company']} on their recent funding milestone and align your pitch with their expansion goals."
        elif row["intent_signal"] == "Hiring growth":
            next_step = f"Highlight team onboarding and scalability workflows as {row['company']} expands headcount."
        else:
            next_step = f"Continue multi-threading with {row['lead_name']} and schedule a technical discovery check-in."

        st.markdown(f"""
        <div class="g-action-banner">
            <div class="g-action-tag">Recommended Next Step</div>
            <div class="g-action-text">{next_step}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("No leads match the current filter criteria. Lower the minimum priority score to inspect accounts.")
    st.markdown("</div>", unsafe_allow_html=True)


# ==================== TAB 3: PIPELINE & VELOCITY ====================
with tab_pipeline:
    # Row 1: Stacked Stage Breakdown by Industry + Deal Value Box/Strip Distribution
    p1, p2 = st.columns([1.3, 1.0], gap="medium")

    with p1:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-header">
                <div>
                    <div class="g-card-title">Open Pipeline Composition by Industry & Stage</div>
                    <div class="g-card-sub">Stacked breakdown showing where deals sit across verticals</div>
                </div>
                <span class="g-badge-mini">Stacked Bar</span>
            </div>
        """, unsafe_allow_html=True)

        if not open_deals.empty:
            ind_stage = open_deals.groupby(["industry", "stage"], as_index=False)["deal_value_usd"].sum()
            ind_totals = open_deals.groupby("industry")["deal_value_usd"].sum().sort_values(ascending=True).index.tolist()

            fig_stack = px.bar(
                ind_stage,
                x="deal_value_usd",
                y="industry",
                color="stage",
                orientation="h",
                category_orders={"industry": ind_totals, "stage": STAGE_ORDER_OPEN},
                color_discrete_map=STAGE_COLORS,
            )
            fig_stack.update_traces(
                marker_line_width=0.5,
                marker_line_color="#FFFFFF",
                hovertemplate="<b>%{y} · %{fullData.name}</b><br>Value: $%{x:,.0f}<extra></extra>",
            )
            fig_stack.update_layout(barmode="stack")
            fig_stack.update_xaxes(tickprefix="$", tickformat="~s", title="")
            fig_stack.update_yaxes(title="", showgrid=False)
            st.plotly_chart(style_plotly(fig_stack, 345, show_legend=True), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with p2:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-header">
                <div>
                    <div class="g-card-title">Deal Size Distribution Across Stages</div>
                    <div class="g-card-sub">Median, quartiles, and high-value outliers per stage</div>
                </div>
                <span class="g-badge-mini">Box Plot</span>
            </div>
        """, unsafe_allow_html=True)

        if not filtered.empty:
            fig_box = px.box(
                filtered,
                x="stage",
                y="deal_value_usd",
                color="stage",
                category_orders={"stage": STAGE_ORDER_ALL},
                color_discrete_map=STAGE_COLORS,
                points="outliers",
            )
            fig_box.update_traces(
                hovertemplate="<b>%{x}</b><br>Deal Value: $%{y:,.0f}<extra></extra>",
            )
            fig_box.update_xaxes(title="", tickangle=-25)
            fig_box.update_yaxes(title="", tickprefix="$", tickformat="~s")
            st.plotly_chart(style_plotly(fig_box, 345, show_legend=False), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Row 2: Sales Rep Leaderboard + Funnel Conversion
    f_col, r_col = st.columns([1.0, 1.3], gap="medium")

    with f_col:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-header">
                <div>
                    <div class="g-card-title">Funnel Stage Conversion</div>
                    <div class="g-card-sub">Account progression from initial lead to Closed Won</div>
                </div>
                <span class="g-badge-mini">Funnel</span>
            </div>
        """, unsafe_allow_html=True)

        funnel_order = ["New", "Qualified", "Meeting Scheduled", "Proposal", "Negotiation", "Closed Won"]
        stage_counts = (
            filtered["stage"]
            .value_counts()
            .reindex(funnel_order, fill_value=0)
            .reset_index()
        )
        stage_counts.columns = ["stage", "count"]
        fig_funnel = px.funnel(
            stage_counts,
            x="count",
            y="stage",
            color="stage",
            color_discrete_map=STAGE_COLORS,
        )
        fig_funnel.update_traces(textinfo="value+percent initial")
        fig_funnel.update_layout(yaxis_title="", xaxis_title="")
        st.plotly_chart(style_plotly(fig_funnel, 330, show_legend=False), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with r_col:
        st.markdown("""
        <div class="g-card">
            <div class="g-card-header">
                <div>
                    <div class="g-card-title">Sales Rep Revenue & Pipeline Leaderboard</div>
                    <div class="g-card-sub">Closed-won bookings vs. active open pipeline by owner</div>
                </div>
                <span class="g-badge-mini">Comparison</span>
            </div>
        """, unsafe_allow_html=True)

        rep_won = won.groupby("sales_owner", as_index=False)["deal_value_usd"].sum().rename(columns={"deal_value_usd": "Closed Won"})
        rep_open = open_deals.groupby("sales_owner", as_index=False)["deal_value_usd"].sum().rename(columns={"deal_value_usd": "Open Pipeline"})
        rep_df = pd.merge(rep_won, rep_open, on="sales_owner", how="outer").fillna(0).sort_values("Closed Won", ascending=True)

        fig_rep = go.Figure()
        fig_rep.add_trace(go.Bar(
            y=rep_df["sales_owner"],
            x=rep_df["Closed Won"],
            name="Closed Won",
            orientation="h",
            marker_color="#1A73E8",
            hovertemplate="<b>%{y}</b><br>Closed Won: $%{x:,.0f}<extra></extra>",
        ))
        fig_rep.add_trace(go.Bar(
            y=rep_df["sales_owner"],
            x=rep_df["Open Pipeline"],
            name="Open Pipeline",
            orientation="h",
            marker_color="#AECBFA",
            hovertemplate="<b>%{y}</b><br>Open Pipeline: $%{x:,.0f}<extra></extra>",
        ))
        fig_rep.update_layout(barmode="group")
        fig_rep.update_xaxes(tickprefix="$", tickformat="~s", title="")
        fig_rep.update_yaxes(title="", showgrid=False)
        st.plotly_chart(style_plotly(fig_rep, 330, show_legend=True), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Row 3: Stale Deals Watchlist
    st.markdown("""
    <div class="g-card">
        <div class="g-card-header">
            <div>
                <div class="g-card-title">At-Risk & Stale Opportunities (21+ Days Inactive)</div>
                <div class="g-card-sub">High-value open deals requiring immediate follow-up to prevent slippage</div>
            </div>
            <span class="g-badge-mini">Slippage Risk</span>
        </div>
    """, unsafe_allow_html=True)

    stale = open_deals[open_deals["days_since_last_activity"] >= 21].sort_values("deal_value_usd", ascending=False).head(15)
    stale_view = stale[["company", "stage", "deal_value_usd", "days_since_last_activity", "sales_owner", "expected_close_date"]].rename(
        columns={
            "company": "Account",
            "stage": "Stage",
            "deal_value_usd": "Deal Value",
            "days_since_last_activity": "Days Inactive",
            "sales_owner": "Owner",
            "expected_close_date": "Target Close",
        }
    )
    st.dataframe(
        stale_view,
        use_container_width=True,
        hide_index=True,
        height=310,
        column_config={
            "Deal Value": st.column_config.NumberColumn("Deal Value", format="$%d"),
            "Target Close": st.column_config.DateColumn("Target Close", format="MMM DD, YYYY"),
        },
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("SalesPulse · Google Material 3 Workspace Edition · Synthetic B2B demonstration dataset (800 accounts).")
