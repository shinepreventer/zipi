Zipi图绘制工具
这是一个用Python编写的工具，用于根据节点的Zi和Pi值，绘制网络的Zipi图，以及输出节点的角色和其他信息。Zipi图是一种用于分析网络结构和节点角色的可视化方法，它可以将节点根据它们在社区内部和社区间的连接度，分为不同的区域，反映节点的不同角色。例如，模块中心，模块枢纽，网络枢纽，边缘节点等。

功能
这个工具可以实现以下的功能：

读取边文件和节点文件，构建网络图，并使用Louvain算法进行社区划分。
计算每个节点的Zi和Pi值，以及所属的社区，度数，角色，标签等信息，并将它们存储在一个数据框中。
绘制Zipi图，根据节点的Zi和Pi值，将节点分为四个或七个区域，用不同的颜色表示不同的角色，并将Zipi图保存为png格式的图片。
输出数据框，将每个节点的信息输出到一个txt文件中，方便查看和分析。
使用方法
要使用这个工具，您需要按照以下的步骤操作：

运行zipi.py文件，这会弹出一个窗口，提示您选择边文件，节点文件和输出文件夹的路径。
选择边文件，这是一个txt格式的文件，每一行表示一条边，由两个节点的标签和一个权重组成，用空格分隔。例如，A B 1表示节点A和节点B之间有一条权重为1的边。
选择节点文件，这是一个txt格式的文件，每一行表示一个节点，由一个节点的标签和一个标签组成，用空格分隔。例如，A apple表示节点A的标签是apple。
选择输出文件夹，这是一个文件夹的路径，用于存储输出的Zipi图和数据框。例如，C:\Users\user\Desktop\output表示输出文件夹是桌面上的output文件夹。
点击运行按钮，这会开始执行代码，构建网络图，计算节点的信息，绘制Zipi图，输出数据框。这可能需要一些时间，取决于您的网络的大小和复杂度。
等待运行完成，这会在窗口上显示一个消息，告诉您运行是否成功，以及输出文件的路径。您可以在输出文件夹中查看Zipi图和数据框，或者使用其他的工具进行进一步的分析。
依赖的包
要运行这个工具，您需要安装以下的Python包：

pandas: 用于处理数据框和文件的输入输出。
networkx: 用于构建和分析网络图。
matplotlib: 用于绘制Zipi图和其他的可视化。
numpy: 用于进行数学和统计的计算。
tkinter: 用于创建图形用户界面。
community: 用于进行社区划分的算法。
您可以使用pip或conda等工具来安装这些包，或者使用已经包含这些包的Python发行版，例如Anaconda。

Zipi Plot Drawing Tool
This is a tool written in Python, used to draw Zipi plots of networks based on the Zi and Pi values of the nodes, and output the roles and other information of the nodes. Zipi plot is a visualization method for analyzing network structure and node roles, which can divide nodes into different regions according to their degree of connectivity within and between communities, reflecting the different roles of nodes. For example, module hubs, module connectors, network hubs, peripherals, etc.

Features
This tool can achieve the following features:

Read edge file and node file, build network graph, and use Louvain algorithm for community partitioning.
Calculate the Zi and Pi values of each node, as well as the community, degree, role, label and other information of each node, and store them in a data frame.
Draw Zipi plot, according to the Zi and Pi values of the nodes, divide the nodes into four or seven regions, use different colors to indicate different roles, and save the Zipi plot as a png format image.
Output data frame, output the information of each node to a txt file, for easy viewing and analysis.
Usage
To use this tool, you need to follow the following steps:

Run zipi.py file, this will pop up a window, prompting you to select the path of the edge file, node file and output folder.
Select edge file, this is a txt format file, each line represents an edge, consisting of two node labels and a weight, separated by spaces. For example, A B 1 means that there is an edge with a weight of 1 between node A and node B.
Select node file, this is a txt format file, each line represents a node, consisting of a node label and a label, separated by spaces. For example, A apple means that the label of node A is apple.
Select output folder, this is a folder path, used to store the output Zipi plot and data frame. For example, C:\Users\user\Desktop\output means that the output folder is the output folder on the desktop.
Click the run button, this will start executing the code, building the network graph, calculating the node information, drawing the Zipi plot, outputting the data frame. This may take some time, depending on the size and complexity of your network.
Wait for the run to complete, this will display a message on the window, telling you whether the run was successful, and the output file path. You can view the Zipi plot and data frame in the output folder, or use other tools for further analysis.
Dependencies
To run this tool, you need to install the following Python packages:

pandas: for handling data frames and file input and output.
networkx: for building and analyzing network graphs.
matplotlib: for drawing Zipi plots and other visualizations.
numpy: for mathematical and statistical calculations.
tkinter: for creating graphical user interface.
community: for community partitioning algorithm.
You can use tools like pip or conda to install these packages, or use a Python distribution that already contains these packages, such as Anaconda.
