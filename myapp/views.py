from django.shortcuts import render
import networkx as nx
from django.http import HttpResponse

from django.shortcuts import render
from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.charts import Bar
from django.shortcuts import redirect

#Función que recibe la cantidad de nodos para decidir que trabajar y calcular los ciclos de Hamilton
def encontrar_ciclos_hamilton(G, vertice_partida=None):
    # Inicializar la lista de ciclos de Hamilton
    ciclos_hamilton = []

    # Definir la función de backtracking
    def backtrack(v, camino):
        # Si el camino tiene la misma longitud que el número de vértices, es un ciclo de Hamilton
        if len(camino) == len(G.nodes):
            # Verificar si el camino es un ciclo
            if G.has_edge(camino[-1], camino[0]):
                ciclos_hamilton.append(camino[:])
            return

        # Explorar todos los vecinos del vértice actual
        for w in G.neighbors(v):
            # Si el vecino no está en el camino, agregarlo y seguir explorando
            if w not in camino:
                camino.append(w)
                backtrack(w, camino)
                camino.pop()

    # Si se especifica un vértice de partida, iniciar el backtracking desde ese vértice
    if vertice_partida is not None:
        if vertice_partida in G.nodes:
            backtrack(vertice_partida, [vertice_partida])
        else:
            print("El vértice de partida no existe en el grafo")
    # Si no se especifica un vértice de partida, iniciar el backtracking desde cada vértice
    else:
        for v in G.nodes:
            backtrack(v, [v])
    ciclos = []
    lista = []
    for ciclo in ciclos_hamilton:
        for i in range(len(ciclo)):
            if i+1 < len(ciclo):
                tupla = (ciclo[i],ciclo[i+1])
            elif i == len(ciclo):
                tupla = (ciclo[i],ciclo[0])
            lista.append(tupla)
        ciclos.append(lista)
        #print(lista)
        lista = []
    ciclos_p = []
    for ciclo in ciclos:
        datos = [[n[0],n[1],G.get_edge_data(n[0], n[1])['weight']] for n in ciclo]
        ciclos_p.append(datos)
    peso = 0
    dic_ciclos = dict()
    for ciclo in ciclos_p:
        for vertice in ciclo:
            peso+= vertice[-1]
            vertice.pop()
        dic_ciclos.update({ciclos_p.index(ciclo): {"ciclo":ciclo, 'weight': peso}})
        peso = 0
    return dic_ciclos


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
