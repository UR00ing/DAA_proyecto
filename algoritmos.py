import	graph_lib	as	gp
import	random		as	rd

def	MetodoMalla(n,m):
	"""
	n=filas
	m=columnas
	"""
	#	Generacion del grafo
	gr0	=	gp.Graph('malla0')
	#	Se crean todos los nodos
	for	T	in	range(n*m):
		gr0.addNode(str(T))
	#	Se crean los nodos por fila y columna
		#	Se definen los contadores para los nombres de las aristas
		#	horizontales y verticales
	h_count	=	0
	v_count	=	0
	for	i	in	range(n):	# filas
		for	j	in	range(m):	# columnas
			nodo_actual	=	(i*m)+j
			#	Si el nodo está en la segunda columna o despues entonces se conecta 
			#	con el nodo de la columna anterior anterior en la misma fila
			if	j	<	m-1:
				nodo_der	=	nodo_actual	+	1
				gr0.addEdge('h'	+	str(h_count),str(nodo_actual),str(nodo_der))
				h_count	+=	1
			#	Si el nodo está en la segunda fila o despues entonces se conecta
			#	con el nodo de la fila anterior en la misma columa
			if	i	<	n-1:
				nodo_down	=	nodo_actual	+	m
				gr0.addEdge('v'	+	str(v_count),str(nodo_actual),str(nodo_down))
				v_count	+=	1
	#	Se regresa el grafo
	return	gr0

def	MetodoErdosyRenyi(n,m):
	"""
	n=numero de nodos
	m=numero de aristas
	"""
	#	Generacion del grafo
	gr0	=	gp.Graph('EyR0')
	#	Se crean todos los nodos del grafo
	for	i	in 	range(n):
		gr0.addNode(str(i))
	#	Se propone un contador de aristas para crear todas
	ed	=	0
	#	Se crean las aristas con las condiciones
	while	ed	<	m:
		#	Se proponen 2 nodos aleatoreos
		n0	=	rd.randint(0,n-1)
		n1	=	rd.randint(0,n-1)
		#	Si los nodos son iguales no se hace la arista
		if	n1	!=	n0:
			#	Si ya existe la arista en cualquiera de los sentidos entonces se ignora
			if	not gr0.edge_exist(str(n0)+str(n1))	and	not gr0.edge_exist(str(n1)+str(n0)):
				#	Se agrga la arista y se cuenta
				E	=	gr0.addEdge(str(n0)+str(n1),n0,n1)
				if	E	!=	None:
					ed	+=	1
	#	Se regresa el grafo
	return	gr0

def	MetodoGilbert(n,p):
	"""
	n=numero de nodos
	p=probabilidad(0-1) de generar una arista entre un par dee nodos
	"""
	#	Generacion del grafo
	gr0	=	gp.Graph('Gilgert0')
	#	Se da un contador de aristas para dar un nombre a las aristas
	count	=	0
	#	Se generan todos los nodos			
	for	i	in	range(n):
		gr0.addNode(i)
	#	Se recorren los nodos para generar las aristas sin repetir nodos
	#	ni aristas en ninguna direccion
	for	i	in	range(n):
		for	j	in	range(i,n):
			#	Si se gana el sorteo procedemos
			if	rd.random()	<	p:
				#	Si los nodos no son iguales se genera la arista 
				#	y se aumenta el contador para los nombres
				if	j	!=	i:
					gr0.addEdge(count,i,j)
					count	+=	1
	#	Se regresa el grafo
	return	gr0

def	MetodoGeoSimp(n,r):
	"""
	n=numero de nodos
	r=distancia maxima entre nodos(0-1.4142)
	"""
	#	Generacion del grafo
	gr0	=	gp.Graph('GeoSimp0')
	#	Se establece la distancia maxima entre 2 puntos en un cuadro
	#	unitario, es la raiz de 2
	DisMax	=	2	**	0.5
	#	Se establece un valor maximo aceptable en caso de que sea mayor
	#	 el propuesto por el usuario
	rNew	=	r
	if	r	>	DisMax:
		rNew	=	DisMax
	#	Se crea un contador de aristas para nombrarlas
	count	=	0
	#	Se generan todos los nodos
	for	i	in	range(n):
		gr0.addNode(i)
	#	Se recorren todos los nodos para obtener las distancias entre ellos
	for	i	in	range(n):
		for	j	in	range(i,n):
			#	Se descartan los nodos que son iguales
			if	i	!=	j:
				#	Se obtiene la distancia entre los nodos
				dist	=	(((gr0.get_node_pos(i)[0]	-	gr0.get_node_pos(j)[0])	**	2)	+	
			((gr0.get_node_pos(i)[1]	-	gr0.get_node_pos(j)[1])	**	2))	**	0.5
				if	dist	<=	rNew:
					gr0.addEdge(count,i,j)
					count	+=	1
	#	Se regresa el grafo
	return	gr0

def	MetodoBarabasiAlbert(n,d):
	"""
	n=numero de nodos
	d=cantidad de aristas maxima por nodos
	"""
	#	Generacion del grafo
	gr0	=	gp.Graph('Barabasi')
	#	Se crea el primer nodo
	gr0.addNode(1)
	#	Se crea un bucle para crear todos los nodos
	for	i	in	range(1,n):
		#	Se crea el nodo que se va a conectar
		gr0.addNode(i+1)
		#	Se crea un bucle para recorrer todos los nodos ya creado
		for	j	in	range(1,i+1):
			#	Se obtiene el grado del nodo al que 
			#	se quiere conectar
			deg	=	gr0.get_node_degree(j)
			#	Se obtiene la disponibilidad el nodo
			p	=	1	-	(deg	/	d)
			#	Se compara la disponibilidad con la probabilidad 
			if	rd.random()	<	p:
				#	Si se cumple se cra la arista
				gr0.addEdge(str(i)+','+str(j),i+1,j)
	#	Se regresa el grafo
	return	gr0

def	MetodoDorogovtsev(n):
	"""
	n=numero de nodos
	"""
	#	Se crea el grafo
	gr0	=	gp.Graph('Dorogovtesv00')
	#	Se heace el primer triangulo de nodos
	gr0.addEdge('t0',0,1)
	gr0.addEdge('t1',1,2)
	gr0.addEdge('t2',2,0)
	#	Se delimita el metodo a 3 nodos
	if	n	<=	3:
		return	gr0
	for	i	in	range(3,n):
		rand	=	gr0.get_random_edge()
		gr0.addEdge("a"+str(i),i,rand.TARGET.id)
		gr0.addEdge("b"+str(i),i,rand.SOURCE.id)
	return	gr0
