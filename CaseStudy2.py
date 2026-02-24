# Temperature Monitoring
# Mukesh Kumar
# 202501100700200

import random
import time

# Accept minimum and maximum temperature from user
min_temp = float(input("Enter minimum temperature limit: "))
max_temp = float(input("Enter maximum temperature limit: "))

print("\nMonitoring temperature...\n")

while True:
    # Generate random temperature between 0 and 100
    temperature = random.randint(0, 100)
    
    print("Generated Temperature:", temperature)

    # Compare with limits
    if temperature > max_temp:
        print("Alert: Temperature is too high")
    elif temperature < min_temp:
        print("Alert: Temperature is too low")
    else:
        print("Temperature is within acceptable limit")

    print("-----------------------------")
    
    # Wait for 2 seconds
    time.sleep(2)