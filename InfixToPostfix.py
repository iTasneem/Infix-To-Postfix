def is_operator(char): #ction checks if char is one of the operators
    return char in {'+', '-', '*', '/', '^'}

def precedence(op): #checks priority of operators
    precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence_map.get(op, 0)

def infix_to_postfix(expression): # takes an infix expression
    output = [] #stores the postfix expression as a sequence of tokens.
    operator_stack = [] # stack that holds operators

    i = 0 #It's an index variable used to cut expression
    while i < len(expression):
        char = expression[i]

        if char.isdigit() or char == '.':
            num_str = char
            i += 1
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                i += 1
            output.append(num_str)
        elif char in {'(', ')'}:
            if char == '(':
                operator_stack.append(char)
            else:
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            i += 1
        elif is_operator(char):
            while operator_stack and is_operator(operator_stack[-1]) and precedence(operator_stack[-1]) >= precedence(char):
                #checks if operator stack is not empty& if last element is operator not parentheses
                #& compares the precedence of the last operator 
                output.append(operator_stack.pop())
            operator_stack.append(char)
            i += 1
        else:
            i += 1

    while operator_stack:
        output.append(operator_stack.pop())

    return ' '.join(output) # concatenates output list as a single string.

def evaluate_postfix(postfix):
    operand_stack = []

    tokens = postfix.split()
    for token in tokens:
        if token.isdigit() or '.' in token:
            operand_stack.append(float(token))
        elif is_operator(token):
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token == '^':
                result = operand1 ** operand2
            operand_stack.append(result)

    return operand_stack[0]

def is_valid_expression(expression):
    #If any errors occur during the process (like a division by zero or invalid characters), 
    # it catches the exceptions and returns False. Otherwise, it returns True
    try:
        postfix = infix_to_postfix(expression)
        result = evaluate_postfix(postfix)
        return True
    except (ValueError, ZeroDivisionError, IndexError):
        return False

if __name__ == "__main__":
    infix_expression = input("Enter the infix expression: ")
    if is_valid_expression(infix_expression):
        postfix_expression = infix_to_postfix(infix_expression)
        print("Postfix expression:", postfix_expression)
        result = evaluate_postfix(postfix_expression)
        print("Result:", result)
    else:
        print("Invalid expression.")
