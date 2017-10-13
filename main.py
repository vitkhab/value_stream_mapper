import yaml

filename = "examples/development.yml"
stream = open(filename, "r")
steps = yaml.load(stream)