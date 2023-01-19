# OffTheChain
Simple game made in python processing where a chain chomp breaks off its chain and chases around Toad.

How to play:
- Download or clone the repo
- Install processing and the py processing 3 if not done already
- Click play and the game will go through all the intro scenes
- Once at the street maze use the WASD keys to maneuver through the game
- Catch Toad and you win

Game Scenes:
1. Chomp on pole and Toad is taunting
2. The chain breaks into a lot of pieces
3. The chomp is now off the chain and begins chasing Toad
4. Transition scene of Chomp chasing Toad 
5. Game scene, chase Toad around with the Chomp
6. Game win scene 

Completed Work:
- Made characters using self written geometries and matrix stack
- Implemented basic character control of the chomp character using the wasd keys
- Implemented a basic game engine to handle logic of the game, ie collision with walls and capture of the toad
- Implemented a basic AI for Toad where it will go the location farther away from the player by Euclidian distance
- Created procedural animations for the movement of game characters
- Created a procedural particle simulation for the breaking of the chain 
- Create a random street grid generator for when the player chases around Toad
- Learned the importance of properly structuring a game for running on limited processing power

Future Work:
- Update toad AI to look 2 moves ahead for better movement interpolation
- Update particle system animation to look more like an explosion
- Create tile for the streets, grass, and walls to make them look better
- Implement turning interpolation for the player
- Animate the tail of the chomp
