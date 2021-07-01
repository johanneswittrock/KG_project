import rdflib

from ontolearn import KnowledgeBase
from ontolearn.concept_learner import CustomConceptLearner
from ontolearn.heuristics import DLFOILHeuristic
import pandas as pd
from sklearn.metrics import f1_score
import IndividualsParser as individualsParser

g = rdflib.Graph()
g.parse("kg-mini-project-grading.ttl", format="turtle")
print(len(g))

kb = KnowledgeBase(path='carcinogenesis.owl')

i = 26
while i <= 50:

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

    missingIndividuals = individualsParser.getMissingIndividuals(list(positiveExamples) + list(negativeExamples))
    predictions = model.predict(individuals=missingIndividuals, hypotheses=hypotheses)

    print("Learning Problem: " + str(i))
    print(predictions)
    

    i = i + 1


