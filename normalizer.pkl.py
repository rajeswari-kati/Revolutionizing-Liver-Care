import pandas as pd
from sklearn.preprocessing import Normalizer
import joblib

# 1. Load your dataset
df = pd.read_csv("liver_dataset.csv")

# 2. Drop target column (assuming it's named 'Target')
X = df.drop(columns=['Target'])

# 3. Handle missing values (example)
X = X.fillna(X.median())

# 4. Create and fit the Normalizer
normalizer = Normalizer(norm='l1')
X_normalized = normalizer.fit_transform(X)

# 5. Save the normalizer
joblib.dump(normalizer, 'normalizer.pkl')

print("Normalizer saved successfully as normalizer.pkl")
