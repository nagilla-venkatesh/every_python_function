#  Faster 

def feet_to_meters(feet):
    return feet * 0.3048

for feet in (1.0, 10.0, 100.0, 2000.0, 3000.0, 4000.0):
    print(f"{feet:7.1f} feet is {feet_to_meters(feet):7.1f} meters")

import dis

dis.dis(feet_to_meters, adaptive=True)

print(f" 5000.0 feet is {feet_to_meters(5000.0):7.1f} meters")

dis.dis(feet_to_meters, adaptive=True)
