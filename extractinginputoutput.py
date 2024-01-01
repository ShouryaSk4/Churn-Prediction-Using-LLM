import json

# Load data from the JSON file
with open('output.json', 'r') as file:
    data = json.load(file)


# Function to categorize charges into bins
def categorize_charges(charges):
    if charges < 50:
        return "<50"
    elif 50 <= charges < 100:
        return "50-100"
    elif 100 <= charges < 150:
        return "100-150"
    else:
        return ">=150"


# Extract relevant fields and combine conceptually related features
new_data = []

# Process only the first 250 input-output pairs
for item in data[:250]:
    # Extract age and gender
    age_gender = item["input"].split("gender ")[1].split(" ")[0]

    # Combine PhoneService and MultipleLines into a single phone plan feature
    phone_plan = f"PhoneService {item['input'].split('PhoneService ')[1].split(' ')[0]} MultipleLines {item['input'].split('MultipleLines ')[1].split(' ')[0]}"

    # Combine PaperlessBilling and PaymentMethod into a single payment method feature
    payment_method = f"PaperlessBilling {item['input'].split('PaperlessBilling ')[1].split(' ')[0]} PaymentMethod {item['input'].split('PaymentMethod ')[1].split(' ')[0]}"

    # Extract MonthlyCharges and TotalCharges
    monthly_charges = float(item["input"].split("MonthlyCharges ")[1].split(" ")[0])
    total_charges = float(item["input"].split("TotalCharges ")[1].split(" ")[0])

    # Categorize MonthlyCharges and TotalCharges into bins
    monthly_charges_category = categorize_charges(monthly_charges)
    total_charges_category = categorize_charges(total_charges)

    # Create a new item with combined features
    new_item = {
        "input": f"Demographics AgeGender {age_gender} Services {phone_plan} Payment {payment_method} Charges MonthlyCharges {monthly_charges_category} TotalCharges {total_charges_category}",
        "output": item["output"]
    }

    new_data.append(new_item)

# Save the new data to a text file
with open('datacombinedt.txt', 'w') as file:
    for item in new_data:
        file.write(f"Input: {item['input']}\nOutput: {item['output']}\n\n")
