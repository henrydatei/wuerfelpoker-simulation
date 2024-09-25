# wuerfelpoker-simulation
I played a game of Würfelpoker and asked myself, has this game some strategy?

# Rules
You have 5 dices, each has a 9, a 10, a jack, a queen, a king and an ass on one of its sides. You have at maximum 3 rounds and in each round you roll the not saved dices (obviously in the first round are no saved dices, so you roll all 5) and after that you decide which of the rolled dices you want to add to the saved dices. In the third round you have to save all dices.

You don't have to play all 3 rounds, you can go directly to the scorecard step after the first round, if you want. In the scorecard step you have to choose in which category you want to put your result. The categories are:
- number of 9's: Number of rolled nines multiplied by 1 point
- number of 10's: Number of rolled tens multiplied by 2 points
- number of jacks: Number of rolled jacks multiplied by 3 points
- number of queens: Number of rolled queens multiplied by 4 points
- number of kings: Number of rolled kings multiplied by 5 points
- number of aces: Number of rolled aces multiplied by 6 points
- street: You get 20 points if you have a nine, ten, jack, queen and king or a ten, jack, queen, king and ass
- full house: You get 30 points if you have a three of a kind and a double (i.e. 2 nines and 3 aces) 
- poker: You get 40 points if you have four of a kind
- grande: You get 50 points if you have 5 of a kind

If you get a street, full house, poker or grande in the first round and go directly to the scorecard step, you get 5 bonus points.

You must go to the scorecard step, even if you don't have anything that fits one of the categories. You then get 0 points in this category.

Important is the added amount of points from every category. The player with the most points win.