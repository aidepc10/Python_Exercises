
class Calculator:
    print 'Welcome\n'
    number2 = 15



    def prompt(self):

        number1 = input('Please enter first number: ')

        while True:
            print 'Please select the operation you want to perform: '
            operation = input ('\n 1 SUM \n 2 Multipl \n 3 Sustraction\n 4 Division\n 0 EXIT\n')

            if operation in (1,2,3,4):
                if operation == 1:
                   print self.sum(number1)
                elif operation == 2:
                    print self.multiplication(number1)
                elif operation == 3:
                    print self.sustraction(number1)
                elif operation == 4:
                    print self.division(number1)
            else:
                break


    def sum(self,number1):
        res_sum = number1 + self.number2
        return res_sum

    def multiplication(self,number1):
        res_mult = number1 * self.number2
        return res_mult

    def sustraction(self,number1):
        res_sus = number1 - self.number2
        return res_sus

    def division(self,number1):
        res_div = number1 / self.number2
        return res_div



calc1 = Calculator()
calc1.prompt()