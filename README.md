# Directory Structure Generator

**Directory Structure Generator** is a Python-based GUI tool that lets users create a hierarchical view of directory structures. Users can visualize their folder and file organization, save the structure to a `.txt` file, or copy it to the clipboard. Designed with a user-friendly dark theme, it ensures an intuitive and visually appealing experience.

---

## Features
- **Dynamic Directory Selection**: Users can select a directory, and the tool recursively generates its file structure.
- **Exclusion Filters**: Skip directories like `node_modules`, `.git`, `__pycache__`, and `site-packages`.
- **Save and Copy Options**: Save the generated structure to a `.txt` file or copy it directly to the clipboard.
- **Dark Theme GUI**: A modern, eye-friendly dark mode interface for seamless usage.
- **Loading Animation**: Displays a loading spinner while generating the directory structure for larger directories.

---
## Snapshot

![generate_structure_snap](https://github.com/user-attachments/assets/8e727e93-e464-4bb6-8bd0-9bb972d25b17)


---

## Quick Use

Use the already built generate_structure.exe file. ![Click here](https://github.com/kndnsow/Directory-Structure-Generator/blob/main/dist).

---
## Installation

### Prerequisites
- Python 3.8 or higher
- `tkinter` (Usually included with Python installations)

### Clone the Repository
```bash
git clone https://github.com/kndnsow/Directory-Structure-Generator.git
cd Directory-Structure-Generator

*No additional libraries beyond Python's built-in modules are required for this project.*

---

## Usage

1. Run the Python script:
   ```bash
   python directory_structure_generator.py
   ```

2. Use the **Select Directory** button to choose a folder.

3. The directory structure will be displayed in the text box.

4. Save the structure using the **Save File** button or copy it to the clipboard using **Copy to Clipboard**.

---

## Project Structure
```
Directory-Structure-Generator/
├── directory_structure_generator.py   # Main Python script
├── README.md                          # Project documentation
└── requirements.txt                   # Dependency file (if needed)
```

---

## Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request with your enhancements.

1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add YourFeature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
Special thanks to contributors and the open-source community for inspiration!

---

Let me know if you'd like me to customize this further or add more details about specific aspects of the project! 🚀
