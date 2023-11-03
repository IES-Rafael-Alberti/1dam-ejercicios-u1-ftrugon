def main():
    correo = input("Dame tu correo: ")
    correo2 = correo.split("@")
    
    print(f"Ahora tu correo es {correo2[0]}@ceu.es")
if __name__ == "__main__":
    main()  