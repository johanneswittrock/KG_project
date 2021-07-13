import rdflib

# retrieves the missing individuals which are not contained in the examples
def getMissingIndividuals(examples):

    # parse the training dataset, because the positive + negative examples from a LP in the 
    # training dataset consist of all individuals
    g = rdflib.Graph()
    g.parse("kg-mini-project-train.ttl", format="turtle")

    #SPARQL query to get all positive examples from the first LP
    qres = g.query(
        "SELECT ?ex WHERE {<https://lpbenchgen.org/resource/lp_1> <https://lpbenchgen.org/property/includesResource> ?ex .}"
    )

    # save the positive examples as strings in a set
    allPositiveExamples = set()
    for row in qres:
        ex = str(row.ex)
        allPositiveExamples.add(ex)

    #SPARQL query to get all negative examples from the first LP
    qres = g.query(
        "SELECT ?ex WHERE {<https://lpbenchgen.org/resource/lp_1> <https://lpbenchgen.org/property/excludesResource> ?ex .}"
    )

    # save the negative examples as strings in a set
    allNegativeExamples = set()
    for row in qres:
        ex = str(row.ex)
        allNegativeExamples.add(ex)

    # the positive and negative examples of a learning problem from the training dataset contain all individuals
    allIndividuals = list(allPositiveExamples) + list(allNegativeExamples)

    missingIndividuals = []

    # iterate over all individuals
    for individual in allIndividuals:
      # check whether an individual is contained in the examples
      if individual not in examples:
        # if not then the individual is an missing individual
        # append the missing individual to a list
        missingIndividuals.append(individual)
    
    # return the list of the missing individuals
    return missingIndividuals
  
 
