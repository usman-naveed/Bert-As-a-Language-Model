import readData

#run lm_predict and get the BERT score for each of the documents
def main():

    #retrieve edited sentences
    documents = readData.read_data()
    print(documents[1])
