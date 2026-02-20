def read_numbers_from_file(filename: str):
    """Reads numbers from a file and returns them as a list of integers."""
    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        print("File opened successfully.\n")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            try:
                number = int(line)
                numbers.append(number)
            except ValueError: 
                pass

    print(f"Read {len(numbers)} numbers \n")
    return numbers


def compute_statistics(numbers):
    """
    Computes total count, sum, and average of the given list of integers.
    Returns (count, total_sum, average).
    """
    count = len(numbers)
    total_sum = sum(numbers)
    average = (total_sum / count) if count > 0 else None
    return count, total_sum, average


def append_log(filename, count, total_sum, average):
    """Appends a list of log messages to the log file, one per line."""
    with open(filename, "a", encoding="utf-8") as log_file:
        log_file.write("File opened successfully.\n")
        log_file.write(f"Read {count} numbers\n")
        log_file.write(f"Sum: {total_sum}\n")
        log_file.write(f"Average: {average}\n")
        log_file.write("Program executed successfully.\n")


def main():
    input_filename = "numbers.txt"
    log_filename = "results.log"

    try:
        numbers = read_numbers_from_file(input_filename)
        print(f"Numbers read from file: {numbers}")
        count, total_sum, average = compute_statistics(numbers)
        append_log(log_filename, count, total_sum, average)
    except FileNotFoundError:
        with open(log_filename, "a", encoding="utf-8") as log_file:
            log_file.write(f"Error: File not found: {input_filename}\n")
            log_file.write("Processing aborted.\n")
        print(f"Error: {input_filename} not found.")
    except Exception as e:
        with open(log_filename, "a", encoding="utf-8") as log_file:
            log_file.write(f"Unexpected error: {e}\n")
            log_file.write("Processing aborted.\n")
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
    