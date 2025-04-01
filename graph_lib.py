import	random	as rd
import	numpy	as np
import pathlib	as pl

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

	def	__init__(self,name):
		self.NAME	=	name	+	"_GRAPH"
		self.NODES	=	{}
		self.EDGES	=	{}
	
	def addNode(self,id):
		if id not in self.NODES:
			self.NODES[str(id)]	=	Node(str(id))
		return	self.NODES[str(id)]
	
	def	addEdge(self,id,nodeSource,nodeTarget):
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
	
	def	GraphViz(self,GVdoc):
		# Obtener el directorio actual del script
		current_dir	=	pl.Path(__file__).parent.absolute()
		save_dir	=	current_dir / "SaveGraph"
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
		return node in self.NODES
	
	def edge_exist(self, edge):
		"""
		Verifica si una arista existe en el grafo
		"""
		return edge in self.EDGES
	
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
	
	def	get_node_from_edge(self,edge):
		"""
		regresa los nodos conectados a una arista
		"""