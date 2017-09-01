#!/usr/bin/env python

"""Generates directories for screenshots"""
import os

#####################
# variables go here #
#####################
FIRST_FOLDER = "One"
SECOND_FOLDER = "Two"

##Rename these as required##
CATEGORIES = [
    "A category", "One lemon", "I like eggs",
    "Another folder", "Here", "We",
    "Go", "You get", "The idea"
]

###############################
# creates initial directories #
###############################
os.mkdir(FIRST_FOLDER)
os.mkdir(SECOND_FOLDER)
os.mkdir("Empty folder")

####################################################
#   Loops that make directories from CATEGORIES    #
# inside FIRST and SECOND directories respectively #
####################################################
for folder in CATEGORIES:
    os.mkdir(os.path.join(FIRST_FOLDER, folder))

for folder in CATEGORIES:
    os.mkdir(os.path.join(SECOND_FOLDER, folder))
