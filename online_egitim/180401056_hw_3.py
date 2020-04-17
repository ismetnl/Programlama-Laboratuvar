from sympy import Symbol,Piecewise
import sympy.plotting as syp
import matplotlib.pyplot as plt

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')


function = 1/(b-a)

def u_d_syp(alt_limit,ust_limit):
    if ust_limit < alt_limit:
        temp = ust_limit
        ust_limit = alt_limit
        alt_limit = temp

    syp.plot(Piecewise((0,(x < alt_limit) | (x > ust_limit)),(function.subs({a:alt_limit,b:ust_limit}),True)),(x,-10,10),title ='uniform distribution')

def u_d_plt(alt_limit,ust_limit):
    if ust_limit < alt_limit:
        temp = ust_limit
        ust_limit = alt_limit
        alt_limit = temp

    x_values =[]
    y_values =[]
    value = float(-10) # Görüntünün syp.plot'taki gibi olması için variable'ı float atıyoruz ve artışı küçültüyoruz

    while value < 20.0:
        y = Piecewise((0,(value < alt_limit) | (value > ust_limit)),(function.subs({a:alt_limit,b:ust_limit}),True))
        x_values.append(value)
        y_values.append(y)
        value += 0.1

    plt.suptitle('Uniform Distribition')
    plt.plot(x_values,y_values)
    plt.show()

u_d_plt(0,2)
u_d_syp(5,1)

"""
Uniform Distribution : Verilen aralıktaki olayların sürekli aynı sabit olasılık gösteren olasılık dağılım türüdür.

Kodda olasılık yoğunluk fonksiyonu kullanılmıştır ve bu koşullu fonksiyonu kullanabilmek için Piecewise methodundan
yardım alarak,syp.plot ve plt.plot ile grafiklerini çizdirilmiştir.

"""









