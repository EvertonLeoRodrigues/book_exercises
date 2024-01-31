
while(True):
    expression = input("Digit a expression using just \"(\" \")\" or \"0\" for exit: ")
    if(expression =="0"):
        break

    def check_expression(expression):
        pilha = []
        for char in expression:
            if(char == "("):
                pilha.append(char)
            elif(char==")"):
                if not pilha:
                    return False
                pilha.pop(-1)
        return not pilha
    if check_expression(expression):
        print(f"The expression {expression} is correct!")
    else:
        print(f"The expression {expression} isn't correct!")
