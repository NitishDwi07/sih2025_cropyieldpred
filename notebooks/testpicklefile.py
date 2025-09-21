import pickle
import sys

if len(sys.argv) != 2:
    print("Usage: python testpickelfile.py <pickle_file>")
    sys.exit(1)

file_path = sys.argv[1]

with open(file_path, "rb") as f:
    obj = pickle.load(f)

print(f"Loaded from {file_path}:")
print("Type:", type(obj))

# Try to inspect content
if hasattr(obj, "predict"):  # ML model objects usually have this
    print(" This looks like a trained model (has predict method).")
elif isinstance(obj, (list, tuple)):
    print("List/Tuple content sample:", obj[:10])
elif hasattr(obj, "shape"):
    print("Shape:", obj.shape)
    print("Sample content:", obj[:10])
else:
    print("Content:", obj)
