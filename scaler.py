import numpy as np
import subprocess

predicted_usage = np.loadtxt("predicted.csv", delimiter=",")
scale_up_threshold = 75
scale_down_threshold = 30

def scale_up():
    print("Scaling up... Launching extra worker")
    subprocess.Popen(["python", "worker.py"])

def scale_down():
    print("🛑 Scaling down... Simulating shutdown")  # Optional: Terminate with PID

def scale_decision(predictions):
    avg = np.mean(predictions)
    print(f"📊 Predicted Average CPU: {avg:.2f}%")
    if avg > scale_up_threshold:
        scale_up()
    elif avg < scale_down_threshold:
        scale_down()
    else:
        print("Load Normal - No Scaling Needed")

scale_decision(predicted_usage)
