# Reflection:
# 1. In Exercise 3 you saw the difference between .get() and bracket notation. 
# When in real work would you use each one, and what's your rule of thumb for choosing?
# Answer: Use .get() when a key might be missing and you want a safe fallback value without crashing the program. Use bracket notation when the key is strictly required and its absence is a critical bug.
# 
# 2. Exercise 8 asked you to build a summary dictionary with a loop. What does this 
# pattern remind you of from Excel, and why might the Python version be more useful for large datasets?
# Answer: This reminds me of an Excel PivotTable or SUMIF function. Python is more useful for large datasets because it handles millions of rows efficiently without performance degradation.

# --- Exercise 1 ---
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1200.0
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)
# --- Exercise 2 ---
customer["phone"] = "555-1234"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)
# --- Exercise 3 ---
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError:
    print("KeyError caught")

# --- Exercise 4 ---
for k, v in customer.items():
    print(f"{k}: {v}")
# Iterating without .items() only loops through keys, while .items() gives both keys and values.

# --- Exercise 5 ---
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}
tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
final_price = 200 * (1 - discount)
print(tier, discount, final_price)