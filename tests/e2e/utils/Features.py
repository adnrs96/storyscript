from distutils.util import strtobool


def parse_features(features, text):
    parsed_features = features.copy()
    for line in text.splitlines():
        if line.startswith("// FEAT"):
            line = line.split(":")[1].strip()
            for item in line.split(" "):
                k, v = item.split("=")
                parsed_features[k] = strtobool(v)
    return parsed_features
