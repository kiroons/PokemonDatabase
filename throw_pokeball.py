#!/usr/bin/python

import random
import sqlite3

def insert_into_db(pokemon, nick):
    c = conn.cursor()
    c.execute('SELECT id FROM Pokemon WHERE name = ?', (pokemon, ))
    poke_id = c.fetchone()[0]
    c.execute('INSERT INTO Caught VALUES (?, ?)', (poke_id, nick))
    conn.commit()

def list_caught():
    c = conn.cursor()
    for row in c.execute('SELECT name, type, nickname FROM Caught JOIN Pokemon ON Caught.id = Pokemon.id ORDER BY Pokemon.name'):
        print(row)

conn = sqlite3.connect('Pokemon.db')

if __name__ == "__main__":

    name = input("Enter your name: ")
    pokemon = input("Enter pokemon: ")
    
    print("%s threw a pokeball at %s!" % (name, pokemon))

    if (random.random() <= 0.25):
        print('You caught %s!' % (pokemon))
        nick = input('Enter a nickname: ')
        insert_into_db(pokemon, nick)
        print("Pokemon you've caught:")
        list_caught()
    else:
        print('%s got away..' % (pokemon))

    conn.close()
