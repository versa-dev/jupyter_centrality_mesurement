import networkx as nx
import pandas as pd

Data = pd.read_csv("1.csv")
chessID = list(Data["chessID"])
meetingID = list(Data["meetingID"])
year = list(Data["year"])
area = list(Data["area"])
index_range = len(area)
mem_count = len(list(dict.fromkeys(chessID)))
graph = []
num = []
for yy in range(2007, 2018):
    G = nx.Graph()
    for i in range(index_range):
        if(year[i] == yy):
            
            try:
                index = meetingID[i+1:].index(meetingID[i])
                G.add_edge((chessID[i],yy),(chessID[i+index+1],yy))
            except ValueError:
                pass
    graph.append(G)
    num.append(G.number_of_nodes())
G = nx.Graph()

for it in graph:
    degree = []
    degree = it.degree()
    ID = []
    Y = []
    deg = []
    for item in degree:
        ID.append(item[0][0])
        Y.append(item[0][1])
        deg.append(item[1])
    print("id",ID,"\n")
    print("year", Y, "\n")
    print("deg", deg,"\n")