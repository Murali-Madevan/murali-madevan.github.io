"""Generate assets/resume.pdf for GitHub Pages download button."""

from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "resume.pdf"


def build_pdf() -> None:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 10, "Murali Madevan", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 7, "Fresher | Machine Learning Engineer | Python Developer", ln=True)
    pdf.cell(0, 7, "Bengaluru, Karnataka, India", ln=True)
    pdf.cell(0, 7, "muralimadevan82@gmail.com | github.com/Murali-Madevan", ln=True)
    pdf.ln(6)

    sections = [
        (
            "PROFESSIONAL SUMMARY",
            "Fresher ML engineer with 6 months of internship experience at Test Yantra. "
            "Skilled in Python, FastAPI, TensorFlow, NLP, and building AI-powered web applications. "
            "Strong project portfolio in deep learning, resume analysis, and production-style backend development.",
        ),
        (
            "EXPERIENCE",
            "- Test Yantra Software Solutions | Intern (6 Months) | Bengaluru\n"
            "  Software development internship with focus on Python, AI/ML workflows, Git, and agile delivery.\n\n"
            "- Academic & Personal Projects\n"
            "  Built AI Resume Matcher (FastAPI, Docker, CI/CD) and Skin Cancer Prediction (Flask, TensorFlow).",
        ),
        (
            "TECHNICAL SKILLS",
            "Languages: Python, JavaScript, SQL, HTML/CSS\n"
            "ML/AI: TensorFlow, scikit-learn, NLP, Deep Learning, Gemini API\n"
            "Backend: FastAPI, Flask, REST APIs, Pydantic\n"
            "Tools: Git, GitHub Actions, Docker, MySQL, Streamlit",
        ),
        (
            "PROJECTS",
            "- AI Resume Matcher: NLP scoring, skill-gap analysis, Gemini integration, Docker & CI/CD\n"
            "- Skin Cancer Prediction: CNN-based detection portal with Flask and MySQL\n"
            "- Personal Portfolio: Responsive GitHub Pages site (HTML, CSS, JavaScript)",
        ),
        (
            "ACHIEVEMENTS",
            "- Research publication (IJRASET, 2025) on skin cancer prediction using deep learning\n"
            "- Smart India Hackathon participant (2023)\n"
            "- Production-grade refactor of AI Resume Matcher with tests and documentation",
        ),
    ]

    for title, body in sections:
        pdf.set_font("Arial", "B", 12)
        pdf.set_text_color(0, 51, 102)
        pdf.cell(0, 8, title, ln=True)
        pdf.set_font("Arial", "", 10)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 5, body)
        pdf.ln(3)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUTPUT))
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
