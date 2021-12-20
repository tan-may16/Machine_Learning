import sys
import csv
import numpy as np

def LoadData(input_file):
  data=[]
  with open(input_file) as tsv_file:
    line_count=0
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    for row in read_tsv:
      if (line_count==0):
        line_count=1
      else:
        data.append(row)
    data=np.asarray(data)
    return data

def PredictClass(train_data):
  
  attribute_names=np.unique(train_data[:,split_index])
  y_names=np.unique(train_data[:,-1])
  
  train_data_y=[]
  train_data_n=[]

  for i in range(len(train_data)):
    if (train_data[i][split_index]==attribute_names[1]):
      train_data_y.append(train_data[i])
  train_data_y=np.asarray(train_data_y)

  for i in range(len(train_data)):
    if (train_data[i][split_index]==attribute_names[0]):
      train_data_n.append(train_data[i])
  train_data_n=np.asarray(train_data_n)
 
  
  x1_y0=train_data_y[train_data_y[:,-1]==y_names[0]]
  x1_y1=train_data_y[train_data_y[:,-1]==y_names[1]]
  x0_y0=train_data_n[train_data_n[:,-1]==y_names[0]]
  x0_y1=train_data_n[train_data_n[:,-1]==y_names[1]]
  
  if (x1_y0.shape[0]>=x1_y1.shape[0]):
    Label_y=y_names[0]
    
  else:
    Label_y=y_names[1]

  if (x0_y0.shape[0]>=x0_y1.shape[0]):
    Label_n=y_names[0]  
  else:
    Label_n=y_names[1]
  
  Label=[attribute_names,Label_y,Label_n]

  return Label


def FindClass(train_input,test_input,split_index,train_data_prediction,test_data_prediction,metrics_file):
  test_data=LoadData(test_input)
  train_data=LoadData(train_input)

  Label=PredictClass(train_data)

  train_output=[]
  for i in range(train_data.shape[0]):
    if (train_data[i,split_index]==Label[0][1]):
      train_output.append(Label[1])
    else:
      train_output.append(Label[2])
  train_output=np.asarray(train_output)

  test_output=[]
  for i in range(test_data.shape[0]):
    if (test_data[i,split_index]==Label[0][1]):
      test_output.append(Label[1])
    else:
      test_output.append(Label[2])
  test_output=np.asarray(test_output)
  # print(test_output)

  train_wrong=train_output[train_output!=train_data[:,-1]]
  train_error=train_wrong.shape[0]/train_output.shape[0]
  test_wrong=test_output[test_output!=test_data[:,-1]]
  test_error=test_wrong.shape[0]/test_output.shape[0]

  file_train=open(train_data_prediction,'w')
  for output in train_output:
    file_train.write(output)
    file_train.write('\n')
  file_test=open(test_data_prediction,'w')
  for output in test_output:
    file_test.write(output)
    file_test.write('\n')

  file_metrics=open(metrics_out,'w')
  file_metrics.write("error(train):")
  file_metrics.write(str(train_error))
  file_metrics.write('\n')
  file_metrics.write("error(test):")
  file_metrics.write(str(test_error))
  

if __name__=='__main__':
  
  train_input=sys.argv[1]
  test_input=sys.argv[2]
  split_index=int(sys.argv[3])
  train_out=sys.argv[4]
  test_out=sys.argv[5]
  metrics_out=sys.argv[6]
  FindClass(train_input,test_input,split_index,train_out,test_out,metrics_out)
  
  