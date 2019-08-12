import os
import pandas as pd
import numpy as np


def read_data():
    #ensure working directory is correct
    os.chdir("/data/naveed/queensData")
    cwd = os.getcwd()

    if cwd != "/data/naveed/queensData":
        print("Not correct directory, current directory of operation is: ", cwd)
        exit()

    #loop through all the document in the directory and merge edited_sentence col for each document
    list_of_DF = np.array()
    for filename in os.listdir(cwd):
        df = pd.read_csv(filename, sep='\t')
        edited_sentences = df['edited_sentence'].apply(''.join).reset_index()
        list_of_DF.append(edited_sentences)

    return list_of_DF

