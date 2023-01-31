import pandas as pd
import numpy as np

# Número de data_points
n = int(input())

# Coletando os pontos e salvando em uma lista
lst = [input() for i in range(n)]

# Transformando os valores de string para float e armazenando em dataframe
data_points = pd.DataFrame([np.array(lst[i].split()).astype(float) for i in range(len(lst))],
                            columns=['data_points_x', 'data_points_y'])

# Calculando a distância entre o ponto e centroid (0,0)
dist_centroids_0 = pd.Series([np.linalg.norm(np.array([data_points['data_points_x'][i],
                                                        data_points['data_points_y'][i]])-[0,0])
                                                        .round(2) for i in range(len(data_points))])

# Calculando a distância entre o ponto e centroid (2,2)
dist_centroids_2 = pd.Series([np.linalg.norm(np.array([data_points['data_points_x'][i],
                                                        data_points['data_points_y'][i]])-[2,2])
                                                        .round(2) for i in range(len(data_points))])

# Inserindo as series no dataframe
data_points.insert(value=dist_centroids_0, column='dist_centroids_(0,0)',loc=2)
data_points.insert(value=dist_centroids_2, column='dist_centroids_(2,2)',loc=3)

# Determinando o centroid mais próximo do ponto
centroids = pd.Series(['(0,0)' if data_points['dist_centroids_(0,0)'][i] <= data_points['dist_centroids_(2,2)'][i]
                                    else '(2,2)' for i in range(len(data_points))])

# Inserindo as series no dataframe
data_points.insert(value=centroids, column='centroids',loc=4)

# Calculando os novos centroids
new_centroids = pd.DataFrame(data_points[['data_points_x', 'data_points_y', 'centroids']]
                             .groupby(['centroids'])
                             .mean()
                             .round(2))

# Verificando se os pontos foram atribuídos ou não
if '(0,0)' not in set(centroids):
    print(None)
else:
    print(np.array(new_centroids.iloc[0,:]))

if '(2,2)' not in set(centroids):
    print(None)
else:
    print(np.array(new_centroids.iloc[1,:]))
