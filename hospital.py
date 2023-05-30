# Define the knowledge base as a set of rules
knowledge_base = {
    "Rule 1": {
        "conditions": {
            "symptom": "fever",
            "duration": "long"
        },
        "action": "Recommend further investigation for possible infection."
    },
    "Rule 2": {
        "conditions": {
            "symptom": "cough",
            "duration": "short"
        },
        "action": "Suggest over-the-counter cough medicine."
    },
    # Add more rules as needed
}

# Function to match conditions and execute corresponding actions
def execute_expert_system(symptom, duration):
    for rule_name, rule_data in knowledge_base.items():
        conditions = rule_data["conditions"]
        if conditions["symptom"] == symptom and conditions["duration"] == duration:
            return rule_data["action"]
    return "No matching rule found."

# Example usage
symptom = "fever"
duration = "long"
action = execute_expert_system(symptom, duration)
print("Expert System:", action)
