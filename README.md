# Student-academic-record
A beginner-friendly blockchain implementation in Python for securely storing student academic records.

This project demonstrates how blockchain principles can be used in education to ensure tamper-proof academic history, traceability, and data integrity across semesters, teachers, and subjects.

🚀 Features

✅ Genesis Block Creation – Begins the student’s academic history with a first block.

✅ Add Academic Records – Store subject, teacher, and grade per semester or session.

✅ Student-wise Blockchain – Each student has their own private, secure chain.

✅ View Academic History – Retrieve all past academic records in order.

✅ Tamper-Proof Verification – Detects if any academic record has been modified.

✅ Interactive CLI Menu – Easily add/view records through terminal interface.

✅ Beginner-Friendly Python Code – Teaches blockchain concepts without added complexity.

⚙️ How It Works

A new student is initialized with a Genesis block.

Each subject-grade record (along with teacher info) becomes a new block.

All blocks are linked using SHA-256 hashing, forming an immutable chain.

Users can view full academic history or verify data integrity.

Any tampering (modifying or deleting data) will break the chain's hash linkage.

🔑 Concepts Used
Concept	Description
🧱 Blockchain	Each block represents a subject-grade entry linked chronologically.
🔒 SHA-256 Hashing	Hashes ensure blocks are securely linked and immutable.
✨ Immutability	Past academic records cannot be edited without detection.
📜 Traceability	Full academic performance from start to finish is visible.
✅ Data Validation	The chain can be checked for tampering by verifying hashes.
📂 File Structure
student_blockchain.py    # Main Python script
README.md                # Project overview

💻 Sample CLI Output
Enter student name: Alice Johnson

1. Add Academic Record
2. Show Academic History
3. Exit

Enter choice: 1
Subject: Mathematics
Teacher's Name: Mr. Lee
Grade: A
✅ Grade added successfully!

💡 Future Enhancements

🧾 Export academic record to PDF or JSON

🧑‍🎓 Add support for multiple students with persistent storage

🌐 Build a web dashboard using Flask/Django

🛡 Encrypt sensitive data (e.g., grades)

✅ Add full chain validation via is_chain_valid() function

📚 Educational Purpose

This project is built to help students and educators understand how blockchain can be applied in real-world education scenarios. By learning how records are stored immutably and securely, learners get a hands-on introduction to:

Data structures

Hashing

Chain linking

Blockchain logic

✅ Ready to Use

If you'd like, I can also:

Provide the full working Python script

Add a chain validation function

Package it for easy use (as ZIP or module)
