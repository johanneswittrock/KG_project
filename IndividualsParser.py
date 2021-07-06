from owlready2 import * 
import rdflib

# retrieves the missing individuals which are not contained in the examples
def getMissingIndividuals(examples):
    print("examples length: " + str(len(examples)))

    # parse the training dataset, because all individuals are contained in the training dataset
    g = rdflib.Graph()
    g.parse("kg-mini-project-train.ttl", format="turtle")

    #SPARQL query to get all positive examples
    qres = g.query(
        "SELECT ?ex WHERE {<https://lpbenchgen.org/resource/lp_1> <https://lpbenchgen.org/property/includesResource> ?ex .}"
    )
    allPositiveExamples = set()
    for row in qres:
        ex = str(row.ex)
        allPositiveExamples.add(ex)

    #SPARQL query to get all negative examples
    qres = g.query(
        "SELECT ?ex WHERE {<https://lpbenchgen.org/resource/lp_1> <https://lpbenchgen.org/property/excludesResource> ?ex .}"
    )
    allNegativeExamples = set()
    for row in qres:
        ex = str(row.ex)
        allNegativeExamples.add(ex)

    # the positive and negative examples of a learning problem from the training dataset contain all individuals
    allIndividuals = list(allPositiveExamples) + list(allNegativeExamples)
    print("allindividuals length: " + str(len(allIndividuals)))

    missingIndividuals = []

    # iterate over all individuals
    for individual in allIndividuals:
      # check whether an individual is contained in the examples
      if individual not in examples:
        # if not then the individual is an missing individual
        missingIndividuals.append(individual)
    print("missingindividuals length: " + str(len(missingIndividuals)))
    return missingIndividuals
  
 
