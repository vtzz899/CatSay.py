def cat_say(message):
    # Define a larger cat drawing with arms and legs using ASCII art
    cat = r"""
          /\_/\  
         ( o.o ) 
          > ^ <
        /       \
       /         \
      |           |
     /  |       |  \
    /   |       |   \
   (    |       |    )
    """

    # Create the speech bubble above the cat with the input message
    bubble = f"""
        {create_bubble(message)}
        {cat}
    """

    # Print the result
    print(bubble)


def create_bubble(message):
    # Create a basic speech bubble around the message
    message_lines = message.split("\n")
    max_length = max(len(line) for line in message_lines)

    # Top of the bubble
    top = " " + "_" * (max_length + 2)
    # Bottom of the bubble
    bottom = " " + "-" * (max_length + 2)

    # Create bubble with message inside
    bubble_content = [top]
    for line in message_lines:
        bubble_content.append(f"| {line.ljust(max_length)} |")
    bubble_content.append(bottom)

    return "\n".join(bubble_content)


# Ask the user for input
message = input("Enter a message for the cat: ")

# Call the cat_say function to display the result
cat_say(message)