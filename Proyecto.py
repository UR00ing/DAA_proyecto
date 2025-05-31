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
PgrMalla.change_name('Pocos_Malla')
PgrEyR.change_name('Pocos_Erdos')
PGilbert.change_name('Pocos_Gilbert')
PGeoGraph.change_name('Pocos_Geographic')
PBarabasi.change_name('Pocos_Barabasi')
PDorogovtsev.change_name('Pocos_Dorogostev')
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
MgrMalla.change_name('Muchos_Malla')
MgrEyR.change_name('Muchos_Erdos')
MGilbert.change_name('Muchos_Gilbert')
MBarabasi.change_name('Muchos_Geographic')
MGeoGraph.change_name('Muchos_Barabasi')
MDorogovtsev.change_name('Muchos_Dorogostev')
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
Kruskal_d_PgrMalla		=	PgrMalla.kruskal()
Kruskal_d_PgrEyR		=	PgrEyR.kruskal()
Kruskal_d_PGilbert		=	PGilbert.kruskal()
Kruskal_d_PGeoGraph		=	PGeoGraph.kruskal()
Kruskal_d_PBarabasi		=	PBarabasi.kruskal()
Kruskal_d_PDorogovtsev	=	PDorogovtsev.kruskal()
#	muchos
Kruskal_d_MgrMalla		=	MgrMalla.kruskal()
Kruskal_d_MgrEyR		=	MgrEyR.kruskal()
Kruskal_d_MGilbert		=	MGilbert.kruskal()
Kruskal_d_MBarabasi		=	MBarabasi.kruskal()
Kruskal_d_MGeoGraph		=	MGeoGraph.kruskal()
Kruskal_d_MDorogovtsev	=	MDorogovtsev.kruskal()

Kruskal_d_PgrMalla.GraphVizDijkstra		(P_Graph_Malla	+	'_Kruskal_directo',DirKruskal)
Kruskal_d_PgrEyR.GraphVizDijkstra		(P_Graph_Erdos	+	'_Kruskal_directo',DirKruskal)
Kruskal_d_PGilbert.GraphVizDijkstra		(P_Graph_Gilb	+	'_Kruskal_directo',DirKruskal)
Kruskal_d_PGeoGraph.GraphVizDijkstra	(P_Graph_Geo	+	'_Kruskal_directo',DirKruskal)
Kruskal_d_PBarabasi.GraphVizDijkstra	(P_Graph_Bara	+	'_Kruskal_directo',DirKruskal)
Kruskal_d_PDorogovtsev.GraphVizDijkstra	(P_Graph_Doro	+	'_Kruskal_directo',DirKruskal)

Kruskal_d_MgrMalla.GraphVizDijkstra		(M_Graph_Malla	+	'_Kruskal_directo',DirKruskal)
Kruskal_d_MgrEyR.GraphVizDijkstra		(M_Graph_Erdos	+	'_Kruskal_directo',DirKruskal)
Kruskal_d_MGilbert.GraphVizDijkstra		(M_Graph_Gilb	+	'_Kruskal_directo',DirKruskal)
Kruskal_d_MBarabasi.GraphVizDijkstra	(M_Graph_Geo	+	'_Kruskal_directo',DirKruskal)
Kruskal_d_MGeoGraph.GraphVizDijkstra	(M_Graph_Bara	+	'_Kruskal_directo',DirKruskal)
Kruskal_d_MDorogovtsev.GraphVizDijkstra	(M_Graph_Doro	+	'_Kruskal_directo',DirKruskal)

