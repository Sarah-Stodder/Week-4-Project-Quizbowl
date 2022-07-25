from api_calls import *
from questions import *


class User():
    def __init__(self):
          self.email = " "
          self.password = " "
          self.user_tokens = " "
          self.admin = " "
    def login(self, email):
        clear_screen()
        self.password=getpass("Password: ")
        self.user_tokens = get_token(user.email,user.password)
        self.user = login_user(self.email, self.password) 
        return self.user

    def register(self):
        clear_screen()
        print("Registration:")
        self.email = input("Email: ")
        self.first_name = input("First Name: ")
        self.last_name = input("Last Name: ")
        self.password = getpass("Password: ")
        confirm = getpass("Confirm password: ")
        if self.password != confirm:
            print("Passwords don't match!")
            sleep(2)
            self.register()
            return

        user_dict={
            "email":self.email,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "password":self.password
        }
        return register_user(user_dict)
user= User()
def do_log_in():
    
    while True:
        clear_screen()
        print("Welcome to A Likely Story Quizathon!")
        email = input("Type your email to login or Type `register` to Register ")
        if email == 'register':
            success_register= user.register()
            if success_register:
                print("You have successfully registered")
                continue
        elif email.lower() == "quit":
            print("Goodbye")
            break
        else:
            try:
                user.login(email)
                break
            except:
                print("Invalid Username/Password combo")
                sleep(2)
                continue
    
    
    
def quiz():
        num = 0
        correct_count = 0
        print(f"Welcome to the Quizathon!")
        while True:
            print(get_one_question(num, user.user_tokens))
            guess = input("When you are ready to guess the answer, type your guess. Or type answer to see Answer: ")
            if guess.lower() == get_answer(num, user.user_tokens).lower():
                print("Good Job!")
                correct_count += 1
                num += 1
                continue

            elif guess.lower() == "answer":
                print(get_answer(num, user.user_tokens))
                num += 1
                sleep(2)
                continue
            elif guess.lower() == "quit":
                print(f"{user.first_name} answered {correct_count} questions correctly")
                sleep(2)
                break
            elif correct_count >= 10:
                print(f"{user.first_name} answered {correct_count} questions correctly")
                sleep(2)
                break
            else: 
                print("incorrect!")
                continue
            

    
    
    
    
    
    
    
    
def main():
    do_log_in()
    if user.email == 'sjsarahboo@gmail.com':
           while True:
            print("""
            Welcome to the Admin section          
    You can:            
    1. See all Questions
    2. Add new questions
    3. Edit questions
    4. Take Quiz
    5. Quit     """)

            command = input("Select your Fate: ")
            if command == "1":
                print(all_questions(user.user_tokens))
                input("Press enter to continue")
                continue
            elif command == "2":
                question_payload = {  "question": input("Type your question"),
    "answer": input("Type the Answer")

            }
                create_question(user.user_tokens, question_payload)
                input("Press enter to continue")
                continue
            elif command == "3":
                edit_payload = {
                    input("What would you like to edit? type question or answer") : input("type your new full question/answer")

                }
                edit_question(user.user_tokens, edit_payload)
                input("Press enter to continue")
                continue

            elif command == "4":
                quiz()
                continue
                    
            elif command == "5":
                print("Goodbye")
                break
                    
            else:
                print("Invalid Selection")
                sleep(2)
                continue
    else:
        quiz()
        
    
    
main()