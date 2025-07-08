import psutil
import pandas as pd
import time

data = []

print("Starting CPU monitoring...")

for _ in range(60):  # monitor for 60 seconds
    cpu = psutil.cpu_percent(interval=1)
    data.append(cpu)
    print(f"CPU Usage: {cpu}%")

df = pd.DataFrame(data, columns=["CPU_Usage"])
df.to_csv("cpu_data.csv", index=False)
print("✅ CPU data saved to cpu_data.csv")
