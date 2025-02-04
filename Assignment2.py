import random

class TrafficSignalController:
    def __init__(self, lanes):
        self.lanes = lanes  # List of lane names
        self.state = {lane: {'vehicles': 0, 'waiting_time': 0, 'priority': 1} for lane in lanes}
    
    def update_traffic_data(self):
        """Simulates real-time traffic data updates."""
        for lane in self.lanes:
            self.state[lane]['vehicles'] = random.randint(0, 10)
            self.state[lane]['waiting_time'] = random.randint(0, 60)
            self.state[lane]['priority'] = 2 if lane == 'emergency' else 1
    
    def calculate_utility(self, lane):
        """Utility function to determine priority of a lane."""
        alpha, beta, gamma = 1.5, 1.0, 2.0  # Weights for factors
        n = self.state[lane]['vehicles']
        w = self.state[lane]['waiting_time']
        p = self.state[lane]['priority']
        return (alpha * n) + (beta * w) + (gamma * p)
    
    def select_best_signal(self):
        """Selects the traffic signal configuration with the highest utility."""
        best_lane = max(self.lanes, key=lambda lane: self.calculate_utility(lane))
        return best_lane
    
    def control_traffic(self):
        """Simulates traffic signal control based on utility calculation."""
        self.update_traffic_data()
        best_lane = self.select_best_signal()
        print("Traffic state:")
        for lane in self.lanes:
            print(f"{lane}: {self.state[lane]}")
        print(f"Green signal given to: {best_lane}\n")

# Example Usage
if __name__ == "__main__":
    lanes = ['north', 'south', 'east', 'west', 'emergency']
    controller = TrafficSignalController(lanes)
    for _ in range(5):  
        controller.control_traffic()
