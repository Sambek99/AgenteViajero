from django.shortcuts import render
import networkx as nx

from django.shortcuts import render
from pyecharts import options as opts
from pyecharts.charts import Graph

#def index(request):
#    line_chart = (
#        Line()
#        .add_xaxis(["Jan", "Feb", "Mar", "Apr", "May"])
#        .add_yaxis("Sales", [5, 20, 36, 10, 75])
#        .set_global_opts(title_opts=opts.TitleOpts(title="Line Chart"))
#    )
#    line_chart.render("myapp/static/line_chart.html")
#    return render(request, 'index.html')

#
def graph_view(request):
    # Crear un grafo simple
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5)])

    # Convertir el grafo a un formato que pyecharts pueda usar
    nodes = [{'name': str(node), 'symbolSize': 20} for node in G.nodes()]
    links = [{'source': str(edge[0]), 'target': str(edge[1])} for edge in G.edges()]

    # Crear el gráfico con pyecharts
    graph = (
        Graph()
        .add('', nodes, links, repulsion=8000)
        .set_global_opts(title_opts=opts.TitleOpts(title='Grafo'))
    )

    # Renderizar el gráfico en HTML
    graph_html = graph.render_embed()

    # Pasar el HTML a la plantilla
    context = {'graph_html': graph_html}
    return render(request, 'myapp/graph.html', context)

def home_view(request): 
    return render(request, 'myapp/home.html')

# Create your views here.
