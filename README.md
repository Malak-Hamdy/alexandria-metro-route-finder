# Alexandria Metro Route Finder

A Python application that uses Breadth-First Search (BFS) to find and visualize routes between stations in a modeled Alexandria metro network.

## Overview

This project represents metro stations as a graph and uses BFS to find a route between a starting station and a destination. The application uses Pygame to display the route, highlight visited stations, and animate a metro icon along the calculated path.

## Features

- **BFS route finding:** Finds a route between two selected stations.
- **Graph representation:** Models station connections using an adjacency list.
- **Interactive input:** Accepts a starting station and destination.
- **Route visualization:** Highlights the calculated route on a metro map.
- **Visited-station visualization:** Displays the stations visited during BFS traversal.
- **Metro animation:** Animates a metro icon along the selected route.
- **Route summary:** Displays the station sequence, visited order, and number of stops.
- **Custom visual assets:** Includes a custom metro map and metro icon created for the project.

## Technologies Used

- Python
- Pygame
- `collections.deque`
- Graphs and Breadth-First Search

## How It Works

1. The metro network is represented as a graph.
2. The user enters a starting station and destination.
3. BFS explores the graph level by level while tracking visited stations and parent relationships.
4. The parent mapping is used to reconstruct the route.
5. Pygame visualizes the visited stations and route, then animates the metro icon along the path.

For an unweighted graph, BFS finds a route with the fewest edges, provided the destination is reachable.

## Project Structure

- `main.py` — Main application, Pygame interface, route visualization, and animation.
- `bfs.py` — BFS traversal and path reconstruction.
- `data.py` — Metro graph and station coordinates.
- `icon.png` — Application icon.
- `myMetro.png` — Metro icon used in the animation.
- `pygame_map (1).png` — Metro map background.

## Running the Project

1. Install Python 3.
2. Install Pygame:

   ```bash
   pip install pygame
   ```

3. Ensure the Python files and required assets are in the expected locations.
4. Update the image and font paths in `main.py` to match your local environment, if necessary.
5. Run the application:

   ```bash
   python main.py
   ```

## Important Notes

This project was originally developed and tested in a local development environment. The image and font assets may use machine-specific absolute paths, so you may need to update these paths in `main.py` before running the application.

The original custom font and image assets are required unless the corresponding code is adjusted to use alternatives. The project has not yet been verified on a fresh computer setup.

## Concepts Demonstrated

- Graph representation using adjacency lists.
- Breadth-First Search traversal.
- Queue-based exploration using `deque`.
- Visited-node tracking and parent mapping.
- Path reconstruction.
- Interactive graphical interfaces and animation with Pygame.
