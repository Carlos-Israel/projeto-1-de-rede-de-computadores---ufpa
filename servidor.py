import socket
import struct

# SERVIDOR
HOST = "localhost"
PORT = 50000

# Criar o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
    s.listen()
    print("Aguardando conexão")
    conn, ender = s.accept()
    print("Conectado em", ender)
    
    # Enviar mensagem de boas-vindas ao cliente
    bem_vindo = "Mensagem do servidor: Bem-vindo!"
    conn.sendall(bem_vindo.encode('utf-8'))
    
    while True:
        try:
            # Receber a opção do cliente
            opcao_data = conn.recv(1024)
            if not opcao_data:
                print("Cliente desconectado.")
                break
            
            opcao = struct.unpack('!I', opcao_data)[0]
            print("Opção recebida:", opcao)
            
            # Receber o número do cliente
            num_data = conn.recv(1024)
            if not num_data:
                print("Cliente desconectado.")
                break
            
            num_deci = int(num_data.decode('utf-8'))  # Converte os dados de byte para string e depois para inteiro
            print('Número recebido:', num_deci)
            
            # Processar a opção do cliente
            if opcao == 1:
                num_bin = bin(num_deci)[2:]  # Converte o número decimal para binário
                conn.sendall(num_bin.encode('utf-8'))  # Envia o número binário de volta ao cliente
                print(f"Enviou: {num_bin}")
            elif opcao == 2:
                num_oct = oct(num_deci)[2:]  # Converte o número decimal para octal
                conn.sendall(num_oct.encode('utf-8'))  # Envia o número octal de volta ao cliente
                print(f"Enviou: {num_oct}")
            elif opcao == 3:
                num_hex = hex(num_deci)[2:]  # Converte o número decimal para hexadecimal
                conn.sendall(num_hex.encode('utf-8'))  # Envia o número hexadecimal de volta ao cliente
                print(f"Enviou: {num_hex}")
        except Exception as e:
            print(f"Erro durante a comunicação com o cliente: {e}")
            break
except Exception as e:
    print(f"Não foi possível iniciar o servidor: {e}")
finally:
    conn.close()
    print("Conexão fechada.")
    s.close()
