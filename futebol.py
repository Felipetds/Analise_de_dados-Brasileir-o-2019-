# -*- coding: utf-8 -*-
"""Futebol

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ejzq5wkY1EbINuS_nhtU3IAMWbwQejWj
"""

import pandas as pd

campeonato = pd.read_csv("brasileirao_serie_a.csv")
#campeonato.head()
campeonato_2019 = campeonato.query("ano_campeonato == 2019")

campeonato_2019.head()

teste_ida = campeonato_2019.query("time_vis == 'Flamengo'")
teste_volta = campeonato_2019.query("time_man == 'Flamengo'")

teste_ida = teste_ida[['data', 'ano_campeonato', 'time_man', 'time_vis', 'gols_man', 'gols_vis']]
teste_volta = teste_volta[['data', 'ano_campeonato', 'time_man', 'time_vis', 'gols_man', 'gols_vis']]

#gols_ida = teste_ida.sum()["gols_vis"]
#gols_volta = teste_volta.sum()["gols_man"]

#gols = gols_ida + gols_volta
#gols

vitorias_casa = teste_volta.query("gols_man > gols_vis")
vitorias_fcasa = teste_ida.query("gols_vis > gols_man")

empates_casa = teste_volta.query("gols_man == gols_vis")
empates_fcasa = teste_ida.query("gols_vis == gols_man")

derrotas_casa = teste_volta.query("gols_man < gols_vis")
derrotas_fcasa = teste_ida.query("gols_vis < gols_man")

vitorias_casa = len(vitorias_casa)
vitorias_fcasa = len(vitorias_fcasa)

empates_casa = len(empates_casa)
empates_fcasa = len(empates_fcasa)

derrotas_casa = len(derrotas_casa)
derrotas_fcasa = len(derrotas_fcasa)

total_vitorias = vitorias_casa + vitorias_fcasa
total_empates = empates_casa + empates_fcasa
total_derrotas = derrotas_casa + derrotas_fcasa

total_vitorias, total_empates, total_derrotas

times = campeonato_2019.groupby('time_man').count()
#times = times[['time_man']]
#times = times.drop('gols_man')
#times
#times.drop(['gols_man'])
times# = times[times]
teste = times[2]
#for i in range(19):
#  print(times[i])

#times = campeonato_2019.groupby('time_man').count()

times = campeonato_2019.groupby('time_man').count()
times = times.drop(columns=['data','ano_campeonato','horario','rodada','estadio','arbitro','publico','publico_max','time_vis','tecnico_man'])
times

time_2 = pd.Series({'time':'Athletico-PR','gols':'51'})
time_2
time_1 = pd.Series({'time':'Flamengo','gols':'86'}) 
time_1
lista_times = pd.DataFrame([time_2, time_1])
lista_times = lista_times.set_index("time")
lista_times

lista_times = pd.DataFrame([time_2, time_1])
lista_times = lista_times.set_index("time")
lista_times

times = campeonato_2019.iloc[:,[8]]
times = times.drop_duplicates()


for i in range(20):
  print(times.iloc[i]['time_man'])

times_teste = []
s_gols = []

for i in range(20):

  nome = times.iloc[i]['time_man']
  #nome = str(nome)
  teste_ida = campeonato_2019.query("time_man == @nome")
  teste_volta = campeonato_2019.query("time_vis == @nome")
  teste_ida = teste_ida[['data', 'ano_campeonato', 'time_man', 'time_vis', 'gols_man', 'gols_vis']]
  teste_volta = teste_volta[['data', 'ano_campeonato', 'time_man', 'time_vis', 'gols_man', 'gols_vis']]

  gols_ida = teste_ida.sum()["gols_vis"]
  gols_volta = teste_volta.sum()["gols_man"]

  gols = gols_ida + gols_volta

  times_teste.append(nome)
  s_gols.append(gols)

times_teste, s_gols

gols_levados = pd.DataFrame([times_teste, s_gols])
#lista_times = lista_times.set_index("time")
gols_levados = gols_levados.transpose()
#gols_feitos = gols_feitos.columns = ['times','gols_feitos']
#gols_feitos = gols_feitos.columns = ["times","gols_feitos"]
gols_levados

times_teste = []
vit = []
emp = []
der = []

for i in range(20):

  nome = times.iloc[i]['time_man']

  teste_ida = campeonato_2019.query("time_vis == @nome")
  teste_volta = campeonato_2019.query("time_man == @nome")

  teste_ida = teste_ida[['data', 'ano_campeonato', 'time_man', 'time_vis', 'gols_man', 'gols_vis']]
  teste_volta = teste_volta[['data', 'ano_campeonato', 'time_man', 'time_vis', 'gols_man', 'gols_vis']]

  vitorias_casa = teste_volta.query("gols_man > gols_vis")
  vitorias_fcasa = teste_ida.query("gols_vis > gols_man")

  empates_casa = teste_volta.query("gols_man == gols_vis")
  empates_fcasa = teste_ida.query("gols_vis == gols_man")

  derrotas_casa = teste_volta.query("gols_man < gols_vis")
  derrotas_fcasa = teste_ida.query("gols_vis < gols_man")

  vitorias_casa = len(vitorias_casa)
  vitorias_fcasa = len(vitorias_fcasa)

  empates_casa = len(empates_casa)
  empates_fcasa = len(empates_fcasa)

  derrotas_casa = len(derrotas_casa)
  derrotas_fcasa = len(derrotas_fcasa)

  total_vitorias = vitorias_casa + vitorias_fcasa
  total_empates = empates_casa + empates_fcasa
  total_derrotas = derrotas_casa + derrotas_fcasa

  times_teste.append(nome)
  vit.append(total_vitorias)
  emp.append(total_empates)
  der.append(total_derrotas)

desempenho = pd.DataFrame([times_teste, vit, emp, der])
#lista_times = lista_times.set_index("time")
desempenho = desempenho.transpose()
#gols_feitos = gols_feitos.columns = ['times','gols_feitos']
#gols_feitos = gols_feitos.columns = ["times","gols_feitos"]
desempenho