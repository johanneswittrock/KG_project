import rdflib
from ontolearn import KnowledgeBase,SampleConceptLearner, Refinement
from ontolearn.metrics import F1, PredictiveAccuracy, CELOEHeuristic,DLFOILHeuristic


g = rdflib.Graph()
g.parse("kg-mini-project-train.ttl", format="turtle")

print(len(g))
for subject, predicate, object in g:
    print(subject)
    print(predicate)
    print(object)
    break

#select positive (i think include resources are positive examples and exclude resources negative) examples for the first learning problem
qres = g.query(
    """SELECT ?ex 
    WHERE {<https://lpbenchgen.org/resource/lp_4> <https://lpbenchgen.org/property/includesResource> ?ex .}"""
)
positiveExamples = set()
for row in qres:
    ex = str(row.ex)
    positiveExamples.add(ex)


qres = g.query(
    """SELECT ?ex 
    WHERE {<https://lpbenchgen.org/resource/lp_4> <https://lpbenchgen.org/property/excludesResource> ?ex .}"""
)
negativeExamples = set()
for row in qres:
    ex = str(row.ex)
    negativeExamples.add(ex)

kb = KnowledgeBase(path='carcinogenesis.owl')
rho = Refinement(kb)
#for refs in enumerate(rho.refine(kb.thing)):
 #   print(refs)

model = SampleConceptLearner(knowledge_base=kb,
                             quality_func=F1(),
                             terminate_on_goal=True,
                             heuristic_func=DLFOILHeuristic(),
                             iter_bound=100,
                             verbose=False)

#does not work yet, i dont know why that error occurs
model.predict(pos=positiveExamples, neg=negativeExamples)
model.show_best_predictions(top_n=10)

