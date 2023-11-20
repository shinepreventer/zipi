import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog
#模块中心，这些节点在其所属社区中有很高的内部连接度，但与其他社区的连接很少，它们是社区内部的核心节点，维持着社区的稳定性和一致性。
#Module hubs, these nodes have a high degree of internal connectivity within their communities, but few connections with other communities. They are the core nodes within the communities, maintaining the stability and consistency of the communities. These nodes are characterized by Zi > 2.5 and Pi < 0.62.
#模块枢纽，这些节点在其所属社区中有很高的内部连接度，同时也有一定的外部连接，它们是社区内部的重要节点，也是社区间的桥梁节点，促进了社区的交流和合作。
#Connectors, these nodes have a high degree of internal connectivity within their communities, as well as some external connections. They are important nodes within the communities, as well as bridge nodes between communities, facilitating communication and cooperation among communities. These nodes are characterized by Zi < 2.5 and Pi > 0.62.
#网络枢纽，这些节点在其所属社区中有很高的内部连接度，同时也有很多的外部连接，它们是网络中的关键节点，连接了不同的社区，形成了网络的骨干结构，对网络的整体性和效率有重要影响。
#Network hubs, these nodes have a high degree of internal connectivity within their communities, as well as many external connections. They are key nodes in the network, connecting different communities, forming the backbone structure of the network, and having a significant impact on the network’s integrity and efficiency. These nodes are characterized by Zi > 2.5 and Pi > 0.62.
#边缘节点，这些节点在其所属社区中有很低的内部连接度，也几乎没有外部连接，它们是社区内部的边缘节点，对社区的贡献和影响很小。
#Peripherals, these nodes have a low degree of internal connectivity within their communities, and almost no external connections. They are marginal nodes within the communities, contributing and influencing little to the communities.
#R1，超边缘节点，这些节点在其所属社区中有很高的内部连接度，但与其他社区的连接非常少，它们是社区内部的孤立节点，几乎没有与其他节点的联系。这些节点的特征是Zi > 2.5 且 Pi < 0.05。
#R2，边缘节点，这些节点在其所属社区中有很高的内部连接度，但与其他社区的连接很少，它们是社区内部的边缘节点，对社区的贡献和影响很小。这些节点的特征是Zi > 2.5 且 0.05 <= Pi < 0.62。
#R3，非中心连接节点，这些节点在其所属社区中有很高的内部连接度，同时也有一定的外部连接，它们是社区内部的连接节点，但不是社区间的桥梁节点，对社区的交流和合作有一定的作用。这些节点的特征是Zi > 2.5 且 Pi > 0.62。
#R4，非中心无亲节点，这些节点在其所属社区中有很低的内部连接度，也几乎没有外部连接，它们是社区内部的无亲节点，没有与其他节点的联系，也没有与社区的归属感。这些节点的特征是-2.5 <= Zi <= 2.5 且 Pi < 0.05。
#R5，省级中心，这些节点在其所属社区中有很低的内部连接度，但与其他社区的连接很少，它们是社区内部的中心节点，对社区的稳定性和一致性有重要影响。这些节点的特征是-2.5 <= Zi <= 2.5 且 0.05 <= Pi < 0.62。
#R6，连接中心，这些节点在其所属社区中有很低的内部连接度，同时也有很多的外部连接，它们是社区间的桥梁节点，连接了不同的社区，对社区的交流和合作有重要作用。这些节点的特征是-2.5 <= Zi <= 2.5 且 Pi > 0.62。
#R7，无亲中心，这些节点在其所属社区中有很低的内部连接度，同时也有很多的外部连接，它们是网络中的关键节点，连接了不同的社区，形成了网络的骨干结构，对网络的整体性和效率有重要影响。这些节点的特征是Zi < -2.5 且 Pi > 0.62。
#R1, Ultra-peripheral nodes, these nodes have a high degree of internal connectivity within their communities, but very few connections with other communities. They are isolated nodes within the communities, having almost no contact with other nodes. These nodes are characterized by Zi > 2.5 and Pi < 0.05.
#R2, Peripheral nodes, these nodes have a high degree of internal connectivity within their communities, but few connections with other communities. They are marginal nodes within the communities, contributing and influencing little to the communities. These nodes are characterized by Zi > 2.5 and 0.05 <= Pi < 0.62.
#R3, Non-hub connectors, these nodes have a high degree of internal connectivity within their communities, as well as some external connections. They are connecting nodes within the communities, but not bridge nodes between communities, having some role in communication and cooperation among communities. These nodes are characterized by Zi > 2.5 and Pi > 0.62.
#R4, Non-hub kinless nodes, these nodes have a low degree of internal connectivity within their communities, and almost no external connections. They are kinless nodes within the communities, having no contact with other nodes, nor a sense of belonging to the communities. These nodes are characterized by -2.5 <= Zi <= 2.5 and Pi < 0.05.
#R5, Provincial hubs, these nodes have a low degree of internal connectivity within their communities, but few connections with other communities. They are central nodes within the communities, having a significant impact on the stability and consistency of the communities. These nodes are characterized by -2.5 <= Zi <= 2.5 and 0.05 <= Pi < 0.62.
#R6, Connector hubs, these nodes have a low degree of internal connectivity within their communities, as well as many external connections. They are bridge nodes between communities, connecting different communities, having a significant role in communication and cooperation among communities. These nodes are characterized by -2.5 <= Zi <= 2.5 and Pi > 0.62.
#R7, Kinless hubs, these nodes are the key nodes in the network, connecting different communities and forming the backbone structure of the network, has an important impact on the integrity and efficiency of the network. These nodes are characterized by Zi < -2.5 and Pi > 0.62.
#增加：节点连接度k输出

