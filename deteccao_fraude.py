import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

print("Baixando e carregando os dados... Por favor, aguarde.")
url = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"
df = pd.read_csv(url)

df["Amount_log"] = np.log1p(df["Amount"])
scaler = StandardScaler()
df["Amount_scaled"] = scaler.fit_transform(df[["Amount"]])

X = df.drop("Class", axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.3, random_state=42
)

print("\n--- Treinando Regressão Logística ---")
model_log = LogisticRegression(max_iter=1000)
model_log.fit(X_train, y_train)
y_pred_log = model_log.predict(X_test)

print("\n--- RESULTADO: REGRESSÃO LOGÍSTICA ---")
print(classification_report(y_test, y_pred_log))

print("\nBalanceando os dados com SMOTE... Isso pode levar um momento.")
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X_train, y_train)

print("\n--- Treinando Random Forest (Processamento pesado...) ---")
rf = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1)
rf.fit(X_res, y_res)

y_pred_rf = rf.predict(X_test)

print("\n" + "="*30)
print("--- RELATÓRIO FINAL: RANDOM FOREST ---")
print("="*30)
print(classification_report(y_test, y_pred_rf))
