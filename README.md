# MLLM_ONTO
![Alt Text](https://github.com/anonymousUserblanked/MLLM_ONTO/blob/main/framework.PNG)
This repository contains the code, data and results for our paper Integrating Multimodal Large Language Models and Ontology for Visual Concept Identification,Inference and explainability.
For more details, please check our paper. 
In our paper, we used the platform  [Vision-Arena](https://huggingface.co/spaces/WildVision/vision-arena) to prompt Multimodal Larege Language Models (MLLMs) since it provides the opportunity to use MLLMs without API access keys.
Results could be seen in [/Results](https://github.com/anonymousUserblanked/MLLM_ONTO/tree/main/Results))
However, in this repository, we share all the needed code to reproduce the results when having API key access.

## Used Dataset
* **Image dataset**: Our dataset of rice diseases images consists of four classes which are brown spot, leaf blast, leaf scald and narrow brown spot. It was originally proposed in [1].
* **Rice disease ontology**: In this work, we will employ the RiceDO ontology. This OWL ontology models knowledge related to traits and phenotypes of various rice diseases including abnormal appearance characteristics and symptoms [2].
### Multimodal Larege Language Models (MLLMs)
We prompt and evaluate the performance of four leading MLLMs using the ontology: 
* [GPT-4V](https://openai.com/index/gpt-4v-system-card)
* [Gemini-Pro-Vision](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#gemini-pro-vision)
* [LLaVA v1.6-7/34b](https://huggingface.co/liuhaotian/llava-v1.6-34b)
* [Claude-3opus-20240229](https://www.anthropic.com/claude).
### Contents
* [run_mllm.py](https://github.com/anonymousUserblanked/MLLM_ONTO/blob/main/run_mllm.py): This script enables prompting different multimodal large language models, including LLAVA, gpt4vision, Gemini, and Claude. The script allow users to specify the model, an ontology file, the image dataset directory and the output directory. The script calls the generate_prompt function from the [prompt_ontology](https://github.com/anonymousUserblanked/MLLM_ONTO/blob/main/prompt_ontology.py) module, which generates a prompt automatically using disease concepts from the ontology. Then, the created prompt and image are passed to the chosen MLLM, where observed abnormalities (color, shape, and symptoms) are returned in a JSON format. All the results considering the class of the image, the image name, and the observed abnormalities are added. Then, the owl_expression_creation method from [owl_expression_generalization.py](https://github.com/anonymousUserblanked/MLLM_ONTO/blob/main/owl_expression_generalization.py)  will be called to create an owl expression of all observed abnormalities.
* [prompt_ontology.py](https://github.com/anonymousUserblanked/MLLM_ONTO/blob/main/prompt_ontology.py):This script takes the ontology and extracts the abnormality concepts (color, shape, and symptoms), then creates the textual prompt 
* [owl_expression_generalization.py](https://github.com/anonymousUserblanked/MLLM_ONTO/blob/main/owl_expression_generalization.py): This script will take the generated CSV file in the previous step and automatically create the OWL expression for the corresponding observation
* mllm/: this folder contains scripts to prompt Multimodal Larege Language Models (MLLMs) 
* reasoner/: this folder contains the script to take the owl expression for each image from the CSV file and give it to the reasoner to obtain the corresponding disease class from the ontology; the result will be saved in a new CSV file to have the diagnosis of each image disease.
### Usage
* For prompting mllm the user needs to run the following:
```
Python run_mllm.py  <model> <ontology_path> <dataset_dir> <output_folder> 
where:
  * <model>: Name of the model to use (llava, gpt4vision, gemini, or claude).
  * <ontology_path>: Path to the ontology file.
  * <dataset_dir>: Path to the directory containing the image dataset
  * <output_folder>: this is the folder where the {args.model}_results.csv file will be saved. The file contains the prompting result for each image. And {args.model}_owlexpression_results.csv that contains the OWL expressions for each abnormality observation.
```
*For calling the reasoner and get the diagnosis of each image the user need to run the following:
```
javac reasoner/DLQuery_reasoner.java
java reasoner.DLQuery_reasoner <ontology_path> <class_expressions_path> <output_csv_path>
Where:
  * <ontology_path> is the path for the ontology 
  * <class_expressions_path> is the path for the {model}_owlexpression_result.csv created in the previous step
  * <output_csv_path> is the csv file that will have the result of the reasoner which is the diagnosis of the disease for each image
```
* A shell script [run_all.sh](https://github.com/anonymousUserblanked/MLLM_ONTO/blob/main/run_all.sh) is also provided to run the whole process

```
chmod +x run_all.sh
./run_all.sh <model> <ontology_path> <dataset_dir> <output_folder> <output_csv_path>
```
## References
 * [1] Hosain, A.S., Mehedi, M.H.K., Jerin, T.J., Hossain, M.M., Raja, S.H., Ferdoushi,H., Iqbal, S., Rasel, A.A.: Rice leaf disease detection with transfer learning approach. In: 2022 IEEE International Conference on Artificial Intelligence in Engineering and Technology (IICAIET). pp. 1–6. IEEE (2022)
 * [2]Jearanaiwongkul, W., Anutariya, C., Racharak, T., Andres, F.: An ontology-based expert system for rice disease identification and control recommendation. Applied Sciences 11(21), 10450 (2021)
