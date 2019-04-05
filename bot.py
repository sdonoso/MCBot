import json
import requests
import sys
import random

frase=sys.argv[1]
palabra=frase.split(" ")[-1]
#print(palabra)

word = palabra
req =  requests.get("https://api.datamuse.com/words?rel_rhy="+word+"&v=es")
#print(req.json())
results = req.json()
if results==[]:
    print("me trabé :(")
    exit(1)
random.shuffle(results)
wordrhyme=results[0]["word"]

req =  requests.get("https://fraze.it/api/phrase/"+wordrhyme+"/es/1/no/1e1b742e-5a7e-43a2-863e-990a2209aea2")
#print(req.json())
try:
    results = req.json()['results']
except:
    print("sorry men no tengo rima")
    exit(1)
#print(results)
contador=0
while(results[0]["phrase"].find(word)<=10 and contador<20):
    random.shuffle(results)
    contador+=1
    #print(results[0]["phrase"])
    #print(contador)
#print(wordrhyme)
print(results[0]["phrase"][:results[0]["phrase"].find(wordrhyme)+len(wordrhyme)+1])
"""
for phrase in results:
        #if phrase["phrase"].find(word)>=10:
        print(phrase["phrase"])
"""