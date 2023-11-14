artisiniva = int(input("cual es el importe sin IVA del articulo: "))
parcentiva = int(input("cuanto es e1 IVA: "))
articoniva = (parcentiva/100) * artisiniva + artisiniva
print("Este es el precio con IVA del producto: "+ str(articoniva)+"€")