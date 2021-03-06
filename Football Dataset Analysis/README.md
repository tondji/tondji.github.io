# <img src="https://github.com/knaggita/Football-Dataset-Analysis/blob/master/logo.png" width="600" alt="Football Dataset Analysis project">

## What is this project?
Football Dataset Analysis is a group project meant to study, analyse and extract information from the [kaggle football dataset](https://www.kaggle.com/secareanualin/football-events/home).

## Description
## Context

Most publicly available football (soccer) statistics are limited to aggregated data such as Goals, Shots, Fouls, Cards. When assessing performance or building predictive models, this simple aggregation, without any context, can be misleading. For example, a team that produced 10 shots on target from long range has a lower chance of scoring than a club that produced the same amount of shots from inside the box. However, metrics derived from this simple count of shots will similarly asses the two teams.

A football game generates much more events and it is very important and interesting to take into account the context in which those events were generated. This dataset should keep sports analytics enthusiasts awake for long hours as the number of questions that can be asked is huge.

## Content

This dataset is a result of a very tiresome effort of webscraping and integrating different data sources. The central element is the text commentary. All the events were derived by reverse engineering the text commentary, using regex. Using this, I was able to derive 11 types of events, as well as the main player and secondary player involved in those events and many other statistics. In case I've missed extracting some useful information, you are gladly invited to do so and share your findings. The dataset provides a granular view of 9,074 games, totaling 941,009 events from the biggest 5 European football (soccer) leagues: England, Spain, Germany, Italy, France from 2011/2012 season to 2016/2017 season as of 25.01.2017. There are games that have been played during these seasons for which I could not collect detailed data. Overall, over 90% of the played games during these seasons have event data.

The [dataset](https://www.kaggle.com/secareanualin/football-events/home) is organized in 3 files:

    * events.csv contains event data about each game. Text commentary was scraped from: bbc.com, espn.com and onefootball.com
    * ginf.csv - contains metadata and market odds about each game. odds were collected from oddsportal.com
    * dictionary.txt contains a dictionary with the textual description of each categorical variable coded with integers



### What does Kaggle mean?
Kaggle, according to [Wikipedia](https://en.wikipedia.org/wiki/Kaggle) "is an online community of data scientists and machine learners, owned by Google, Inc that allows users to find and publish data sets, explore and build models in a web-based data-science environment, work with other data scientists and machine learning engineers, and enter competitions to solve data science challenges."

### What is Football Dataset Analysis project about?
The project is aimed at studying the kaggle football dataset, to analyse, extract information from it and make predictions based on the data.

The main goal is to find the weaknesses and strengths of the team and assess the ways of measurement and improvement of the team performance

We got the most effective events and capitalised on their characteristics in order to achieve the set goal



**Examples of events used to determine the extent of the teams' weaknesses:**
1. Yellow and red cards served
2. Fouls against the team 
4. Shoots off target 
5. Penalty against the team 
6. Offsides
7. Shot place
8. Too high
9. High and wide
10. Goals against the team

**Examples of events used to determine the extent of the teams' strengths:**

1. Goals scored
2. Penalty
3. Cornes
4. Shoots on target
5. Shoots in bar
7. Shot_place
8. Location
9. Penalty spot
10. Very close range
11. Difficult angle and long range
12. Difficult angle on the left
13. Difficult angle on the right

**Below are the tasks we have accomplised:**

1.  Determined the probability of the team winning in a league 
2.  Determined the best combination of  players and strategies to increase the probability of winning
3.  Determined the players that make a great team based on features like attempts, strikes, assists, goals scored and so on
4.  Predicted the highly paid player based on performance in the teams and league at large.
5.  Predicted cards both yellow and red served to a team 
6.  Determined the effect of cards on the team's performance
7.  Found the relationship between receiving cards in the first half and performance in the second half.
8.  Determined the teams that are likely to attack from a given flank 
9.  Determined the correlation between strategies, ball possession and probabilility of winning.
10. Determined the qualitites that make a player crucial to the team's success


# How can I contribute to the Football Dataset Analysis project?

## Steps to follow

1. Fork the project to your respository
4. Clone the project repository and run the project, refer to the "How to setup section" to know how to do that.
3. Study the project code, suggest changes, rectificiations and any inquiries you might have about the project
5. To suggest these changes, you can either
	1. Open an issue on the project where you highlight what you think needs to be changed and how you would like it to be after the change
	2. Make the necessary changes you might want to see in the project, then push your your new changes to abranch on your repository.
	Thereafter, request for your changes to be reviewed by opening a pull request on the main repository. You can review the [GitHub artice](https://help.github.com/articles/creating-a-pull-request/) and other resources to learn to make a pull request.

## Tools used

Tools and librariesused for development;
- Editor: [Jupyter Notebook](https://github.com/jupyter/notebook)
- Programming language: [Python 3](https://www.python.org/download/releases/3.0/)
- Libraries: 
	1. numpy
	2. zipfile
	3. warning
	4. matplotlib
	5. pandas
	6. seaborn
	7. sklearn
	8. venn 
	9. pytorch


## How to set up the enviroment?
- Assuming you have python3 and all the dependencies installed.
- Create a directory and change to that directory
```sh
  > mkdir Data analysis
  > cd Data analysis
```
- Clone this repository.
```sh
> git clone https://github.com/knaggita/Football-Dataset-Analysis
```
- Run Jupyter notebook from commandline
```sh
> jupyter notebook
```
- Run the application.
```sh
> Open the application and run 
```



