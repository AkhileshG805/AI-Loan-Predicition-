import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # completely blank layout

    assets_dir = r'C:\Users\Dell\.gemini\antigravity\scratch\AI_Loan_Prediction\ppt_assets'
    logo_ngp = os.path.join(assets_dir, 'akhilesh_slide_1_img_0.png')
    logo_dlk = os.path.join(assets_dir, 'akhilesh_slide_3_img_1.jpg')
    img_code = os.path.join(assets_dir, 'akhilesh_slide_9_img_5.png')
    img_form = os.path.join(assets_dir, 'form_input_cropped.png')
    img_app = os.path.join(assets_dir, 'result_approved_cropped.png')
    img_rej = os.path.join(assets_dir, 'result_rejected_cropped.png')
    img_thanks = os.path.join(assets_dir, 'akhilesh_slide_14_img_0.jpg')

    # Color definitions
    COLOR_BLACK = RGBColor(0, 0, 0)
    COLOR_DARK = RGBColor(30, 41, 59)
    COLOR_NAVY = RGBColor(11, 25, 44)
    COLOR_MUTED = RGBColor(100, 116, 139)
    COLOR_TEAL = RGBColor(44, 122, 123)
    COLOR_CYAN_BG = RGBColor(51, 161, 222)
    COLOR_CARD_BG = RGBColor(241, 245, 249)
    COLOR_CARD_BORDER = RGBColor(203, 213, 225)
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_GREEN = RGBColor(5, 150, 105)
    COLOR_RED = RGBColor(220, 38, 38)

    FONT_FAMILY = "Times New Roman"

    def add_header(slide, title_text):
        tx_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.35), Inches(12.33), Inches(0.70))
        tf = tx_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.alignment = PP_ALIGN.CENTER
        p.font.name = FONT_FAMILY
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = COLOR_BLACK

    def add_footer(slide, slide_num):
        # Date (left)
        b_date = slide.shapes.add_textbox(Inches(0.4), Inches(7.15), Inches(2.0), Inches(0.30))
        tf_d = b_date.text_frame
        tf_d.margin_left = tf_d.margin_top = tf_d.margin_right = tf_d.margin_bottom = 0
        p_d = tf_d.paragraphs[0]
        p_d.text = "9/25/2026"
        p_d.font.name = FONT_FAMILY
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = COLOR_MUTED

        # Center: SUMMER INTERNSHIP
        b_c = slide.shapes.add_textbox(Inches(4.66), Inches(7.15), Inches(4.0), Inches(0.30))
        tf_c = b_c.text_frame
        tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
        p_c = tf_c.paragraphs[0]
        p_c.text = "SUMMER INTERNSHIP"
        p_c.alignment = PP_ALIGN.CENTER
        p_c.font.name = FONT_FAMILY
        p_c.font.size = Pt(11)
        p_c.font.color.rgb = COLOR_MUTED

        # Right: Slide Number
        b_n = slide.shapes.add_textbox(Inches(12.5), Inches(7.15), Inches(0.4), Inches(0.30))
        tf_n = b_n.text_frame
        tf_n.margin_left = tf_n.margin_top = tf_n.margin_right = tf_n.margin_bottom = 0
        p_n = tf_n.paragraphs[0]
        p_n.text = str(slide_num)
        p_n.alignment = PP_ALIGN.RIGHT
        p_n.font.name = FONT_FAMILY
        p_n.font.size = Pt(11)
        p_n.font.color.rgb = COLOR_MUTED

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    if os.path.exists(logo_ngp):
        slide1.shapes.add_picture(logo_ngp, Inches(0.45), Inches(0.32), Inches(1.35), Inches(1.35))

    # College Title
    b_col = slide1.shapes.add_textbox(Inches(1.90), Inches(0.28), Inches(10.90), Inches(0.45))
    tf_col = b_col.text_frame
    tf_col.word_wrap = True
    p = tf_col.paragraphs[0]
    p.text = "Dr. N.G.P. INSTITUTE OF TECHNOLOGY"
    p.alignment = PP_ALIGN.CENTER
    p.font.name = FONT_FAMILY
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLACK

    # College Address
    b_addr = slide1.shapes.add_textbox(Inches(1.90), Inches(0.70), Inches(10.90), Inches(1.0))
    tf_addr = b_addr.text_frame
    tf_addr.word_wrap = True
    p = tf_addr.paragraphs[0]
    p.text = "Coimbatore  - 48\n(An Autonomous Institution)\n(Approved by AICTE, New Delhi & Affiliated to Anna University, Chennai)\nRecognized by UGC & Accredited by NAAC A+ and NBA (CSE, BME, EEE, ECE and Mech) Dr.N.G.P. Nagar,\nKalapatti Main Rd, Coimbatore, Tamil Nadu 641048"
    p.alignment = PP_ALIGN.CENTER
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9.5)
    p.font.color.rgb = COLOR_DARK

    # Department
    b_dept = slide1.shapes.add_textbox(Inches(0.50), Inches(1.95), Inches(12.33), Inches(0.40))
    tf_dept = b_dept.text_frame
    p = tf_dept.paragraphs[0]
    p.text = "DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND DATA SCIENCE"
    p.alignment = PP_ALIGN.CENTER
    p.font.name = FONT_FAMILY
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLACK

    # Course
    b_crs = slide1.shapes.add_textbox(Inches(0.50), Inches(2.45), Inches(12.33), Inches(0.70))
    tf_crs = b_crs.text_frame
    p1 = tf_crs.paragraphs[0]
    p1.text = "22EEC501 – PROFESSIONAL READINESS COURSE"
    p1.alignment = PP_ALIGN.CENTER
    p1.font.name = FONT_FAMILY
    p1.font.size = Pt(15)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_DARK

    p2 = tf_crs.add_paragraph()
    p2.text = "on 18/05/2026 – 03/06/2026"
    p2.alignment = PP_ALIGN.CENTER
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(13)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(180, 0, 0)

    # Project Title Box (Card)
    card_title = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.8), Inches(3.35), Inches(9.73), Inches(1.20))
    card_title.fill.solid()
    card_title.fill.fore_color.rgb = RGBColor(240, 249, 255)
    card_title.line.color.rgb = RGBColor(56, 189, 248)
    card_title.line.width = Pt(1.5)

    tf_title = card_title.text_frame
    tf_title.word_wrap = True
    p_t1 = tf_title.paragraphs[0]
    p_t1.text = "SUMMER INTERNSHIP PROJECT PRESENTATION"
    p_t1.alignment = PP_ALIGN.CENTER
    p_t1.font.name = FONT_FAMILY
    p_t1.font.size = Pt(11)
    p_t1.font.bold = True
    p_t1.font.color.rgb = COLOR_TEAL

    p_t2 = tf_title.add_paragraph()
    p_t2.text = "AI-Based Loan Approval Prediction and Decision Support System"
    p_t2.alignment = PP_ALIGN.CENTER
    p_t2.font.name = FONT_FAMILY
    p_t2.font.size = Pt(19)
    p_t2.font.bold = True
    p_t2.font.color.rgb = COLOR_NAVY

    # Faculty In-Charge (Left)
    b_fac = slide1.shapes.add_textbox(Inches(1.40), Inches(4.80), Inches(5.00), Inches(1.50))
    tf_fac = b_fac.text_frame
    tf_fac.word_wrap = True
    pf1 = tf_fac.paragraphs[0]
    pf1.text = "FACULTY IN-CHARGE"
    pf1.font.name = FONT_FAMILY
    pf1.font.size = Pt(13)
    pf1.font.bold = True
    pf1.font.color.rgb = COLOR_BLACK

    pf2 = tf_fac.add_paragraph()
    pf2.text = "Mr. T. Raghunathan, M.E., (PhD)\nAssistant Professor (SS) / AI&DS\nDr.NGPiTech"
    pf2.font.name = FONT_FAMILY
    pf2.font.size = Pt(12)
    pf2.font.color.rgb = COLOR_DARK

    # Student Details (Right)
    b_stu = slide1.shapes.add_textbox(Inches(6.90), Inches(4.80), Inches(5.80), Inches(1.50))
    tf_stu = b_stu.text_frame
    tf_stu.word_wrap = True
    ps1 = tf_stu.paragraphs[0]
    ps1.text = "PRESENTED BY:"
    ps1.font.name = FONT_FAMILY
    ps1.font.size = Pt(13)
    ps1.font.bold = True
    ps1.font.color.rgb = COLOR_BLACK

    ps2 = tf_stu.add_paragraph()
    ps2.text = "AKHILESH G (Reg No: 710724243007)\nDepartment of Artificial Intelligence & Data Science\nInternship: DLK Software Solutions Pvt. Ltd., Chennai"
    ps2.font.name = FONT_FAMILY
    ps2.font.size = Pt(12)
    ps2.font.color.rgb = COLOR_DARK

    add_footer(slide1, 1)

    # ==========================================
    # SLIDE 2: OUTLINE
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "OUTLINE")

    b_out = slide2.shapes.add_textbox(Inches(1.80), Inches(1.35), Inches(10.0), Inches(5.50))
    tf_out = b_out.text_frame
    tf_out.word_wrap = True

    outline_items = [
        "About the Company",
        "Key Learnings from the Internship",
        "About the Project",
        "System Requirements",
        "Tools and Technology Used",
        "List of Modules with Explanation",
        "Implementation",
        "Output Screenshots",
        "Conclusion",
        "Contributions in the Project",
        "References"
    ]

    for idx, item in enumerate(outline_items):
        p = tf_out.paragraphs[0] if idx == 0 else tf_out.add_paragraph()
        p.text = "●   " + item
        p.font.name = FONT_FAMILY
        p.font.size = Pt(16.5)
        p.font.color.rgb = COLOR_DARK
        p.space_after = Pt(8)

    add_footer(slide2, 2)

    # ==========================================
    # SLIDE 3: ABOUT THE COMPANY
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "ABOUT THE COMPANY")

    if os.path.exists(logo_dlk):
        slide3.shapes.add_picture(logo_dlk, Inches(10.4), Inches(0.40), Inches(2.2), Inches(0.65))

    # Table layout matching sample PPT
    table_shape = slide3.shapes.add_table(7, 2, Inches(1.30), Inches(1.50), Inches(10.73), Inches(5.10))
    table = table_shape.table
    table.columns[0].width = Inches(3.60)
    table.columns[1].width = Inches(7.13)

    table_data = [
        ("COMPANY NAME", "DLK Software Solutions"),
        ("STARTED YEAR", "2012"),
        ("LOCATION", "Vadapalani, Chennai, Tamil Nadu"),
        ("SERVICES OFFERED", "Software Development, Web & Mobile Apps, Data Science & AI, Digital Marketing & Internships"),
        ("INDUSTRY MENTOR NAME", "Mr. Satheesh Kumar"),
        ("DESIGNATION", "Chief Executive Officer"),
        ("DURATION OF INTERN", "18/05/2026 – 03/06/2026 (15 days)")
    ]

    for row_idx, (col0, col1) in enumerate(table_data):
        cell0 = table.cell(row_idx, 0)
        cell1 = table.cell(row_idx, 1)

        cell0.vertical_anchor = MSO_ANCHOR.MIDDLE
        cell1.vertical_anchor = MSO_ANCHOR.MIDDLE

        if row_idx == 0:
            cell0.fill.solid()
            cell0.fill.fore_color.rgb = COLOR_CYAN_BG
            cell1.fill.solid()
            cell1.fill.fore_color.rgb = COLOR_CYAN_BG
        else:
            bg_col = RGBColor(255, 255, 255) if row_idx % 2 == 1 else RGBColor(240, 249, 255)
            cell0.fill.solid()
            cell0.fill.fore_color.rgb = bg_col
            cell1.fill.solid()
            cell1.fill.fore_color.rgb = bg_col

        p0 = cell0.text_frame.paragraphs[0]
        p0.text = col0
        p0.alignment = PP_ALIGN.CENTER if row_idx == 0 else PP_ALIGN.LEFT
        p0.font.name = FONT_FAMILY
        p0.font.size = Pt(13 if row_idx > 0 else 14)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_WHITE if row_idx == 0 else COLOR_NAVY

        p1 = cell1.text_frame.paragraphs[0]
        p1.text = col1
        p1.alignment = PP_ALIGN.CENTER if row_idx == 0 else PP_ALIGN.LEFT
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(13 if row_idx > 0 else 14)
        p1.font.bold = (row_idx == 0)
        p1.font.color.rgb = COLOR_WHITE if row_idx == 0 else COLOR_DARK

    add_footer(slide3, 3)

    # ==========================================
    # SLIDE 4: KEY LEARNINGS FROM THE INTERNSHIP
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "KEY LEARNINGS FROM THE INTERNSHIP")

    col_data_s4 = [
        ("Technical Skills", [
            "Python programming",
            "NumPy & Pandas for data handling",
            "Matplotlib for data visualization",
            "Scikit-learn for Machine Learning",
            "Flask for application integration",
            "Postman for API testing"
        ]),
        ("Machine Learning", [
            "Data preprocessing & cleaning",
            "Classification algorithms (LR, KNN, SVM, Tree)",
            "Model training & parameter tuning",
            "Model evaluation (Accuracy, F1-Score)",
            "Prediction & inference testing"
        ]),
        ("Professional Skills", [
            "Problem-solving & algorithm design",
            "Debugging & code optimization",
            "Time management in 15-day sprint",
            "Systematic project documentation",
            "Academic defense preparation"
        ])
    ]

    card_w = Inches(3.70)
    card_gap = Inches(0.35)
    start_x = Inches(0.85)

    for i, (title, items) in enumerate(col_data_s4):
        cx = start_x + i * (card_w + card_gap)
        card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.50), card_w, Inches(5.10))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_CARD_BORDER
        card.line.width = Pt(1)

        # Header box
        hdr = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.50), card_w, Inches(0.60))
        hdr.fill.solid()
        hdr.fill.fore_color.rgb = COLOR_NAVY
        hdr.line.fill.background()
        p_hdr = hdr.text_frame.paragraphs[0]
        p_hdr.text = title
        p_hdr.alignment = PP_ALIGN.CENTER
        p_hdr.font.name = FONT_FAMILY
        p_hdr.font.size = Pt(16)
        p_hdr.font.bold = True
        p_hdr.font.color.rgb = COLOR_WHITE

        # Text inside card
        tx = slide4.shapes.add_textbox(cx + Inches(0.15), Inches(2.25), card_w - Inches(0.30), Inches(4.20))
        tf = tx.text_frame
        tf.word_wrap = True
        for j, it in enumerate(items):
            p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
            p.text = "• " + it
            p.font.name = FONT_FAMILY
            p.font.size = Pt(14.5)
            p.font.color.rgb = COLOR_DARK
            p.space_after = Pt(10)

    add_footer(slide4, 4)

    # ==========================================
    # SLIDE 5: ABOUT THE PROJECT
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "ABOUT THE PROJECT")

    # Left Column
    b_left5 = slide5.shapes.add_textbox(Inches(0.85), Inches(1.40), Inches(6.80), Inches(5.30))
    tf5_l = b_left5.text_frame
    tf5_l.word_wrap = True

    p = tf5_l.paragraphs[0]
    p.text = "AI-Based Loan Approval Prediction System"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(19)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY
    p.space_after = Pt(8)

    p = tf5_l.add_paragraph()
    p.text = "A Machine Learning-based decision-support system that predicts whether a loan application is likely to be approved or not approved based on applicant demographic and financial records."
    p.font.name = FONT_FAMILY
    p.font.size = Pt(15.5)
    p.font.color.rgb = COLOR_DARK
    p.space_after = Pt(14)

    p = tf5_l.add_paragraph()
    p.text = "Key Objectives"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLACK
    p.space_after = Pt(6)

    objectives = [
        "Prepare loan data through cleaning, encoding, and feature engineering.",
        "Train and compare classification models for loan approval prediction.",
        "Evaluate performance using Accuracy, Precision, Recall, and F1-Score.",
        "Integrate the trained ML pipeline with Flask.",
        "Provide predictions through a simple, user-friendly web interface."
    ]
    for obj in objectives:
        p = tf5_l.add_paragraph()
        p.text = "• " + obj
        p.font.name = FONT_FAMILY
        p.font.size = Pt(14.5)
        p.font.color.rgb = COLOR_DARK
        p.space_after = Pt(6)

    # Right Column: Workflow
    card_wf = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.10), Inches(1.40), Inches(4.40), Inches(5.10))
    card_wf.fill.solid()
    card_wf.fill.fore_color.rgb = RGBColor(248, 250, 252)
    card_wf.line.color.rgb = COLOR_CARD_BORDER

    # Workflow title
    hdr_wf = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.10), Inches(1.40), Inches(4.40), Inches(0.55))
    hdr_wf.fill.solid()
    hdr_wf.fill.fore_color.rgb = COLOR_TEAL
    hdr_wf.line.fill.background()
    p_hwf = hdr_wf.text_frame.paragraphs[0]
    p_hwf.text = "Project Workflow"
    p_hwf.alignment = PP_ALIGN.CENTER
    p_hwf.font.name = FONT_FAMILY
    p_hwf.font.size = Pt(16)
    p_hwf.font.bold = True
    p_hwf.font.color.rgb = COLOR_WHITE

    wf_steps = [
        ("1", "Data Collection & Inspection", "Kaggle benchmark (614 records)"),
        ("2", "Data Preprocessing", "Median/Mode imputation & scaling"),
        ("3", "Feature Engineering", "Total Income & Income-to-Loan ratio"),
        ("4", "Model Training", "Logistic Regression, KNN, SVM, Tree"),
        ("5", "Model Evaluation", "Selected Best Model by F1-Score"),
        ("6", "Flask Integration & Web UI", "Real-time decision support serving")
    ]

    step_y = Inches(2.15)
    for num, title, desc in wf_steps:
        # circle
        circle = slide5.shapes.add_shape(MSO_SHAPE.OVAL, Inches(8.35), step_y, Inches(0.40), Inches(0.40))
        circle.fill.solid()
        circle.fill.fore_color.rgb = COLOR_NAVY
        circle.line.fill.background()
        pc = circle.text_frame.paragraphs[0]
        pc.text = num
        pc.alignment = PP_ALIGN.CENTER
        pc.font.name = FONT_FAMILY
        pc.font.size = Pt(13)
        pc.font.bold = True
        pc.font.color.rgb = COLOR_WHITE

        # step text
        st_box = slide5.shapes.add_textbox(Inches(8.85), step_y - Inches(0.05), Inches(3.50), Inches(0.45))
        tf_s = st_box.text_frame
        tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
        p_st = tf_s.paragraphs[0]
        p_st.text = title
        p_st.font.name = FONT_FAMILY
        p_st.font.size = Pt(12.5)
        p_st.font.bold = True
        p_st.font.color.rgb = COLOR_BLACK

        p_sd = tf_s.add_paragraph()
        p_sd.text = desc
        p_sd.font.name = FONT_FAMILY
        p_sd.font.size = Pt(10.5)
        p_sd.font.color.rgb = COLOR_MUTED

        step_y += Inches(0.70)

    add_footer(slide5, 5)

    # ==========================================
    # SLIDE 6: SYSTEM REQUIREMENTS
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "SYSTEM REQUIREMENTS")

    # Left Card: Software
    card_sw = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.20), Inches(1.50), Inches(5.10), Inches(5.10))
    card_sw.fill.solid()
    card_sw.fill.fore_color.rgb = COLOR_CARD_BG
    card_sw.line.color.rgb = COLOR_CARD_BORDER

    hdr_sw = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.20), Inches(1.50), Inches(5.10), Inches(0.60))
    hdr_sw.fill.solid()
    hdr_sw.fill.fore_color.rgb = COLOR_NAVY
    p_hsw = hdr_sw.text_frame.paragraphs[0]
    p_hsw.text = "Software Requirements"
    p_hsw.alignment = PP_ALIGN.CENTER
    p_hsw.font.name = FONT_FAMILY
    p_hsw.font.size = Pt(16)
    p_hsw.font.bold = True
    p_hsw.font.color.rgb = COLOR_WHITE

    tx_sw = slide6.shapes.add_textbox(Inches(1.50), Inches(2.30), Inches(4.50), Inches(4.0))
    tf_sw = tx_sw.text_frame
    sw_items = [
        "Python 3.x",
        "Visual Studio Code",
        "Pandas & NumPy",
        "Scikit-learn",
        "Flask Framework",
        "HTML5 & CSS3",
        "Web Browser (Edge / Chrome)",
        "Postman (API Testing)"
    ]
    for idx, item in enumerate(sw_items):
        p = tf_sw.paragraphs[0] if idx == 0 else tf_sw.add_paragraph()
        p.text = "• " + item
        p.font.name = FONT_FAMILY
        p.font.size = Pt(15.5)
        p.font.color.rgb = COLOR_DARK
        p.space_after = Pt(11)

    # Right Card: Development Environment
    card_de = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.03), Inches(1.50), Inches(5.10), Inches(5.10))
    card_de.fill.solid()
    card_de.fill.fore_color.rgb = COLOR_CARD_BG
    card_de.line.color.rgb = COLOR_CARD_BORDER

    hdr_de = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.03), Inches(1.50), Inches(5.10), Inches(0.60))
    hdr_de.fill.solid()
    hdr_de.fill.fore_color.rgb = COLOR_TEAL
    p_hde = hdr_de.text_frame.paragraphs[0]
    p_hde.text = "Development Environment"
    p_hde.alignment = PP_ALIGN.CENTER
    p_hde.font.name = FONT_FAMILY
    p_hde.font.size = Pt(16)
    p_hde.font.bold = True
    p_hde.font.color.rgb = COLOR_WHITE

    tx_de = slide6.shapes.add_textbox(Inches(7.33), Inches(2.30), Inches(4.50), Inches(4.0))
    tf_de = tx_de.text_frame
    de_items = [
        "Python Virtual Environment",
        "Flask WSGI Web Server",
        "Trained Model Pipeline (best_model.pkl)",
        "Preprocessing Pipeline (preprocessor.pkl)",
        "Web-Based Interactive Prediction Interface",
        "Dataset Benchmark (loan_data.csv)",
        "Matplotlib & Seaborn Chart Generator"
    ]
    for idx, item in enumerate(de_items):
        p = tf_de.paragraphs[0] if idx == 0 else tf_de.add_paragraph()
        p.text = "• " + item
        p.font.name = FONT_FAMILY
        p.font.size = Pt(15.5)
        p.font.color.rgb = COLOR_DARK
        p.space_after = Pt(11)

    add_footer(slide6, 6)

    # ==========================================
    # SLIDE 7: TOOLS AND TECHNOLOGIES USED
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "TOOLS AND TECHNOLOGIES USED")

    cols_s7 = [
        ("Data Handling", [
            ("Python", "Core programming language"),
            ("NumPy", "Numerical operations & vector math"),
            ("Pandas", "Data cleaning, manipulation, and CSV handling")
        ]),
        ("Machine Learning", [
            ("Scikit-learn", "Model training, pipeline, and evaluation"),
            ("Classification Algorithms", "Logistic Regression, KNN, SVM, Decision Tree")
        ]),
        ("Deployment", [
            ("Flask", "Connects trained model to web application"),
            ("HTML & CSS", "Responsive LoanAI frontend interface")
        ]),
        ("Development", [
            ("Visual Studio Code", "Project scripting and debugging environment"),
            ("Postman", "REST API endpoint verification & testing")
        ])
    ]

    card7_w = Inches(2.78)
    card7_gap = Inches(0.24)
    start7_x = Inches(0.85)

    for i, (hdr_text, items) in enumerate(cols_s7):
        cx = start7_x + i * (card7_w + card7_gap)
        # Background card
        card = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.50), card7_w, Inches(5.10))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_CARD_BORDER

        # Header box
        hdr = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.50), card7_w, Inches(0.60))
        hdr.fill.solid()
        hdr.fill.fore_color.rgb = COLOR_CYAN_BG if i % 2 == 0 else COLOR_TEAL
        p_hdr = hdr.text_frame.paragraphs[0]
        p_hdr.text = hdr_text
        p_hdr.alignment = PP_ALIGN.CENTER
        p_hdr.font.name = FONT_FAMILY
        p_hdr.font.size = Pt(15)
        p_hdr.font.bold = True
        p_hdr.font.color.rgb = COLOR_WHITE

        # Content
        tx = slide7.shapes.add_textbox(cx + Inches(0.12), Inches(2.25), card7_w - Inches(0.24), Inches(4.20))
        tf = tx.text_frame
        tf.word_wrap = True
        for j, (tool, desc) in enumerate(items):
            p1 = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
            p1.text = tool
            p1.font.name = FONT_FAMILY
            p1.font.size = Pt(15)
            p1.font.bold = True
            p1.font.color.rgb = COLOR_BLACK

            p2 = tf.add_paragraph()
            p2.text = desc
            p2.font.name = FONT_FAMILY
            p2.font.size = Pt(12)
            p2.font.color.rgb = COLOR_MUTED
            p2.space_after = Pt(14)

    add_footer(slide7, 7)

    # ==========================================
    # SLIDE 8: LIST OF MODULES WITH EXPLANATION
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "LIST OF MODULES WITH EXPLANATION")

    modules = [
        ("1", "Data Collection & Preprocessing", "Loads Kaggle loan benchmark dataset (614 rows). Handles missing values via median and mode imputation without data leakage."),
        ("2", "Feature Preparation & Engineering", "Converts categorical strings into numerical binaries. Engineers TotalIncome and Income_to_Loan_Ratio to capture true borrower repayment capacity."),
        ("3", "Model Training Module", "Trains four distinct supervised classification algorithms (Logistic Regression, KNN, SVM, Decision Tree) on an 80/20 stratified split."),
        ("4", "Model Evaluation Module", "Computes comprehensive evaluation metrics: Accuracy, Precision, Recall, F1-Score, and Confusion Matrix. Selects Logistic Regression based on optimal F1-score (90.81%)."),
        ("5", "Prediction & Inference Module", "Accepts applicant demographic and credit parameters in real-time and applies the saved ColumnTransformer pipeline to compute approval probability."),
        ("6", "Flask Integration & Dashboard", "Deploys the trained ML engine as an interactive web system with live validation, Indian Rupee (₹) formatting, and PDF decision reports.")
    ]

    m_w = Inches(3.70)
    m_h = Inches(2.40)
    m_gap_x = Inches(0.35)
    m_gap_y = Inches(0.30)
    top_y = Inches(1.50)

    for idx, (num, title, desc) in enumerate(modules):
        col_idx = idx % 3
        row_idx = idx // 3

        cx = start_x + col_idx * (m_w + m_gap_x)
        cy = top_y + row_idx * (m_h + m_gap_y)

        # Card
        card = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, m_w, m_h)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_CARD_BORDER

        # Number circle
        circle = slide8.shapes.add_shape(MSO_SHAPE.OVAL, cx + Inches(0.18), cy + Inches(0.18), Inches(0.45), Inches(0.45))
        circle.fill.solid()
        circle.fill.fore_color.rgb = COLOR_NAVY
        circle.line.fill.background()
        pc = circle.text_frame.paragraphs[0]
        pc.text = num
        pc.alignment = PP_ALIGN.CENTER
        pc.font.name = FONT_FAMILY
        pc.font.size = Pt(14)
        pc.font.bold = True
        pc.font.color.rgb = COLOR_WHITE

        # Title
        tbox = slide8.shapes.add_textbox(cx + Inches(0.72), cy + Inches(0.12), m_w - Inches(0.85), Inches(0.55))
        tf_t = tbox.text_frame
        tf_t.word_wrap = True
        pt = tf_t.paragraphs[0]
        pt.text = title
        pt.font.name = FONT_FAMILY
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_BLACK

        # Description
        dbox = slide8.shapes.add_textbox(cx + Inches(0.18), cy + Inches(0.72), m_w - Inches(0.36), Inches(1.55))
        tf_d = dbox.text_frame
        tf_d.word_wrap = True
        pd = tf_d.paragraphs[0]
        pd.text = desc
        pd.font.name = FONT_FAMILY
        pd.font.size = Pt(12)
        pd.font.color.rgb = COLOR_DARK

    add_footer(slide8, 8)

    # ==========================================
    # SLIDE 9: IMPLEMENTATION
    # ==========================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "IMPLEMENTATION")

    # Left Column: Stages & Testing
    b_left9 = slide9.shapes.add_textbox(Inches(0.85), Inches(1.40), Inches(6.00), Inches(5.30))
    tf9 = b_left9.text_frame
    tf9.word_wrap = True

    p = tf9.paragraphs[0]
    p.text = "Main Implementation Stages"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLACK
    p.space_after = Pt(6)

    stages = [
        "1. Data collection & preprocessing (SimpleImputer, StandardScaler)",
        "2. Feature engineering (TotalIncome, Income_to_Loan_Ratio)",
        "3. Classification model training (LR, KNN, SVM, Decision Tree)",
        "4. Model evaluation and selection based on F1-score",
        "5. Flask application integration and API routing",
        "6. Loan approval prediction and decision report generation"
    ]
    for st in stages:
        p = tf9.add_paragraph()
        p.text = st
        p.font.name = FONT_FAMILY
        p.font.size = Pt(13)
        p.font.color.rgb = COLOR_DARK
        p.space_after = Pt(4)

    p = tf9.add_paragraph()
    p.text = "Testing & Validation"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLACK
    p.space_before = Pt(8)
    p.space_after = Pt(6)

    tests = [
        "• Tested the model using actual applicant input scenarios.",
        "• Verified prediction responses on holdout test set (123 samples).",
        "• Tested positive (approved) and negative (rejected) cases.",
        "• Verified connection between ML model and Flask frontend."
    ]
    for ts in tests:
        p = tf9.add_paragraph()
        p.text = ts
        p.font.name = FONT_FAMILY
        p.font.size = Pt(13)
        p.font.color.rgb = COLOR_DARK
        p.space_after = Pt(4)

    # Workflow summary banner
    wf_box = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.85), Inches(6.15), Inches(5.90), Inches(0.45))
    wf_box.fill.solid()
    wf_box.fill.fore_color.rgb = RGBColor(240, 249, 255)
    wf_box.line.color.rgb = COLOR_TEAL
    p_wf = wf_box.text_frame.paragraphs[0]
    p_wf.text = "Workflow: Data → Preprocessing → Training → Evaluation → Flask → Prediction"
    p_wf.alignment = PP_ALIGN.CENTER
    p_wf.font.name = FONT_FAMILY
    p_wf.font.size = Pt(11)
    p_wf.font.bold = True
    p_wf.font.color.rgb = COLOR_NAVY

    # Right Column: Implementation picture
    if os.path.exists(img_code):
        slide9.shapes.add_picture(img_code, Inches(7.15), Inches(1.45), Inches(5.35), Inches(4.90))

    add_footer(slide9, 9)

    # ==========================================
    # SLIDE 10: OUTPUT SCREENSHOTS (Form Input)
    # ==========================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "OUTPUT SCREENSHOTS")

    # Display clean LoanAI Form Screenshot
    if os.path.exists(img_form):
        slide10.shapes.add_picture(img_form, Inches(2.20), Inches(1.35), Inches(8.93), Inches(5.20))

    # Caption
    b_cap10 = slide10.shapes.add_textbox(Inches(1.0), Inches(6.65), Inches(11.33), Inches(0.40))
    tf_c10 = b_cap10.text_frame
    p_c10 = tf_c10.paragraphs[0]
    p_c10.text = "Figure 10.1: LoanAI Interactive Application Form — Input Parameters & Live Preview (with Indian Rupee ₹ Formatting)"
    p_c10.alignment = PP_ALIGN.CENTER
    p_c10.font.name = FONT_FAMILY
    p_c10.font.size = Pt(13)
    p_c10.font.italic = True
    p_c10.font.color.rgb = COLOR_DARK

    add_footer(slide10, 10)

    # ==========================================
    # SLIDE 11: OUTPUT SCREENSHOTS (Prediction Results)
    # ==========================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "OUTPUT SCREENSHOTS")

    # Left: Approved case
    if os.path.exists(img_app):
        slide11.shapes.add_picture(img_app, Inches(0.85), Inches(1.60), Inches(5.60), Inches(4.50))

    # Title for Approved
    b_t_app = slide11.shapes.add_textbox(Inches(0.85), Inches(1.25), Inches(5.60), Inches(0.35))
    tf_ta = b_t_app.text_frame
    pt_a = tf_ta.paragraphs[0]
    pt_a.text = "Approved Case: Credit History = 1.0 (Likely Approved — 81.3%)"
    pt_a.alignment = PP_ALIGN.CENTER
    pt_a.font.name = FONT_FAMILY
    pt_a.font.size = Pt(13.5)
    pt_a.font.bold = True
    pt_a.font.color.rgb = COLOR_GREEN

    # Right: Rejected case
    if os.path.exists(img_rej):
        slide11.shapes.add_picture(img_rej, Inches(6.88), Inches(1.60), Inches(5.60), Inches(4.50))

    # Title for Rejected
    b_t_rej = slide11.shapes.add_textbox(Inches(6.88), Inches(1.25), Inches(5.60), Inches(0.35))
    tf_tr = b_t_rej.text_frame
    pt_r = tf_tr.paragraphs[0]
    pt_r.text = "Rejected Case: Credit History = 0.0 (Likely Not Approved — 93.2%)"
    pt_r.alignment = PP_ALIGN.CENTER
    pt_r.font.name = FONT_FAMILY
    pt_r.font.size = Pt(13.5)
    pt_r.font.bold = True
    pt_r.font.color.rgb = COLOR_RED

    # Disclaimer Note at bottom
    b_disc = slide11.shapes.add_textbox(Inches(1.0), Inches(6.25), Inches(11.33), Inches(0.40))
    tf_disc = b_disc.text_frame
    p_disc = tf_disc.paragraphs[0]
    p_disc.text = "Note: The system provides a Machine Learning-based prediction and does not guarantee the final decision of a bank."
    p_disc.alignment = PP_ALIGN.CENTER
    p_disc.font.name = FONT_FAMILY
    p_disc.font.size = Pt(13)
    p_disc.font.bold = True
    p_disc.font.color.rgb = COLOR_MUTED

    add_footer(slide11, 11)

    # ==========================================
    # SLIDE 12: CONCLUSION
    # ==========================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "CONCLUSION")

    b_con = slide12.shapes.add_textbox(Inches(1.30), Inches(1.65), Inches(10.73), Inches(5.0))
    tf_con = b_con.text_frame
    tf_con.word_wrap = True

    conclusions = [
        "The project successfully developed an AI-based loan approval prediction and decision-support system.",
        "The system processes demographic and financial applicant data to assist underwriting teams in risk evaluation.",
        "Multiple supervised classification algorithms were evaluated, with Logistic Regression achieving the optimal F1-score of 90.81% and 86.18% accuracy.",
        "Credit history compliance was confirmed as the single most critical statistical feature influencing sanction decisions.",
        "The trained machine learning pipeline was seamlessly integrated into a responsive Flask web application.",
        "The 15-day internship at DLK Software Solutions significantly strengthened practical competencies in Machine Learning, Flask API deployment, and end-to-end data science workflows."
    ]

    for idx, c in enumerate(conclusions):
        p = tf_con.paragraphs[0] if idx == 0 else tf_con.add_paragraph()
        p.text = "●   " + c
        p.font.name = FONT_FAMILY
        p.font.size = Pt(16.5)
        p.font.color.rgb = COLOR_DARK
        p.space_after = Pt(14)

    add_footer(slide12, 12)

    # ==========================================
    # SLIDE 13: CONTRIBUTIONS IN THE PROJECT
    # ==========================================
    slide13 = prs.slides.add_slide(blank_layout)
    add_header(slide13, "CONTRIBUTIONS IN THE PROJECT")

    b_cnt = slide13.shapes.add_textbox(Inches(1.30), Inches(1.65), Inches(10.73), Inches(5.0))
    tf_cnt = b_cnt.text_frame
    tf_cnt.word_wrap = True

    contributions = [
        "Collected, inspected, and preprocessed the Kaggle loan prediction benchmark dataset (614 records).",
        "Engineered domain-specific features: Total Income and Income-to-Loan Ratio to capture borrower capacity.",
        "Built a robust preprocessing pipeline using SimpleImputer, StandardScaler, and OneHotEncoder without data leakage.",
        "Trained and evaluated Logistic Regression, KNN, SVM, and Decision Tree classification algorithms.",
        "Serialized the production model and ColumnTransformer pipeline using Joblib.",
        "Developed and integrated a Flask web server to serve real-time predictions with Indian Rupee (₹) formatting.",
        "Conducted end-to-end testing across 14 test scenarios and verified input validation safeguards.",
        "Prepared comprehensive academic documentation and presentation materials for college viva voce review."
    ]

    for idx, ct in enumerate(contributions):
        p = tf_cnt.paragraphs[0] if idx == 0 else tf_cnt.add_paragraph()
        p.text = "●   " + ct
        p.font.name = FONT_FAMILY
        p.font.size = Pt(15.5)
        p.font.color.rgb = COLOR_DARK
        p.space_after = Pt(10)

    add_footer(slide13, 13)

    # ==========================================
    # SLIDE 14: REFERENCES
    # ==========================================
    slide14 = prs.slides.add_slide(blank_layout)
    add_header(slide14, "REFERENCES")

    b_ref = slide14.shapes.add_textbox(Inches(1.30), Inches(1.70), Inches(10.73), Inches(4.80))
    tf_ref = b_ref.text_frame
    tf_ref.word_wrap = True

    references = [
        "Python Documentation – https://docs.python.org/3/",
        "NumPy Documentation – https://numpy.org/doc/",
        "Pandas Documentation – https://pandas.pydata.org/docs/",
        "Matplotlib Documentation – https://matplotlib.org/stable/",
        "Scikit-Learn Documentation – https://scikit-learn.org/stable/",
        "Flask Documentation – https://flask.palletsprojects.com/",
        "Postman Documentation – https://learning.postman.com/docs/",
        "Kaggle / Analytics Vidhya – Loan Prediction Practice Problem Benchmark Dataset"
    ]

    for idx, ref in enumerate(references):
        p = tf_ref.paragraphs[0] if idx == 0 else tf_ref.add_paragraph()
        p.text = "●   " + ref
        p.font.name = FONT_FAMILY
        p.font.size = Pt(16.5)
        p.font.color.rgb = COLOR_DARK
        p.space_after = Pt(12)

    add_footer(slide14, 14)

    # ==========================================
    # SLIDE 15: THANK YOU
    # ==========================================
    slide15 = prs.slides.add_slide(blank_layout)
    if os.path.exists(img_thanks):
        slide15.shapes.add_picture(img_thanks, Inches(0), Inches(0), Inches(13.333), Inches(7.5))

    out_path1 = r'C:\Users\Dell\.gemini\antigravity\scratch\AI_Loan_Prediction\Akhilesh_AI_Loan_Prediction_Internship_Presentation.pptx'
    out_path2 = r'C:\Users\Dell\Downloads\Akhilesh_AI_Loan_Prediction_Internship_Presentation.pptx'

    prs.save(out_path1)
    prs.save(out_path2)
    print(f"Successfully generated PowerPoint presentations:")
    print(f"1. {out_path1} ({os.path.getsize(out_path1)} bytes)")
    print(f"2. {out_path2} ({os.path.getsize(out_path2)} bytes)")

if __name__ == '__main__':
    build_presentation()
