import sqlite3
import random
from faker import Faker
import datetime

conn = sqlite3.connect("my_hr_data.db")
cursor = conn.cursor()
fake = Faker()

# Drop tables if they exist
cursor.executescript("""
DROP TABLE IF EXISTS employee_projects;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS projects;
""")

# Create tables
cursor.execute("""
CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    age INTEGER,
    department_id INTEGER,
    salary REAL,
    FOREIGN KEY(department_id) REFERENCES departments(id)
)
""")

cursor.execute("""
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT,
    start_date TEXT,
    end_date TEXT
)
""")

cursor.execute("""
CREATE TABLE employee_projects (
    employee_id INTEGER,
    project_id INTEGER,
    FOREIGN KEY(employee_id) REFERENCES employees(id),
    FOREIGN KEY(project_id) REFERENCES projects(id)
)
""")

# Insert departments
departments = ['Engineering', 'HR', 'Finance', 'Marketing', 'IT Support']
for dept in departments:
    cursor.execute("INSERT INTO departments (department_name) VALUES (?)", (dept,))

# Insert employees
for _ in range(100):  # 100 employees
    name = fake.name()
    email = fake.email()
    age = random.randint(21, 60)
    dept_id = random.randint(1, len(departments))
    salary = round(random.uniform(30000, 120000), 2)
    cursor.execute("""
        INSERT INTO employees (name, email, age, department_id, salary)
        VALUES (?, ?, ?, ?, ?)
    """, (name, email, age, dept_id, salary))

# Insert projects
for i in range(10):
    name = f"Project {fake.word().capitalize()}"
    start_date = fake.date_between(start_date='-1y', end_date='today')
    end_date = start_date + datetime.timedelta(days=random.randint(30, 180))
    cursor.execute("""
        INSERT INTO projects (project_name, start_date, end_date)
        VALUES (?, ?, ?)
    """, (name, start_date.isoformat(), end_date.isoformat()))

# Assign employees to projects (many-to-many)
for _ in range(150):  # 150 random assignments
    emp_id = random.randint(1, 100)
    proj_id = random.randint(1, 10)
    cursor.execute("""
        INSERT INTO employee_projects (employee_id, project_id)
        VALUES (?, ?)
    """, (emp_id, proj_id))

conn.commit()
conn.close()
print(" Large HR database created: my_hr_data.db")
