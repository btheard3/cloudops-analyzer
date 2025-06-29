--- AWS Total Spend by Service ---\
SELECT
  service,
  ROUND(SUM(cost), 2) AS total_spend
FROM `cloudops-analyzer.finops_sim.aws_cur`
GROUP BY service
ORDER BY total_spend DESC;

--- AWS Spend by Usage Type ---
SELECT
  usage_type,
  ROUND(SUM(cost), 2) AS total_spend
FROM `cloudops-analyzer.finops_sim.aws_cur`
GROUP BY usage_type
ORDER BY total_spend DESC;

--- Azure Spend by Service ---
SELECT
  service,
  ROUND(SUM(cost), 2) AS total_spend
FROM `cloudops-analyzer.finops_sim.azure_costs`
GROUP BY service
ORDER BY total_spend DESC;

--- Azure Spend by Meter Category ---
SELECT
  meter_category,
  ROUND(SUM(cost), 2) AS total_spend
FROM `cloudops-analyzer.finops_sim.azure_costs`
GROUP BY meter_category
ORDER BY total_spend DESC;
