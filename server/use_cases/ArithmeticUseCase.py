class ArithmeticUseCase:
    def execute(self, request, response):
        first_number = request['body']['first_number']
        second_number = request['body']['second_number']
        operation = request['body']['operation']

        try:
            first_number = float(first_number)
            second_number = float(second_number)
            operation = operation
        except Exception as error:
            # TODO: Response error message
            raise error
        
        result = self.arithmetic_operation(first_number, second_number, operation)

        response({
            'result': result
        })

    def arithmetic_operation(self, a: float, b: float, operation: str) -> float:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: a / b,
            "*": lambda a, b: a * b
        }
        
        if operation not in operations.keys():
            return None

        operation = operations[operation]
        return operation(a, b)
