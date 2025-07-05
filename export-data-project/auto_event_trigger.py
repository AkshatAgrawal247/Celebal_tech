import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f" File detected: {event.src_path}")
            subprocess.run(["python", "export_data.py"])

observer = Observer()
observer.schedule(Watcher(), path="./watch_folder", recursive=False)
observer.start()
print(" Watching 'watch_folder/' for file arrivals...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
