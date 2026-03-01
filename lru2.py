from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            print(f" Key '{key}' not found.")
            return None

        self.cache.move_to_end(key)
        value = self.cache[key]
        print(f" {key} -> {value}")
        return value

    def put(self, key, value):
        if key in self.cache:
            print(f"[UPDATE] Key '{key}' updated.")
            self.cache.move_to_end(key)
        else:
            print(f"[INSERT] Key '{key}' added.")

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            evicted_key, evicted_value = self.cache.popitem(last=False)
            print(f"[EVICTED] {evicted_key} -> {evicted_value}")

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            print(f"[DELETED] Key '{key}' removed.")
        else:
            print(f"[ERROR] Key '{key}' not found.")

    def clear(self):
        self.cache.clear()
        print("[CLEARED] Cache emptied.")

    def size(self):
        print(f"[SIZE] Current size: {len(self.cache)}/{self.capacity}")

    def show(self):
        if not self.cache:
            print("[EMPTY] Cache is empty.")
            return

        print("\n===== CACHE STATE =====")
        for k, v in self.cache.items():
            print(f"{k} -> {v}")
        print("-----------------------")
        first_key = next(iter(self.cache))
        last_key = next(reversed(self.cache))
        print(f"LRU : {first_key}")
        print(f"MRU : {last_key}")
        print("=======================\n")
if __name__ == "__main__":

    while True:
        try:
            capacity = int(input("Enter cache capacity: "))
            if capacity <= 0:
                print("Capacity must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    lru = LRUCache(capacity)
    print("""
Available Commands:
put     -> Insert/Update key
get     -> Retrieve value
delete  -> Remove a key
show    -> Display cache
size    -> Show cache size
clear   -> Clear entire cache
exit    -> Exit program
""")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "put":
            key = input("Enter key: ")
            value = input("Enter value: ")
            lru.put(key, value)

        elif command == "get":
            key = input("Enter key: ")
            lru.get(key)

        elif command == "delete":
            key = input("Enter key: ")
            lru.delete(key)

        elif command == "show":
            lru.show()

        elif command == "size":
            lru.size()

        elif command == "clear":
            lru.clear()

        elif command == "exit":
            print("Exiting program.")
            break

        else:
            print("Invalid command.")