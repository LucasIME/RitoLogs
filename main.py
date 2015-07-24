#imports
import os
import re
import operator

#configutation variables
filepath = "F:\\Jogos\\LoL\\League of Legends\\Logs\\Game - R3d Logs"
summonerName = "Uerex"
champMap = {}
playerMap = {}
playerChampMap = {}

for filename in os.listdir(filepath):
    #file = open(filepath +"\\"+ filename, 'r', encoding="cp852")
    file = open(filepath +"\\"+ filename, 'r', encoding="utf8")
    data = file.readline()
    while data != '':
        if "created for " in data:
            playerName = re.split("(.*Hero )(.*)(\(.*created for )(.*)", data)[4]
            if playerName not in playerMap:
                playerMap[playerName] = 1
            else:
                playerMap[playerName] += 1
        if "created for " + summonerName in data:
            champPlayed = re.split("(.*Hero )(.*)(\(.*created for )(.*)", data)[2]
            if champPlayed not in champMap:
                champMap[champPlayed] = 1
            else:
                champMap[champPlayed]+=1
        data = file.readline()

sortedchampMap = sorted(champMap.items(), key=operator.itemgetter(1), reverse=True)
sortedPlayerMap = sorted(playerMap.items(), key=operator.itemgetter(1), reverse=True)
total=0
for p in sortedchampMap:
    print(p[0] +"," + str(p[1]))
    total +=p[1]

print(champMap)

print("Total Games Played: "+ str(total))

for p in sortedPlayerMap:
    print(p[0] + "," +str(p[1]))
