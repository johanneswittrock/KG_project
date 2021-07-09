# KG_project
Project for "Foundations of Knowledge Graphs"
Group name: KG_Mates

# Setup
Prerequisite: Download Anaconda under https://www.anaconda.com/products/individual

To run the program the following steps (only tested on Windows) need to be done:

1. Download/Clone the Ontolearn repository: git clone https://github.com/dice-group/Ontolearn.git
2. Start Anaconda Navigator
3. Launch CMD.exe Prompt
4. type "conda create -n temp python=3.7.1"
5. type "conda activate temp"
6. Move to the Ontolearn directory within the cmd.exe
7. type "pip install -e ."
8. type "python -c "import ontolearn" "
9. To check whether Ontolearn is installed correctly type: "python -m pytest tests"
10. Move to the project directory within the cmd.exe
11. pip install requests
12. Run the program: python main.py

Running the program may take a while. The result file can be found under "classification_result.ttl"
