# -*- coding: utf-8 -*-
"""Taller1AyC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jOob3fIuT6zM-OpMbto7N6QxiB19wie0
"""

#Se desarrolla un control difuso para: segmentación de clientes en un banco.
#By Giovanni Pantoja - 220160070

#Control difuso
!pip install scikit-fuzzy

#Importar librerias
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#variables de entrada

#Cantidad dinero ahorrado en el banco, se denota la variable como: cda
cda = ctrl.Antecedent(np.arange(0,550,1),'cda')
#Salario que gana el cliente, se denota la variable como: sgc
sgc = ctrl.Antecedent(np.arange(0,18,0.1),'sgc')

#variables de salida

# Probabilidad de ser cliente preferencial, se denota la varialbe como: pcp
pcp = ctrl.Consequent(np.arange(0,101,1),'pcp')

#Funciones de membresia

#Cantidad dinero ahorrado en el banco
cda['muy_poco'] = fuzz.trimf(cda.universe,[0,0,5])
cda['poco'] = fuzz.trimf(cda.universe,[2.5,20,32])
cda['normal'] = fuzz.trimf(cda.universe,[22,70,100])
cda['aceptable'] = fuzz.trimf(cda.universe,[90,170,250])
cda['muy_aceptable'] = fuzz.trapmf(cda.universe,[200,350,550,550])

cda.view()

#Salario que gana el cliente
sgc['poco'] = fuzz.trimf(sgc.universe,[0,0,1.5])
sgc['normal'] = fuzz.trimf(sgc.universe,[1,3,5])
sgc['aceptable'] = fuzz.trimf(sgc.universe,[3,6,10])
sgc['muy_aceptable'] = fuzz.trapmf(sgc.universe,[8,12,16,16])
sgc.view()

#Probabilidad de ser cliente preferencial
pcp['cero'] = fuzz.trimf(pcp.universe,[0,0,12])
pcp['bajo'] = fuzz.trimf(pcp.universe,[10,32,50])
pcp['normal'] = fuzz.trimf(pcp.universe,[45,60,75])
pcp['alto'] = fuzz.trimf(pcp.universe,[71,100,100,])
pcp.view()

#crear reglas difusas
regla11 = ctrl.Rule(sgc['poco'] & cda['muy_poco'],pcp['cero'])
regla12 = ctrl.Rule(sgc['poco'] & cda['poco'],pcp['cero'])
regla13 = ctrl.Rule(sgc['poco'] & cda['normal'],pcp['cero'])
regla14 = ctrl.Rule(sgc['poco'] & cda['aceptable'],pcp['bajo'])
regla15 = ctrl.Rule(sgc['poco'] & cda['muy_aceptable'],pcp['normal'])

regla21 = ctrl.Rule(sgc['normal'] & cda['muy_poco'],pcp['cero'])
regla22 = ctrl.Rule(sgc['normal'] & cda['poco'],pcp['cero'])
regla23 = ctrl.Rule(sgc['normal'] & cda['normal'],pcp['bajo'])
regla24 = ctrl.Rule(sgc['normal'] & cda['aceptable'],pcp['normal'])
regla25 = ctrl.Rule(sgc['normal'] & cda['muy_aceptable'],pcp['normal'])

regla31 = ctrl.Rule(sgc['aceptable'] & cda['muy_poco'],pcp['cero'])
regla32 = ctrl.Rule(sgc['aceptable'] & cda['poco'],pcp['normal'])
regla33 = ctrl.Rule(sgc['aceptable'] & cda['normal'],pcp['alto'])
regla34 = ctrl.Rule(sgc['aceptable'] & cda['aceptable'],pcp['alto'])
regla35 = ctrl.Rule(sgc['aceptable'] & cda['muy_aceptable'],pcp['alto'])

regla41 = ctrl.Rule(sgc['muy_aceptable'] & cda['muy_poco'],pcp['cero'])
regla42 = ctrl.Rule(sgc['muy_aceptable'] & cda['poco'],pcp['cero'])
regla43 = ctrl.Rule(sgc['muy_aceptable'] & cda['normal'],pcp['normal'])
regla44 = ctrl.Rule(sgc['muy_aceptable'] & cda['aceptable'],pcp['alto'])
regla45 = ctrl.Rule(sgc['muy_aceptable'] & cda['muy_aceptable'],pcp['alto'])

sistema_control = ctrl.ControlSystem(
    [
        regla11,
        regla12,
        regla13,
        regla14,
        regla15,
        regla21,
        regla22,
        regla23,
        regla24,
        regla25,
        regla31,
        regla32,
        regla33,
        regla34,
        regla35,
        regla41,
        regla42,
        regla43,
        regla44,
        regla45
    ]
)
controlador = ctrl.ControlSystemSimulation(sistema_control)

#Se calcula el resultado obtenido para cada caso

#Caso 1
#Adriana

#Salario que gana el cliente
controlador.input['sgc'] = 15
#Cantidad de dinero ahorrado
controlador.input['cda'] = 500

controlador.compute()

#obtener resultado
pcp_calculado = controlador.output['pcp']
print(f"La probabilidad de ser cliente preferencial es del: {pcp_calculado}%")

#Caso 2
#Nelson

#Salario que gana el cliente
controlador.input['sgc'] = 9
#Cantidad de dinero ahorrado
controlador.input['cda'] = 30

controlador.compute()

#obtener resultado
pcp_calculado = controlador.output['pcp']
print(f"La probabilidad de ser cliente preferencial es del: {pcp_calculado}%")

#Caso 3
#Federico

#Salario que gana el cliente
controlador.input['sgc'] = 1.160
#Cantidad de dinero ahorrado
controlador.input['cda'] = 40

controlador.compute()

#obtener resultado
pcp_calculado = controlador.output['pcp']
print(f"La probabilidad de ser cliente preferencial es del: {pcp_calculado}%")

#Caso 4
#Veronica

#Salario que gana el cliente
controlador.input['sgc'] = 1.5
#Cantidad de dinero ahorrado
controlador.input['cda'] = 0

controlador.compute()

#obtener resultado
pcp_calculado = controlador.output['pcp']
print(f"La probabilidad de ser cliente preferencial es del: {pcp_calculado}%")