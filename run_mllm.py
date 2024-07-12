import os
import argparse
from mllm import prompting_gemini
from mllm import prompting_gpt4v
from mllm import prompting_claude
from mllm import prompting_llava
import prompt_ontology
# Function to call the selected multimodal model and save results
def process_image_prompt(image_path, prompt, model):
    result = None
    if model == 'llava':
        result = prompting_llava.prompt_llava(image_path, prompt)
    elif model == 'gpt4vision':
        result = prompting_gpt4v.prompt_gpt4_vision(image_path, prompt)
    elif model == 'gemini':
        result = prompting_gemini.prompt_gemini(image_path, prompt)
    elif model == 'claude':
        result = prompting_claude.prompt_claude(image_path, prompt)
    else:
        print("Invalid model selection. Please choose from 'llava', 'gpt4vision', 'gemini', or 'claude'.")

    return result

# Function to parse command-line arguments
def parse_arguments(argv):
    parser = argparse.ArgumentParser(description='Process images using multimodal models.')
    parser.add_argument('model', type=str, help='Name of the model to use (llava, gpt4vision, gemini, claude)')
    parser.add_argument('ontology_path', type=str, help='Path to the ontology file')
    parser.add_argument('dataset_dir', type=str, help='Path to the directory containing the image dataset')
    parser.add_argument('output_folder', type=str, help='Path to the output folder to save the results')
    return parser.parse_args(argv)

def main(args):
    # Create output folder if it does not exist
    os.makedirs(args.output_folder, exist_ok=True)
    
    # Prompt creation using ontology
    prompt = prompt_ontology.generate_prompt(args.ontology_path)
    # Create output CSV file path
    output_csv_file = os.path.join(args.output_folder, f"{args.model}_results.csv")
    # Open CSV file for writing
    with open(output_csv_file, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header row
        writer.writerow(['Class Name', 'Image Name', 'Result'])

        # Iterate over each image in the dataset
        for class_name in os.listdir(args.dataset_dir):
            class_dir = os.path.join(args.dataset_dir, class_name)
            if os.path.isdir(class_dir):
                for image_name in os.listdir(class_dir):
                    image_path = os.path.join(class_dir, image_name)
                    
                    # Call function to process each image and prompt using the selected model
                    result = process_image_prompt(image_path, prompt, args.model)
                    if result is not None:
                        writer.writerow([class_name, image_name, result])
    # Call the function to process the observed abnormalities result from mllm and create owl expression out of it
    output_owlexpression_csv=owl_expression_generalization(output_csv_file,os.path.join(args.output_folder, f"{args.model}_owlexpression_results.csv"))
if __name__ == "__main__":
    # Parse command-line arguments
    args = parse_arguments(sys.argv[1:])
    main(args)
