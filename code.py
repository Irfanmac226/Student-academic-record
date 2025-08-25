import hashlib, json, time

# Utility: hashing
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Block class
class Block:
    def __init__(self, index, prev_hash, record, timestamp=None):
        self.index = index
        self.prev_hash = prev_hash
        self.record = record
        self.timestamp = timestamp or time.time()
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "prev_hash": self.prev_hash,
            "record": self.record,
            "timestamp": self.timestamp
        }, sort_keys=True)
        return sha256(block_string)

# Blockchain for student
class AcademicBlockchain:
    def __init__(self, student_name):
        self.student_name = student_name
        self.chain = []
        self.create_genesis()

    def create_genesis(self):
        genesis = Block(0, "0", {"msg": "Genesis Block - Academic Records"})
        self.chain.append(genesis)

    def add_grade(self, subject, teacher, grade):
        record = {
            "Student": self.student_name,
            "Subject": subject,
            "Teacher": teacher,
            "Grade": grade
        }
        prev = self.chain[-1]
        new_block = Block(len(self.chain), prev.hash, record)
        self.chain.append(new_block)

    def get_academic_history(self):
        history = []
        for b in self.chain:
            if isinstance(b.record, dict) and b.record.get("Student") == self.student_name:
                history.append(b.record)
        return history


# ------------------------------
# DEMO with User Input
# ------------------------------
name = input("Enter student name: ")
ab = AcademicBlockchain(name)

while True:
    print("\n1. Add Academic Record")
    print("2. Show Academic History")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        subject = input("Subject: ")
        teacher = input("Teacher's Name: ")
        grade = input("Grade: ")
        ab.add_grade(subject, teacher, grade)
        print("✅ Grade added successfully!")

    elif choice == "2":
        history = ab.get_academic_history()
        print(f"\n📚 Academic History of {ab.student_name}:")
        for h in history:
            print(h)

    elif choice == "3":
        print("Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice, try again.")
