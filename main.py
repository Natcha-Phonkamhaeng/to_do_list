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
	
def add_task(): # 1
	task_name = input("what is your task?: \n")
	task_status = input("pending or complete ?: \n")
	task[task_name] = task_status

def view_task(): # 2
	print(task)

def remove_task(): # 3
	rm_task = input("what task you want to remove?: \n")

	if rm_task in task:
		del task[rm_task]
	else:
		print("your task is not in to-do list. Try Again")


def mark_complete(): # 4
	# writing if else condition
	task_ch = input("what task you want to change status?: \n")
	if task_ch in task:
		status_ch = input("what is your new status?: \n")
		task[task_ch] = status_ch
	else:
		print("this task is not in to-do list. Try Again")


while True:
	
	menu()
	
	try:
		
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

	except ValueError:
		print("please input items as numeric only")






