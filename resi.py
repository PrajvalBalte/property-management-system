from collections import deque, defaultdict
from math import inf
import heapq

# Base class for properties
class Property:
    def __init__(self, name, location, price):
        self.name = name
        self.location = location
        self.price = price

    def __str__(self):
        return f"Property(Name: {self.name}, Location: {self.location}, Price: {self.price})"

# Subclass for Residential Property
class ResidentialProperty(Property):
    def __init__(self, name, location, price, bedrooms):
        super().__init__(name, location, price)
        self.bedrooms = bedrooms

    def __str__(self):
        return f"ResidentialProperty(Name: {self.name}, Location: {self.location}, Price: {self.price}, Bedrooms: {self.bedrooms})"

# Subclass for Commercial Property
class CommercialProperty(Property):
    def __init__(self, name, location, price, business_type):
        super().__init__(name, location, price)
        self.business_type = business_type

    def __str__(self):
        return f"CommercialProperty(Name: {self.name}, Location: {self.location}, Price: {self.price}, Business Type: {self.business_type})"

class PropertyManager:
    def __init__(self):
        self.properties = []  # List to hold all properties
        self.urgent_queue = deque()  # Queue for urgent properties
        self.graph = defaultdict(list)  # Adjacency list for location connections
        self.property_graph = defaultdict(list)  # Adjacency list for property connections
        self.last_added = None  # For undo functionality

    def add_property(self, property):
        self.properties.append(property)
        self.last_added = property
        # Automatically connect this property to others with the same location
        for prop in self.properties:
            if prop.location == property.location and prop != property:
                self.property_graph[prop.name].append(property.name)
                self.property_graph[property.name].append(prop.name)
        print(f"\n✔️  Added: {property}")

    def undo_last_property(self):
        if self.last_added:
            self.properties.remove(self.last_added)
            print(f"\n✔️  Undo: Removed {self.last_added}")
            self.last_added = None
        else:
            print("\n❌  No property to undo.")

    def display_properties(self):
        print("\n--- All Properties ---")
        if not self.properties:
            print("No properties available.")
            return
        for prop in self.properties:
            print(prop)
        print("----------------------")

    def sort_properties_by_price(self):
        self.properties.sort(key=lambda x: x.price)
        print("\n✔️  Properties sorted by price.")

    def total_value_of_properties(self):
        return sum(prop.price for prop in self.properties)

    def average_price_of_properties(self):
        if len(self.properties) == 0:
            return 0
        return self.total_value_of_properties() / len(self.properties)

    def enqueue_urgent_property(self, property):
        self.urgent_queue.append(property)
        print(f"\n✔️  Urgent property added: {property}")

    def dequeue_urgent_property(self):
        if self.urgent_queue:
            urgent_property = self.urgent_queue.popleft()
            print(f"\n✔️  Urgent property sold: {urgent_property}")
        else:
            print("\n❌  No urgent properties.")

    # Graph functions to manage property locations
    def connect_locations(self, location1, location2):
        self.graph[location1].append(location2)
        self.graph[location2].append(location1)
        print(f"\n✔️  Connected {location1} with {location2}")

    def bfs(self, start):
        print("\n--- BFS Traversal ---")
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            location = queue.popleft()
            print(location, end=" ")
            for neighbor in self.graph[location]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        print("\n----------------------")

    def dfs(self, start):
        print("\n--- DFS Traversal ---")
        visited = set()
        self._dfs_recursive(start, visited)
        print("\n----------------------")

    def _dfs_recursive(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    # Modified Dijkstra's algorithm to find the shortest path between properties
    def dijkstra(self, start_property_name, end_property_name):
        # Check if properties exist
        if start_property_name not in self.property_graph or end_property_name not in self.property_graph:
            print(f"\n❌  Either {start_property_name} or {end_property_name} does not exist in the property list.")
            return

        distances = {prop.name: inf for prop in self.properties}
        distances[start_property_name] = 0
        priority_queue = [(0, start_property_name)]

        while priority_queue:
            current_distance, current_property = heapq.heappop(priority_queue)

            if current_distance > distances[current_property]:
                continue

            for neighbor in self.property_graph[current_property]:
                distance = current_distance + 1  # Assume distance between any two properties is 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        if distances[end_property_name] == inf:
            print(f"\n❌  No path between {start_property_name} and {end_property_name}")
        else:
            print(f"\n✔️  Shortest path from {start_property_name} to {end_property_name} is {distances[end_property_name]} steps")

    # Backtracking: Find properties within a budget
    def find_properties_within_budget(self, budget):
        result = []
        self._find_combinations(0, [], budget, result)
        return result

    def _find_combinations(self, index, current, remaining_budget, result):
        # If within budget, add the current combination to the result
        if remaining_budget >= 0:
            result.append(list(current))

        # Return if no more properties are left to consider
        if index == len(self.properties):
            return

        # Include current property and recurse
        current.append(self.properties[index])
        self._find_combinations(index + 1, current, remaining_budget - self.properties[index].price, result)
        current.pop()

        # Exclude current property and recurse
        self._find_combinations(index + 1, current, remaining_budget, result)

def print_menu():
    print("\n" + "╔" + "═" * 54 + "╗")
    print("║          🏠 Property Management System Menu 🏠       ║")
    print("╠" + "═" * 54 + "╣")
    print("║ 1. Add a Residential Property                        ║")
    print("║ 2. Add a Commercial Property                         ║")
    print("║ 3. Display All Properties                            ║")
    print("║ 4. Undo Last Added Property                          ║")
    print("║ 5. Sort Properties by Price                          ║")
    print("║ 6. Calculate Total and Average Price of Properties   ║")
    print("║ 7. Add Property to Urgent Queue                      ║")
    print("║ 8. Dequeue Urgent Property                           ║")
    print("║ 9. Connect Two Property Locations                    ║")
    print("║ 10. Perform BFS (Breadth-First Search)               ║")
    print("║ 11. Perform DFS (Depth-First Search)                 ║")
    print("║ 12. Find Shortest Path Between Two Properties        ║")
    print("║ 13. Find Properties Within Budget                    ║")
    print("║ 14. Exit                                             ║")
    print("╚" + "═" * 54 + "╝")

def main():
    manager = PropertyManager()

    while True:
        print_menu()
        try:
            choice = int(input("Select an option (1-14): "))
        except ValueError:
            print("\n❌  Invalid input. Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter property name: ")
            location = input("Enter property location: ")
            price = int(input("Enter property price: "))
            bedrooms = int(input("Enter number of bedrooms: "))
            manager.add_property(ResidentialProperty(name, location, price, bedrooms))

        elif choice == 2:
            name = input("Enter property name: ")
            location = input("Enter property location: ")
            price = int(input("Enter property price: "))
            business_type = input("Enter business type: ")
            manager.add_property(CommercialProperty(name, location, price, business_type))

        elif choice == 3:
            manager.display_properties()

        elif choice == 4:
            manager.undo_last_property()

        elif choice == 5:
            manager.sort_properties_by_price()
            manager.display_properties()

        elif choice == 6:
            print(f"\n💰  Total Value: {manager.total_value_of_properties()}")
            print(f"💵  Average Price: {manager.average_price_of_properties()}")

        elif choice == 7:
            name = input("Enter property name: ")
            location = input("Enter property location: ")
            price = int(input("Enter property price: "))
            bedrooms = int(input("Enter number of bedrooms: "))
            manager.enqueue_urgent_property(ResidentialProperty(name, location, price, bedrooms))

        elif choice == 8:
            manager.dequeue_urgent_property()

        elif choice == 9:
            loc1 = input("Enter first location: ")
            loc2 = input("Enter second location: ")
            manager.connect_locations(loc1, loc2)

        elif choice == 10:
            start = input("Enter starting location for BFS: ")
            manager.bfs(start)

        elif choice == 11:
            start = input("Enter starting location for DFS: ")
            manager.dfs(start)

        elif choice == 12:
            start_property = input("Enter the name of the starting property: ")
            end_property = input("Enter the name of the destination property: ")
            manager.dijkstra(start_property, end_property)

        elif choice == 13:
            budget = int(input("Enter your budget: "))
            properties_in_budget = manager.find_properties_within_budget(budget)
            if properties_in_budget:
                for combo in properties_in_budget:
                    print("Combination: ", [str(prop) for prop in combo])
            else:
                print("❌  No properties found within this budget.")

        elif choice == 14:
            print("\n👋  Exiting the Property Management System...")
            break

        else:
            print("\n❌  Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
