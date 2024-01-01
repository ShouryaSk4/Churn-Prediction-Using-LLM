import langchain
import numpy as np

# Load the local LLm
model_path = "C:\\Users\\srkyo\\text-generation-webui\\models\\stabilityai_StableBeluga-7B"
model = langchain.models.LocalLLM(
    model_dir=model_path,
    max_length=4096,
    temperature=0.6,
    top_p=0.9,
    no_repeat_ngram=2,
)

# Load the Lora model
lora_model_path = "C:\\Users\\srkyo\\text-generation-webui\\loras\\loratrainedmodel1300"
lora_model = langchain.models.LocalLLM(
    model_dir=lora_model_path,
    max_length=4096,
    temperature=0.6,
    top_p=0.9,
    no_repeat_ngram=2,
)

# Load the test dataset
test_data = np.load("test_data.npy")
test_labels = np.load("test_labels.npy")

# Make predictions using the LLm and Lora combination
predictions = []
for text, label in zip(test_data, test_labels):
    # Generate text using the LLm
    generated_text = model.generate(prompt=text)

    # Score the generated text using the Lora model
    lora_score = lora_model.score(prompt=generated_text, reference=text)

    # Make a prediction based on the Lora score
    prediction = 1 if lora_score > 0.5 else 0
    predictions.append(prediction)

# Evaluate the predictions
from sklearn.metrics import precision_score, recall_score, f1_score

precision = precision_score(y_true=test_labels, y_pred=predictions)
recall = recall_score(y_true=test_labels, y_pred=predictions)
f1 = f1_score(y_true=test_labels, y_pred=predictions)

print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
