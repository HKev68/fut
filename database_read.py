# -*- coding: utf-8 -*-
"""
Created on Thu May 12 14:21:01 2016

@author: Kevin Henry
"""

from urllib2 import urlopen
from bs4 import BeautifulSoup

# Structure which will contain all the players database
database = []

class Player:
    def __init__(self, player_id = 0, player_firstname = "", player_lastname = "", player_surname = None, player_rating = 0, player_nationality = ""):
        self.id = player_id
        self.firstname = player_firstname
        self.lastname = player_lastname
        self.surname = player_surname
        self.rating = player_rating
        self.nationality = player_nationality
    def print_info(self):
        print "-----------------------------------"
        print self.firstname + " " + self.lastname
        if self.surname is not None :
            print "Surname : " + self.surname
        else :
            print "No Surname"
        print "Rating : " + str(self.rating)
        print "Nationality : " + self.nationality
        print "ID : " + str(self.id)
        print "-----------------------------------" 
        
def create_player_database() :
    """ Create the database according to the .json file """
    global database
    player_database = []
    response = urlopen('http://cdn.content.easports.com/fifa/fltOnlineAssets/CC8267B6-0817-4842-BB6A-A20F88B05418/2017/fut/items/web/players.json')
    db_soup = BeautifulSoup(response.read(), from_encoding=response.headers.getparam('charset'))
    db_text = str(db_soup)[13:-3] # May need to be changed depending on the computer
    #db_text = str(db_soup)[28:-21] # May need to be changed depending on the computer
    
    # Add the players to the databse
    for player_legends in range (0,2) :
        db_players = db_text.split('}],"LegendsPlayers":[{')[player_legends]
        db_list = db_players.split("},{")
        i = 0
        for players_description in db_list :
            dummy = db_list[i].split(",") 
            new_player = Player()
            for j in range(0, len(dummy)) :
                if dummy[j].split(":")[0] == '"f"' :
                    new_player.firstname = dummy[j].split(":")[1][1:-1] 
                elif dummy[j].split(":")[0] == '"l"' :
                    new_player.lastname = dummy[j].split(":")[1][1:-1]                 
                elif dummy[j].split(":")[0] == '"c"' :
                    new_player.surname = dummy[j].split(":")[1][1:-1] 
                elif dummy[j].split(":")[0] == '"id"' :
                    new_player.id = dummy[j].split(":")[1] 
                elif dummy[j].split(":")[0] == '"r"' :
                    new_player.rating = dummy[j].split(":")[1]
                elif dummy[j].split(":")[0] == '"n"' :
                    new_player.nationality = dummy[j].split(":")[1]   
                else :
                    print "Error in database creation"
                    return None
            player_database.append(new_player) 
            i += 1
    
    # Correct non-UTF-8 characters
    for player in player_database :
        # Correct firstname
        player.firstname = player.firstname.replace("\u00c1", "A")
        player.firstname = player.firstname.replace("\u00c2", "A")
        player.firstname = player.firstname.replace("\u00c4", "A")
        player.firstname = player.firstname.replace("\u00c5", "A")
        player.firstname = player.firstname.replace("\u00c7", "C")
        player.firstname = player.firstname.replace("\u00c9", "E")
        player.firstname = player.firstname.replace("\u00cd", "I")
        player.firstname = player.firstname.replace("\u00d1", "N")
        player.firstname = player.firstname.replace("\u00d3", "O")
        player.firstname = player.firstname.replace("\u00d6", "O")
        player.firstname = player.firstname.replace("\u00d8", "O")
        player.firstname = player.firstname.replace("\u00dc", "U")
        player.firstname = player.firstname.replace("\u00de", "D")
        player.firstname = player.firstname.replace("\u00df", "B")
        player.firstname = player.firstname.replace("\u00e0", "a")
        player.firstname = player.firstname.replace("\u00e1", "a")
        player.firstname = player.firstname.replace("\u00e2", "a")
        player.firstname = player.firstname.replace("\u00e3", "a")
        player.firstname = player.firstname.replace("\u00e4", "a")
        player.firstname = player.firstname.replace("\u00e5", "a")
        player.firstname = player.firstname.replace("\u00e6", "ae")
        player.firstname = player.firstname.replace("\u00e7", "c")
        player.firstname = player.firstname.replace("\u00e8", "e")
        player.firstname = player.firstname.replace("\u00e9", "e")
        player.firstname = player.firstname.replace("\u00ea", "e")
        player.firstname = player.firstname.replace("\u00eb", "e")
        player.firstname = player.firstname.replace("\u00ed", "i")
        player.firstname = player.firstname.replace("\u00ee", "i")
        player.firstname = player.firstname.replace("\u00ef", "i")
        player.firstname = player.firstname.replace("\u00f0", "d")
        player.firstname = player.firstname.replace("\u00f1", "n")
        player.firstname = player.firstname.replace("\u00f2", "o")
        player.firstname = player.firstname.replace("\u00f3", "o")
        player.firstname = player.firstname.replace("\u00f4", "o")
        player.firstname = player.firstname.replace("\u00f5", "o")
        player.firstname = player.firstname.replace("\u00f6", "o")
        player.firstname = player.firstname.replace("\u00f8", "o")
        player.firstname = player.firstname.replace("\u00fa", "u")
        player.firstname = player.firstname.replace("\u00fc", "u")
        player.firstname = player.firstname.replace("\u00fd", "y")
        player.firstname = player.firstname.replace("\u00fe", "b")
        # Correct lastname
        player.lastname = player.lastname.replace("\u00c1", "A")
        player.lastname = player.lastname.replace("\u00c2", "A")
        player.lastname = player.lastname.replace("\u00c4", "A")
        player.lastname = player.lastname.replace("\u00c5", "A")
        player.lastname = player.lastname.replace("\u00c7", "C")
        player.lastname = player.lastname.replace("\u00c9", "E")
        player.lastname = player.lastname.replace("\u00cd", "I")
        player.lastname = player.lastname.replace("\u00d1", "N")
        player.lastname = player.lastname.replace("\u00d3", "O")
        player.lastname = player.lastname.replace("\u00d6", "O")
        player.lastname = player.lastname.replace("\u00d8", "O")
        player.lastname = player.lastname.replace("\u00dc", "U")
        player.lastname = player.lastname.replace("\u00de", "D")
        player.lastname = player.lastname.replace("\u00df", "B")
        player.lastname = player.lastname.replace("\u00e0", "a")
        player.lastname = player.lastname.replace("\u00e1", "a")
        player.lastname = player.lastname.replace("\u00e2", "a")
        player.lastname = player.lastname.replace("\u00e3", "a")
        player.lastname = player.lastname.replace("\u00e4", "a")
        player.lastname = player.lastname.replace("\u00e5", "a")
        player.lastname = player.lastname.replace("\u00e6", "ae")
        player.lastname = player.lastname.replace("\u00e7", "c")
        player.lastname = player.lastname.replace("\u00e8", "e")
        player.lastname = player.lastname.replace("\u00e9", "e")
        player.lastname = player.lastname.replace("\u00ea", "e")
        player.lastname = player.lastname.replace("\u00eb", "e")
        player.lastname = player.lastname.replace("\u00ed", "i")
        player.lastname = player.lastname.replace("\u00ee", "i")
        player.lastname = player.lastname.replace("\u00ef", "i")
        player.lastname = player.lastname.replace("\u00f0", "d")
        player.lastname = player.lastname.replace("\u00f1", "n")
        player.lastname = player.lastname.replace("\u00f2", "o")
        player.lastname = player.lastname.replace("\u00f3", "o")
        player.lastname = player.lastname.replace("\u00f4", "o")
        player.lastname = player.lastname.replace("\u00f5", "o")
        player.lastname = player.lastname.replace("\u00f6", "o")
        player.lastname = player.lastname.replace("\u00f8", "o")
        player.lastname = player.lastname.replace("\u00fa", "u")
        player.lastname = player.lastname.replace("\u00fc", "u")
        player.lastname = player.lastname.replace("\u00fd", "y")
        player.lastname = player.lastname.replace("\u00fe", "b")
        # Correct surname
        if player.surname is not None :
            player.surname = player.surname.replace("\u00c1", "A")
            player.surname = player.surname.replace("\u00c2", "A")
            player.surname = player.surname.replace("\u00c4", "A")
            player.surname = player.surname.replace("\u00c5", "A")
            player.surname = player.surname.replace("\u00c7", "C")
            player.surname = player.surname.replace("\u00c9", "E")
            player.surname = player.surname.replace("\u00cd", "I")
            player.surname = player.surname.replace("\u00d1", "N")
            player.surname = player.surname.replace("\u00d3", "O")
            player.surname = player.surname.replace("\u00d6", "O")
            player.surname = player.surname.replace("\u00d8", "O")
            player.surname = player.surname.replace("\u00dc", "U")
            player.surname = player.surname.replace("\u00de", "D")
            player.surname = player.surname.replace("\u00df", "B")
            player.surname = player.surname.replace("\u00e0", "a")
            player.surname = player.surname.replace("\u00e1", "a")
            player.surname = player.surname.replace("\u00e2", "a")
            player.surname = player.surname.replace("\u00e3", "a")
            player.surname = player.surname.replace("\u00e4", "a")
            player.surname = player.surname.replace("\u00e5", "a")
            player.surname = player.surname.replace("\u00e6", "ae")
            player.surname = player.surname.replace("\u00e7", "c")
            player.surname = player.surname.replace("\u00e8", "e")
            player.surname = player.surname.replace("\u00e9", "e")
            player.surname = player.surname.replace("\u00ea", "e")
            player.surname = player.surname.replace("\u00eb", "e")
            player.surname = player.surname.replace("\u00ed", "i")
            player.surname = player.surname.replace("\u00ee", "i")
            player.surname = player.surname.replace("\u00ef", "i")
            player.surname = player.surname.replace("\u00f0", "d")
            player.surname = player.surname.replace("\u00f1", "n")
            player.surname = player.surname.replace("\u00f2", "o")
            player.surname = player.surname.replace("\u00f3", "o")
            player.surname = player.surname.replace("\u00f4", "o")
            player.surname = player.surname.replace("\u00f5", "o")
            player.surname = player.surname.replace("\u00f6", "o")
            player.surname = player.surname.replace("\u00f8", "o")
            player.surname = player.surname.replace("\u00fa", "u")
            player.surname = player.surname.replace("\u00fc", "u")
            player.surname = player.surname.replace("\u00fd", "y")
            player.surname = player.surname.replace("\u00fe", "b")
        
    print "Players database created, there is actually " + str(len(player_database)) + " different players in the Ultimate Team Database"   
    
    database = player_database
    
    return player_database

