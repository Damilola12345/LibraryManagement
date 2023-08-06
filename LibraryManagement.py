import csv
new_data_entry = []
concluding_records = []
input_data_2 = []
students_data_set = []

def menu_printout(choices,response): 
    print(f'{choices}')
    user_choice = input(f'{user_prompt}')
    while user_choice not in response:
        print(f'{error_notification}')
        user_choice = input(f'{user_prompt}')
    return user_choice

def row_loop(file_object):
    with open(file_object, 'r', encoding='utf8') as file_object:
        csv_reader = csv.reader(file_object)
        row_line = list(csv_reader)  
        if 0 <= len(row_line):
            return row_line
        else:
            return 'Line number is out of range.'
def delete_student_entry(student_registry, placement):
    try:
        student_registry.remove(placement)
    except ValueError:
        print('The specified student was not found!')

begin_program = True
reception_m = '\nGreetings, and welcome to the library management software.'
closing_statement = "\nYou're welcome! Have a wonderful day ahead!"
primary_options = '\n1. Explore \n2. Administer Books \n3. Access Book Information \n4. Exit'
search_choices = '\n1. Title Search \n2. Genre Search \n3. Year Search \n4. Author Search'
administer_book_menu = '\n1. Add New Book \n2. Check-Out \n3. Return \n4. View Outanding'
book_details_panel = '\n1. Information by ID \n2. Information by ISBN'
result_quantity_feedback = 'Your search resulted in a total count of '
result_quantity_feedback_end = ' results.'
user_prompt = '\nEnter option: '
book_identifier_prompt = '\nEnter Book Id:'
isbn_prompt = '\nEnter Book ISBN:'
title_search_prompt = '\nEnter Book Title: '
genre_search_prompt = '\nEnter Genre: '
year_search_prompt = '\nEnter Year Of Publication: '
author_search_prompt = '\nEnter Name Of Author: '
continue_prompt = '\nContinue using program? Y:N : '
title_input_prompt = 'Enter Book Title: '
author_input_prompt = 'Enter Author: '
book_publication_prompt = 'Enter Publication Date: '
book_genre_prompt = 'Enter Genre: '
book_isbn_prompt = 'Enter ISBN: '
book_publisher_prompt = 'Enter Publisher: '
book_language_prmpt = 'Enter Language: '
book_page_count_prompt = 'Enter Page Count: '
book_available_copies_prompt = 'Enter Available Copies: '
book_rating_prompt = 'Enter Rating: '
book_price_prompt = 'Enter Price: '
main_menu_choice = ['1', '2', '3', '4']
input_search_choice = ['1', '2', '3', '4']
input_manage_book_selection = ['1', '2', '3','4']
input_details_choice = ['1', '2']
error_notification = 'Please enter a valid option'
number_of_results = 0




