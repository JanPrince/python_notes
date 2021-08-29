import psutil
import platform
from datetime import datetime

print("="*40, "System  Info", "="*40)
general = platform.uname()

print("System    : " + general.system)
print("Node Name : " + general.node)
print("Release   : " + general.release)
print("Version   : " + general.version)
print("Machine   : " + general.machine)
print("Processor : " + general.processor)

print("\n")

# Boot time
print("="*40, "Boot Time", "="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)

print("Boot Time {}/{}/{} {}:{}:{}".format(bt.year, bt.month, bt.day, bt.hour, bt.minute, bt.second))

print("\n")

# CPU Info
print("="*40, "CPU Info" , "="*40)

# number of cores
print("Physical cores  : ", psutil.cpu_count(logical=False))
print("Total cores     : ", psutil.cpu_count(logical=True))

# CPU freqs
cpufreq = psutil.cpu_freq()

print(f"Max Frequency  : {cpufreq.max:.2f}Mhz")
print(f"Min Frequency  :{cpufreq.min:.2f}Mhz")

print("CPU Usage per Core")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
    print("Core", i, ":", percentage, "%")
print("Total CPU Usage :", psutil.cpu_percent(), "%")
