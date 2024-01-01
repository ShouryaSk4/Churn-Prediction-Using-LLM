import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV files
response_df = pd.read_csv('responseR.csv')
prompt_df = pd.read_csv('prompt-50.csv')

# Compare 'response' and 'output' columns directly
y_true = response_df['response']
y_pred = prompt_df['output']

# Generate confusion matrix
conf_matrix = confusion_matrix(y_true, y_pred)

# Compute accuracy, precision, and recall scores
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='weighted')
recall = recall_score(y_true, y_pred, average='weighted')

# Plot confusion matrix using seaborn and matplotlib
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=prompt_df['output'].unique(), yticklabels=prompt_df['output'].unique())
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Print scores
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
