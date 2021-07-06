import rdflib

from ontolearn import KnowledgeBase
from ontolearn.concept_learner import CustomConceptLearner
from ontolearn.heuristics import DLFOILHeuristic
import IndividualsParser as individualsParser
import ResultFile as resultFile

# parse the grading dataset
g = rdflib.Graph()
g.parse("kg-mini-project-grading.ttl", format="turtle")

# set the knowledge base to the carcinogenesis data
kb = KnowledgeBase(path='carcinogenesis.owl')

# iterate over all learning problems
i = 26
resultNumber = 1
while i <= 50:

    # SPARQL query to get the positive examples of the learning problem
    qres = g.query(
        "SELECT ?ex WHERE {<https://lpbenchgen.org/resource/lp_" + str(i) + "> <https://lpbenchgen.org/property/includesResource> ?ex .}"
    )
    positiveExamples = set()
    for row in qres:
        ex = str(row.ex)
        positiveExamples.add(ex)

    # SPARQL query to get the negative examples of the learning problem
    qres = g.query(
        "SELECT ?ex WHERE {<https://lpbenchgen.org/resource/lp_" + str(i) + "> <https://lpbenchgen.org/property/excludesResource> ?ex .}"
    )
    negativeExamples = set()
    for row in qres:
        ex = str(row.ex)
        negativeExamples.add(ex)

    # create the model with ontolearn
    model = CustomConceptLearner(knowledge_base=kb, heuristic_func=DLFOILHeuristic())

    # fit the model with the positive and negative examples
    model.fit(pos=positiveExamples, neg=negativeExamples)
    hypotheses = model.best_hypotheses(n=1)

    # get the missing individuals (individuals which are not in the positive or negative examples)
    missingIndividuals = individualsParser.getMissingIndividuals(list(positiveExamples) + list(negativeExamples))

    # classify the missing individuals
    predictions = model.predict(individuals=missingIndividuals, hypotheses=hypotheses)

    # rename prediction column
    predictions.columns = ["predictions"]

    # save the positive and negative individuals in a list
    positiveResults = list(predictions.loc[predictions["predictions"] == 1.0].index)
    negativeResults = list(predictions.loc[predictions["predictions"] == 0].index)

    # write the classification results to a result file
    resultFile.createResultFile(i, resultNumber, positiveResults, negativeResults)
    
    print("Learning Problem: " + str(i))
    print(predictions)
    

    i += 1
    resultNumber += 1


