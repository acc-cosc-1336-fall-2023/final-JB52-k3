#add import
from question_c import get_most_likely_ancestor_consensus

def menu():
    print("""
DNA String Locator:
Enter 2 string sequences. Sequence 1 must between 8 and 16 characters. Sequence 2 must be exactly 4 characters. This program will locate the position of each string by the first character.
""")
    user_quit = input('Press any key to enter sequences and start the program. Type QUIT and press enter to end program: ').upper()
    return user_quit


def main():
    while True:
        user_selection = menu()
        if user_selection == 'QUIT':
            print ('Ending program...')
            break   
        else:

            dna_string1 = input('Enter a DNA string between 8-16 characters comprised of only letters G,A,T,C: ').upper()
            dna_string2 = input('Enter a DNA string of exactly 4 characters comprised of only letters G,A,T,C: ').upper()
            if len(dna_string1) >= 8 and len(dna_string1) <=16 and len(dna_string2):
                result = get_most_likely_ancestor_consensus(dna_string1,dna_string2)
                print('String location(s): ', result)
            else:
                print('Invalid inputs. Please try again.')
                main()

main()