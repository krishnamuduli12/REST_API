import pickle

# Example of pickling
data = {"name": "Alice", "age": 30, "is_admin": True}
with open("data.pkl", "wb") as file:  # Open a file in write-binary mode
    pickle.dump(data, file)  # Serialize the dictionary and save it
