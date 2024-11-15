def generate_instructions(hats):
    n = len(hats)
    segments = []
    start = None

    for i in range(n):
        if hats[i] == '': 
            if start is not None:
                segments.append((start, i - 1, hats[start]))
                start = None
        elif start is None or hats[i] != hats[start]:
            if start is not None:
                segments.append((start, i - 1, hats[start]))
            start = i

    if start is not None:
        segments.append((start, n - 1, hats[start]))

    forward_flips = []
    backward_flips = []

    for start, end, direction in segments:
        if direction == 'F':  
            if start == end:
                backward_flips.append(f"{start}")
            else:
                backward_flips.append(f"{start} & {end}")
        elif direction == 'B': 
            if start == end:
                forward_flips.append(f"{start}")
            else:
                forward_flips.append(f"{start} & {end}")

    if len(forward_flips) <= len(backward_flips):
        return forward_flips
    else:
        return backward_flips

hats = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', '', 'B']

instructions = generate_instructions(hats)
for instruction in instructions:
    print(instruction)
