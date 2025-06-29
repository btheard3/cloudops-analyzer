# CloudOps Analyzer – Multi-Cloud FinOps Dashboard

This project simulates multi-cloud billing data (GCP, AWS, Azure) to analyze cloud spend, detect optimization opportunities, and showcase FinOps KPIs using SQL and Python.

## Features

- Synthetic billing data for all 3 major clouds
- SQL-based cost analytics (spend by service, region, commitment type)
- Ready for integration with Streamlit dashboard and AI summaries

## Structure

- `/data/` – simulated billing data
- `/notebooks/sql/` – BigQuery SQL queries for FinOps KPIs
- `/dashboard/` – future dashboard components
- `/reports/` – PDF summaries, presentation material

## Next Steps

- Integrate LLMs for AI summaries
- Build executive dashboard in Streamlit
- Add cost anomaly detection and forecasting
