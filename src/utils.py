import json
from pathlib import Path

def ensure_directory(path):
    """
    Create directory if it doesn't exist.
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def save_json(data, filepath):
    """
    Save dictionary as JSON file.
    """
    ensure_directory(Path(filepath).parent)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def load_json(filepath):
    """
    Load JSON file and return data.
    """
    with open(filepath, 'r') as f:
        return json.load(f)


def print_section(title):
    """
    Print formatted section header.
    """
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


# Example usage
if __name__ == "__main__":
    print_section("Pipeline Utilities Loaded")

    # Test JSON save & load
    sample_data = {"name": "MLOps", "status": "working"}

    save_json(sample_data, "data/sample.json")
    loaded_data = load_json("data/sample.json")

    print("Saved & Loaded Data:", loaded_data)