"""
Kruskal_I
"""
#	pocos
Kruskal_i_PgrMalla		=	PgrMalla.kruskal_inverso()
Kruskal_i_PgrEyR		=	PgrEyR.kruskal_inverso()
Kruskal_i_PGilbert		=	PGilbert.kruskal_inverso()
Kruskal_i_PGeoGraph		=	PGeoGraph.kruskal_inverso()
Kruskal_i_PBarabasi		=	PBarabasi.kruskal_inverso()
Kruskal_i_PDorogovtsev	=	PDorogovtsev.kruskal_inverso()
#	muchos
Kruskal_i_MgrMalla		=	MgrMalla.kruskal_inverso()
Kruskal_i_MgrEyR		=	MgrEyR.kruskal_inverso()
Kruskal_i_MGilbert		=	MGilbert.kruskal_inverso()
Kruskal_i_MBarabasi		=	MBarabasi.kruskal_inverso()
Kruskal_i_MGeoGraph		=	MGeoGraph.kruskal_inverso()
Kruskal_i_MDorogovtsev	=	MDorogovtsev.kruskal_inverso()

Kruskal_i_PgrMalla.GraphVizDijkstra		(P_Graph_Malla	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_i_PgrEyR.GraphVizDijkstra		(P_Graph_Erdos	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_i_PGilbert.GraphVizDijkstra		(P_Graph_Gilb	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_i_PGeoGraph.GraphVizDijkstra	(P_Graph_Geo	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_i_PBarabasi.GraphVizDijkstra	(P_Graph_Bara	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_i_PDorogovtsev.GraphVizDijkstra	(P_Graph_Doro	+	'_Kruskal_indirecto',DirKruskal_I)

Kruskal_i_MgrMalla.GraphVizDijkstra		(M_Graph_Malla	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_i_MgrEyR.GraphVizDijkstra		(M_Graph_Erdos	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_i_MGilbert.GraphVizDijkstra		(M_Graph_Gilb	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_i_MBarabasi.GraphVizDijkstra	(M_Graph_Geo	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_i_MGeoGraph.GraphVizDijkstra	(M_Graph_Bara	+	'_Kruskal_indirecto',DirKruskal_I)
Kruskal_i_MDorogovtsev.GraphVizDijkstra	(M_Graph_Doro	+	'_Kruskal_indirecto',DirKruskal_I)

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
"""
Impresion de pesos de todo el grafo.(para todos los grafos)
"""
# Pocos
# Definimos un ancho fijo para cada columna
name_width = 20
weight_width = 15

print(f'Grafo: {PgrMalla.NAME:<{name_width}} Weight: {str(PgrMalla.graph_weight()):<{weight_width}} '
		f'Kruskal Weight: {str(Kruskal_d_PgrMalla.graph_weight()):<{weight_width}} '
		f'Kruskal_I Weight: {str(Kruskal_i_PgrMalla.graph_weight()):<{weight_width}} '
		f'Prim Weight: {str(Prim_PgrMalla.graph_weight()):<{weight_width}}')

print(f'Grafo: {PgrEyR.NAME:<{name_width}} Weight: {str(PgrEyR.graph_weight()):<{weight_width}} '
		f'Kruskal Weight: {str(Kruskal_d_PgrEyR.graph_weight()):<{weight_width}} '
		f'Kruskal_I Weight: {str(Kruskal_i_PgrEyR.graph_weight()):<{weight_width}} '
		f'Prim Weight: {str(Prim_PgrEyR.graph_weight()):<{weight_width}}')

print(f'Grafo: {PGilbert.NAME:<{name_width}} Weight: {str(PGilbert.graph_weight()):<{weight_width}} '
		f'Kruskal Weight: {str(Kruskal_d_PGilbert.graph_weight()):<{weight_width}} '
		f'Kruskal_I Weight: {str(Kruskal_i_PGilbert.graph_weight()):<{weight_width}} '
		f'Prim Weight: {str(Prim_PGilbert.graph_weight()):<{weight_width}}')

print(f'Grafo: {PGeoGraph.NAME:<{name_width}} Weight: {str(PGeoGraph.graph_weight()):<{weight_width}} '
		f'Kruskal Weight: {str(Kruskal_d_PGeoGraph.graph_weight()):<{weight_width}} '
		f'Kruskal_I Weight: {str(Kruskal_i_PGeoGraph.graph_weight()):<{weight_width}} '
		f'Prim Weight: {str(Prim_PGeoGraph.graph_weight()):<{weight_width}}')

print(f'Grafo: {PBarabasi.NAME:<{name_width}} Weight: {str(PBarabasi.graph_weight()):<{weight_width}} '
		f'Kruskal Weight: {str(Kruskal_d_PBarabasi.graph_weight()):<{weight_width}} '
		f'Kruskal_I Weight: {str(Kruskal_i_PBarabasi.graph_weight()):<{weight_width}} '
		f'Prim Weight: {str(Prim_PBarabasi.graph_weight()):<{weight_width}}')

print(f'Grafo: {PDorogovtsev.NAME:<{name_width}} Weight: {str(PDorogovtsev.graph_weight()):<{weight_width}} '
		f'Kruskal Weight: {str(Kruskal_d_PDorogovtsev.graph_weight()):<{weight_width}} '
		f'Kruskal_I Weight: {str(Kruskal_i_PDorogovtsev.graph_weight()):<{weight_width}} '
		f'Prim Weight: {str(Prim_PDorogovtsev.graph_weight()):<{weight_width}}')

# Muchos
# Definimos un ancho fijo para cada columna
name_width = 20
weight_width = 15

print(f'Grafo: {MgrMalla.NAME:<{name_width}} Weight: {str(MgrMalla.graph_weight()):<{weight_width}} '
      f'Kruskal Weight: {str(Kruskal_d_MgrMalla.graph_weight()):<{weight_width}} '
      f'Kruskal_I Weight: {str(Kruskal_i_MgrMalla.graph_weight()):<{weight_width}} '
      f'Prim Weight: {str(Prim_MgrMalla.graph_weight()):<{weight_width}}')

print(f'Grafo: {MgrEyR.NAME:<{name_width}} Weight: {str(MgrEyR.graph_weight()):<{weight_width}} '
      f'Kruskal Weight: {str(Kruskal_d_MgrEyR.graph_weight()):<{weight_width}} '
      f'Kruskal_I Weight: {str(Kruskal_i_MgrEyR.graph_weight()):<{weight_width}} '
      f'Prim Weight: {str(Prim_MgrEyR.graph_weight()):<{weight_width}}')

print(f'Grafo: {MGilbert.NAME:<{name_width}} Weight: {str(MGilbert.graph_weight()):<{weight_width}} '
      f'Kruskal Weight: {str(Kruskal_d_MGilbert.graph_weight()):<{weight_width}} '
      f'Kruskal_I Weight: {str(Kruskal_i_MGilbert.graph_weight()):<{weight_width}} '
      f'Prim Weight: {str(Prim_MGilbert.graph_weight()):<{weight_width}}')

print(f'Grafo: {MGeoGraph.NAME:<{name_width}} Weight: {str(MGeoGraph.graph_weight()):<{weight_width}} '
      f'Kruskal Weight: {str(Kruskal_d_MGeoGraph.graph_weight()):<{weight_width}} '
      f'Kruskal_I Weight: {str(Kruskal_i_MGeoGraph.graph_weight()):<{weight_width}} '
      f'Prim Weight: {str(Prim_MGeoGraph.graph_weight()):<{weight_width}}')

print(f'Grafo: {MBarabasi.NAME:<{name_width}} Weight: {str(MBarabasi.graph_weight()):<{weight_width}} '
      f'Kruskal Weight: {str(Kruskal_d_MBarabasi.graph_weight()):<{weight_width}} '
      f'Kruskal_I Weight: {str(Kruskal_i_MBarabasi.graph_weight()):<{weight_width}} '
      f'Prim Weight: {str(Prim_MBarabasi.graph_weight()):<{weight_width}}')

print(f'Grafo: {MDorogovtsev.NAME:<{name_width}} Weight: {str(MDorogovtsev.graph_weight()):<{weight_width}} '
      f'Kruskal Weight: {str(Kruskal_d_MDorogovtsev.graph_weight()):<{weight_width}} '
      f'Kruskal_I Weight: {str(Kruskal_i_MDorogovtsev.graph_weight()):<{weight_width}} '
      f'Prim Weight: {str(Prim_MDorogovtsev.graph_weight()):<{weight_width}}')