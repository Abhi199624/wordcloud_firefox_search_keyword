#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:24:19 2018

@author: Abhishek Kumar Sinha
@Email: Aksinha334@gmail.com
"""
import sys
import os
import sqlite3
from wordcloud import WordCloud
import matplotlib.pyplot as plt



    # getting the firefox history sqlite file from PC

def getting_database_Path():

    history_path = os.path.expanduser('~') + "/.mozilla/firefox/"

    # finding the .default file ### Generalize form ###
    for element in os.listdir(history_path):
        if element.endswith('.default'):
            history_db = history_path + element + '/places.sqlite'

    try:
        if os.path.isfile(history_db):
            print('Browser history file detected !!!')
    except ValueError:
        print('Browser history file is not detected..!!!')
        sys.exit()
    return history_db


    # checking path file is exist or not print True else False

def connect_database():

    con = sqlite3.connect(getting_database_Path()) # connection to the database 'places.sqlite'
    print('connected Successfully')
    cursor = con.cursor()

    return cursor

    # firing the queries

def firing_query(select_statement = "select moz_places.title, moz_places.visit_count from moz_places;"):

    cursor = connect_database()   # connecting to database
    cursor.execute(select_statement)  # executing the statement
    variable = cursor.fetchall()      # fetching all the data

    #  Refining the data, Removing the NONE type data

    file = []
    for each_element in variable:
        if each_element[0] is not None:
            file.append(each_element[0])
    return file



    # processing the data

def data_processing():

    # calling the firing_query()

    data = firing_query()

    # concatenating each raw data into string for further processing

    txt_file = ''
    for each_data in data:
        txt_file = txt_file +' '+ each_data

    #  converting to lower to make it easier
    txt_file = txt_file.lower()

    return txt_file

def main():

    # passing the txt into wordcloud with various parameters
    # you can change as per your need
    txt = data_processing()

    wordcloud = WordCloud(
                          background_color = 'black',relative_scaling = 0.5,
                            width=1200,height=800,collocations=False
                          ).generate(txt)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    main()

