import	graph_lib	as	gp
import	algoritmos	as	alg
import	pathlib		as	pl

#	Directorios a usar
Dir				=	pl.Path(__file__).parent.absolute()
Dir				=	Dir /	"proyecto_4"
DirS			=	Dir	/	"Graph"
DirKruskal		=	Dir	/	"Kruskal"
DirKruskal_I	=	Dir	/	"Kruskal_i"
DirPrim			=	Dir	/	"Prim"
#	Nombres de los grafos
	#	Pocos
P_Graph_Malla	=	'01Malla,9,9'
P_Graph_Erdos	=	'01Erdos,80,190'
P_Graph_Gilb	=	'01Gilbert,80,0_3'
P_Graph_Geo		=	'01Geografico,80,0_35'
P_Graph_Bara	=	'01Barabasi,80,5'
P_Graph_Doro	=	'01Dorogovtsev,80'
	#	Muchos
M_Graph_Malla	=	'02Malla,18,20'
M_Graph_Erdos	=	'02Erdos,350,1100'
M_Graph_Gilb	=	'02Gilbert,350,0_02'
M_Graph_Geo		=	'02Geografico,350,0_12'
M_Graph_Bara	=	'02Barabasi,350,5'
M_Graph_Doro	=	'02Dorogovtsev,350'

# Crear los directorios si no existen (incluyendo el directorio padre proyecto_4)
Dir.mkdir(exist_ok=True)
DirS.mkdir(exist_ok=True)
DirKruskal.mkdir(exist_ok=True)

"""
Generacion de los grafos mediante generadores aleatorios
"""
#	pocos	80 aprox
PgrMalla		=	alg.MetodoMalla(9,9)
PgrEyR			=	alg.MetodoErdosyRenyi(80,190)
PGilbert		=	alg.MetodoGilbert(80,0.3)
PGeoGraph		=	alg.MetodoGeoSimp(80,0.35)
PBarabasi		=	alg.MetodoBarabasiAlbert(80,5)
PDorogovtsev	=	alg.MetodoDorogovtsev(80)
PgrMalla.GraphVizDijkstra		(P_Graph_Malla,DirS)
PgrEyR.GraphVizDijkstra			(P_Graph_Erdos,DirS)
PGilbert.GraphVizDijkstra		(P_Graph_Gilb,DirS)
PGeoGraph.GraphVizDijkstra		(P_Graph_Geo,DirS)
PBarabasi.GraphVizDijkstra		(P_Graph_Bara,DirS)
PDorogovtsev.GraphVizDijkstra	(P_Graph_Doro,DirS)
#	muchos	350 aprox
MgrMalla		=	alg.MetodoMalla(18,20)
MgrEyR			=	alg.MetodoErdosyRenyi(350,1100)
MGilbert		=	alg.MetodoGilbert(350,0.02)
MBarabasi		=	alg.MetodoBarabasiAlbert(350,5)
MGeoGraph		=	alg.MetodoGeoSimp(350,0.12)
MDorogovtsev	=	alg.MetodoDorogovtsev(350)
MgrMalla.GraphVizDijkstra		(M_Graph_Malla,DirS)
MgrEyR.GraphVizDijkstra			(M_Graph_Erdos,DirS)
MGilbert.GraphVizDijkstra		(M_Graph_Gilb,DirS)
MGeoGraph.GraphVizDijkstra		(M_Graph_Geo,DirS)
MBarabasi.GraphVizDijkstra		(M_Graph_Bara,DirS)
MDorogovtsev.GraphVizDijkstra	(M_Graph_Doro,DirS)

"""
Kruskal
"""
#	pocos
Kruskal_I_PgrMalla		=	PgrMalla.kruskal()
Kruskal_I_PgrEyR		=	PgrEyR.kruskal()
Kruskal_I_PGilbert		=	PGilbert.kruskal()
Kruskal_I_PGeoGraph		=	PGeoGraph.kruskal()
Kruskal_I_PBarabasi		=	PBarabasi.kruskal()
Kruskal_I_PDorogovtsev	=	PDorogovtsev.kruskal()
#	muchos
Kruskal_I_MgrMalla		=	MgrMalla.kruskal()
Kruskal_I_MgrEyR		=	MgrEyR.kruskal()
Kruskal_I_MGilbert		=	MGilbert.kruskal()
Kruskal_I_MBarabasi		=	MBarabasi.kruskal()
Kruskal_I_MGeoGraph		=	MGeoGraph.kruskal()
Kruskal_I_MDorogovtsev	=	MDorogovtsev.kruskal()

Kruskal_I_PgrMalla.GraphVizDijkstra		(P_Graph_Malla	+	'_Kruskal_directo',DirKruskal)
Kruskal_I_PgrEyR.GraphVizDijkstra		(P_Graph_Erdos	+	'_Kruskal_directo',DirKruskal)
Kruskal_I_PGilbert.GraphVizDijkstra		(P_Graph_Gilb	+	'_Kruskal_directo',DirKruskal)
Kruskal_I_PGeoGraph.GraphVizDijkstra	(P_Graph_Geo	+	'_Kruskal_directo',DirKruskal)
Kruskal_I_PBarabasi.GraphVizDijkstra	(P_Graph_Bara	+	'_Kruskal_directo',DirKruskal)
Kruskal_I_PDorogovtsev.GraphVizDijkstra	(P_Graph_Doro	+	'_Kruskal_directo',DirKruskal)

