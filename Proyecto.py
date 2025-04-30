import	graph_lib	as	gp
import	algoritmos	as	alg
import	pathlib		as	pl

#	Directorios a usar
Dir			=	pl.Path(__file__).parent.absolute()
Dir			=	Dir / "proyecto_2"
DirS		=	Dir	/	"SaveGraph"
DirBFS		=	Dir	/	"SaveGraph/BFS"
DirDFSi		=	Dir	/	"SaveGraph/DFSi"
DirDFSr		=	Dir	/	"SaveGraph/DFSr"

"""
Funcion para obtener los nombres de los archivos en un directorio
"""
def	List_files_on(addr):
	lista_nombres = []
	for archivo in pl.Path(addr).iterdir():
		if archivo.is_file() and archivo.suffix == '.gv':
			lista_nombres.append(archivo.stem)  # .stem elimina automáticamente la extensión
	return	lista_nombres

"""
Para proyecto 1
se crean los grafos con los metodos de generacion
"""
#	30 nodos
grMalla		=	alg.MetodoMalla(6,5)
grMalla.GraphViz('1Malla,6,5',DirS)
grEyR		=	alg.MetodoErdosyRenyi(30,75)
grEyR.GraphViz('1Erdos,30,75',DirS)
Gilbert		=	alg.MetodoGilbert(30,0.5)
Gilbert.GraphViz('1Gilbert,30,0_5',DirS)
GeoGraph	=	alg.MetodoGeoSimp(30,0.40)
GeoGraph.GraphViz('1Geografico,30,0_40',DirS)
Barabasi	=	alg.MetodoBarabasiAlbert(30,4)
Barabasi.GraphViz('1Barabasi,30,4',DirS)
Dorogovtsev	=	alg.MetodoDorogovtsev(30)
Dorogovtsev.GraphViz('1Dorogovtsev,30',DirS)
#	100 nodos
grMalla		=	alg.MetodoMalla(10,10)
grMalla.GraphViz('2Malla,10,10',DirS)
grEyR		=	alg.MetodoErdosyRenyi(100,250)
grEyR.GraphViz('2Erdos,100,250',DirS)
Gilbert		=	alg.MetodoGilbert(100,0.3)
Gilbert.GraphViz('2Gilbert,100,0_3',DirS)
GeoGraph	=	alg.MetodoGeoSimp(100,0.3)
GeoGraph.GraphViz('2Geografico,100,0_3',DirS)
Barabasi	=	alg.MetodoBarabasiAlbert(100,4)
Barabasi.GraphViz('2Barabasi,100,4',DirS)
Dorogovtsev	=	alg.MetodoDorogovtsev(100)
Dorogovtsev.GraphViz('2Dorogovtsev,100',DirS)
#	500 nodos
grMalla		=	alg.MetodoMalla(29,18)
grMalla.GraphViz('3Malla,29,18',DirS)
grEyR		=	alg.MetodoErdosyRenyi(500,1300)
grEyR.GraphViz('3Erdos,500,1300',DirS)
Gilbert		=	alg.MetodoGilbert(500,0.15)
Gilbert.GraphViz('3Gilbert,500,0_15',DirS)
GeoGraph	=	alg.MetodoGeoSimp(500,0.25)
GeoGraph.GraphViz('3Geografico,500,0_25',DirS)
Barabasi	=	alg.MetodoBarabasiAlbert(500,5)
Barabasi.GraphViz('3Barabasi,500,5',DirS)
Dorogovtsev	=	alg.MetodoDorogovtsev(500)
Dorogovtsev.GraphViz('3Dorogovtsev,500',DirS)

"""
Para proyecto 2
se leen los grafos y se crean los arboles con los 
metodos BFS y DFS(para metodo iterativo y recursivo)
"""

#	Lectura de los archivos
grafos	=	[]
names	=	List_files_on(DirS)
for	l	in	names:
	grafos.append(gp.Graph(l).load_graph(l,DirS))
TempOrder	=	[]
GRtemp		=	gp.Graph()
#	Creacion de arboles en BFS
for i in range(len(names)):
	TempOrder,GRtemp	=	grafos[i].BFS()
	GRtemp.GraphViz(names[i].replace('\n', ''),DirBFS)
#	Creacion de arboles en DFS iterativo
for i in range(len(names)):
	TempOrder,GRtemp	=	grafos[i].DFS_i()
	GRtemp.GraphViz(names[i].replace('\n', ''),DirDFSi)
#	Creacion de arboles en DFS recursivo
for i in range(len(names)):
	TempOrder,GRtemp	=	grafos[i].DFS_r()
	GRtemp.GraphViz(names[i].replace('\n', ''),DirDFSr)