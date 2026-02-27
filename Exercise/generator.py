import os

# Generate 1MB of random binary noise
random_bytes = os.urandom(1024 * 1024) 

with open(r"File Handling\random.img", "wb") as f:
    f.write(random_bytes)

print("✅ random.img created (1MB size)!")