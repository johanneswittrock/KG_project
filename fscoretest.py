import rdflib

from ontolearn import KnowledgeBase
from ontolearn.concept_learner import CustomConceptLearner
from ontolearn.heuristics import DLFOILHeuristic
import pandas as pd
from sklearn.metrics import f1_score

g = rdflib.Graph()
g.parse("kg-mini-project-train.ttl", format="turtle")
print(len(g))

kb = KnowledgeBase(path='carcinogenesis.owl')

i = 1
while i <= 25:

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

    predictions = model.predict(individuals=list(positiveExamples) + list(negativeExamples), hypotheses=hypotheses)

    df = pd.DataFrame(predictions)
    df.columns = ["predictions"]
    prediction_values = df["predictions"].tolist()
    
    true_values = []
    for v in positiveExamples:
        true_values.append(1.0)
    for v in negativeExamples:
        true_values.append(0)

    print("Learning Problem: " + str(i))
    

    f1 = f1_score(true_values,prediction_values)

    print("F1 Score: " + str(f1))

    i = i + 1


