def decode_message(message: str, pattern: str) -> bool:
    msg_index = 0
    pat_index = 0
    star_pos = -1
    match_pos = -1

    while msg_index < len(message):
        if pat_index < len(pattern) and (pattern[pat_index] == message[msg_index] or pattern[pat_index] == '?'):
            msg_index += 1
            pat_index += 1
        elif pat_index < len(pattern) and pattern[pat_index] == '*':
            star_pos = pat_index
            match_pos = msg_index
            pat_index += 1
        elif star_pos != -1:
            pat_index = star_pos + 1
            match_pos += 1
            msg_index = match_pos
        else:
            return False

    while pat_index < len(pattern) and pattern[pat_index] == '*':
        pat_index += 1

    return pat_index == len(pattern)