print(f'{reception_m}')
while begin_program:
    library_information = 'library.csv'
    student_information = 'students.csv'
    row = row_loop(library_information)
    student_row = row_loop(student_information)
    selection_main_menu = menu_printout(choices=primary_options,response=main_menu_choice)
        
    if selection_main_menu == '1': #main choices search
        decision_search_menu = menu_printout(choices=search_choices, response=input_search_choice)
        if decision_search_menu == '1':
            retrieved_book= input(title_search_prompt).title()
        elif decision_search_menu == '2':
            retrieved_genre = input(genre_search_prompt).title()
        elif decision_search_menu =='3':
            searched_year = input(year_search_prompt).title()
        elif decision_search_menu == '4':
            searched_author = input(author_search_prompt).title()
        else:
            print(error_notification)
            
    elif selection_main_menu == '2': # main choices manage
        manage_book_menu_user_answer = menu_printout(choices=administer_book_menu, response=input_manage_book_selection)
        if manage_book_menu_user_answer == '1':
            book_id_add = input(book_identifier_prompt).title()
            book_title = input(f'{title_input_prompt}').title()
            book_author = input(f'{author_input_prompt}').title()
            book_publication_date = input(f'{book_publication_prompt}')
            book_genre = input(f'{book_genre_prompt}').title()
            book_isbn = input(f'{book_isbn_prompt}').upper()
            book_publisher = input(f'{book_publisher_prompt}').title()
            book_language = input(f'{book_language_prmpt}').title()
            book_page_count = (input(f'{book_page_count_prompt}'))
            book_available_copies = input(f'{book_available_copies_prompt}')
            book_rating = input(f'{book_rating_prompt}')
            book_price = input(f'{book_price_prompt}')           
        if manage_book_menu_user_answer == '2':
            student_name = input('Enter the name of the student: ').title()
            student_mat_no = input('Enter the Student Matriculation Number: ')
            book_id_manage = input('Enter the book id: ')
            checkout_date = input('Enter checkout Date: ')
            return_date = input('Enter return date: ')
        if manage_book_menu_user_answer == '4':
            for index, student_full_info in enumerate(student_row):
                for student_info in student_full_info:
                    name_of_student = student_full_info[0]
                    mat_no_of_student = student_full_info[1]
                    book_id_taken = student_full_info[2]
                    date_taken = student_full_info[3]
                    date_to_return = student_full_info[4]
                    student_row_no = index
                print(f'\nName of Students: {name_of_student} \nMatriculation: {mat_no_of_student} \nBook Id: {book_id_taken} \
                    \nDate Taken: {date_taken} \nReturn Date: {date_to_return} \nIndex: {index+1}')
                
    elif selection_main_menu == '3': #details choices
        book_by_details_user_answer = menu_printout(choices=book_details_panel, response=input_details_choice)
        if book_by_details_user_answer == '1':
            id_no = input(book_identifier_prompt)
        elif book_by_details_user_answer == '2':
            isbn_no = input(isbn_prompt)
        else:
            print(f'{error_notification}')
    elif selection_main_menu == '4':
        print(f'{closing_statement}')
        begin_program = False
    for index, sublist in enumerate(row):
                for name in sublist:
                    book_id= sublist[0]
                    title = sublist[1].title()
                    author = sublist[2].title()
                    publication_date = sublist[3]
                    genre = sublist[4].title()
                    isbn = sublist[5]
                    publisher = sublist[6]
                    language = sublist[7]
                    page_count = sublist[8]
                    available_copies = sublist[9]
                    rating = sublist[10]
                    price = sublist[11]
                    
                    result = (f'\nTitle:{title}\n Author:{author}\n ID:{book_id}\n Genre:{genre}\n Rating:{rating}')
                    full_result = (f'\nTitle:{title}\n Author:{author}\n ID:{book_id}\n Genre:{genre}\n Rating:{rating}\n Year:{publication_date}\
                                    \n ISBN:{isbn}\n Publisher:{publisher}\n Page Count:{page_count} pages\n Available Copies:{available_copies}\n Price: ${price}')
                if selection_main_menu == '1':
                    if decision_search_menu == '1':
                        if retrieved_book in title:
                            number_of_results = number_of_results + 1
                            print(f'{result}')
                    if decision_search_menu == '2':
                        if retrieved_genre in genre:
                            number_of_results = number_of_results + 1
                            print(f'{result}')
                        
                    if decision_search_menu == '3':
                        if searched_year in publication_date:
                            number_of_results = number_of_results + 1
                            print(f'{result}')
                            
                    if decision_search_menu == '4':
                        if searched_author in author:
                            number_of_results = number_of_results + 1
                            print(f'{result}')
                if selection_main_menu == '3':
                    if book_by_details_user_answer == '1':
                        if id_no == book_id:
                            number_of_results = number_of_results + 1
                            print(f'{full_result}')
                    if book_by_details_user_answer == '2':
                        if isbn_no == isbn:
                            number_of_results = number_of_results + 1
                            print(f'{full_result}')
    if selection_main_menu == '1' or selection_main_menu == '3':
        print(f'\n{result_quantity_feedback}{number_of_results}{result_quantity_feedback_end}')
    if selection_main_menu == '2':
        if manage_book_menu_user_answer == '1':
            new_data_entry.append(book_id_add)
            new_data_entry.append(book_title)
            new_data_entry.append(book_author)
            new_data_entry.append(book_publication_date)
            new_data_entry.append(book_genre)
            new_data_entry.append(book_isbn)
            new_data_entry.append(book_publisher)
            new_data_entry.append(book_language)
            new_data_entry.append(book_language)
            new_data_entry.append(book_page_count)
            new_data_entry.append(book_available_copies)
            new_data_entry.append(book_price)
            concluding_records.append(new_data_entry)
            print(concluding_records)
            with open(library_information, 'a', newline='') as file_object:
                csv_writer = csv.writer(file_object)
                csv_writer.writerows(concluding_records)
        elif manage_book_menu_user_answer == '2':
            input_data_2.append(student_name)
            input_data_2.append(student_mat_no)
            input_data_2.append(book_id_manage)
            input_data_2.append(checkout_date)
            input_data_2.append(return_date)
            students_data_set.append(input_data_2)
            with open(student_information, 'a', newline='') as file_object:
                csv_writer = csv.writer(file_object)
                csv_writer.writerows(students_data_set)
        elif manage_book_menu_user_answer == '3':
            student_row_entered_answer_initial = int(input(f'Enter student row placement: '))
            student_row_entered_answer = student_row_entered_answer_initial - 1
            student_row_entered = student_row[student_row_entered_answer]
            delete_student_entry(student_row,student_row_entered)
            with open(student_information, 'w', newline='') as file_object:
                csv_writer = csv.writer(file_object)
                csv_writer.writerows(student_row)
                print(f'Student {student_row_entered_answer_initial} has returned book and successfully removed')
        try_again = input(f'{continue_prompt}').upper()
        if try_again == 'Y':
            begin_program = True
        elif try_again == 'N':
            begin_program = False
        else:
            print(f'{error_notification}')
    begin_program == False
