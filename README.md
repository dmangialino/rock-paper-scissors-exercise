# rock-paper-scissors-exercise

A Python script to simulate the game "Rock, Paper, Scissors, Shoot!" between a user and the computer.


## Prerequisites

    + Anaconda 3.7+
    + Python 3.7+
    + Pip


## Installation

Clone this repository to your local machine. Then, navigate to the root folder of the repository.

    cd rock-paper-scissors-exercise

## Setup

Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":

    conda create -n my-game-env python=3.8 
    conda activate my-game-env

After activating the virtual environment, run the below to install packages dependencies (identified in the requiremetns.txt file):

    pip install -r requirements.txt

## Configuring environment variables

To customize your username, create a new file called ".env" in the root directory of your repository. Update the contents of the ".env" file with the bleow, specifying your desired username within the double quotes:

    USER_NAME="Add Username Here"

Be sure to save the .env file after updating the username.


## Usage

Then, to run the game, run the below command:

    python game.py