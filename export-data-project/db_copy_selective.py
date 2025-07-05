import pandas as pd
from sqlalchemy import create_engine

src_engine = create_engine("sqlite:///my_hr_data.db")
dest_engine = create_engine("sqlite:///hr_selective_copy.db")

# Example: only high salary employees
query = "SELECT name, email, salary FROM employees WHERE salary > 90000"

df = pd.read_sql(query, src_engine)
df.to_sql("high_salary_employees", dest_engine, index=False, if_exists="replace")

print(" Copied selective employee data to new database.")
