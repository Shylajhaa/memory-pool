from .functions import Functions

def execute(user_choice):
    functions = Functions()
    user_controls = {
        "1": "signup",
        2: "add_picture",
        3: "delete_picture",
        4: "edit_picture",
        5: "send_request",
        6: "accept_request",
        7: "view_profile",
        8: "get_user_dashboard"
    }
    functions.invoke(user_controls[user_choice])

if __name__ == "__main__":
    print("Welcome to Memory Pool!")
    print("What would you like to do today?")
    print("--------------------------------")
    print("1. Signup")
    print("2. Post a picture")
    print("3. Delete a picture")
    print("4. Edit a picture")
    print("5. Send a connection request")
    print("6. Accept a connection request")
    print("7. View profile")
    print("8. View User Dashboard")
    print("---------------------------------")

    user_choice = input()
    execute(user_choice)


    