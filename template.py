import os

directories = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "models",
    "src"
]

for dir_ in directories:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        print("Directory {} Created Successfully".format(dir_))

files = [
    "dvc.yaml",
    "params.yaml",
    os.path.join("src", "__init__.py"),
    "README.md"
]

for file in files:
    with open(file, "w") as f:
        print("File {} Created Successfully".format(file))
