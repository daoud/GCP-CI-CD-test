# With this:
#from urllib.parse import quote as url_quote
from urllib.parse import quote
from google.cloud import bigquery
from flask import Flask
from flask import request
import os 


app = Flask(__name__)
client = bigquery.Client()



@app.route('/')
def main(big_query_client=client):
    table_id = "second-project-mlops.test_schema.us_states" 
    # project id : gleaming-bot-447411-c2, Schema name : test_schema, table Name : us_states
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
    )
    uri = "gs://mlops-daoud/us-states.csv" 
    #gs:// prefix indicates that the URI points to a resource in Google Cloud Storage
    ## bucket name : ml-ops-daoud, file name : us-states.csv

    load_job = big_query_client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )

    load_job.result()  

    destination_table = big_query_client.get_table(table_id)
    return {"data": destination_table.num_rows}

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080)
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5052)))
