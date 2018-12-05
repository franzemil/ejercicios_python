import math
Unidad=["","I","II","III","IV","V","VI","VII","VIII","IX"]
Decena=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
Centena=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
unidades=["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez","once","doce","trece","catorce","quince","dieciseis","diecisiete","dieciocho","diecinueve","veinte"]
numero1= str (input('ingrese el primer numero en letras :'))
numero2=str(input('ingrse el numero en letras:'))
n1=unidades.index(int(numero1))
n2=unidades.index(numero2)
multi=n1*n2
u=multi%10


d=int(math.floor(multi/10))%10
c=int(math.floor(multi/100))
if (multi>=100):
    print(Centena[c]+Decena[d]*Unidad[u])
else:
    if(multi>=10):
        print(Decena[d]+Unidad[u])



    else:
        print(Unidad[multi])