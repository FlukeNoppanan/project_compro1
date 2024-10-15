from menu import MenuClass
import os
def main():
    menu = MenuClass()
    #check if .bin files exist
    if not os.path.exists('student.bin'):
        print("Creating student.bin...")
        with open('student.bin', 'wb') as file:
            pass
    if not os.path.exists('teacher.bin'):
        print("Creating teacher.bin...")
        with open('teacher.bin', 'wb') as file:
            pass

    while True:
        print('-----------------Student management-----------------')
        print('Menu')
        print('1. Add data')
        print('2. Show data')
        print('3. Get specific data')
        print('4. Update data')
        print('5. Delete data')
        print('6. Create report')
        print('7. Exit')
        try:
            choice = input('Enter your choice: ')
            print('------------------------------------------------------')
        except:
            print('Invalid choice')
            continue
        if choice == '1':
            menu.add_data()
        elif choice == '2':
            menu.show_data()
        elif choice == '3':
            menu.get_specific_data()
        elif choice == '4':
            menu.update_data()
        elif choice == '5':
            menu.delete_data()
        elif choice == '6':
            menu.create_report()
        elif choice == '7':
            break
        else:
            print('Invalid choice')

main()