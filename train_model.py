import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Normalizer
from sklearn.metrics import accuracy_score
import joblib
import json

# Load dataset
df = pd.read_excel(r"C:\revolutionizing\data\HealthCareData.xlsx")

# Clean dirty numeric values like "o.4"
df = df.replace(r'^\s*[Oo]\.', '0.', regex=True)
df = df.replace(r'[^\d\.\-]+', '', regex=True)

# Rename target
df.rename(columns={
    'Predicted Value(Out Come-Patient suffering from liver  cirrosis or not)': 'Target'
}, inplace=True)

# Select relevant features
selected_features = [
    'Age',
    'Gender',
    'Duration of alcohol consumption(years)',
    'Diabetes Result',
    'Albumin   (g/dl)',
    'Total Bilirubin    (mg/dl)',
    'SGPT/ALT (U/L)',
    'Target'
]
df = df[selected_features]

# Map target
df['Target'] = df['Target'].apply(lambda x: 1 if str(x).strip().upper() == "YES" else 0)

# ✅ Clean and map Gender safely
df['Gender'] = df['Gender'].astype(str).str.strip().str.lower().map({'male': 1, 'female': 0})
df['Gender'] = df['Gender'].fillna(0)  # fill unmapped/missing as 0 (default to female)

# ✅ Clean and map Diabetes Result safely
df['Diabetes Result'] = df['Diabetes Result'].astype(str).str.strip().str.lower().map({'yes': 1, 'no': 0})
df['Diabetes Result'] = df['Diabetes Result'].fillna(0)  # default to "no"

# Convert everything to numeric
df = df.apply(pd.to_numeric, errors='coerce')

# ✅ Fill all remaining NaNs with medians
df.fillna(df.median(numeric_only=True), inplace=True)

# Final check
na_columns = df.columns[df.isna().any()].tolist()
if na_columns:
    print(f"❌ Still has NaNs: {na_columns}")
else:
    print("✅ No missing values")

# Train model
X = df.drop(columns=['Target'])
y = df['Target']

normalizer = Normalizer(norm='l1')
X_normalized = normalizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_normalized, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"✅ Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Save outputs
joblib.dump(model, "rf_model.pkl")
joblib.dump(normalizer, "normalizer.pkl")
with open("feature_names.json", "w") as f:
    json.dump(list(X.columns), f)

print("✅ Model, normalizer, and features saved successfully.")
