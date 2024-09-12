# OffTheChain

**OffTheChain** is a simple game developed in Python using Processing, where a Chain Chomp breaks free from its chain and chases Toad through a procedurally generated street maze.

### How to Play:
1. Download or clone this repository.
2. Install Processing and the Python Processing 3 library if you haven't already.
3. Run the game and watch as it progresses through the introductory scenes.
4. When the game reaches the street maze, use the **WASD** keys to control the Chomp and chase Toad.
5. Catch Toad to win the game!

### Game Scenes:
1. **Chomp on Pole**: Toad taunts the Chomp while it’s chained to a pole.
2. **Chain Breaks**: The Chomp’s chain shatters into pieces.
3. **Chomp Unleashed**: Now free from the chain, the Chomp starts chasing Toad.
4. **Chase Transition**: A short scene showing Chomp pursuing Toad.
5. **Main Game**: Navigate the street maze as the Chomp and chase down Toad.
6. **Win Scene**: Capture Toad to trigger the winning screen.

### Completed Features:
- **Custom Character Design**: Characters created using custom geometries and a matrix stack.
- **Chomp Controls**: Basic character control for the Chomp, using **WASD** keys for movement.
- **Game Engine**: Implemented a custom game engine to handle core mechanics like wall collisions and capturing Toad.
- **Toad AI**: Developed a basic AI for Toad, making it move to the farthest location from the Chomp based on Euclidean distance.
- **Procedural Animations**: Created procedural animations for character movements.
- **Particle Simulation**: Designed a particle system to simulate the chain breaking into pieces.
- **Random Street Grid**: Implemented a random street maze generator for the Toad chase sequence.
- **Performance Optimization**: Learned and applied best practices for structuring the game to run efficiently on limited processing power.

### Planned Improvements:
- **Toad AI Upgrade**: Enhance Toad's AI to predict the Chomp’s movement two steps ahead, allowing for more strategic evasion.
- **Particle Effects Enhancement**: Improve the particle animation for the chain break to resemble a more realistic explosion.
- **Visual Improvements**: Add tiles for streets, grass, and walls to enhance the overall aesthetics of the game world.
- **Movement Interpolation**: Implement smoother turning interpolation for the Chomp’s movement.
- **Chomp Tail Animation**: Add animation for the Chomp’s tail to bring the character to life.
