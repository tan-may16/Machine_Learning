import numpy as np
import inspection
import sys
import math as m


def MutualInformation(train_data,attribute_index):

    dataNum=train_data.shape[0]
    
    Entropy_Y=inspection.CalculateEntropy(train_data)
    attribute_names=np.unique(train_data[:,attribute_index])
    
    specific_data_0=train_data[train_data[:,attribute_index]==attribute_names[0]]
    specific_probability_0=specific_data_0.shape[0]/dataNum
    if attribute_names.shape[0]==1:
        specific_probability_1=0
        specific_Entropy_1=0
    else:
        specific_data_1=train_data[train_data[:,attribute_index]==attribute_names[1]]
        specific_probability_1=specific_data_1.shape[0]/dataNum
        specific_Entropy_1=inspection.CalculateEntropy(specific_data_1)
    
    specific_Entropy_0=inspection.CalculateEntropy(specific_data_0)
    
    I= Entropy_Y - (specific_probability_0*specific_Entropy_0) - (specific_probability_1*specific_Entropy_1)
    return I

def Find_Split_Index(train_data):
    I=[]
    for i in range(train_data.shape[1]):
        I_temp=MutualInformation(train_data,i)
        I.append(I_temp)
    I=np.asarray(I)
    split_index=np.argmax(I)
    return split_index

if __name__=="__main__":
    train_input=sys.argv[1]
    test_input=sys.argv[2]
    max_depth=int(sys.argv[3])
    train_out=sys.argv[4]
    test_out=sys.argv[5]
    metrics_out=sys.argv[6]
    train_data=inspection.LoadData(train_input)
    
    split_index=Find_Split_Index(train_data)
    
    
    
    