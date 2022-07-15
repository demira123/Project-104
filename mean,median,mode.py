import pandas as pd
from collections import Counter 
def meanFunction():
    data=pd.read_csv("heightWeight.csv")

    weight= data["Weight(Pounds)"].tolist()

    sum=0
    for i in weight:
        sum=sum+i
    n = len(weight)

    mean=sum/n

    print("Mean : " , mean)
meanFunction()

def medianFunction():
    data=pd.read_csv("heightWeight.csv")

    weight = data["Weight(Pounds)"].tolist()


    weight.sort()

    n=len(weight)
    if n % 2 == 0:
        m1 = float(weight[n//2])  
        m2=float(weight[n//2-1])
        median=(m1+m2)/2
    else:
        median=float(weight[n//2])
    print("Median: ", median)
medianFunction()

def modeFunction():
    d = pd.read_csv("heightWeight.csv")

    weight = d["Weight(Pounds)"].tolist()

    data = Counter(weight)

    mode_data_for_range = {
                        "50-60" : 0,
                        "60-70" : 0,
                        "70-80" : 0
    }

    for weight,occurance in data.items():
        if 50 < float(weight)< 60:
            mode_data_for_range["50-60"] += occurance
        elif 60< float(weight)<70:
            mode_data_for_range["60-70"]+=occurance    
        elif 70<float(weight)<80:
            mode_data_for_range["70-80"] +=occurance   


    mode_range, mode_occurence = 0, 0

    for range, occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

    mode = float((mode_range[0] + mode_range[1]) / 2)

    print(f"Mode is :" , mode)
modeFunction()

