def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = int(input("Enter temperature in Celsius"))
    fahrenheit = (9/5 * celcius) + 32

    print(f"Temperature in Fahrenheit \t {fahrenheit: .2f}")

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
