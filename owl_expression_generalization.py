import csv

def owl_expression_creation(input_csv_file, output_csv_file):
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            class_name, image_name, result_str = row
            result_dict = dict(item.strip().split(": ") for item in result_str.strip("{}").split(", "))

            # Extract symptom, color, and shape from result
            symptom = result_dict.get("SymptomAbnormality", "N/A")
            color = result_dict.get("ColorAbnormality", "N/A")
            shape = result_dict.get("ShapeOfSymptomAbnormality", "N/A")

            # create OWL expression
            owl_expression = f"abnormalityGroup some ((hasSymptom some {symptom}) and (hasColor some {color}) and (hasShape some {shape}))"

            # add class name, image name, and OWL expression to data list
            data.append([class_name, image_name, owl_expression])

    # Save data to CSV file
    save_to_csv(data, output_csv_file)

# function to save data to CSV file
def save_to_csv(data, output_csv_file):
    with open(output_csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Class Name', 'Image Name', 'OWL Expression'])
        writer.writerows(data)


