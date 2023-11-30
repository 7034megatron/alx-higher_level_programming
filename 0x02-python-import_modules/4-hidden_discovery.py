#!/usr/bin/python3
import dis

if __name__ == "__main__":
    with open('hidden_4.pyc', 'rb') as file:
        code = file.read()

    instructions = dis.get_instructions(code)
    names = set()

    for instruction in instructions:
        if instruction.opname == 'LOAD_NAME' and not instruction.argrepr.startswith('__'):
            names.add(instruction.argrepr)

    for name in sorted(names):
        print(name)