def zipi(G, node):
    module = G.nodes[node]['module']
    neighbors = list(G.neighbors(node))
    k = len(neighbors)
    k_in = 0
    k_out = 0
    for n in neighbors:
        if G.nodes[n]['module'] == module:
            k_in += 1
        else:
            k_out += 1
    k_in_mean = np.mean([len(list(G.neighbors(n))) for n in G.nodes if G.nodes[n]['module'] == module])
    k_in_std = np.std([len(list(G.neighbors(n))) for n in G.nodes if G.nodes[n]['module'] == module])
    if k_in_std == 0:
        Zi = 0
    else:
        Zi = (k_in - k_in_mean) / k_in_std
    Pi = k_out / k
    return Zi, Pi

def role(Zi, Pi):
    if Zi > 2.5 and Pi < 0.62:
        return 'Module hubs'
    elif Zi < 2.5 and Pi > 0.62:
        return 'Connectors'
    elif Zi > 2.5 and Pi > 0.62:
        return 'Network hubs'
    else:
        return 'Peripherals'

def role_7(Zi, Pi):
    names = {'R1': 'Ultra-peripheral node', 'R2': 'Peripheral node', 'R3': 'Non-hub connector', 'R4': 'Non-hub kinless node', 'R5': 'Provincial hub', 'R6': 'Connector hub', 'R7': 'Kinless hub'}
    if Zi > 2.5 and Pi < 0.05:
        return 'R1'
    elif Zi > 2.5 and 0.05 <= Pi < 0.62:
        return 'R2'
    elif Zi > 2.5 and Pi > 0.62:
        return 'R3'
    elif -2.5 <= Zi <= 2.5 and Pi < 0.05:
        return 'R4'
    elif -2.5 <= Zi <= 2.5 and 0.05 <= Pi < 0.62:
        return 'R5'
    elif -2.5 <= Zi <= 2.5 and Pi > 0.62:
        return 'R6'
    else:
        return 'R7'

def zipi_plot(G, output_path):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.set_title('Zipi plot')
    ax.set_xlabel('Pi')
    ax.set_ylabel('Zi')
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-10, 10)
    ax.set_xticks(np.arange(0, 1.1, 0.1))
    ax.set_yticks(np.arange(-10, 10.1, 1))
    ax.grid(True)
    regions = {'Module hubs' : 'lightblue'  , 'Connectors' : 'lightgreen' , 'Network hubs' : 'lightyellow' , 'Peripherals' : 'lightpink' }
    ax.fill_between([0, 0.62], [2.5, 2.5], 10, color=regions['Module hubs'])
    ax.fill_between([0.62, 1], [2.5, 2.5], 10, color=regions['Network hubs'])
    ax.fill_between([0, 0.62], [-10, -10], 2.5, color=regions['Peripherals'])
    ax.fill_between([0.62, 1], [-10, -10], 2.5, color=regions['Connectors'])
    colors = {'R1': 'red', 'R2': 'orange', 'R3': 'yellow', 'R4': 'green', 'R5': 'blue', 'R6': 'purple', 'R7': 'black'}
    for node in G.nodes:
        Zi = G.nodes[node]['Zi']
        Pi = G.nodes[node]['Pi']
        role = G.nodes[node]['role_7']
        color = colors[role]
        ax.scatter(Pi, Zi, c=color, s=50, alpha=0.8, edgecolors='none')
    plt.savefig(output_path + '/zipi_plot.png')
    plt.show()

