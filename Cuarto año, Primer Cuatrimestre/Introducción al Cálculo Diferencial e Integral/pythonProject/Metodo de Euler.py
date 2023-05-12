from matplotlib import pyplot as plt
from math import exp
#****************************************************
#METODOS NUMERICOS
#****************************************************
def euler(f, x0, y0, h, x_final):
  xs =[x0]
  ys = [y0]
  xn = x0
  yn = y0
  while xn < x_final:
    yn = yn + h * f(xn, yn)
    xn = xn + h
    xs.append(xn)
    ys.append(yn)
  return xs, ys

#****************************************************
#ECUACION DIFERENCIAL Y CONDICION INICIAL
#****************************************************
def f(x, y):
  return 2 * x * y

x0 = 0
y0 = 1
#****************************************************
#PASOS
#****************************************************
h = 0.25 #TAMAÑO DEL PASO
#DADO UNA CANTIDAD DE PASOS N, PUEDE CALCULARSE h = (x_final - x0) / N
x_final = 1 #VALOR FINAL DE x

#****************************************************
#SOLUCION REAL
#****************************************************
n = 100
x_sol = [i * (x_final - x0)/n for i in range(n + 1)]
y_sol = [exp(x**2) for x in x_sol]
#PUEDEN COMENTARLA SI NO LA QUIEREN
#SI QUIEREN OTRA SOLUCION PUEDEN BUSCARLA Y REESCRIBIRLA

#****************************************************
#GRAFICO
#****************************************************
xs, ys = euler(f, x0, y0, h, x_final)

plt.plot(x_sol, y_sol, 'b', label='analitica')
plt.plot(xs, ys, 'r', label='aproximada')
plt.legend()
#****************************************************
#VALORES FINALES
#****************************************************
print("y({x}) = ".format(x=x_final), y_sol[-1])
print("y_aprox = ", ys[-1])