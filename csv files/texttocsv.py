import csv

def process_data(input_data):
    # Split the input data into individual components
    components = input_data.split()

    # Extract prompt and output
    prompt = ' '.join(components[1:components.index('Output:')])
    output = ' '.join(components[components.index('Output:') + 1:])

    return prompt, output

def main():
    input_file_path = 'datacombinedt.txt'
    output_file_path = 'prompt.csv'

    # Initialize CSV file with headers
    with open(output_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['prompt', 'output'])

    with open(input_file_path, 'r') as file:
        data = file.read()

    # Split data based on "Input:"
    inputs = data.split('Input:')[1:]

    # Process each input and write to CSV
    with open(output_file_path, mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for input_data in inputs:
            prompt, output = process_data(input_data)
            csv_writer.writerow([prompt, output])

if __name__ == "__main__":
    main()
