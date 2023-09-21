# Python Docker Container for learning Python
This docker container will help people to hone their python skills from Interview perspective

## Pre - Requisites
1. Install Docker - platform agnostic
2. Install vscode - platform agnostic
3. Install docker extension on vscode

## Running the Container:
1. Open the folder which contains .devcontainer folder in vscode
2. vscode will prompt you to reopen the project in a dev container
3. Reopen the project
4. First time opening will take some time, check log to see the status

## Contents:
1. Helloworld - Simple Hello world Project
2. python_sololearn_course - All basic Python covered here, going forward from here it will be advanced python
3. esp32cam - OpenCV and ESP32 Cam -> not working in docker
4. helloworldproject - Hello World Project for Django
5. Data_science - Data Science course from sololearn - see below for more details

## How to use this container
1. For single file execution -> open the file in editior -> press shift + ctrl + p -> Run Task -> Run Python Script
2. For running django development server -> press shift+ctrl+p -> Run task -> Run Django Development Server

## Data Science Course
1. The Sololearn data science course is done in a complex way - 
2. Half the project is in .py files and half is in Jupyter notebook. End part from Classification is from Kaggle Notebook
3. Plan is to port everything to Kaggle in future

## Github Codespaces
1. This repo is also linked with github codespaces
2. A docker container is automatically initialized from Dockerfile
3. All the extensions, tasks and settings are taken from the json files of vscode in the repo
4. It is an excellent platform to start developement from anywhere just with a system and good internet connection