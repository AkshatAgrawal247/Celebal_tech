import schedule
import time
import subprocess

def run_pipeline():
    print(" Scheduled trigger: Running export_data.py")
    subprocess.run(["python", "export_data.py"])

schedule.every(1).minutes.do(run_pipeline)

while True:
    schedule.run_pending()
    time.sleep(1)
