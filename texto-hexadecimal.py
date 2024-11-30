# 100SECURITY
# Converter Textos e Arquivos <> Hexadecimal
# Por: Marcos Henrique
# Site: www.100security.com.br

import os
from colorama import Fore, Style

# Limpar a Tela
def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux ou macOS
        os.system('clear')
        
clear_screen()

# Inicializa o Colorama
from colorama import init
init(autoreset=True)

# Banner
projeto = f"{Style.BRIGHT}{Fore.YELLOW}# - - - - - - - - 100SECURITY - - - - - - - - #\n"
titulo = f"{Style.BRIGHT}{Fore.GREEN}Converter Textos e Arquivos <> Hexadecimal"
github = f"{Style.BRIGHT}{Fore.WHITE}GitHub: {Fore.WHITE}github.com/100security/{Style.BRIGHT}{Fore.LIGHTCYAN_EX}texto-hexadecimal"
instagram = f"{Style.BRIGHT}{Fore.WHITE}Instagram: {Fore.WHITE}{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}@100security"

print(f"{projeto}\n{titulo}\n{github}\n{instagram}")

# Função para converter texto em Hexadecimal Normal (com espaços entre octetos)
def text_to_hex_normal(text):
    return ' '.join(format(ord(char), '02x') for char in text)

# Função para converter texto em Hexadecimal Compacto (no formato 0x..., tratado como IP)
def text_to_hex_compacto(text):
    try:
        # Divide o texto pelos pontos, converte cada parte para inteiro e depois para hexadecimal
        octetos = [int(octeto) for octeto in text.split('.')]
        # Combina os octetos em um único valor hexadecimal
        return f"0x{''.join(format(octeto, '02X') for octeto in octetos)}"
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Erro: entrada inválida. Certifique-se de inserir um endereço IP válido.")
        return None

# Função para converter Hexadecimal Normal para texto
def hex_normal_to_text(hex_values):
    try:
        # Converte os valores hexadecimais (separados por espaços) em texto
        return ''.join(chr(int(hex_value, 16)) for hex_value in hex_values.split())
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Erro na conversão. Verifique o conteúdo hexadecimal normal.")

# Função para converter Hexadecimal Compacto para texto (tratado como IP)
def hex_compacto_to_text(hex_values):
    try:
        # Remover o prefixo "0x" antes da conversão
        if hex_values.startswith("0x"):
            hex_values = hex_values[2:]
        # Dividir os hexadecimais em grupos de dois para representar os octetos
        octetos = [str(int(hex_values[i:i+2], 16)) for i in range(0, len(hex_values), 2)]
        return '.'.join(octetos)
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Erro na conversão. Verifique o conteúdo hexadecimal compacto.")

# Função para salvar o conteúdo em um arquivo
def salvar_em_arquivo(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Resultado salvo em {file_name}")

# Função para exibir o menu
def exibir_menu():
    print(f"\n{Style.BRIGHT}{Fore.RED}# - - - - - - - - - M E N U - - - - - - - - - #\n")
    print(f"{Style.BRIGHT}{Fore.WHITE}1 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Hexadecimal Normal")
    print(f"{Style.BRIGHT}{Fore.WHITE}2 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Endereço IP {Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Hexadecimal Compacto")
    print(f"{Style.BRIGHT}{Fore.WHITE}3 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Hexadecimal Normal {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Texto")
    print(f"{Style.BRIGHT}{Fore.WHITE}4 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Hexadecimal Compacto {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Endereço IP")
    print(f"{Style.BRIGHT}{Fore.WHITE}5 {Style.NORMAL}{Fore.WHITE}- {Style.BRIGHT}{Fore.LIGHTRED_EX}Sair\n")

# Função principal
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            texto = input("Digite o Texto a ser convertido para Hexadecimal Normal: ")
            hex_normal_result = text_to_hex_normal(texto)
            salvar_em_arquivo('hexadecimal-normal.txt', hex_normal_result)
            print(f"Texto original: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto}")
            print(f"Conversão para Hexadecimal Normal: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{hex_normal_result}")
        
        elif opcao == '2':
            texto = input("Digite o Endereço IP (ex: 192.168.0.1): ")
            hex_compacto_result = text_to_hex_compacto(texto)
            if hex_compacto_result:
                salvar_em_arquivo('hexadecimal-compacto.txt', hex_compacto_result)
                print(f"Endereço IP: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto}")
                print(f"Conversão para Hexadecimal Compacto: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{hex_compacto_result}")
        
        elif opcao == '3':
            hex_normal_input = input("Digite o valor Hexadecimal Normal (com espaços): ")
            texto_result = hex_normal_to_text(hex_normal_input)
            if texto_result:
                salvar_em_arquivo('texto-convertido.txt', texto_result)
                print(f"Hexadecimal Normal: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{hex_normal_input}")
                print(f"Conversão para Texto: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto_result}")
        
        elif opcao == '4':
            hex_compacto_input = input("Digite o valor Hexadecimal Compacto (no formato 0x...): ")
            texto_result = hex_compacto_to_text(hex_compacto_input)
            if texto_result:
                salvar_em_arquivo('ip-convertido.txt', texto_result)
                print(f"Hexadecimal Compacto: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{hex_compacto_input}")
                print(f"Conversão para Endereço IP: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto_result}")
        
        elif opcao == '5':
            print(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}Saindo...")
            break

        else:
            print(f"{Style.BRIGHT}{Fore.RED}Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()
