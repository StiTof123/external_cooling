import time

while True:
    with open('/sys/module/coretemp/drivers/platform:coretemp/coretemp.0/hwmon/hwmon3/temp2_input') as file_object:
        contents = file_object.read()
    print(contents.rstrip())
    if contents >= '55000':
        print('Cpu Warm')
    else:
        print('Cpu temp nominal prefix super duper  duo turbo 2004xt pluss MEGA')
    time.sleep(1)