def find_player_with_name(player_database, firstname, lastname):
    """ Returns the player id from the player having firstname and lastname """
    for player in player_database :
        if (player.firstname == firstname) & (player.lastname == lastname) :
            return player.id 
    else :
        return None

def find_player_with_id(player_database, id_to_find):
    """ Returns the player name from the player having id """
    for player in player_database :
        if (player.id == id_to_find):
            return player.firstname + " " + player.lastname 
    else :
        return None

def get_player_with_id(player_database, id_to_find):
    """ Return the players structure from a specific id """
    for player in player_database :
        if (player.id == id_to_find):
            return player
    else :
        return None    
        
def get_player_list(name):
    """ Return all players having the string name in their name or surname """
    global database
    name = name.toLower()
    player_list = []
    # Filter the database
    for player in database :
        player_lastname = player.lastname.lower()
        player_firstname = player.firstname.lower()
        if player.surname is not None :
            player_surname = player.surname.lower()
            if (player_surname.find(name) != -1) or (player_lastname.find(name) != -1) or (player_firstname.find(name) != -1) :
                player_list.append(player)
        else :
            if (player_lastname.find(name) != -1) or (player_firstname.find(name) != -1) :
                player_list.append(player)
    
    # Classify per ranking
    if len(player_list) != 0 :
        player_list = sorted(player_list, key=lambda player: player.rating, reverse=True)
           
    if len(player_list) != 0 :
        if len(player_list) > 50 :
           return -1
        else :
            return player_list
    else :
        return 0
