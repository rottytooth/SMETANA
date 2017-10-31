import sys
import re

# from Jay Cambell's Ruby implementation: https://esolangs.org/wiki/User:JayCampbell/smatiny.rb

def interpret(program_text):
    program_lines = program_text.splitlines()
    memory = {}
    out_str = '' # for print, we both print to the screen and return a string (for testing)

    #parse source
    for line in program_lines:

        # remove comments
        line = re.sub("#.*", "", line)

        # spaces and puntuations are optional, case-insensitive
        match = re.match("(\d+)\.?\s*[Ss]wap\s*(\d+)\s*[Ww]ith\s*(\d+)\s*\.?", line)
        if (match):
            memory[int(match.group(1))] = [int(match.group(2)), int(match.group(3))]
            continue
    
        match = re.match("(\d+)\.?\s*[Dd]o\s*[Nn]othing\s*\.?", line)
        if (match):
            memory[int(match.group(1))] = None
            continue

        match = re.match("(\d+)\.?\s*[Oo]utput\s*[Tt]his\s*[Bb]lock's\s*[Pp]osition\s*\.?", line)
        if (match):
            memory[int(match.group(1))] = 'print'
            continue

        sys.stderr.write("Bad line: " + line)        


    #execute
    pointer = min(memory) - 1
    while pointer < max(memory): # need to do more like a c-style for loop, since we change pointer in the loop itself

        pointer += 1

        if not pointer in memory:
            continue

        instruction = memory[pointer]

        # SMATINY
        if instruction == 'print':
            sys.stdout.write(chr(pointer))
            out_str += chr(pointer)

        elif isinstance(instruction, list):
            x = pointer
            y = instruction[0]
            z = instruction[1]

            if (not y in memory): memory[y] = None
            if (not z in memory): memory[z] = None

            memory[y], memory[z] = memory[z], memory[y]

            if (x == y): pointer = z
            elif (x == z): pointer = y

    return out_str
