import random   
import string   

def gerar_senha(comprimento, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas!")
    comprimento = int(input("Digite o comprimento da senha desejada: "))
    usar_numeros = input("Deseja usar números na senha? (s/n): ").lower() == 's'
    usar_simbolos = input("Deseja usar símbolos na senha? (s/n): ").lower() == 's'

    senha = gerar_senha(comprimento, usar_numeros, usar_simbolos)
    print("Sua senha gerada é:", senha)

if __name__ == "__main__":
    main()
