import psutil

def check_system_health ():
    cpu_threshold= int(input("Enter CPU threshold value:- "))
    memory_threshold= int(input("Enter memory threshold value:- "))

    current_cpu= psutil.cpu_percent(interval=1)
    current_memory= psutil.virtual_memory()

    print("Current CPU usage is:- ", current_cpu)
    print("Current Virtual Memory is:- ", current_memory)
    if cpu_threshold > current_cpu:
        print("Emergency! Sent an email to the admin")
    else:
        print("Cpu is fine")
    
    if current_memory.available < memory_threshold  :
        print("Emergency! Sent an email to the admin")
    else:
        print("Everything is fine")

check_system_health()