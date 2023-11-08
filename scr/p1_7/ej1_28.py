def main():
    num1 = int(input("dime un numero: "))
    num2 = int(input("dime otro numero: "))
    if num2 == num1:
        print("Los numeros no pueden ser iguales entre si")
    else:
        print(f"El numero menor es {min(num1,num2)} y entre ellos existe una diferencia de {abs(num1 - num2)} números")

if __name__ == "__main__":
    main()