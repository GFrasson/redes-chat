class Arithmetic:
    def get_elements_from_message(message) -> (float, float, str):
        elements = message.strip().split(' ')

        try:
            first_number = float(elements[0])
            second_number = float(elements[2])
            operator = elements[1]
        except Exception as error:
            raise error
        
        return first_number, second_number, operator

    def arithmetic_operation(a: float, b: float, operator: str):
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: a / b,
            "*": lambda a, b: a * b
        }
        
        if operator not in operations.keys():
            return None

        operation = operations[operator]
        return operation(a, b)
