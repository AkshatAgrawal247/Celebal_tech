import pandas as pd
from sqlalchemy import create_engine
from fastavro import writer, parse_schema

# Connect to your HR database
engine = create_engine("sqlite:///my_hr_data.db")

# Choose the table to export (e.g., 'employees')
table_name = 'employees'
df = pd.read_sql(f"SELECT * FROM {table_name}", engine)

# Export to CSV
df.to_csv(f"{table_name}.csv", index=False)

# Export to Parquet
df.to_parquet(f"{table_name}.parquet", index=False)

# Export to Avro
schema = {
    "type": "record",
    "name": f"{table_name}_record",
    "fields": [{"name": col, "type": "string"} for col in df.columns]
}
parsed = parse_schema(schema)
records = df.astype(str).to_dict(orient="records")

with open(f"{table_name}.avro", "wb") as f:
    writer(f, parsed, records)

print(f" Exported '{table_name}' to CSV, Parquet, and Avro.")
