import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv('../data/triangles.csv')
X = df[['a', 'b']]
y = df['c']

# Train linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Evaluate
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"MSE: {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Create plots directory if needed
os.makedirs('../data', exist_ok=True)

# Plot predictions vs true values
plt.figure(figsize=(6, 6))
plt.scatter(y, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], '--', color='red')
plt.xlabel('True Hypotenuse')
plt.ylabel('Predicted Hypotenuse')
plt.title('Prediction vs True Value')
plt.grid(True)
plt.savefig('../data/pred_vs_real.png')
plt.close()
