from django.shortcuts import render
import networkx as nx

from django.shortcuts import render
from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.charts import Bar

#Función que recibe la cantidad de nodos para decidir que trabajar y calcular los ciclos de Hamilton
def calcular_ruta(n):
    if n == 5:
        G= nx.Graph()
        G.add_nodes_from(["A","B","C","D","E"])
        G.add_edges_from([("A", "B", {'weight': 4}),("A", "C", {'weight': 3}),("A", "D", {'weight': 5}),("A", "E", {'weight': 3}),("B", "C", {'weight': 5}),("B", "D", {'weight': 7}),("B", "E", {'weight': 2}),("C", "D", {'weight': 4}),("C", "E", {'weight': 6}),("D", "E", {'weight': 3})])



def bienvenida_view(request):
    # Crear una gráfica con pyecharts
    bar = Bar()
    bar.add_xaxis(["A", "B", "C", "D"])
    bar.add_yaxis("Ejemplo", [10, 20, 30, 40])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Gráfica Estática"))
    
    # Renderizar la gráfica en HTML
    bar_html = bar.render_embed()
    
    return render(request, 'myapp/bienvenida.html', {'bar_html': bar_html})

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
    return render(request, 'myapp/home.html', context)

def home_view(request): 
    return render(request, 'myapp/home.html')

# Vista para la página siguiente
def siguiente_view(request):
    # Puedes procesar el input del usuario aquí si es necesario
    user_input = request.POST.get('user_input', None)
    
    return render(request, 'myapp/bienvenida.html', {'user_input': user_input})

# Create your views here.
