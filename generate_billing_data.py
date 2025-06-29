import pandas as pd
import random
from datetime import datetime, timedelta

# Common fields
projects = ['prod-video', 'dev-ml', 'shared-data', 'eng-streaming']
regions = ['us-central1', 'us-east1', 'europe-west1']
days = [datetime(2025, 6, 1) + timedelta(days=i) for i in range(30)]

# GCP Simulation
gcp_services = ['BigQuery', 'Cloud Storage', 'Dataflow', 'Compute Engine']
gcp_usage = ['OnDemand', 'CUD']
gcp_data = []

for day in days:
    for _ in range(15):
        gcp_data.append({
            "project": random.choice(projects),
            "service": random.choice(gcp_services),
            "sku": random.choice(['Standard', 'Premium']),
            "usage_type": random.choice(gcp_usage),
            "region": random.choice(regions),
            "cost": round(random.uniform(20, 800), 2),
            "usage_amount": round(random.uniform(50, 2000), 2),
            "start_time": day.strftime('%Y-%m-%d')
        })

pd.DataFrame(gcp_data).to_csv("data/gcp_billing.csv", index=False)

# AWS Simulation
aws_services = ['EC2', 'S3', 'Redshift', 'Athena']
aws_usage = ['OnDemand', 'RI', 'SavingsPlan']
aws_data = []

for day in days:
    for _ in range(15):
        aws_data.append({
            "account": random.choice(projects),
            "service": random.choice(aws_services),
            "usage_type": random.choice(aws_usage),
            "region": random.choice(regions),
            "cost": round(random.uniform(10, 700), 2),
            "usage_quantity": round(random.uniform(10, 1000), 2),
            "usage_date": day.strftime('%Y-%m-%d')
        })

pd.DataFrame(aws_data).to_csv("data/aws_cur.csv", index=False)

# Azure Simulation
azure_services = ['VM', 'Blob Storage', 'Data Lake', 'Cosmos DB']
azure_data = []

for day in days:
    for _ in range(15):
        azure_data.append({
            "subscription": random.choice(projects),
            "service": random.choice(azure_services),
            "meter_category": random.choice(['Compute', 'Storage']),
            "region": random.choice(regions),
            "cost": round(random.uniform(5, 500), 2),
            "quantity": round(random.uniform(5, 800), 2),
            "billing_date": day.strftime('%Y-%m-%d')
        })

pd.DataFrame(azure_data).to_csv("data/azure_costs.csv", index=False)

print("✅ Synthetic billing data generated in /data folder.")
