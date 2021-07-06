import os

prefix = """@prefix lpclass: <https://lpbenchgen.org/class/> .
@prefix carcinogenesis: <http://dl-learner.org/carcinogenesis#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml:   <http://www.w3.org/XML/1998/namespace> .
@prefix owl11: <http://www.w3.org/2006/12/owl11#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix lpres: <https://lpbenchgen.org/resource/> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix lpprop: <https://lpbenchgen.org/property/> .
@prefix owl11xml: <http://www.w3.org/2006/12/owl11-xml#> . \n"""

initialized = False

# deletes the result file if it exists and creates a new one with the prefixes
def initializeResultFile():
    global initialized
    global prefix
    if os.path.exists("classification_result.ttl"):
        os.remove("classification_result.ttl")
    f = open("classification_result.ttl", "w")
    f.write(prefix)
    f.close()
    initialized = True

# writes the positive and the negative individuals of a learning problem to the result file
def createResultFile(lp, resultNumber, positiveResults, negativeResults):
    global initialized

    # if the result file is not yet initialized, initialize the file
    if initialized is False:
        initializeResultFile()

    # string formatting the positive individuals
    presults1 = "lpres:result_" + str(resultNumber) + "pos lpprop:belongsToLP true ; \n"
    presults2 = "lpprop:pertainsTo lpres:lp_" + str(lp) + " ; \n"
    presults3 = "lpprop:resource  "
    for positiveResult in positiveResults:
        strresult = str(positiveResult)
        rhs = strresult[15:]
        presult = "carcinogenesis:" + rhs
        presults3 = presults3 + presult + " , "
    presults3 = presults3[:-2] + "."

    presults = presults1 + presults2 + presults3

    # string formatting the negative individuals
    nresults1 = "lpres:result_" + str(resultNumber) + "neg lpprop:belongsToLP false; \n"
    nresults2 = "lpprop:pertainsTo lpres:lp_" + str(lp) + " ; \n"
    nresults3 = "lpprop:resource  "
    for negativeResult in negativeResults:
        strresult = str(negativeResult)
        rhs = strresult[15:]
        nresult = "carcinogenesis:" + rhs
        nresults3 = nresults3 + nresult + " , "
    nresults3 = nresults3[:-2] + "."

    nresults = nresults1 + nresults2 + nresults3

    # write the positive and negative individuals to the result file
    result = presults + "\n" + nresults + "\n"
    f = open("classification_result.ttl", "a")
    f.write(result)
    f.close()
