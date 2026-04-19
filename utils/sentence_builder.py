# utils/sentence_builder.py

import time

sentence = ""
prev_char = ""
last_time = 0

def update_sentence(char):
    global sentence, prev_char, last_time

    current_time = time.time()

    if current_time - last_time > 1:  # delay
        if char == "SPACE":
            sentence += " "
        elif char == "DELETE":
            sentence = sentence[:-1]
        elif char != prev_char:
            sentence += char

        prev_char = char
        last_time = current_time

    return sentence