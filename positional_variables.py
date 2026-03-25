import sys


id = sys.argv[1]
description = sys.argv[2]
status = sys.argv[3]
createdAt = sys.argv[4]
updatedAt = sys.argv[5]

data = {
    "id": id,
    "description": description,
    "status": status,
    "createdAt": createdAt,
    "updatedAt": updatedAt
}

print(data["status"])
print(data["description"])
print(data["id"])