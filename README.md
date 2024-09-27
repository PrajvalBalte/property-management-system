# property-management-system
You are tasked with building a Real Estate Property Management System using
Object-Oriented Programming (OOP) principles in Python. The system will allow users to manage various residential and commercial properties, perform property-related operations, and manage location connections for properties. The system will also include several algorithms like BFS, DFS, Dijkstra's algorithm, and backtracking to solve various property-related problems.
23°C
Cloudy
Project Requirements:
1. Class Structure:
Implement a base class Property to represent common attributes for all properties (name, location, price).
Create two subclasses: I
1. ResidentialProperty: with an additional attribute for the number of bedrooms.
2. CommercialProperty: with an additional attribute for business type.
3. ⁠Project Requirements:
1. Class Structure:
• Implement a base class Property to represent common attributes for all properties (name, location, price).
Create two subclasses:
1. ResidentialProperty: with an additional attribute for the number of bedrooms.
2. CommercialProperty: with an additional attribute for business type.
2. PropertyManager Class:
Properties Management:
1. Maintain a list of properties (both residential and commercial).
2. Provide functionality to add, display, undo the last added property, and sort properties by price.
3. Implement methods to calculate the total value and average price of all properties.
Urgent Queue:
1. Implement a queue to add urgent properties for quick sale.Urgent Queue:
1. Implement a queue to add urgent properties for quick sale.
Graph Management:
1. Implement methods to connect locations of properties and manage connections using a graph (adjacency list).
2. Implement BFS (Breadth-First Search) and DFS (Depth-First Search)
for location traversal.
• Dijkstra's Algorithm:
1. Implement a method to find the shortest path between two property locations.
Backtracking (Subset Sum):
1. Implement a method to find combinations of properties that fit within a given budget using backtracking.Provide a menu-driven interface to allow users to interact with the system:
1. Add a residential or commercial property.
2. Display all properties.
3. Add properties to the urgent queue.
4. Undo the last added property.
5. Calculate total value and average price of properties.
6. Sort properties by price and display them.
7. Search for a property by name.
8. Find properties with the minimum and maximum price.
9. Connect two property locations and perform BFS, DFS, and shortest path search between them.
10. Find properties within a given budget using backtracking
11. ⁠Conditions:
• Object-Oriented Design: Ensure the system is designed using proper object-oriented principles like inheritance, encapsulation, and abstraction.
• Exception Handling: Implement basic exception handling to handle invalid inputs.
• Performance: Use appropriate data structures like deque for the queue and heapg for priority queues.
• Graph Algorithms: Implement and apply BFS, DFS, and Dijkstra's algorithm on the property graph.
• Backtracking: Use backtracking to explore all valid combinations of properties within a budget.
• User-Friendly Interface: The system should allow the user to interact with it through a console-based menu. Input validation and error handling should be implemented.Expected Deliverables:
1. Python Code for the project.
2. README file with clear instructions on how to run the program.
Sample input and output screenshots demonstrating all functionalities.
4. Explanation of the usage of algorithms like BFS, DFS, Dijkstra, and Backtracking.
IMPORTS:
from collections import deque, defaultdict from math import inf import heapg
