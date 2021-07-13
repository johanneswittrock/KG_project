import os

# the prefixex as string for the result file
prefix = """@prefix carcinogenesis: <http://dl-learner.org/carcinogenesis#> .
@prefix lpres: <https://lpbenchgen.org/resource/> .
@prefix lpprop: <https://lpbenchgen.org/property/> . \n"""

initialized = False

# deletes the result file if it exists and creates a new one with the prefixes
def initializeResultFile():
    global initialized
    global prefix

    # check if the file already exists
    if os.path.exists("classification_result.ttl"):
        # if yes then delete it
        os.remove("classification_result.ttl")
    
    # create the result file
    f = open("classification_result.ttl", "w")
    # write the prefixes to the file
    f.write(prefix)
    f.close()
    # the file is now initialized
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
        # a individual is at this point a string which begins with "carcinogenesis."
        # but we want "carcinogenesis:"
        # therefore cut of the first 15 chars
        rhs = strresult[15:]
        # replace the first 15 chars with "carcinogenesis:"
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
        # a individual is at this point a string which begins with "carcinogenesis."
        # but we want "carcinogenesis:"
        # therefore cut of the first 15 chars
        rhs = strresult[15:]
        # replace the first 15 chars with "carcinogenesis:"
        nresult = "carcinogenesis:" + rhs
        nresults3 = nresults3 + nresult + " , "
    nresults3 = nresults3[:-2] + "."

    nresults = nresults1 + nresults2 + nresults3

    # write the positive and negative individuals to the result file
    result = presults + "\n" + nresults + "\n"
    f = open("classification_result.ttl", "a")
    f.write(result)
    f.close()
