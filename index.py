#   imports
import pandas as panda, plotly_express as plotly

#   code
framed_data = panda.read_csv(r"C:\Swarup\WhiteHat Jr\Python\Projects\DataVis\Covid_data.csv")
scatter_graph = plotly.scatter(framed_data, x="date", y="cases", color="country")
scatter_graph.show()