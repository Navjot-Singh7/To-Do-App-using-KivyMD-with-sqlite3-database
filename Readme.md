# ✅ Smart Todo App

A **beautiful and efficient** todo application built with Python and KivyMD, featuring SQLite database integration and a sleek material design interface.

## ✨ Features

- **✅ Add & Manage Tasks** - Simple task creation and organization
- **🎯 Mark Completion** - Checkbox system for task tracking
- **🗑️ Safe Deletion** - Confirmation dialogs to prevent accidents
- **💾 Data Persistence** - SQLite database stores all your tasks
- **🚫 Duplicate Prevention** - Smart validation for unique tasks
- **🎨 Beautiful UI** - Material Design with dark theme
- **📱 Responsive Design** - Works seamlessly on different screen sizes
- **⚡ Real-time Updates** - Instant UI feedback for all operations

## 🛠 Tech Stack

- **Python 3** - Core programming language
- **KivyMD** - Material Design components
- **SQLite3** - Lightweight database for data storage
- **Kivy** - Cross-platform framework

## 🚀 Quick Start

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Navjot-Singh7/smart-todo-app.git
cd smart-todo-app
```

1. Install dependencies

```bash
pip install kivy kivymd
```

1. Run the application

```bash
python main.py
```

💡 Key Implementation Details

Database Schema

```python
# Tasks table structure:
# - id (INTEGER PRIMARY KEY)
# - task_text (TEXT)
# - completed (TEXT)  # '0' for incomplete, '1' for complete
```

Smart Features

· Duplicate Detection - Prevents adding existing tasks
· Empty State Handling - Shows helpful message when no tasks
· Persistent Storage - Tasks survive app restarts
· Smooth Animations - KivyMD transitions and dialogs

🎨 Customization

Changing Theme

Modify the theme in main.py:

```python
self.theme_cls.theme_style = "Dark"  # Change to "Light"
self.theme_cls.primary_palette = "DeepPurple"  # Change color scheme
```

Adding New Features

The modular architecture makes it easy to extend:

· Add due dates
· Implement categories
· Add task priorities
· Include search functionality

🔧 Code Architecture

```python
# Clean separation of concerns:
- main.py → UI and user interactions
- todo_database.py → Database operations
- KivyMD → Beautiful material design components
```

🤝 Contributing

Feel free to contribute by:

· Adding new features
· Improving UI/UX
· Optimizing database operations
· Enhancing documentation

⭐ If this project helps you learn KivyMD or inspires your own projects, please give it a star!

---

Built with passion by Navjot Singh - Demonstrating that great apps can be built anywhere, even on mobile! 📱💻