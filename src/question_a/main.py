#add import
import question_a
def menu():
    menu = int(input("""
Multiplication Table Menu
1 - Display Table
2 - Quit
"""))
    return menu

def main():
    cont = True
    while True:
        selection = menu()

        if selection == 1:
            display_vals = question_a.display_multiplication_table()
            print(display_vals)

        elif selection == 2:
            cont = False
            print('Quitting...')
            break
        

        else:
            print('Invalid input. Select 1 or 2.')

main()