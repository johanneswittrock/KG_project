from owlready2 import * 
import rdflib


def getMissingIndividuals(examples):
    print("examples length: " + str(len(examples)))
    g = rdflib.Graph()
    g.parse("kg-mini-project-train.ttl", format="turtle")

    qres = g.query(
        "SELECT ?ex WHERE {<https://lpbenchgen.org/resource/lp_1> <https://lpbenchgen.org/property/includesResource> ?ex .}"
    )
    allPositiveExamples = set()
    for row in qres:
        ex = str(row.ex)
        allPositiveExamples.add(ex)


    qres = g.query(
        "SELECT ?ex WHERE {<https://lpbenchgen.org/resource/lp_1> <https://lpbenchgen.org/property/excludesResource> ?ex .}"
    )
    allNegativeExamples = set()
    for row in qres:
        ex = str(row.ex)
        allNegativeExamples.add(ex)

    allIndividuals = list(allPositiveExamples) + list(allNegativeExamples)
    print("allindividuals length: " + str(len(allIndividuals)))

    missingIndividuals = []

    for individual in allIndividuals:
      if individual not in examples:
        missingIndividuals.append(individual)
    print("missingindividuals length: " + str(len(missingIndividuals)))
    return missingIndividuals
  
 
