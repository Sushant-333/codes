# Define the knowledge base as a set of rules
knowledge_base = {
    "Rule 1": {
        "conditions": {
            "current_price": 100,
            "moving_average": 90
        },
        "action": "Buy"
    },
    "Rule 2": {
        "conditions": {
            "current_price": 120,
            "moving_average": 150
        },
        "action": "Sell"
    },
    # Add more rules as needed
}

# Function to match conditions and execute corresponding actions
def execute_expert_system(current_price, moving_average):
    for rule_name, rule_data in knowledge_base.items():
        conditions = rule_data["conditions"]
        if conditions["current_price"] == current_price and conditions["moving_average"] == moving_average:
            return rule_data["action"]
    return "No matching rule found."

# Example usage
current_price = 110
moving_average = 100
action = execute_expert_system(current_price, moving_average)
print("Expert System:", action)
