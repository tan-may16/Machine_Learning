from os import error
import numpy as np
import csv
import sys
import math as m

def LoadData(input_file):
    data=[]
    line_count=0
    with open(input_file) as file:
        raw_data = csv.reader(file, delimiter="\t")
        for row in raw_data:
            if (line_count==0):
                line_count=1
            else:
                data.append(row) 
    data=np.asarray(data)
    return data

def CalculateEntropy(train_data):
    Labels=np.unique(train_data[:,-1])
    total_data=train_data.shape[0]
    y0=(train_data[train_data[:,-1]==Labels[0]])
    P0=y0.shape[0]/total_data
    
    if Labels.shape[0]==1:
        P1=0
        H=-(P0*m.log2(P0))
    else:
        y1=(train_data[train_data[:,-1]==Labels[1]])
        P1=y1.shape[0]/total_data
        H=-(P0*m.log2(P0) + P1*m.log2(P1))
    return H

def ReturnMajority(train_data):
    Labels=np.unique(train_data[:,-1])
    y0=(train_data[train_data[:,-1]==Labels[0]])
    y1=(train_data[train_data[:,-1]==Labels[1]])
    if (y0.shape[0]>=y1.shape[0]):
        return Labels[0]
    return Labels[1]

if __name__=="__main__":
    train_tsv=sys.argv[1]
    output_txt=sys.argv[2]
    train_data=LoadData(train_tsv)
    Entropy=CalculateEntropy(train_data)
    Majority_Label=ReturnMajority(train_data)
    
    error=train_data[train_data[:,-1]==Majority_Label].shape[0]/train_data.shape[0]

    OutputFile=open(output_txt,'w')
    OutputFile.write(f"entropy:{Entropy} \n")
    OutputFile.write(f"error:{error}")

