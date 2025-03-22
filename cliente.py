import socket
import struct

# Configurações do Cliente
HOST = "127.0.0.1"
PORT = 50000
opcoes = {
    1: "binário",
    2: "octal",
    3: "hexadecimal"
}

# Cria o socket do cliente
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOST, PORT))
    
    # Recebe e imprime a mensagem de boas-vindas do servidor
    print(s.recv(1024).decode('utf-8'))
    
    while True:
        try:
            # Pede ao usuário para escolher a base de conversão
            opcao = int(input("Para qual base você deseja converter?\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n"))

            if opcao in opcoes:
                # Solicita o número a ser convertido
                s.sendall(struct.pack('!I', opcao))
                num = input(f"Digite um número para converter para {opcoes[opcao]}: ")
                s.sendall(num.encode('utf-8'))
                
                # Recebe a resposta do servidor e imprime o resultado
                resposta = s.recv(1024).decode('utf-8')
                print(f"Em {opcoes[opcao]}: {resposta}")
                 # Pergunta se deseja converter outro número
                if input("Deseja converter outro número? [S/N]: ").strip().lower() in 'não':
                    break
            else:
                print("Opção inválida!")
                if input("Tentar novamente? [S/N]: ").strip().lower() in 'não':
                    break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            if input("Tentar novamente? [S/N]: ").strip().lower() in 'não':
                break
except Exception as e:
    print(f"Não foi possível iniciar o cliente: {e}")

finally:
    s.close()
    print("Conexão fechada.")
