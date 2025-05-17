import	random	as	rd
import	numpy	as	np
import	pathlib	as	pl
import	heapq	as	queue
import	math	as	mt

EDGE	=	'edge'
NEIG	=	'neighbor'
POS		=	'position'
DIST	=	'distancia de dijkstra'

class	Node:
	"	NODO	"

	def	__init__(self,id):
		self.id		=	str(id)
		self.dijAttr	=	{
			DIST:	0
		}
		self.attr	=	{
			EDGE:	[],
			NEIG:	[],
			POS:	np.array([rd.random(),rd.random()])	#	x,y
		}

class	Edge:
	"	ARISTA	"

	def __init__(self,Nsource,Ntarget,id,Eweight=0.1):
		self.SOURCE	=	Nsource
		self.TARGET	=	Ntarget
		self.WEIGHT	=	Eweight
		self.id		=	str(id)

class	Graph:
	"	GRAFO	"

	def	__init__(self,name="GR",dir='N'):
		self.NAME	=	str(name)	+	"_GRAPH"
		self.NODES	=	{}
		self.EDGES	=	{}
		self.DIREC	=	dir.upper()
	
	def	change_name(self,newName):
		"""
		Cambia el nombre identificador del grafo
		"""
		self.NAME	=	newName
	
	def	get_name(self):
		"""
		Entrega el nombre identificador del grafo
		"""
		return	self.NAME
	
	def	get_nodes(self):
		"""
		Entrega el diccionario de nodos del grafo
		"""
		return	self.NODES
	
	def	get_edges(self):
		"""
		Entrega el diccionario de aristas del grafo
		"""
		return	self.EDGES

	def addNode(self,id):
		"""
		Agrega un nodo al grafo
		"""
		if id not in self.NODES:
			self.NODES[str(id)]	=	Node(str(id))
		return	self.NODES[str(id)]
	
	def	addEdge(self,id,nodeSource,nodeTarget,weight=None):
		"""
		Agrega una arista al grafo
		"""
		if id not in self.EDGES:
			"	NODOS DE LA ARISTA	"
			n0				=	self.addNode(str(nodeSource))
			n1				=	self.addNode(str(nodeTarget))
			"	PESO DE LA ARISTA	"
			pos0			=	n0.attr[POS]
			pos1			=	n1.attr[POS]
			if	weight	is None:
				W0			=	mt.sqrt((pos0[0] - pos1[0])**2 + (pos0[1] - pos1[1])**2)
			else:
				W0			=	weight
			if	self.DIREC	==	'N':
				for edges in n0.attr[EDGE]:
					if	(edges.SOURCE.id	==	n1.id)	or	(edges.TARGET.id	==	n1.id):
						return	None
			edge			=	Edge(n0,n1,str(id),W0)
			self.EDGES[id]	=	edge
			"	AGREGAR LOS ATRIBUTOS AL NODO	"
			n0.attr[NEIG].append(n1)
			n1.attr[NEIG].append(n0)
			n0.attr[EDGE].append(edge)
			n1.attr[EDGE].append(edge)
		else:
			edge	=	None

		return edge
	
	def	GraphViz(self,GVdoc,GVdir="SaveGraph"):
		"""
		crea el archivo GV para gephi
		"""
		# Obtener el directorio actual del script
		current_dir	=	pl.Path(__file__).parent.absolute()
		save_dir	=	current_dir / GVdir
		# Crear la carpeta si no existe
		save_dir.mkdir(exist_ok=True)
		# Crear la ruta completa del archivo
		file_dir	=	save_dir / f"{GVdoc}.gv"

		nodelist	=	list(self.NODES.keys())
		body	=	'graph G {\n'
		for edge	in	self.EDGES.values():
			node0		=	edge.SOURCE.id
			node1		=	edge.TARGET.id
			Weight		=	round(edge.WEIGHT,4)
			nodoBody	=	str(node0)	+	' -- '	+	str(node1)
			EdgeBody	=	' [label="'	+	str(Weight)	+	'"];\n'
			body		+=	nodoBody	+	EdgeBody
			if str(node0) in nodelist:
				nodelist.remove(str(node0))
			if str(node1) in nodelist:
				nodelist.remove(str(node1))
		for	remainigNode	in	nodelist:
			body	+=	remainigNode	+	';\n'
		body	+=	'}\n'
		print("GUARDANDO ARCHIVO ",GVdoc,".gv.....\n",end="")
		file 	=	open(file_dir,'w+')
		file.write(body)
		print("ARCHIVO GUARDADO EXITOSAMENTE..")
	
	def node_exist(self, node):
		"""
		Verifica si un nodo existe en el grafo
		"""
		return node in self.NODES.values()
	
	def edge_exist(self, edge):
		"""
		Verifica si una arista existe en el grafo
		"""
		return edge in self.EDGES.values()
	
	def get_node_pos(self, node):
		"""
		Obtiene la posición (POS) de un nodo específico
		"""
		if str(node) in self.NODES:
			return self.NODES[str(node)].attr[POS]
		return	None
	
	def	get_node_degree(self,node):
		"""
		entrega el grado de un nodo
		"""
		if str(node) not in self.NODES:
			return	None
		return	int(len(self.NODES[str(node)].attr[NEIG]))
	
	def	get_random_edge(self):
		"""
		busca y entrega aleatoreamente una arista
		"""
		return	rd.choice(list(self.EDGES.values()))
	
	def	get_random_node(self):
		"""
		busca y entrega aleatoriamente un nodo
		"""
		return	rd.choice(list(self.NODES.values()))

	def	clone_Graph(self,name="self"):
		r	=	Graph()

		if	name	==	"self":
			r.NAME	=	self.NAME	+	"_Clone"
		else:
			r.NAME	=	str(name)
		r.NODES	=	self.NODES.copy()
		r.EDGES	=	self.EDGES.copy()

		return	r
	
	def	get_nodes_of_edge(self,edge):
		"""
		Entrega los nodos conectados a una arista 
		en formato de lista 
		"""
		nodes	=	[]
		if	self.edge_exist(edge):
			nodes.append(edge.SOURCE)
			nodes.append(edge.TARGET)
			return nodes
		return	None
	
	@staticmethod
	def	load_graph(FileName,FileDir,GraphName=None):
		"""
		Lee un archivo .gv y lo convierte en un grafo
		de esta clase.
		"""
		# Obtener el directorio actual del script
		current_dir	=	pl.Path(__file__).parent.absolute()
		save_dir	=	current_dir / FileDir
		# Crear la carpeta si no existe
		save_dir.mkdir(exist_ok=True)
		# Crear la ruta completa del archivo
		file_dir	=	save_dir / f"{FileName}.gv"
		print("Creando grafo   ...   ...")
		if	GraphName	==	None:
			Gret	=	Graph(str(FileName))
		else:
			Gret	=	Graph(str(GraphName))
		f	=	open(file_dir,'r')
		lines	=	f.readlines()
		for i in range(1,len(lines)-1):
			line	=	lines[i].replace('\n', '')
			line	=	line.replace(';', '')
			elements	=	line.split(' ')
			if len(elements)	==	3:
				Gret.addEdge('e'+str(i),elements[0],elements[2])
			else:
				Gret.addNode(elements[0])
		return	Gret
		
	def DFS_i(self, start_node=None):
		"""
		Realiza un recorrido DFS de modo iterativo y 
		genera el árbol DFS correspondiente 
		"""
		#	Se selecciona el nodo de inicio
		if start_node is None:	
			#	Si no se entrega un nodo se toma uno random
			str_n = self.get_random_node().id
		else:
			str_n = str(start_node.id)
			if str_n not in self.NODES:
				#	Si se entrega un nodo valido se crea uno random
				print("El nodo dado no existe en el grafo, se tomará uno aleatoriamente")
				str_n = self.get_random_node().id

		#	Se crean las listas para uso en la busqueda.
		visited = set()
		stack = [(str_n, None)]  # (nodo_actual, nodo_raiz)
		visit_order = []
		#	Se crea un nuevo grafo para el árbol
		dfs_tree = Graph(self.NAME	+	"_DFS_Tree_iterativo")  

		#	Se inicia la busqueda a lo ancho
		i	=	0	#	Contador para las aristas
		while stack:
			node_id, parent_id = stack.pop()
			if node_id not in visited:
				visited.add(node_id)
				visit_order.append(node_id)
				dfs_tree.addNode(node_id)  # Agregar el nodo al árbol

				# Registrar la arista en el árbol (si no es el nodo raíz)
				if parent_id is not None:
					i	=	i	+	1
					edge_id = "e"	+	str(i)
					dfs_tree.addEdge(edge_id, parent_id, node_id)

				# Apilar vecinos no visitados (en orden inverso para mantener el orden natural)
				neighbors = [neighbor.id for neighbor in self.NODES[node_id].attr[NEIG]]
				for neighbor in reversed(neighbors):
					if neighbor not in visited:
						stack.append((neighbor, node_id))

		return visit_order, dfs_tree
	
	def DFS_r(self, start_node=None):
		"""
		Realiza un recorrido DFS de modo recursivo y 
		genera el árbol DFS correspondiente 
	    """
		#	Se selecciona el nodo de inicio
		if start_node is None:	
			#	Si no se entrega un nodo se toma uno random
			str_n = self.get_random_node().id
		else:
			str_n = str(start_node.id)
			if str_n not in self.NODES:
				#	Si se entrega un nodo valido se crea uno random
				print("El nodo dado no existe en el grafo, se tomará uno aleatoriamente")
				str_n = self.get_random_node().id
			
		#	Se crean las listas para uso en la busqueda.
		visited = set()
		visit_order = []
		#	Se crea un nuevo grafo para el árbol
		dfs_tree = Graph(self.NAME	+	"_DFS_Tree_recursivo")  	
		#	Función auxiliar recursiva
		def _dfs_helper(node_id, parent_id=None):
			"""
		    Función recursiva que realiza el recorrido DFS y construir el árbol
		    """
			#	Marcar nodo como visitado y registrar en estructuras
			visited.add(node_id)
			visit_order.append(node_id)
			dfs_tree.addNode(node_id)  #	Agregar nodo al árbol DFS

			#	Si hay nodo raiz, crear arista en el árbol DFS
			if parent_id is not None:
				edge_id = "DFS_"	+	str(parent_id)	+	"_"	+	str(node_id)
				dfs_tree.addEdge(edge_id, parent_id, node_id)		
		    #	Explorar todos los vecinos del nodo actual
			for neighbor in self.NODES[node_id].attr[NEIG]:
				if neighbor.id not in visited:
					#	Llamada recursiva para vecinos no visitados
					_dfs_helper(neighbor.id, node_id)	#	El nodo actual será la raiz en la recursión
		#	Iniciar el recorrido DFS desde el nodo inicial
		_dfs_helper(str_n)
		return visit_order, dfs_tree
	
	def BFS(self, start_node=None):
		"""Realiza un recorrido BFS y genera el árbol DFS correspondiente 
		"""
		#	Se selecciona el nodo de inicio
		if start_node is None:	
			#	Si no se entrega un nodo se toma uno random
			str_n = self.get_random_node().id
		else:
			str_n = str(start_node.id)
			if str_n not in self.NODES:
				#	Si se entrega un nodo valido se crea uno random
				print("El nodo dado no existe en el grafo, se tomará uno aleatoriamente")
				str_n = self.get_random_node().id

		#	Se crean las listas para uso en la busqueda.
		visited = set()
		queue = [(str_n, None)]	#	(nodo_actual, nodo_raiz)
		visit_order = []
		#	Se crea un nuevo grafo para el árbol
		bfs_tree = Graph(self.NAME	+	"_BFS_Tree")

		#	Se inicia la busqueda a lo ancho
		edge_counter = 0	#	Contador para las aristas
		while queue:
			#	Extraer el primer nodo de la cola
			node_id, parent_id = queue.pop(0)
			
			if node_id not in visited:
				#	Procesar nodo actual
				visited.add(node_id)
				visit_order.append(node_id)
				bfs_tree.addNode(node_id)  # Agregar nodo al árbol

				#	Registrar arista en el árbol (excepto para raíz)
				if parent_id is not None:
					edge_counter += 1
					edge_id = "e"	+	str(edge_counter)
					bfs_tree.addEdge(edge_id, parent_id, node_id)

				#	Encolar vecinos no visitados de manera alfabetica (sorted es para ordenarlo)
				neighbors = sorted(
					[neighbor.id for neighbor in self.NODES[node_id].attr[NEIG]],
					key=lambda x: x  # Orden alfabético/númerico
				)
				for neighbor in neighbors:
					if neighbor not in visited:
						queue.append((neighbor, node_id))

		return visit_order, bfs_tree
	
	def Dijkstra(self, start_node=None):
		"""
		Retorna un árbol de dijkstra.
		Si no se proporciona un nodo inicial válido, se selecciona uno aleatoriamente.
		"""
		# Obtener ID del nodo inicial o seleccionar aleatoriamente si no es válido
		try:
			start_id = str(start_node.id) if hasattr(start_node, 'id') else str(start_node)
			if start_id not in self.NODES:
				start_node = self.get_random_node()
				start_id = start_node.id
		except (AttributeError, TypeError):
			start_node = self.get_random_node()
			start_id = start_node.id

		# Inicialización EXPLÍCITA de distancias
		distancias = {}  # Diccionario para almacenar distancias mínimas
		
		# Para cada nodo en el grafo:
		for node_id in self.NODES:
			# Establecer distancia inicial como infinito (aún no descubierto)
			distancias[node_id] = float('inf')
		
		# La distancia al nodo inicial es 0
		distancias[start_id] = 0

		# Estructuras auxiliares
		padres = {}  # Para reconstruir rutas {hijo: (padre, peso_arista)}
		cola = [(0, start_id)]  # Cola de prioridad (distancia, nodo)
		visitados = set()  # Nodos ya procesados

		# Se crea el grafo a entregar 
		arbol = Graph(str(self.NAME)	+	'_DijkstraTree')	# se crea el arbol
		arbol.addNode(start_id)									# se agrega el nodo 
		arbol.NODES[start_id].dijAttr[DIST] = 0					# se le asigna su distancia de la raiz

		while cola:	# mientras la cola no esté vacia 
			dist_u, u = queue.heappop(cola)	# se extrae el nodo con la distancia minima
			if u in visitados:
				continue
			#	Si no está en visitados continua con el codigo y si está sigue con la siguiente iteración
			visitados.add(u)	# agrega el nodo a visitados
			#	Se revisan los vecinos del nodo actual
			for vecino in self.NODES[u].attr[NEIG]:
				#	Se vuelve a verificar que los nodos vecinos no sean de los explorados
				v = vecino.id
				if v in visitados:
					continue
				# Buscar peso de la arista u-v (versión detallada)
				peso = None
				#	Se busca en todas las aristas del nodo u la que está conectada a v
				for edge in self.NODES[u].attr[EDGE]:
					#	Como el grafo es no dirigido se verifica ambas direcciones de la arista
					if edge.TARGET.id == v or edge.SOURCE.id == v:
						peso = edge.WEIGHT
						break
				#	Solo para casos extremos donde no se encuentre un arista entre u y v
				if peso is None:
					continue
				
				# Se actializan las distancias
				distancia_tentativa = dist_u + peso	# obtenemos la ultima distancia y le agregamos el peso de la arista
				if distancia_tentativa < distancias[v]:	# si la distancia nueva es mejor a la ultima distancia conocida
														# para el nodo v entonces se actualiza
					distancias[v] = distancia_tentativa	# se agrega o cambia la nueva distancia a v
					padres[v] = (u,peso)				# se agrega el el padre de v que es u y el peso de la arista 
														# que los conecta
					queue.heappush(cola, (distancia_tentativa, v))	# se agrega el nuevo nodo con distancia minima y 
																	# su distancia 
					arbol.addNode(v)
					arbol.NODES[v].dijAttr[DIST]	=	distancia_tentativa
					arbol.NODES[v].attr[POS]		=	self.NODES[v].attr[POS]
		# Construcción del árbol
		nn	=	0	#contador de los nombres 
		for v, (u,peso) in padres.items():
			arbol.addEdge(str(nn), u, v,peso)
			nn	+=	1

		return arbol

	def	GraphVizDijkstra(self,GVdoc,GVdir="SaveGraph"):
		"""
		crea el archivo GV para gephi
		"""
		# Obtener el directorio actual del script
		current_dir	=	pl.Path(__file__).parent.absolute()
		save_dir	=	current_dir / GVdir
		# Crear la carpeta si no existe
		save_dir.mkdir(exist_ok=True)
		# Crear la ruta completa del archivo
		file_dir	=	save_dir / f"{GVdoc}.gv"

		nodelist	=	list(self.NODES.keys())
		body	=	'graph G {\n'
		for edge	in	self.EDGES.values():
			node0		=	edge.SOURCE.id
			node1		=	edge.TARGET.id
			Weight		=	round(edge.WEIGHT,4)
			# Obtener distancias de Dijkstra para cada nodo
			dist0		=	round(self.NODES[node0].dijAttr[DIST], 4)
			dist1		=	round(self.NODES[node1].dijAttr[DIST], 4)
			# Formatear los nombres de los nodos con sus distancias
			nodo0_fmt	=	'"'	+	str(node0)	+	'('	+	str(dist0)	+	')"'
			nodo1_fmt	=	'"'	+	str(node1)	+	'('	+	str(dist1)	+	')"'
			nodoBody	=	nodo0_fmt + ' -- ' + nodo1_fmt
			EdgeBody	=	' [label="' + str(Weight) + '"];\n'
			body		+=	nodoBody + EdgeBody
			if str(node0) in nodelist:
				nodelist.remove(str(node0))
			if str(node1) in nodelist:
				nodelist.remove(str(node1))
		for	remainigNode	in	nodelist:
			# Formatear también los nodos sin conexiones
			dist		=	round(self.NODES[remainigNode].dijAttr[DIST], 4)
			body	+=	f'"{remainigNode} ({dist})";\n'
		body	+=	'}\n'
		print("GUARDANDO ARCHIVO ",GVdoc,".gv.....\n",end="")
		file 	=	open(file_dir,'w+')
		file.write(body)
		print("ARCHIVO GUARDADO EXITOSAMENTE..")