import json
import math

def load_journal(val):
    with open(val) as f:
        data=json.load(f)
        f.close()
        return data

def compute_phi(file,event):
    n11=n00=n01=n10=0
    data=load_journal(file)
    for i in range(len(data)):
        if event in data[i]['events'] and data[i]['squirrel']:
            n11+=1
        elif event in data[i]['events']:
            n10+=1
        elif data[i]['squirrel']:
            n01+=1
        else:
            n00+=1
    phi=(n11*n00-n10*n01)/math.sqrt((n10+n11)*(n01+n00)*(n10+n00)*(n11+n01))              
    return phi

def compute_correlations(file):
    data=load_journal(file)
    events={}
    for i in range(len(data)):
        for j in data[i]['events']:
            if j not in events:
                events[j]=compute_phi(file,j) 
    return events

def diagnose(file):
    corr=compute_correlations(file)
    max_corr=max(corr,key = lambda x: corr[x])
    min_corr=min(corr,key = lambda x: corr[x])
    return (max_corr,min_corr)





# Add the functions in this file
