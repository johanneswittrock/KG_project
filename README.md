# KG_project
Project for "Foundations of Knowledge Graphs"
Group name: KG_Mates

# Setup
Prerequisite: Download Anaconda under https://www.anaconda.com/products/individual

To run the program the following steps (only tested on Windows) need to be done:

1. Clone the Ontolearn repository: git clone https://github.com/dice-group/Ontolearn.git
2. Start Anaconda Navigator
3. Launch CMD.exe Prompt
4. conda create -n temp python=3.7.1
5. conda activate temp
6. Move to the Ontolearn directory within the cmd.exe
7. pip install -e .
8. python -c "import ontolearn" 
9. Move to the project directory within the cmd.exe
10. pip install requests
11. Run the program: python main.py

Running the program may take a while. The result file can be found under "classification_result.ttl"
