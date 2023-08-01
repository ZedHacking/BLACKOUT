#!/usr/bin/env python3

import socket
import requests

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
    print(f"{RED}* check_open_ports: Verifica as portas abertas de um site.{BLACK}")
    print(f"{RED}* get_ip: Consulta o IP de um site.{BLACK}")
    print(f"{RED}* check_sql_vulnerabilities: Verifica se um site é vulnerável a SQLi.{BLACK}")
    print(f"{RED}* get_protocol: Consulta se um site usa UDP ou TCP.{BLACK}")

# Exibe a versão do script.
def version():
    print(f"{RED}Versão: {BLACK}1.0")

# Sai do script.
def quit():
    sys.exit(0)

# Exibe o menu de comandos.
def show_commands():
    print(f"{RED}**Menu de comandos**{BLACK}")
    print(f"{RED}* help: Exibe este menu de ajuda.{BLACK}")
    print(f"{RED}* version: Exibe a versão do script.{BLACK}")
    print(f"{RED}* quit: Sai do script.{BLACK}")
    print(f"{RED}* check_open_ports: Verifica as portas abertas de um site.{BLACK}")
    print(f"{RED}* get_ip: Consulta o IP de um site.{BLACK}")
    print(f"{RED}* check_sql_vulnerabilities: Verifica se um site é vulnerável a SQLi.{BLACK}")
    print(f"{RED}* get_protocol: Consulta se um site usa UDP ou TCP.{BLACK}")

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

# Verifica se há um painel de administração.
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

# Limpa a tela.
if commands_executed == 2:
    clear()

commands_executed = commands_executed + 1

# Escolha a funcionalidade que você deseja usar.
while True:
    print(f"{RED}Escolha a funcionalidade que você deseja
