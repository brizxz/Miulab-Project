import json

# Define input and output file paths
input_file = "large_law_problems.txt"  # Change this to your actual file path
output_file = "law_problems.json"  # Output JSON file

# Read the text file
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Process the entries into structured question-answer pairs
questions = []
current_question = None
current_answer = None

for line in lines:
    line = line.strip()
    
    if line == "q":  # New question starts
        if current_question and current_answer:
            questions.append({"question": current_question, "official_answer": current_answer})
        current_question = ""  # Reset for new question
        current_answer = None  # Ensure answer starts fresh
    elif line == "a":  # Answer starts
        current_answer = ""
    elif current_answer is None:  # Still reading the question
        current_question += line + " "
    else:  # Reading the answer
        current_answer += line + " "

# Append the last question-answer pair
if current_question and current_answer:
    questions.append({"question": current_question.strip(), "official_answer": current_answer.strip()})

# Create the final JSON structure
data = {"questions": questions}

# Write to JSON file
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"Conversion complete! JSON saved to {output_file}")
