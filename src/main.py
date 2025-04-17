from textnode import TextNode, TextType

print("hello world")

def main ():
    node = TextNode("This is bold text!", TextType.BOLD, None)  # URL is None here
    print(node)


main()