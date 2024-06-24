def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
 
    pyramid = [list(map(int, line.split()[1:])) for line in lines]
    max_number = max(pyramid[-1])
 
    decoded_words = [line[number - 1] for line in pyramid for number in line if number <= max_number]
 
    decoded_message = ' '.join(decoded_words)
    # return decoded_message
    return pyramid
 
# Example usage:
message_file = 'coding_qual_input.txt'
decoded_message = decode(message_file)
print(decoded_message)