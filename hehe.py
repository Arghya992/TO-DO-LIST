import zipfile
import io

# ------------------ DOCX CONTENT ------------------

CONTENT_TYPES = '''<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/word/document.xml"
              ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
'''

RELS = '''<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1"
                  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"
                  Target="word/document.xml"/>
</Relationships>
'''

# Main document content (Style B – Professional Report Formatting)
TEXT = """
To-Do List Application — Project Documentation

1. Project Title
Console-Based To-Do List Manager in Python

2. Introduction
This project is a console-based To-Do List application written in Python.
It allows users to add tasks, view pending tasks, mark tasks as completed, and delete tasks.
The tasks are stored in a text file for persistent storage.

3. Objectives
• Implement file handling in Python
• Use lists and dictionaries for task management
• Develop a command-line user interface
• Practice modular programming and CRUD operations

4. Technologies Used
• Python 3
• Text File Storage (tasks.txt)
• Any code editor (VS Code, PyCharm, IDLE)

5. Project Structure
ToDoList/
│── tasks.txt
│── todo.py
└── README.md (optional)

6. Screenshots
[ Insert screenshots here ]

7. Conclusion
This project demonstrates the use of file I/O, loops, conditions, and modular programming in Python.
It is easily extendable with features like deadlines, priorities, or a GUI.

8. Future Enhancements
• Add due dates
• Add task categories
• Add priority levels
• Add search functionality
• Add GUI using Tkinter or PyQt
"""

# Build WordprocessingML XML paragraphs
def build_paragraphs(text):
    out = ""
    for line in text.strip().split("\n"):
        line_xml = line.strip().replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        out += f"<w:p><w:r><w:t>{line_xml}</w:t></w:r></w:p>\n"
    return out

DOCUMENT_XML = f'''<?xml version="1.0" encoding="UTF-8"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {build_paragraphs(TEXT)}
    <w:sectPr/>
  </w:body>
</w:document>
'''

# ------------------ WRITE DOCX FILE ------------------

with zipfile.ZipFile("ToDo_Project_Report.docx", "w", zipfile.ZIP_DEFLATED) as docx:
    docx.writestr("[Content_Types].xml", CONTENT_TYPES)
    docx.writestr("_rels/.rels", RELS)
    docx.writestr("word/document.xml", DOCUMENT_XML)

print("✔ DOCX file generated successfully: ToDo_Project_Report.docx")
