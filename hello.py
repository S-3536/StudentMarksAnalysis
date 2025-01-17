from deepdiff import DeepDiff
items1 = {
    "folder": [
        {"name": "fav1"},
        {"name": "fav2"}
    ],
    "category": [
        {"name": "fav1"},
        {"name": "fav2"}
    ],
    "documents": [
        {"name": "fav1"},
        {"name": "fav2"}
    ]
}

items2 = {
    "folder": [
        {"name": "fav1"},
        {"name": "fav2"}
    ],
    "category": [
        {"name": "fav1"},
        {"name": "fav2"}  # Difference here
    ],
    "documents": [
        {"name": "fav1"},
        {"name": "fav2"}
    ]
}

def are_objects_equal(obj1, obj2):
    diff = DeepDiff(obj1, obj2, ignore_order=False)  # `ignore_order` is useful for lists
    return not diff  # If no differences, `DeepDiff` returns an empty dictionary

# Example usage
result = are_objects_equal(items1, items2)
print(result)


# Frontend
    # HTML
    # CSS
    #JavaScript
# Backend
    # Java/Python
    # Springboot/Django
# Java App development
# MySQL/PostgreSQL(DB)

# Editing
# -------- #