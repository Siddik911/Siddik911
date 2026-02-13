#!/usr/bin/env python3
"""
PDF Generator for Bangla MCQ Questions
This script generates a PDF file containing Bangla questions and options only.
No solutions or diagrams are included.
"""

import os
import sys
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def setup_bangla_font():
    """
    Setup Bangla font for PDF generation.
    This function tries to find and register a suitable Bangla Unicode font.
    """
    # Try to use common system fonts that support Bangla
    potential_fonts = [
        '/usr/share/fonts/truetype/noto/NotoSansBengali-Regular.ttf',
        '/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    
    font_registered = False
    for font_path in potential_fonts:
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont('BanglaFont', font_path))
                print(f"✓ Registered font: {font_path}")
                font_registered = True
                break
            except Exception as e:
                print(f"Could not register {font_path}: {e}")
                continue
    
    if not font_registered:
        print("⚠ Warning: No suitable Bangla font found. Using default font.")
        print("  The Bangla text may not render correctly.")
        return None
    
    return 'BanglaFont'

def read_questions_from_markdown(file_path):
    """
    Read questions from markdown file and parse them.
    Returns a list of questions with their options.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    questions = []
    current_question = None
    
    for line in content.split('\n'):
        line = line.strip()
        
        # Skip empty lines and separators
        if not line or line == '---':
            continue
        
        # Skip header and note lines
        if line.startswith('#') and 'MCQ' in line:
            continue
        if line.startswith('**নোট:**'):
            continue
        
        # Question line
        if line.startswith('## প্রশ্ন'):
            if current_question:
                questions.append(current_question)
            current_question = {'title': line.replace('##', '').strip(), 'text': '', 'options': []}
        elif current_question is not None:
            if line.startswith('**ক)**') or line.startswith('**খ)**') or line.startswith('**গ)**') or line.startswith('**ঘ)**'):
                # Option line
                current_question['options'].append(line)
            elif not line.startswith('**'):
                # Question text
                if current_question['text']:
                    current_question['text'] += ' '
                current_question['text'] += line
    
    # Add last question
    if current_question:
        questions.append(current_question)
    
    return questions

def generate_pdf(output_path, questions, font_name='BanglaFont'):
    """
    Generate PDF with questions and options.
    """
    # Create PDF document
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'BanglaTitle',
        parent=styles['Heading1'],
        fontName=font_name if font_name else 'Helvetica-Bold',
        fontSize=16,
        textColor='#333333',
        spaceAfter=30,
        alignment=TA_CENTER,
    )
    
    # Question title style
    question_title_style = ParagraphStyle(
        'BanglaQuestionTitle',
        parent=styles['Heading2'],
        fontName=font_name if font_name else 'Helvetica-Bold',
        fontSize=14,
        textColor='#000000',
        spaceAfter=10,
        spaceBefore=20,
    )
    
    # Question text style
    question_style = ParagraphStyle(
        'BanglaQuestion',
        parent=styles['Normal'],
        fontName=font_name if font_name else 'Helvetica',
        fontSize=12,
        textColor='#000000',
        spaceAfter=10,
        leading=18,
    )
    
    # Option style
    option_style = ParagraphStyle(
        'BanglaOption',
        parent=styles['Normal'],
        fontName=font_name if font_name else 'Helvetica',
        fontSize=11,
        textColor='#333333',
        spaceAfter=6,
        leftIndent=20,
        leading=16,
    )
    
    # Add title
    title = Paragraph('বহুনির্বাচনী প্রশ্ন', title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.3*inch))
    
    # Add questions
    for i, q in enumerate(questions):
        # Question title
        q_title = Paragraph(q['title'], question_title_style)
        elements.append(q_title)
        
        # Question text
        if q['text']:
            q_text = Paragraph(q['text'], question_style)
            elements.append(q_text)
        
        # Options
        for option in q['options']:
            opt_text = Paragraph(option.replace('**', ''), option_style)
            elements.append(opt_text)
        
        # Add space between questions (but not after the last one)
        if i < len(questions) - 1:
            elements.append(Spacer(1, 0.3*inch))
    
    # Build PDF
    try:
        doc.build(elements)
        return True
    except Exception as e:
        print(f"Error building PDF: {e}")
        return False

def main():
    """Main function to generate the PDF."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # Input and output paths
    markdown_file = os.path.join(project_root, 'docs', 'questions_bangla.md')
    output_pdf = os.path.join(project_root, 'docs', 'questions_bangla.pdf')
    
    print("=" * 60)
    print("Bangla MCQ PDF Generator")
    print("=" * 60)
    
    # Check if markdown file exists
    if not os.path.exists(markdown_file):
        print(f"✗ Error: Markdown file not found: {markdown_file}")
        sys.exit(1)
    
    print(f"✓ Found markdown file: {markdown_file}")
    
    # Setup Bangla font
    font_name = setup_bangla_font()
    
    # Read questions
    print("\nReading questions from markdown...")
    questions = read_questions_from_markdown(markdown_file)
    print(f"✓ Found {len(questions)} questions")
    
    # Generate PDF
    print(f"\nGenerating PDF: {output_pdf}")
    success = generate_pdf(output_pdf, questions, font_name)
    
    if success:
        print(f"✓ PDF generated successfully: {output_pdf}")
        file_size = os.path.getsize(output_pdf)
        print(f"  File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        print("\n" + "=" * 60)
        print("Success! The PDF contains only questions and options.")
        print("No solutions or diagrams are included.")
        print("=" * 60)
        return 0
    else:
        print("✗ Failed to generate PDF")
        return 1

if __name__ == '__main__':
    sys.exit(main())
