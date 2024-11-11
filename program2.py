def match_pattern(input_str: str, pattern_str: str) -> bool:
    input_index = 0  # Pointer for traversing the input string
    pattern_index = 0  # Pointer for traversing the pattern string
    wildcard_pos = -1  # Stores the last position of '*' in the pattern
    temp_index = -1  # Stores the position in the input string to retry matching after '*' is processed

    while input_index < len(input_str):
        if pattern_index < len(pattern_str) and (pattern_str[pattern_index] == input_str[input_index] or pattern_str[pattern_index] == '?'):
            # Match characters or '?'
            input_index += 1
            pattern_index += 1
        elif pattern_index < len(pattern_str) and pattern_str[pattern_index] == '*':
            # '*' can match zero or more characters, record its position
            wildcard_pos = pattern_index
            temp_index = input_index
            pattern_index += 1
        elif wildcard_pos != -1:
            # Backtrack to the last '*' and try matching the next character of input_str
            pattern_index = wildcard_pos + 1
            temp_index += 1
            input_index = temp_index
        else:
            # If no match is found, return False
            return False

    # Skip any trailing '*' in the pattern
    while pattern_index < len(pattern_str) and pattern_str[pattern_index] == '*':
        pattern_index += 1

    # If pattern is fully matched, return True
    return pattern_index == len(pattern_str)
