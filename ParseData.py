import rdflib

from ontolearn import KnowledgeBase
from ontolearn.concept_learner import CustomConceptLearner
from ontolearn.heuristics import DLFOILHeuristic

g = rdflib.Graph()
g.parse("kg-mini-project-train.ttl", format="turtle")
print(len(g))

kb = KnowledgeBase(path='carcinogenesis.owl')

i = 1
while i <= 25:

    #select positive (i think include resources are positive examples and exclude resources negative) examples for the first learning problem
    qres = g.query(
        "SELECT ?ex WHERE {<https://lpbenchgen.org/resource/lp_" + str(i) + "> <https://lpbenchgen.org/property/includesResource> ?ex .}"
    )
    positiveExamples = set()
    for row in qres:
        ex = str(row.ex)
        positiveExamples.add(ex)


    qres = g.query(
        "SELECT ?ex WHERE {<https://lpbenchgen.org/resource/lp_" + str(i) + "> <https://lpbenchgen.org/property/excludesResource> ?ex .}"
    )
    negativeExamples = set()
    for row in qres:
        ex = str(row.ex)
        negativeExamples.add(ex)

    model = CustomConceptLearner(knowledge_base=kb, heuristic_func=DLFOILHeuristic())

    model.fit(pos=positiveExamples, neg=negativeExamples)
    hypotheses = model.best_hypotheses(n=1)

    ## vlt in der grading phase die individuals die missing carcinogenesis
    predictions = model.predict(individuals=list(positiveExamples) + list(negativeExamples), hypotheses=hypotheses)

    print("Learning Problem: " + str(i))
    print(predictions)

    i = i + 1


##die negativen sind nur teilweise da, muss die restlichen aus carsinogenesis holen, alle außer die die in den positiven sind
##