#!/usr/bin/env python
import os
import socket

# tcp_ip = '18.204.102.146'
#tcp_ip = '18.204.102.146'
tcp_port = 7015

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', tcp_port))
s.listen(5)

conn, addr = s.accept()

#~ #print 'Endereco de conexao: ', addr

#~ while True:


# data = conn.recv(1024)

while True:
	print("Escutando...\n") 
	data = conn.recv(1024)
	if (data == str.encode('1')):
		print ('Metrica: RTT')
		message = "Requisicao aceita.\n"
		conn.send(str.encode(message))
		print ('Metrica executada com sucesso!\n')
	elif (data == str.encode('2')):
		print ('Metrica: Download')
		message = "Requisicao aceita. Download em andamento:\n"
		conn.send(str.encode(message))
		f = open('texto.txt','rb')
		l = f.read(1024)
		#servidor enviando o arquivo para o cliente
		while (l):
			print(l)
			conn.send(l)
			l = f.read(1024)
		message = "Download concluido com sucesso!"
		conn.send(str.encode(message))
		print ('Metrica executada com sucesso!\n')
		f.close()
	else:
		break
print("Servidor fechado.\n")
conn.close()
