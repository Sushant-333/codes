# Define the knowledge base as a set of rules
knowledge_base = {
    "Rule 1": {
        "conditions": {
            "key_result_areas": ["Quality", "Timeliness"],
            "competencies": ["Communication", "Problem Solving"],
            "rating": "Excellent"
        },
        "action": "Employee performance is excellent."
    },
    "Rule 2": {
        "conditions": {
            "key_result_areas": ["Quantity", "Customer Satisfaction"],
            "competencies": ["Teamwork", "Adaptability"],
            "rating": "Good"
        },
        "action": "Employee performance is good."
    },
    # Add more rules as needed
}

# Function to match conditions and execute corresponding actions
def evaluate_performance(key_result_areas, competencies, rating):
    for rule_name, rule_data in knowledge_base.items():
        conditions = rule_data["conditions"]
        if (set(conditions["key_result_areas"]) == set(key_result_areas) and
                set(conditions["competencies"]) == set(competencies) and
                conditions["rating"] == rating):
            return rule_data["action"]
    return "No matching rule found."

# Example usage
key_result_areas = ["Quality", "Timeliness"]
competencies = ["Communication", "Problem Solving"]
rating = "Excellent"
action = evaluate_performance(key_result_areas, competencies, rating)
print("Expert System:", action)
