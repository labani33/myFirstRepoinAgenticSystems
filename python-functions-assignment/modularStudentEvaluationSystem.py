def greet_student(name):
    return "Hello, " + name + "!"

def calculate_stats(scores):
    count = len(scores)
    average = sum(scores) / count
    return count, average

def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    name = input("Enter student's name: ")
    greeting = greet_student(name)
    raw_scores = input("Enter the scores: ")
    parts = raw_scores.split()
    scores = []
    for p in parts:
        scores.append(float(p))
    subject_count, average = calculate_stats(scores)
    result = evaluate_result(average)
    print("\n=== Student Evaluation ===")
    print(greeting)
    print("Subjects:", subject_count)
    print("Average Score:", round(average, 2))
    print("Result:", result)

main()