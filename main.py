import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from popup import Window
from read_data import Data

################
# popup window #
################
	
def ask_usr(file):
	# ask user to send
	win = Window(file)

	win.popup()
	if win.ed_msg_mail:
		print(win.ed_msg_mail)


###############################
# wait for new file in folder #
###############################

def on_created(event):
	print(f"{event.src_path} was created")
	ask_usr(event.src_path)

def on_deleted(event):
	print(f"{event.src_path} was deleted")

def on_modified(event):
	print(f"{event.src_path} was modified")

def on_moved(event):
	print(f"{event.src_path} was moved to {event.dest_path}")

class Watchdir:

	patterns = "*"
	ignore_patterns = ""
	ignore_directories = False
	case_sensitive = True
	event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

	event_handler.on_created = on_created
	event_handler.on_deleted = on_deleted
	event_handler.on_modified = on_modified
	event_handler.on_moved = on_moved

	path = "."
	go_recursively = True
	observer = Observer()
	observer.schedule(event_handler, path, recursive=go_recursively)

	def run_watch(self):
		self.observer.start()
		try:
			while True:
				time.sleep(1)
		except KeyboardInterrupt:
			self.observer.stop()
			self.observer.join()

################
# main routine #
################

if __name__ == "__main__":
	# wd = Watchdir()
	# wd.run_watch()
	ask_usr("somefile")

