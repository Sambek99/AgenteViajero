from django.shortcuts import render
import networkx as nx
from django.http import HttpResponse

from django.shortcuts import render
from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.charts import Bar
from django.shortcuts import redirect

#Función que recibe la cantidad de nodos para decidir que trabajar y calcular los ciclos de Hamilton
def calcular_ruta(n):
    if n == 5:
        G= nx.Graph()
        G.add_nodes_from(["A","B","C","D","E"])
        G.add_edges_from([("A", "B", {'weight': 4}),("A", "C", {'weight': 3}),("A", "D", {'weight': 5}),("A", "E", {'weight': 3}),("B", "C", {'weight': 5}),("B", "D", {'weight': 7}),("B", "E", {'weight': 2}),("C", "D", {'weight': 4}),("C", "E", {'weight': 6}),("D", "E", {'weight': 3})])
        nodos = G.nodes()
        for i in nodos:
            print()
    return 0        


def bienvenida_view(request):
    # Crear una gráfica con pyecharts
    bar = Bar()
    bar.add_xaxis(["A", "B", "C", "D"])
    bar.add_yaxis("Ejemplo", [10, 20, 30, 40])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Gráfica Estática"))
    
    # Renderizar la gráfica en HTML
    bar_html = bar.render_embed()
    
    return render(request, 'myapp/bienvenida.html', {'bar_html': bar_html})




# Vista para la página siguiente
def siguiente_view(request):
    nodo_partida = None  # Define nodo_partida como None por defecto
    if request.method == 'POST':
        user_input = request.POST.get('user_input', None)
        if user_input:
            nodo_partida = request.session['nodo_partida'] = user_input
            # Devuelve una respuesta HTTP que indique que la solicitud fue procesada correctamente
            #return HttpResponse('Nodo de partida seleccionado correctamente')
    return render(request, 'myapp/home.html',{'nodo_partida': nodo_partida,'is_post': request.method == 'POST'})

# Create your views here.
