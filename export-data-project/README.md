# 📊 Data Pipeline Automation Project

This project implements a complete local ETL pipeline using **Python** and **SQLite**. It includes:

- ✅ Exporting data from a relational database to multiple file formats (CSV, Parquet, Avro)
- 🔁 Automated pipeline execution via schedule and event-based triggers
- 🔄 Full and selective database replication

---

## 📦 Project Structure

```
.
├── setup_database.py           # Create a large HR database
├── export_data.py              # Export table to CSV, Parquet, Avro
├── auto_schedule_trigger.py    # Automate with schedule-based trigger
├── auto_event_trigger.py       # Automate with file arrival event
├── db_copy_all.py              # Copy all tables to a new database
├── db_copy_selective.py        # Copy selective columns/tables
├── my_hr_data.db               # Sample HR database (generated)
├── watch_folder/               # Folder monitored for file triggers
├── employees.csv               # Sample export (CSV)
├── employees.parquet           # Sample export (Parquet)
├── employees.avro              # Sample export (Avro)
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```

---

## 🔧 Setup Instructions

### 1. ✅ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. 📚 Generate the HR Database

```bash
python setup_database.py
```

This creates `my_hr_data.db` with realistic data in 4 tables:
- `departments`
- `employees`
- `projects`
- `employee_projects`

---

## 📤 Task 1: Export to CSV, Parquet, and Avro

```bash
python export_data.py
```

Exports the selected table (default: `employees`) into:
- `employees.csv`
- `employees.parquet`
- `employees.avro`

Modify the `table_name` in the script to export different tables.

---

## ⏰ Task 2: Automate Using Triggers

### 📅 Schedule-Based Trigger

```bash
python auto_schedule_trigger.py
```
Runs `export_data.py` every 1 minute using the `schedule` library.

### ⚡ Event-Based Trigger

```bash
python auto_event_trigger.py
```

Watches the `watch_folder/` directory and runs the export pipeline when a file is added.

---

## 📦 Task 3: Full Database Copy

```bash
python db_copy_all.py
```

Copies all tables and their data from `my_hr_data.db` to `hr_full_copy.db`.

---

## 🎯 Task 4: Selective Table and Column Copy

```bash
python db_copy_selective.py
```

Copies only selected columns (e.g., name, salary) of high-paid employees to `hr_selective_copy.db`.

---

## 🧾 Requirements

Listed in `requirements.txt`:

```
pandas
sqlalchemy
pyarrow
fastavro
schedule
watchdog
faker
```

Install via:

```bash
pip install -r requirements.txt
```

---

## 🛡️ Notes

- Uses **SQLite** for simplicity. Can be adapted to MySQL or PostgreSQL.
- Modular structure for easy customization.
- Ideal for learning ETL concepts, automation, and file format conversions.

---

 

## 📄 License

MIT – Free to use, customize, and extend.
