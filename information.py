# Define the knowledge base as a set of rules
knowledge_base = {
    "Rule 1": {
        "conditions": {
            "input": "search",
            "type": "document"
        },
        "action": "Retrieve the requested document from the database."
    },
    "Rule 2": {
        "conditions": {
            "input": "store",
            "type": "document"
        },
        "action": "Store the document in the appropriate location in the database."
    },
    "Rule 3": {
        "conditions": {
            "input": "delete",
            "type": "document"
        },
        "action": "Remove the document from the database."
    },
    # Add more rules as needed
}

# Function to match conditions and execute corresponding actions
def execute_expert_system(input_data, type_data):
    for rule_name, rule_data in knowledge_base.items():
        conditions = rule_data["conditions"]
        if conditions["input"] == input_data and conditions["type"] == type_data:
            return rule_data["action"]
    return "No matching rule found."

# Main loop to interact with the expert system
while True:
    user_input = input("User: ")
    user_input = user_input.lower().split()

    if len(user_input) == 2:
        action = execute_expert_system(user_input[0], user_input[1])
        print("Expert System:", action)
    else:
        print("Expert System: Please provide both input and type (e.g., search document).")
