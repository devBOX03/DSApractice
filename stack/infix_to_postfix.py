def infixToPostfix(infix_exp: str):
    operator_precedence = {'-': 1, '+': 1, '*': 2, '/': 2, '^': 3}
    postfix_output_list = []
    operator_stack: list = []
    for character in infix_exp:
        # check operand
        if character.isalpha():
            postfix_output_list.append(character)
        elif character == '(':
            operator_stack.append(character)
        # remove characters till opening parenthesis
        elif character == ')':
            for operator in operator_stack[::-1]:
                if operator == '(':
                    operator_stack.pop()
                    break
                postfix_output_list.append(operator_stack.pop())
        else:
            for operator in operator_stack[::-1]:
                try:
                    # pop upper precendence opearators
                    if operator_precedence[character] <= operator_precedence[operator]:
                        postfix_output_list.append(operator_stack.pop())
                    else:
                        break
                except KeyError:
                    break
            # push scanned opearator
            operator_stack.append(character)
        

    while operator_stack:
        postfix_output_list.append(operator_stack.pop())

    return ''.join(postfix_output_list)

if __name__ == '__main__':
    infix_expression = 'a+b*(c^d-e)^(f+g*h)-i'
    postfix_expression = infixToPostfix(infix_expression)
    print("Infix: %s"% infix_expression)
    print("Postfix: %s"% postfix_expression)
    #  abcd^e-fgh*+^*+i-
