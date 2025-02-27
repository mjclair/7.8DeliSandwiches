
sandwich_orders = ["tuna", "ham and cheese", "turkey", "veggie", "chicken"]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  list
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)  

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
