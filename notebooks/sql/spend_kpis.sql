-- Total Spend by Service
SELECT
  service,
  ROUND(SUM(cost), 2) AS total_spend
FROM `cloudops-analyzer.finops_sim.gcp_billing`
GROUP BY service
ORDER BY total_spend DESC;


-- Spend by Region
SELECT
  region,
  ROUND(SUM(cost), 2) AS total_spend
FROM `cloudops-analyzer.finops_sim.gcp_billing`
GROUP BY region
ORDER BY total_spend DESC;


-- Usage Type
SELECT
  usage_type,
  ROUND(SUM(cost), 2) AS total_spend
FROM `cloudops-analyzer.finops_sim.gcp_billing`
GROUP BY usage_type
ORDER BY total_spend DESC;


-- Daily Trend
SELECT
  start_time,
  ROUND(SUM(cost), 2) AS daily_spend
FROM `cloudops-analyzer.finops_sim.gcp_billing`
GROUP BY start_time
ORDER BY start_time;

