def create_profile(**kwargs):
    print("--- User Profile Details ---")
    
    # kwargs acts just like a normal dictionary!
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


create_profile(name="Alex", age=25, hobby="Coding", city="Chennai")