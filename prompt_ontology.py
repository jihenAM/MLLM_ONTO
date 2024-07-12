from owlready2 import *


# Function to extract all subclasses recursively
def extract_subclasses(cls):
    subclasses = []
    for subclass in cls.subclasses():
        subclasses.append(subclass.name)
        subclasses.extend(extract_subclasses(subclass))
    return subclasses


# extract_concepts() function is used to extract abnormality concepts (color, shape and symptoms) from the ontology
def extract_concepts():
    symptom = []
    color = []
    shape = []
    ColorAbnormality = None
    SymptomAbnormality = None
    ShapeAbnormality = None
    # Define the class "Abnormality"
    Abnormality = onto.Abnormality
    for cls in Abnormality.subclasses():
        if cls.name == "ColorAbnormality":
            ColorAbnormality = cls
            color = extract_subclasses(ColorAbnormality)
        elif cls.name == "SymptomAbnormality":
            SymptomAbnormality = cls
            symptom = extract_subclasses(SymptomAbnormality)
        elif cls.name == "ShapeAbnormality":
            ShapeAbnormality = cls
            shape = extract_subclasses(ShapeAbnormality)
    return symptom, color, shape
# Generate the prompt with extracted concepts
def generate_prompt(onto_path):
    #
    onto = get_ontology(onto_path).load()
    symptom, color, shape = extract_concepts()
    prompt = f"""
            As an expert of rice leaves diseases, your task is to examine the given image of the rice leaf in a detailed manner to look for colors abnormalities, symptoms abnormalities and shape of symptoms abnormalities.
            Alongside the image of rice leaf, you will be provided with the possible set of color abnormalities and symptoms abnormalities and the shape of these symptoms delimited by triple quote.

            Return the information in the following JSON format (note xxx is a placeholder, if the information is not available in the image, put “N/A” instead):
            {{"ColorAbnormality": {color}, "SymptomAbnormality": {symptom}, "ShapeOfSymptomAbnormality": {shape}}}
            """
    return prompt




