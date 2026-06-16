from datetime import datetime


def generate_log(data):
    """Generate a dated log file from a list of entries.

    Args:
        data (list): The log entries to write.

    Returns:
        str: The filename of the generated log file.

    Raises:
        ValueError: If data is not a list.
    """
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Created log file: {filename}")
    return filename
