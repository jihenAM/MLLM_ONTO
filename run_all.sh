#!/bin/bash

# Check if correct number of arguments are provided
if [ "$#" -ne 5 ]; then
    echo "Usage: $0 <model> <ontology_path> <dataset_dir> <output_folder> <output_csv_path>"
    exit 1
fi

# Assign arguments to variables
model="$1"
ontology_path="$2"
dataset_dir="$3"
output_folder="$4"
output_csv_path="$5"

# Run Python script
python run_mllm.py "$model" "$ontology_path" "$dataset_dir" "$output_folder"

# Check if Python script successfully created the required CSV file
if [ ! -f "${output_folder}/${model}_owlexpression_results.csv" ]; then
    echo "Error: ${model}_owlexpression_results.csv not found. Python script might have failed."
    exit 1
fi

# Compile and run Java code
javac reasoner/DLQuery_reasoner.java
java reasoner.DLQuery_reasoner "$ontology_path" "${output_folder}/${model}_owlexpression_results.csv" "$output_csv_path"
