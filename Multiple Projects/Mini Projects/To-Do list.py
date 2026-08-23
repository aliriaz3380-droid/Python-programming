# To-Do List ⭐⭐⭐
# Create a menu:
# 1. Add task
# 2. View tasks
# 3. Complete task
# 4. Delete task
# 5. Exit
print("To-Do List")
courses=[]
while True:
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Complete task")
    print ("4 Delete task")
    print("5. Exit")
    choice=input("Enter the choice:")
    if choice=="1":
        user=input("Enter the course you want to add in list:")
        courses.append(user)
        print("Task added!")
    elif choice=="2":
        print("Your Courses are:",courses)
    elif choice=="3":
        course=input("Enter the course You have completed:")
        if course in courses:
           index=courses.index(course)
           courses[index]="✓ " +course
           print("Course Completed!")
        else:
           print("Course not found")
    elif choice=="4":
        new=input("Enter the name you want to delete the course:")
        courses.remove(new) 
        print("Course is deleted.")
    elif choice=="5":
        print("Exit")
        break
    else:
        print("invalid Choice")   
        break          