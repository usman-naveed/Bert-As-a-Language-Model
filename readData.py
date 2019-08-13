import os
import pandas as pd

#ensure working directory is correct
os.chdir("/data/naveed/queensData")
cwd = os.getcwd()
print(cwd)

if cwd != "/data/naveed/queensData":
    print("Not correct directory, current directory of operation is: ", cwd)
    exit()

#loop through all the document in the directory and merge edited_sentence col for each document
list_of_DF = []
for filename in os.listdir(cwd):
    df = pd.read_csv(filename, sep='\t')
    edited_sentences = df['edited_sentence'].str.cat(sep=' ')
    list_of_DF.append(edited_sentences)

print(len(list_of_DF))
print(list_of_DF[1].encode('utf-8', errors='ignore'))
