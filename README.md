# KG_project
Project for "Foundations of Knowledge Graphs"
Group name: KG_Mates

# Approach
Carcinogenesis is the process by which normal cells are transformed into cancer cells. Cell division is a normal physiological process. 
However, mutations in DNA that lead to cancer can disrupt the balance between proliferation and programmed cell death. 
This results in uncontrolled cell division and tumor formation.
There have been several approaches to predict carcinogenicity. Classifying chemicals is a massive challenge, due to the high number 
and diversity of elements, structures, and tests involved in the problem.

Our approach to predict carcinogenicity is based on the Ontolearn library (https://github.com/dice-group/Ontolearn), an open-source 
software library for explainable structured machine learning in Python. The library includes modules for processing knowledge bases, 
representation learning, inductive logic programming and ontology engineering.
Using RDFLib and SPARQL we retrieve the positive and negative examples for each learning problem from the dataset (kg-mini-project-grading.ttl). 
Based on those examples, we fit a model using Ontolearn for each learning problem (25 models in total).
In the next step we retrieve the missing individuals, which are not contained in the positive and negative examples for a learining problem.
Using the fitted model, we predict those missing individuals for each learning problem. The classification results are being written
to the "classification_result.ttl" file.

# Setup
Prerequisite: Download Anaconda under https://www.anaconda.com/products/individual

To run the program the following steps (only tested on Windows) need to be done:

1. Download/Clone the Ontolearn repository: git clone https://github.com/dice-group/Ontolearn.git
2. Start Anaconda Navigator
3. Launch CMD.exe Prompt
4. type "conda create -n temp python=3.7.1"
5. type "conda activate temp"
6. Move to your Ontolearn directory within the cmd.exe
7. type "pip install -e ."
8. type "python -c "import ontolearn""
9. Move to your directory of this project within the cmd.exe
10. type "pip install requests"
11. Run the program: python main.py

Running the program may take a while. The result file can be found under "classification_result.ttl"
