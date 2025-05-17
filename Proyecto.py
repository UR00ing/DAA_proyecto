import	graph_lib	as	gp
import	algoritmos	as	alg
import	pathlib		as	pl

#	Directorios a usar
Dir			=	pl.Path(__file__).parent.absolute()
Dir			=	Dir / "proyecto_3"
DirS		=	Dir	/	"Graph"
DirDijkstra	=	Dir	/	"Dijkstra"

# Crear los directorios si no existen (incluyendo el directorio padre proyecto_3)
Dir.mkdir(exist_ok=True)
DirS.mkdir(exist_ok=True)
DirDijkstra.mkdir(exist_ok=True)

"""
Generacion de los grafos mediante generadores aleatorios
"""
#	pocos	80 aprox
#PgrMalla		=	alg.MetodoMalla(9,9)
#PgrEyR			=	alg.MetodoErdosyRenyi(80,180)
#PGilbert		=	alg.MetodoGilbert(80,0.3)
#PGeoGraph		=	alg.MetodoGeoSimp(80,0.35)
#PBarabasi		=	alg.MetodoBarabasiAlbert(80,5)
#PDorogovtsev	=	alg.MetodoDorogovtsev(80)
#PgrMalla.GraphViz('01Malla,9,9',DirS)
#PgrEyR.GraphViz('01Erdos,80,180',DirS)
#PGilbert.GraphViz('01Gilbert,80,0_3',DirS)
#PGeoGraph.GraphViz('01Geografico,80,0_35',DirS)
#PBarabasi.GraphViz('01Barabasi,80,5',DirS)
#PDorogovtsev.GraphViz('01Dorogovtsev,80',DirS)
#	muchos	350 aprox
MgrMalla		=	alg.MetodoMalla(18,20)
MgrEyR			=	alg.MetodoErdosyRenyi(350,900)
MGilbert		=	alg.MetodoGilbert(350,0.05)
MBarabasi		=	alg.MetodoBarabasiAlbert(350,5)
MGeoGraph		=	alg.MetodoGeoSimp(350,0.12)
MDorogovtsev	=	alg.MetodoDorogovtsev(350)
MgrMalla.GraphViz('02Malla,18,20',DirS)
MgrEyR.GraphViz('02Erdos,350,900',DirS)
MGilbert.GraphViz('02Gilbert,350,0_05',DirS)
MGeoGraph.GraphViz('02Geografico,350,0_12',DirS)
MBarabasi.GraphViz('02Barabasi,350,5',DirS)
MDorogovtsev.GraphViz('02Dorogovtsev,350',DirS)

"""
Dijkstra
"""
#	pocos
#PgrMallaDijkstra		=	PgrMalla.Dijkstra()
#PgrEyRDijkstra			=	PgrEyR.Dijkstra()
#PGilbertDijkstra		=	PGilbert.Dijkstra()
#PGeoGraphDijkstra		=	PGeoGraph.Dijkstra()
#PBarabasiDijkstra		=	PBarabasi.Dijkstra()
#PDorogovtsevDijkstra	=	PDorogovtsev.Dijkstra()
#	muchos
MgrMallaDijkstra		=	MgrMalla.Dijkstra()
MgrEyRDijkstra			=	MgrEyR.Dijkstra()
MGilbertDijkstra		=	MGilbert.Dijkstra()
MBarabasiDijkstra		=	MBarabasi.Dijkstra()
MGeoGraphDijkstra		=	MGeoGraph.Dijkstra()
MDorogovtsevDijkstra	=	MDorogovtsev.Dijkstra()

#PgrMallaDijkstra.GraphVizDijkstra('01MallaDijkstra,9,9',DirDijkstra)
#PgrEyRDijkstra.GraphVizDijkstra('01ErdosDijkstra,80,180',DirDijkstra)
#PGilbertDijkstra.GraphVizDijkstra('01GilbertDijkstra,80,0_3',DirDijkstra)
#PGeoGraphDijkstra.GraphVizDijkstra('01GeograficoDijkstra,80,0_35',DirDijkstra)
#PBarabasiDijkstra.GraphVizDijkstra('01BarabasiDijkstra,80,5',DirDijkstra)
#PDorogovtsevDijkstra.GraphVizDijkstra('01DorogovtsevDijkstra,80',DirDijkstra)

MgrMallaDijkstra.GraphVizDijkstra('02MallaDijkstra,18,20',DirDijkstra)
MgrEyRDijkstra.GraphVizDijkstra('02ErdosDijkstra,350,900',DirDijkstra)
MGilbertDijkstra.GraphVizDijkstra('02GilbertDijkstra,350,0_05',DirDijkstra)
MBarabasiDijkstra.GraphVizDijkstra('02GeograficoDijkstra,350,0_12',DirDijkstra)
MGeoGraphDijkstra.GraphVizDijkstra('02BarabasiDijkstra,350,5',DirDijkstra)
MDorogovtsevDijkstra.GraphVizDijkstra('02DorogovtsevDijkstra,350',DirDijkstra)