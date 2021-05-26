# rock-paper-scissors-exercise

A Python script to simulate the game "Rock, Paper, Scissors, Shoot!" between a user and the computer.


## Prerequisites

    + Anaconda 3.7+
    + Python 3.7+
    + Pip


## Installation

Clone this repository to your local machine. Then, navigate to the root folder of the repository.

Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":

    conda create -n my-game-env python=3.8 
    conda activate my-game-env

Note that the conda create... command will only need to be run the first time you are creating your environment variable in which to run the game.

After activating the virtual environment, run the below pip command to install packages dependencies ( identified in the requiremetns.txt file):

    pip install -r requirements.txt

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    USER_NAME="Add Username Here"


## Usage

Then, to run the game, run the below command:

    python game.py