from typing import List, Dict, Set, Tuple

def compute_user_averages(users: List[Dict[str, object]]) -> List[Tuple[str, float]]:
  
    averages: List[Tuple[str, float]] = []

    for user in users:
        name = user.get("name", "Unknown")
        scores = user.get("scores", [])
        avg = (sum(scores) / len(scores)) if scores else 0.0 
        averages.append((name, avg))

    return averages


def has_admin_access(roles: Set[str]) -> bool:
  
    return "admin" in roles

def main() -> None:
    users: List[Dict[str, object]] = [
        {"name": "Alice",  "scores": [78, 86, 90, 76], "roles": {"editor", "admin"}},
        {"name": "Rahul",  "scores": [65, 72, 80],     "roles": {"viewer"}},
        {"name": "Meera",  "scores": [92, 88, 95, 91], "roles": {"editor", "viewer"}},
        {"name": "Zoya",   "scores": [84, 79, 83],     "roles": {"admin"}},
    ]

    name_avg_tuples = compute_user_averages(users)
    for (name, average), user in zip(name_avg_tuples, users):
        print(f"Name: {name}")
        print(f"Average Score: {average:.2f}")
        print(f"Admin Access: {has_admin_access(user['roles'])}")
        print()


if __name__ == "__main__":
    main()
