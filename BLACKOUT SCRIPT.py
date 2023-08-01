#!/usr/bin/env python3

import sys

# Define a cor vermelha.
RED = '\033[91m'

# Define a cor preta.
BLACK = '\033[0m'

# Exibe o menu de ajuda.
def help():
    print(f"{RED}Menu de ajuda{BLACK}")
    print(f"{RED}Comandos: {BLACK}")
    print(f"{RED}* help: Exibe este menu de ajuda.{BLACK}")
    print(f"{RED}* version: Exibe a versão do script.{BLACK}")
    print(f"{RED}* quit: Sai do script.{BLACK}")

# Exibe a versão do script.
def version():
    print(f"{RED}Versão: {BLACK}1.0")

# Sai do script.
def quit():
    sys.exit(0)

# Escolha o comando.
command = input(f"{RED}Qual comando você deseja executar? {BLACK}")

# Executa o comando.
if command == "help":
    help()
elif command == "version":
    version()
elif command == "quit":
    quit()
else:
    print(f"{RED}Comando inválido.{BLACK}")

# Exibe o texto principal do script em vermelho.
print(f"{RED}Este script verifica portas abertas de um site, consulta o IP do site e consulta se ele é UDP ou TCP, e também verifica painéis de administração e vulnerabilidades SQL.{BLACK}")

# Obtém o nome do site.
site_name = input(f"{RED}Digite o nome do site: {BLACK}")

# Obtém o IP do site.
site_ip = socket.gethostbyname(site_name)

# Verifica as portas abertas no site.
for port in range(1, 65535):
    try:
        socket.create_connection((site_ip, port), 2)
        print(f"{RED}A porta {port} está aberta.{BLACK}")
    except socket.error:
        pass

# Verifica se o site usa UDP ou TCP.
if socket.getservbyport(80, "tcp") == site_ip:
    print(f"{RED}O site usa TCP.{BLACK}")
else:
    print(f"{RED}O site usa UDP.{BLACK}")

# Verifica se existe um painel de administração.
admin_url = f"http://{site_ip}/admin"
try:
    requests.get(admin_url)
    print(f"{RED}Há um painel de administração no site.{BLACK}")
except requests.exceptions.ConnectionError:
    print(f"{RED}Não há painel de administração no site.{BLACK}")

# Verifica se há vulnerabilidades SQL.
sql_vulnerabilities = ["/sqli-labs/", "/sqli-labs/vulnerabilities/"]
for vulnerability in sql_vulnerabilities:
    try:
        requests.get(f"http://{site_ip}{vulnerability}")
        print(f"{RED}O site está vulnerável a SQLi.{BLACK}")
    except requests.exceptions.ConnectionError:
        pass

# Exibe o submenu "Créditos".
def credits():
    print(f"{RED}Créditos: {BLACK}")
    print(f"* Zed Hacking")
    print(f"* https://t.me/BlackoutTeamOfc")

# Escolha o comando.
command = input(f"{RED}Qual comando você deseja executar? {BLACK}")

# Executa o comando.
if command == "help":
    help()
elif command == "version":
    version()
elif command == "quit":
    quit()
elif command == "credits":
    credits()
else:
    print(f"{RED}Comando inválido.{BLACK}")
