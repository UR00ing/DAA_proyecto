import	random	as rd
import	numpy	as np
import	pathlib	as pl
import	copy	as cp

EDGE = 'edge'
NEIG = 'neighbor'
POS = 'position'

class	Node:
	"	NODO	"

	def	__init__(self,id):
		self.id		=	str(id)
		self.attr	=	{
			EDGE:	[],
			NEIG:	[],
			POS:	np.array([rd.random(),rd.random()])
		}

class	Edge:
	"	ARISTA	"

	def __init__(self,Nsource,Ntarget,id):
		self.SOURCE	=	Nsource
		self.TARGET	=	Ntarget
		self.id		=	str(id)

class	Graph:
	"	GRAFO	"

	def	__init__(self,name="GR"):
		self.NAME	=	str(name)	+	"_GRAPH"
		self.NODES	=	{}
		self.EDGES	=	{}
	
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
	
	def	addEdge(self,id,nodeSource,nodeTarget):
		"""
		Agrega una arista al grafo
		"""
		if id not in self.EDGES:
			n0				=	self.addNode(str(nodeSource))
			n1				=	self.addNode(str(nodeTarget))
			edge			=	Edge(n0,n1,str(id))
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
		body	=	'digraph X {\n'
		for edge	in	self.EDGES.values():
			node0	=	edge.SOURCE.id
			node1	=	edge.TARGET.id
			body	+=	str(node0)	+	' -> '	+	str(node1)	+	';\n'
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