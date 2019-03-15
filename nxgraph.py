import networkx as nx
import numpy as np
import pandas as pd

mygraph = nx.DiGraph()

#start nodes
mygraph.add_edge('Start', 'Seattle', weight=0)
mygraph.add_edge('Start', 'Newport', weight=0)
mygraph.add_edge('Start', 'San Francisco', weight=0)
mygraph.add_edge('Start', 'USC', weight=0)

#day 1

mygraph.add_edge('Seattle', 'Boise', weight=494)
mygraph.add_edge('Newport', 'Boise', weight=561)
mygraph.add_edge('San Francisco', 'Boise', weight=648)
mygraph.add_edge('San Francisco', 'Salt Lake', weight=748)
mygraph.add_edge('San Francisco', 'Las Vegas', weight=630)
mygraph.add_edge('USC', 'Las Vegas', weight=275)
mygraph.add_edge('USC', 'Tucson', weight=528)

#day 2

mygraph.add_edge('Boise', 'Casper', weight=669)
mygraph.add_edge('Salt Lake', 'Casper', weight=402)
mygraph.add_edge('Salt Lake', 'Denver', weight=493)
mygraph.add_edge('Salt Lake', 'Albuquerque', weight=609)
mygraph.add_edge('Las Vegas', 'Albuquerque', weight=576)
mygraph.add_edge('Las Vegas', 'El Paso', weight=724)
mygraph.add_edge('Tucson', 'Albuquerque', weight=452)
mygraph.add_edge('Tucson', 'El Paso', weight=320)

#day 3

mygraph.add_edge('Casper', 'Pierre', weight=347)
mygraph.add_edge('Casper', 'Lincoln', weight=635)
mygraph.add_edge('Casper', 'Amarillo', weight=705)
mygraph.add_edge('Denver', 'Pierre', weight=526)
mygraph.add_edge('Denver', 'Lincoln', weight=667)
mygraph.add_edge('Denver', 'Amarillo', weight=424)
mygraph.add_edge('Albuquerque', 'Amarillo', weight=288)
mygraph.add_edge('Albuquerque', 'San Antonio', weight=199)
mygraph.add_edge('El Paso', 'Amarillo', weight=421)
mygraph.add_edge('El Paso', 'San Antonio', weight=555)

#day 4

mygraph.add_edge('Pierre', 'Minneapolis', weight=478)
mygraph.add_edge('Pierre', 'Kansas City', weight=598)
mygraph.add_edge('Lincoln', 'Minneapolis', weight=438)
mygraph.add_edge('Lincoln', 'Kansas City', weight=207)
mygraph.add_edge('Lincoln', 'Ft. Smith', weight=567)
mygraph.add_edge('Amarillo', 'Kansas City', weight=613)
mygraph.add_edge('Amarillo', 'Ft. Smith', weight=539)
mygraph.add_edge('Amarillo', 'Houston', weight=614)
mygraph.add_edge('San Antonio', 'Houston', weight=199)

#day 5

mygraph.add_edge('Minneapolis', 'Chicago', weight=465)
mygraph.add_edge('Minneapolis', 'St. Louis', weight=593)
mygraph.add_edge('Kansas City', 'Chicago', weight=527)
mygraph.add_edge('Kansas City', 'St. Louis', weight=256)
mygraph.add_edge('Kansas City', 'Nashville', weight=618)
mygraph.add_edge('Ft. Smith', 'St. Louis', weight=545)
mygraph.add_edge('Ft. Smith', 'Nashville', weight=501)
mygraph.add_edge('Ft. Smith', 'New Orleans', weight=601)
mygraph.add_edge('Houston', 'New Orleans', weight=352)

#day 6

mygraph.add_edge('Chicago', 'Pittsburg', weight=532)
mygraph.add_edge('Chicago', 'Roanoke', weight=717)
mygraph.add_edge('St. Louis', 'Pittsburg', weight=659)
mygraph.add_edge('St. Louis', 'Roanoke', weight=689)
mygraph.add_edge('Nashville', 'Roanoke', weight=435)
mygraph.add_edge('Nashville', 'Charlotte', weight=434)
mygraph.add_edge('Nashville', 'Talluhassee', weight=495)
mygraph.add_edge('New Orleans', 'Charlotte', weight=725)
mygraph.add_edge('New Orleans', 'Talluhassee', weight=388)

#day 7

mygraph.add_edge('Pittsburg', 'MIT', weight=680)
mygraph.add_edge('Pittsburg', 'Washington', weight=259)
mygraph.add_edge('Roanoke', 'MIT', weight=750)
mygraph.add_edge('Roanoke', 'Washington', weight=233)
mygraph.add_edge('Roanoke', 'Wilmington', weight=306)
mygraph.add_edge('Roanoke', 'Daytona Beach', weight=480)
mygraph.add_edge('Charlotte', 'Washington', weight=397)
mygraph.add_edge('Charlotte', 'Wilmington', weight=206)
mygraph.add_edge('Charlotte', 'Daytona Beach', weight=480)
mygraph.add_edge('Talluhassee', 'Wilmington', weight=496)
mygraph.add_edge('Talluhassee', 'Daytona Beach', weight=316)


#end nodes

mygraph.add_edge('MIT', 'End', weight=0)
mygraph.add_edge('Washington', 'End', weight=0)
mygraph.add_edge('Wilmington', 'End', weight=0)
mygraph.add_edge('Daytona Beach', 'End', weight=0)


#Check the shortest path
#print(nx.dijkstra_path(mygraph,'Start','End'))
#print(nx.shortest_path(mygraph,'Start','End','weight'))



#Initialize viterbi with start
def viterbi(graph):
    trace_list = []
    for i in graph.adj['Start']:
        smaller_list = []
        for x in graph.adj[i]:
            smaller_list.append((graph.adj[i][x]['weight'],x))
        value = min(smaller_list)
        trace_list.append(value)
    big_list = [trace_list]
    for i in range(6):
        trace_list = viterbi_repeat(graph,trace_list)
        big_list.append(trace_list)
    this_list = []
    for i in big_list:
        this_list.append(min(i)[1])
    return this_list,min(trace_list)

#Repeat this for the next days.
def viterbi_repeat(graph,some_list):
    trace_list = []
    for i in some_list:
        smaller_list = []
        for x in graph.adj[i[1]]:
            smaller_list.append((graph.adj[i[1]][x]['weight'] + i[0],x))
        value = min(smaller_list)
        trace_list.append(value)
    return trace_list


#print the trace of the graph and the final destination with the distance.
trace_list,final = viterbi(mygraph)
trace_str = 'Tracing the transcontinental\n'
for i in trace_list:
    trace_str += i
    if i != trace_list[-1]:
        trace_str += ' -> '
trace_str += '\nThe final destination is ' + final[1] + ' and it took ' + str(final[0]) + ' miles.'
print(trace_str)



