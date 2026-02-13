# Bangla MCQ Questions Documentation

This directory contains Bangla multiple-choice questions (MCQ) in both source and PDF formats.

## Files

- **questions_bangla.md** - Source questions in Markdown format (editable)
- **questions_bangla.pdf** - Generated PDF document with questions and options only

## Content

The PDF contains 8 multiple-choice questions (প্রশ্ন ০১ through ০৮) in Bangla language.

**Important:** The PDF includes **ONLY questions and options** - no solutions, explanations, or diagrams are included.

## How to Regenerate the PDF

### Prerequisites

1. **Python 3.6+** installed on your system
2. **pip** (Python package installer)
3. **Bangla fonts** for proper rendering

### Installation

1. Install Python dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```

2. Install Bangla fonts (Linux/Ubuntu):
   ```bash
   sudo apt-get update
   sudo apt-get install fonts-noto-core fonts-noto-ui-core
   ```

   On macOS:
   ```bash
   # Bangla fonts are typically pre-installed
   # If needed, download Noto Sans Bengali from Google Fonts
   ```

   On Windows:
   ```bash
   # Download and install Noto Sans Bengali font from:
   # https://fonts.google.com/noto/specimen/Noto+Sans+Bengali
   ```

### Generate PDF

Run the generation script from the project root:

```bash
python3 scripts/generate_pdf.py
```

Or from this directory:

```bash
python3 ../scripts/generate_pdf.py
```

The script will:
1. Read questions from `questions_bangla.md`
2. Set up proper Bangla font rendering
3. Generate `questions_bangla.pdf`
4. Display success message with file size

### Output

```
============================================================
Bangla MCQ PDF Generator
============================================================
✓ Found markdown file: .../docs/questions_bangla.md
✓ Registered font: /usr/share/fonts/truetype/noto/NotoSansBengali-Regular.ttf

Reading questions from markdown...
✓ Found 8 questions

Generating PDF: .../docs/questions_bangla.pdf
✓ PDF generated successfully
============================================================
```

## Editing Questions

To update or modify the questions:

1. Open `questions_bangla.md` in any text editor
2. Modify questions following the existing format:
   ```markdown
   ## প্রশ্ন ০১
   Your question text here?

   **ক)** First option  
   **খ)** Second option  
   **গ)** Third option  
   **ঘ)** Fourth option

   ---
   ```
3. Save the file
4. Run `python3 scripts/generate_pdf.py` to regenerate the PDF

## Format Guidelines

- Each question should start with `## প্রশ্ন` followed by the question number in Bangla numerals (০১, ০২, etc.)
- Options should use Bangla letters: **ক)**, **খ)**, **গ)**, **ঘ)**
- Separate questions with `---`
- Do NOT include solutions or explanations in the markdown file
- Use proper Bangla Unicode characters

## Technical Details

### PDF Generation Library

The PDF is generated using **ReportLab**, a powerful PDF creation library for Python.

### Font Handling

The script automatically detects and uses available Bangla fonts in this order:
1. Noto Sans Bengali
2. Noto Sans (fallback)
3. Liberation Sans (fallback)
4. DejaVu Sans (fallback)

If no suitable font is found, the script will warn you but still generate a PDF (though Bangla characters may not render correctly).

### PDF Properties

- Page size: A4
- Margins: 1 inch (72 points)
- Font size: 12pt for questions, 11pt for options
- Encoding: UTF-8 (full Unicode support)

## Troubleshooting

### Problem: Bangla characters not displaying correctly

**Solution:** Install proper Bangla fonts:
```bash
# Linux
sudo apt-get install fonts-noto-core fonts-noto-ui-core

# Or download from Google Fonts:
# https://fonts.google.com/noto/specimen/Noto+Sans+Bengali
```

### Problem: "Module 'reportlab' not found"

**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Problem: Permission denied when running script

**Solution:** Make the script executable:
```bash
chmod +x scripts/generate_pdf.py
```

Or run with python explicitly:
```bash
python3 scripts/generate_pdf.py
```

## License

This documentation and the PDF generation system are part of the Siddik911 repository.

## Contact

For questions or issues, contact: hasansiddiki65@gmail.com
