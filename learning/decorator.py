def auth_decorator(func):
    def wrapper(user):
        if user == "admin":
            print("Access granted")
            func()
        else:
            print("Access denied")
    return wrapper

@auth_decorator
def sensitive_operation():
    print("Performing sensitive operation")

sensitive_operation("admin")  # Access granted
sensitive_operation("guest")  # Access denied
