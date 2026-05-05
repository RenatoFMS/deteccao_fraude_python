# Detecção de Fraude em Cartões de Crédito 💳

Este projeto utiliza técnicas de Machine Learning para identificar transações fraudulentas em cartões de crédito. O foco principal foi lidar com o desbalanceamento extremo dos dados utilizando **SMOTE** (Synthetic Minority Over-sampling Technique) e comparar o desempenho de diferentes algoritmos.

## 🚀 Tecnologias Utilizadas
* **Python 3.12**
* **Pandas & Numpy**: Manipulação e análise de dados.
* **Scikit-Learn**: Implementação dos modelos de Regressão Logística e Random Forest.
* **Imbalanced-learn (SMOTE)**: Balanceamento das classes de fraude.

## 📊 Resultados Obtidos

O projeto comparou dois modelos principais. Abaixo estão os relatórios de classificação extraídos durante a execução:

### 1. Regressão Logística (Baseline)
O modelo inicial apresentou uma boa precisão, mas um *recall* moderado para a classe de fraude (0.63).
<img width="415" height="170" alt="image" src="https://github.com/user-attachments/assets/08f5bd84-eb31-4f92-a279-cc21c65ceab9" />

* **Recall (Fraude):** 0.63
* **F1-Score (Fraude):** 0.72

### 2. Random Forest + SMOTE (Modelo Final)
Após aplicar o balanceamento de dados e utilizar um algoritmo de florestas aleatórias, houve uma melhora significativa na detecção das fraudes.
<img width="458" height="244" alt="image" src="https://github.com/user-attachments/assets/f40ce239-8b25-4374-954c-0d567afba62b" />

* **Recall (Fraude):** 0.78 (Aumento significativo na captura de fraudes reais)
* **F1-Score (Fraude):** 0.81

## 📈 Conclusão
O modelo final com **Random Forest** demonstrou ser superior para este problema de segurança, conseguindo identificar **78% das transações fraudulentas**, mantendo uma alta precisão de **0.85**, o que minimiza o bloqueio indevido de clientes legítimos.

---
### Como executar
1. Crie um ambiente virtual: `python3 -m venv venv`
2. Ative o ambiente: `source venv/bin/activate`
3. Instale as dependências: `pip install pandas numpy scikit-learn imbalanced-learn`
4. Execute o script: `python deteccao_fraude.py`
