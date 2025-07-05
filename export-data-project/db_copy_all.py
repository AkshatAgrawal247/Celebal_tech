import pandas as pd
from sqlalchemy import create_engine, inspect

source_db = "sqlite:///my_hr_data.db"
destination_db = "sqlite:///hr_full_copy.db"

src_engine = create_engine(source_db)
dest_engine = create_engine(destination_db)

inspector = inspect(src_engine)
tables = inspector.get_table_names()

for table in tables:
    df = pd.read_sql_table(table, src_engine)
    df.to_sql(table, dest_engine, index=False, if_exists="replace")
    print(f" Copied table: {table}")
