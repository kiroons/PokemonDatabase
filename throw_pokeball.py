#!/usr/bin/python

import random
import sqlite3

conn = sqlite3.connect('Pokemon.db')

name = input("Enter your name: ")
pokemon = input("Enter pokemon: ")

print("%s threw a pokeball at %s!" % (name, pokemon))

if (random.random() <= 0.25):
    print('You caught %s!' % (pokemon))
    nick = input('Enter a nickname: ')
    insert_into_db(pokemon, nick)
    print('Pokemon you\'ve caught:\n')
    list_caught()
    
else:
    print('%s got away..' % (pokemon))

def insert_into_db(pokemon, nick):
    c = conn.cursor()
    c.execute('SELECT id FROM Pokemon WHERE name = %s', (pokemon))
    poke_id = c.fetchone()
    c.execute('INSERT INTO Caught VALUES (%s, %s)', (pokemon, nick))

def list_caught():
    for row in c.execute('SELECT * FROM Caught JOIN Pokemon ON Caught.id = Pokemon.id ORDER BY Pokemon.name'):
        print(row)