def main():
    root = tk.Tk()
    root.title('请输入文件路径')
    root.geometry('400x200')
    label = tk.Label(root, text='请分别选择边文件，节点文件和输出文件夹的路径', font=('Arial', 12))
    label.pack(side='top')
    edge_file = tk.StringVar()
    def select_edge_file():
        path = filedialog.askopenfilename(title='请选择边文件', filetypes=[('TXT', '*.txt')])
        if path:
            edge_file.set(path)
    button1 = tk.Button(root, text='选择边文件', command=select_edge_file)
    button1.pack(side='top', anchor='s')
    node_file = tk.StringVar()
    def select_node_file():
        path = filedialog.askopenfilename(title='请选择节点文件', filetypes=[('TXT', '*.txt')])
        if path:
            node_file.set(path)
    button2 = tk.Button(root, text='选择节点文件', command=select_node_file)
    button2.pack(side='top', anchor='s')
    output_path = tk.StringVar()
    def select_output_path():
        path = filedialog.askdirectory(title='请选择输出文件夹')
        if path:
            output_path.set(path)
    button3 = tk.Button(root, text='选择输出文件夹', command=select_output_path)
    button3.pack(side='top')
    def run():
        edge_file_path = edge_file.get()
        node_file_path = node_file.get()
        output_path_path = output_path.get()
        if edge_file_path and node_file_path and output_path_path:
            edge_df = pd.read_csv(edge_file_path, sep='\t')
            node_df = pd.read_csv(node_file_path, sep='\t')
            G = nx.Graph()
            for i, row in edge_df.iterrows():
                source = row['source']
                target = row['target']
                correlation = row['correlation']
                direct = row['direct']
                G.add_edge(source, target, correlation=correlation, direct=direct)
            for i, row in node_df.iterrows():
                ID = row['ID']
                Domain = row['Domain']
                Kingdom = row['Kingdom']
                Phylum = row['Phylum']
                Class = row['Class']
                Order = row['Order']
                Family = row['Family']
                Genus = row['Genus']
                Species = row['Species']
                mean = row['mean']
                Label = row['Label']
                G.add_node(ID, Domain=Domain, Kingdom=Kingdom, Phylum=Phylum, Class=Class, Order=Order, Family=Family, Genus=Genus, Species=Species, mean=mean, Label=Label)
            import community as community_louvain
            partition = community_louvain.best_partition(G)
            for node in G.nodes:
                G.nodes[node]['module'] = partition[node]
            result_df = pd.DataFrame(columns=['z', 'p', 'module', 'k', 'roles', 'label', 'role_7'])
            for node in G.nodes:
                Zi, Pi = zipi(G, node)
                G.nodes[node]['Zi'] = Zi
                G.nodes[node]['Pi'] = Pi
                k = len(list(G.neighbors(node)))
                G.nodes[node]['k'] = k
                roles = role(Zi, Pi)
                G.nodes[node]['roles'] = roles
                label = G.nodes[node]['Label']
                G.nodes[node]['label'] = label
                names = {'R1': 'Ultra-peripheral node', 'R2': 'Peripheral node', 'R3': 'Non-hub connector', 'R4': 'Non-hub kinless node', 'R5': 'Provincial hub', 'R6': 'Connector hub', 'R7': 'Kinless hub'}
                r7 = role_7(Zi, Pi)
                G.nodes[node]['role_7'] = r7
                result_df = result_df._append({'z': Zi, 'p': Pi, 'module': partition[node], 'k': k, 'roles': roles, 'label': label, 'role_7': names[r7]}, ignore_index=True)
            result_df.to_csv(output_path_path + '/result.csv', sep=',', index=False)
            zipi_plot(G, output_path_path)
    button4 = tk.Button(root, text='运行', command=run)
    button4.pack(side='bottom')
    root.mainloop()

main()
