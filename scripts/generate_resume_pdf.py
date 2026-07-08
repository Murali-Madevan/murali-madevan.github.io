"""Generate a one-page professional resume PDF for GitHub Pages."""

from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "resume.pdf"


class ResumePDF(FPDF):
    def __init__(self) -> None:
        super().__init__()
        self.set_auto_page_break(auto=False)
        self.set_margins(14, 12, 14)

    def section_title(self, title: str) -> None:
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(15, 23, 42)
        self.set_fill_color(241, 245, 249)
        self.cell(0, 6, f"  {title.upper()}", new_x="LMARGIN", new_y="NEXT", fill=True)
        self.ln(1.5)

    def body_text(self, text: str, size: float = 8.5) -> None:
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", size)
        self.set_text_color(30, 41, 59)
        self.multi_cell(0, 3.8, text)
        self.ln(0.5)

    def bullet(self, text: str) -> None:
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(30, 41, 59)
        self.multi_cell(0, 3.8, f"  -  {text}")


def build_pdf() -> None:
    pdf = ResumePDF()
    pdf.add_page()

    # Header
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 7, "Murali Madevan", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 8.5)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(
        0,
        4,
        "+91 8438593087  |  muralimadevan82@gmail.com  |  linkedin.com/in/murali-madevan  |  Bengaluru, Karnataka",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(2)
    pdf.set_x(pdf.l_margin)
    pdf.set_draw_color(20, 184, 166)
    pdf.set_line_width(0.4)
    pdf.line(14, pdf.get_y(), 196, pdf.get_y())
    pdf.ln(3)

    # Executive Summary
    pdf.section_title("Executive Summary")
    pdf.body_text(
        "AI/ML Engineer skilled in building scalable Gen AI and deep learning solutions. Computer Science graduate "
        "with expertise in Python, LangChain, RAG, TensorFlow, and SQL. Experienced in engineering intelligent "
        "applications, including a live Gen AI platform and a medical diagnosis system. Published peer-reviewed "
        "researcher (IJRASET, 2025) with a 92%-accuracy deep learning model."
    )

    # Technical Skills
    pdf.section_title("Technical Skills")
    skills = [
        ("Programming Languages", "Python, SQL"),
        ("AI / ML & Deep Learning", "Scikit-learn, TensorFlow, Keras, CNN, Deep Learning, Model Tuning"),
        ("NLP & Generative AI", "LangChain, RAG, OpenAI APIs, Prompt Engineering, NER, Text Classification, TF-IDF"),
        ("Data & Databases", "Pandas, NumPy, EDA, Feature Engineering, MySQL, PostgreSQL, SQLAlchemy ORM"),
        ("Cloud & DevOps", "AWS SageMaker (concepts), Git, GitHub, Jira, Agile/Scrum"),
        ("Frameworks & Visualization", "Flask, Streamlit, REST APIs, Power BI, Matplotlib, Seaborn"),
    ]
    for label, value in skills:
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(30, 41, 59)
        pdf.multi_cell(0, 3.8, f"{label}: {value}")
    pdf.ln(0.5)

    # Experience
    pdf.section_title("Experience")
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 4, "Qspiders Software Testing & Solutions", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "I", 8.5)
    pdf.set_text_color(20, 184, 166)
    pdf.cell(
        0,
        4,
        "Python Developer Intern (Onsite)  |  Nov 2025 - May 2026  |  Bengaluru, Karnataka",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(0.5)
    for item in [
        "Engineered reproducible ETL pipelines using Python, Pandas, and SQLAlchemy ORM for efficient data collection and transformation.",
        "Cleaned and processed large-scale, multi-source datasets, cutting manual data-handling effort by ~40%.",
        "Performed EDA and statistical analysis to uncover actionable business insights; built Power BI dashboards for stakeholders.",
        "Maintained Git repositories, authored technical documentation, and managed Agile/Scrum sprints via Jira.",
    ]:
        pdf.bullet(item)
    pdf.ln(0.5)

    # Projects
    pdf.section_title("Projects")
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 4, "AI Resume Intelligence Engine", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 3.5, "Python, LangChain, RAG, OpenAI APIs, Streamlit  |  Nov 2025 - Dec 2025", new_x="LMARGIN", new_y="NEXT")
    for item in [
        "Built an end-to-end Gen AI application using LangChain and RAG for intelligent document retrieval and semantic search.",
        "Implemented TF-IDF vectorization and OpenAI LLM APIs for context-aware resume analysis; validated across 100+ test cases.",
        "Deployed live on Streamlit Cloud with full architecture documentation and runbooks.",
    ]:
        pdf.bullet(item)

    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 4, "Skin Cancer Detection Portal", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 3.5, "HTML, CSS, JavaScript, MySQL, TensorFlow  |  Jan 2025 - May 2025", new_x="LMARGIN", new_y="NEXT")
    for item in [
        "Achieved 92% model accuracy in early-stage skin cancer detection; reduced false positives by 15%.",
        "Optimized MySQL queries for patient record management, improving data retrieval time by 35%.",
    ]:
        pdf.bullet(item)
    pdf.ln(0.5)

    # Achievements & Education (compact row-style blocks)
    pdf.section_title("Achievements & Education")
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 3.8, "Research Publication (IJRASET, March 2025)", new_x="LMARGIN", new_y="NEXT")
    pdf.body_text(
        "Published and presented \"Doctor-Patient Portal with Skin Cancer Prediction Using Deep Learning\" at an "
        "International Conference on Recent Trends in Computing & Communication Technologies.",
        size=8,
    )
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 3.8, "Smart India Hackathon (Sep 2023) - Adhiyamaan College of Engineering", new_x="LMARGIN", new_y="NEXT")
    pdf.body_text("Developed a prototype solution focusing on problem-solving and application development.", size=8)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 3.8, "Adhiyamaan College of Engineering, Hosur, Tamil Nadu", new_x="LMARGIN", new_y="NEXT")
    pdf.body_text("B.E. Computer Science and Engineering  |  CGPA: 7.0/10  |  Sep 2021 - May 2025", size=8)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUTPUT))
    print(f"Wrote {OUTPUT} ({pdf.page_no()} page(s))")


if __name__ == "__main__":
    build_pdf()
