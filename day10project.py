print()
print("================================================")
print("          📝  Smart TO-DO List Maker            ")
print("================================================")
print()
tasks=[]
comp=[]
while True:
    print()
    print("📌 Select an Option : ")
    print(f"[1] ➕ Add Task")
    print(f"[2] ❌ Remove Task")
    print(f"[3] 📋 View Tasks")
    print(f"[4] ✅ Mark Task as Done")
    print(f"[5] 🎉 View Completed Tasks")
    print(f"[6] 🚪 Exit")
    print()
    c=int(input("👉 Enter your choice (1-6) : "))

    if c==1:
        print()
        task=input(("🆕 Enter Task : "))
        tasks.append(task)
        print("✅ Task added succesfully")

    elif c==2:
        print()
        task=input("Enter task to Remove : ")
        if task in tasks:
            tasks.remove(task)
            print("❌ Task is Removed ")
        else:
            print("❌ Invalid Task")
        
    elif c==3:
        print()
        if tasks:
            print("📋 Your Tasks")
            print()
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])
        else:
            print("❌ No Tasks Available")

    elif c==4:
        print()
        task=input("✔ Enter task to mark as done : ")
        print()
        if task in tasks:
            tasks.remove(task)
            comp.append(task)
            print("🎉 Task is Marked as Completed ")
        else:
            print()
            print("❌ Invalid Task")

    elif c==5:
        print("✅ Completed Tasks ")
        print(comp)
    
    elif c==6:
        print()
        print("👋 Thank you for using Smart To-Do List!")
        print()
        print("🚀 Keep being productive! ")
        print()
        break
        
    else:
        print("❌ Invalid Choice")