Kruskal_I_MgrMalla.GraphVizDijkstra		(M_Graph_Malla	+	'_Kruskal_directo',DirKruskal)
Kruskal_I_MgrEyR.GraphVizDijkstra		(M_Graph_Erdos	+	'_Kruskal_directo',DirKruskal)
Kruskal_I_MGilbert.GraphVizDijkstra		(M_Graph_Gilb	+	'_Kruskal_directo',DirKruskal)
Kruskal_I_MBarabasi.GraphVizDijkstra	(M_Graph_Geo	+	'_Kruskal_directo',DirKruskal)
Kruskal_I_MGeoGraph.GraphVizDijkstra	(M_Graph_Bara	+	'_Kruskal_directo',DirKruskal)
Kruskal_I_MDorogovtsev.GraphVizDijkstra	(M_Graph_Doro	+	'_Kruskal_directo',DirKruskal)

"""
Kruskal_I
"""
#	pocos
Kruskal_I_PgrMalla		=	PgrMalla.kruskal_inverso()
Kruskal_I_PgrEyR		=	PgrEyR.kruskal_inverso()
Kruskal_I_PGilbert		=	PGilbert.kruskal_inverso()
Kruskal_I_PGeoGraph		=	PGeoGraph.kruskal_inverso()
Kruskal_I_PBarabasi		=	PBarabasi.kruskal_inverso()
Kruskal_I_PDorogovtsev	=	PDorogovtsev.kruskal_inverso()
#	muchos
Kruskal_I_MgrMalla		=	MgrMalla.kruskal_inverso()
Kruskal_I_MgrEyR		=	MgrEyR.kruskal_inverso()
Kruskal_I_MGilbert		=	MGilbert.kruskal_inverso()
Kruskal_I_MBarabasi		=	MBarabasi.kruskal_inverso()
Kruskal_I_MGeoGraph		=	MGeoGraph.kruskal_inverso()
Kruskal_I_MDorogovtsev	=	MDorogovtsev.kruskal_inverso()

Kruskal_I_PgrMalla.GraphVizDijkstra		(P_Graph_Malla	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_I_PgrEyR.GraphVizDijkstra		(P_Graph_Erdos	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_I_PGilbert.GraphVizDijkstra		(P_Graph_Gilb	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_I_PGeoGraph.GraphVizDijkstra	(P_Graph_Geo	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_I_PBarabasi.GraphVizDijkstra	(P_Graph_Bara	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_I_PDorogovtsev.GraphVizDijkstra	(P_Graph_Doro	+	'_Kruskal_indirecto',DirKruskal_I)

Kruskal_I_MgrMalla.GraphVizDijkstra		(M_Graph_Malla	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_I_MgrEyR.GraphVizDijkstra		(M_Graph_Erdos	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_I_MGilbert.GraphVizDijkstra		(M_Graph_Gilb	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_I_MBarabasi.GraphVizDijkstra	(M_Graph_Geo	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_I_MGeoGraph.GraphVizDijkstra	(M_Graph_Bara	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_I_MDorogovtsev.GraphVizDijkstra	(M_Graph_Doro	+	'_Kruskal_indirecto',DirKruskal_I)

"""
Prim
"""
#	pocos
Prim_PgrMalla		=	PgrMalla.prim()
Prim_PgrEyR			=	PgrEyR.prim()
Prim_PGilbert		=	PGilbert.prim()
Prim_PGeoGraph		=	PGeoGraph.prim()
Prim_PBarabasi		=	PBarabasi.prim()
Prim_PDorogovtsev	=	PDorogovtsev.prim()
#	muchos
Prim_MgrMalla		=	MgrMalla.prim()
Prim_MgrEyR			=	MgrEyR.prim()
Prim_MGilbert		=	MGilbert.prim()
Prim_MBarabasi		=	MBarabasi.prim()
Prim_MGeoGraph		=	MGeoGraph.prim()
Prim_MDorogovtsev	=	MDorogovtsev.prim()

Prim_PgrMalla.GraphVizDijkstra		(P_Graph_Malla	+	'_Prim',DirPrim)
Prim_PgrEyR.GraphVizDijkstra		(P_Graph_Erdos	+	'_Prim',DirPrim)
Prim_PGilbert.GraphVizDijkstra		(P_Graph_Gilb	+	'_Prim',DirPrim)
Prim_PGeoGraph.GraphVizDijkstra		(P_Graph_Geo	+	'_Prim',DirPrim)
Prim_PBarabasi.GraphVizDijkstra		(P_Graph_Bara	+	'_Prim',DirPrim)
Prim_PDorogovtsev.GraphVizDijkstra	(P_Graph_Doro	+	'_Prim',DirPrim)

Prim_MgrMalla.GraphVizDijkstra		(M_Graph_Malla	+	'_Prim',DirPrim)
Prim_MgrEyR.GraphVizDijkstra		(M_Graph_Erdos	+	'_Prim',DirPrim)
Prim_MGilbert.GraphVizDijkstra		(M_Graph_Gilb	+	'_Prim',DirPrim)
Prim_MBarabasi.GraphVizDijkstra		(M_Graph_Geo	+	'_Prim',DirPrim)
Prim_MGeoGraph.GraphVizDijkstra		(M_Graph_Bara	+	'_Prim',DirPrim)
Prim_MDorogovtsev.GraphVizDijkstra	(M_Graph_Doro	+	'_Prim',DirPrim)