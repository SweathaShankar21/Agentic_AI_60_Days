from typing import Optional, Any

def create_user_profile(
    name: str, 
    age: int, 
    skills: list[str], 
    metadata: dict[str, Any], 
    bio: Optional[str] = None
) -> dict[str, Any]:
    
    profile = {
        "name": name,
        "age": age,
        "skills": skills,
        "metadata": metadata,
        "bio": bio if bio else "No bio provided"
    }
    return profile


new_user = create_user_profile(
    name="Alex",
    age=25,
    skills=["Python", "n8n"],
    metadata={"tier": "pro"},
    bio=None 
)

print(new_user)