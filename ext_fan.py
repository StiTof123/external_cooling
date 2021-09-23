import os

fd = "/sys/module/coretemp/drivers/platform:coretemp/coretemp.0/hwmon/hwmon3/temp2_input"
file = open('', 'r')
temp = h.readlines()
print(temp)
type()
if temp >= 55000:
    print("cpu cold")
else:    
    print("cpu warm")

