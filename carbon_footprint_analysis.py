from google.cloud import bigquery
import pandas as pd

def run_bq_query(sql, project_id, credentials):
    bq_client = bigquery.Client(project=project_id, credentials=credentials)
    job_config = bigquery.QueryJobConfig()
    client_result = bq_client.query(sql, job_config=job_config)
    job_id = client_result.job_id
    df = client_result.result().to_arrow().to_pandas()
    print(f"Finished job_id: {job_id}")
    return df

def analyze_carbon_footprint(project_id, credentials):
    # Sample query to get carbon footprint data
    query = """
    SELECT usage_month, service.description, location.location, carbon_footprint_total_kgCO2e.location_based
    FROM `sc-gcp-c5-carbon-emissions.carbonfootprint.sample_data`
    WHERE project.number = 11111
    ORDER BY usage_month, service.description
    """
    df = run_bq_query(query, project_id, credentials)
    return df

# Example usage
if __name__ == "__main__":
    from helper import authenticate
    CREDENTIALS, PROJECT_ID = authenticate()
    
    carbon_footprint_data = analyze_carbon_footprint(PROJECT_ID, CREDENTIALS)
    print(carbon_footprint_data)
