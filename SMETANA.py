import sys
import re

def interpret(program_text):
    program_lines = program_text.splitlines()
    memory = {}

    #parse source
    for line in program_lines:

        # remove comments
        line = re.sub("#.*", "", line)

        # spaces and puntuations are optional, case-insensitive
        match = re.match("[Ss]tep\s+(\d+).\.?\s*[Ss]wap\s*[Ss]tep\s+(\d+)\s*[Ww]ith\s*[Ss]tep\s+(\d+)\s*\.?", line)
        if (match):
            memory[int(match.group(1))] = [int(match.group(2)), int(match.group(3))]
            continue
    
        match = re.match("[Ss]tep\s+(\d+)\.?\s*[Gg]o\s*[Tt]o\s*[Ss]tep\s*(\d+)\s*\.?", line)
        if (match):
            memory[int(match.group(1))] = int(match.group(2))
            continue

        sys.stderr.write("Bad line: " + line)        


    #execute
    pointer = min(memory) - 1
    while pointer < max(memory): # need to do more like a c-style for loop, since we change pointer in the loop itself

        pointer += 1

        if not pointer in memory:
            continue

        instruction = memory[pointer]

        if isinstance(instruction, int):
            pointer = instruction

        elif isinstance(instruction, list):
            x = pointer
            y = instruction[0]
            z = instruction[1]

            # these should possibly return an error, or be removed
            #if (not y in memory): memory[y] = None
            #if (not z in memory): memory[z] = None

            memory[y], memory[z] = memory[z], memory[y]

            if (x == y): pointer = z
            elif (x == z): pointer = y

    return memory # return current state at the end, for testing
