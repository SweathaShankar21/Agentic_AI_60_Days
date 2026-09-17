def print_developer_skills(*args: str) -> None:
    print("Skills acquired:")
    for skill in args:
        print(f"{skill}")


print_developer_skills("Python", "FastAPI", "Docker")