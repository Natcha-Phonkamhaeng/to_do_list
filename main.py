# 3 Jan 2026

task = {}

def menu():
	print("")
	print("------ To Do List ------")
	print("1. Add task")
	print("2. View task")
	print("3. Remove task")
	print("4. Mark as complete")
	print("5. Exit program")
	print("")
	

def add_task():
	task_name = input("what is your task?: \n")
	task_status = input("pending or complete ?: \n")
	task[task_name] = task_status

def view_task():
	print(task)

def remove_task():
	pass

def mark_complete():
	pass


while True:
	
	menu()
	user = int(input("please select items you want to do: "))

	if user == 1:
		add_task()
	elif user == 2:
		view_task()
	elif user == 3:
		remove_task()
	elif user == 4:
		mark_complete()
	elif user == 5: # exit
		break






