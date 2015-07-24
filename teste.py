from LogParser import logParser
import sys
import codecs

sys.stdout =  codecs.getwriter("cp852")(sys.stdout.detach())


p=logParser("F:\\Jogos\\LoL\\League of Legends\\Logs\\Game - R3d Logs\\")
print(p.getPlayerChampMap("Uerex"))
mapa = p.getPlayersMap()

f =  open("parserResults.txt", "w", encoding="cp852")
for pa in mapa:
    if mapa[pa]["total"] > 0:
        print(pa, mapa[pa])
        f.write(str(pa) + str(mapa[pa]) + "\n")
f.close()
