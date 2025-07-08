import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("cpu_data.csv")
X = np.arange(len(df)).reshape(-1, 1)
y = df["CPU_Usage"]

poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

X_future = np.arange(len(df), len(df) + 10).reshape(-1, 1)
X_future_poly = poly.transform(X_future)
y_pred = model.predict(X_future_poly)
y_pred = np.clip(y_pred, 0, 100)

# Save predictions to CSV
np.savetxt("predicted.csv", y_pred, delimiter=",")

# Plot
plt.plot(X, y, label="Actual")
plt.plot(X_future, y_pred, 'r--', label="Predicted")
plt.axvline(x=len(df), color='gray', linestyle='--', label='Forecast Start')
plt.title("CPU Usage Forecast")
plt.xlabel("Time")
plt.ylabel("CPU (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
