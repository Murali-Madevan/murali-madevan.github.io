/**
 * Murali Madevan — Portfolio Scripts
 * Vanilla JS: nav, scroll animations, modals, contact form
 */

(function () {
  "use strict";

  /* ---- DOM refs ---- */
  const header = document.getElementById("header");
  const navToggle = document.getElementById("nav-toggle");
  const navMenu = document.getElementById("nav-menu");
  const navLinks = document.querySelectorAll(".nav__link");
  const fadeElements = document.querySelectorAll(".fade-up");
  const statNumber = document.querySelector(".stat__number");
  const modal = document.getElementById("project-modal");
  const modalTitle = document.getElementById("modal-title");
  const modalSubtitle = document.getElementById("modal-subtitle");
  const modalBody = document.getElementById("modal-body");
  const modalLinks = document.getElementById("modal-links");
  const contactForm = document.getElementById("contact-form");
  const yearEl = document.getElementById("year");

  /* ---- Project modal data ---- */
  const projects = {
    "resume-matcher": {
      title: "AI Resume Matcher",
      subtitle: "FastAPI · Streamlit · scikit-learn · Gemini · Docker",
      body: `
        <p>Production-grade resume analysis platform that scores resume–job-description fit using TF-IDF NLP, skill-gap detection, and optional Google Gemini AI insights.</p>
        <ul>
          <li>Layered FastAPI architecture with Pydantic validation and structured logging</li>
          <li>Streamlit UI sharing the same service layer as the REST API</li>
          <li>Docker multi-stage builds, docker-compose, and GitHub Actions CI/CD</li>
          <li>Features: AI resume rewriting, PDF export, cover letter points, recruiter view</li>
        </ul>
      `,
      links: [
        { label: "GitHub", url: "https://github.com/muralimadevan82-source/ai-resume-matcher" },
      ],
    },
    "skin-cancer": {
      title: "Skin Cancer Prediction Portal",
      subtitle: "Flask · TensorFlow · Bootstrap · MySQL",
      body: `
        <p>AI-powered web portal for early-stage skin cancer detection using convolutional neural networks (CNNs) built with TensorFlow.</p>
        <ul>
          <li>Achieved ~92% classification accuracy on validation data</li>
          <li>Responsive Bootstrap frontend with image upload and prediction results</li>
          <li>MySQL backend for patient record management and query optimization</li>
          <li>Research published in IJRASET Journal (2025)</li>
        </ul>
      `,
      links: [
        { label: "GitHub", url: "https://github.com/Murali-Madevan" },
      ],
    },
    portfolio: {
      title: "Personal Portfolio Website",
      subtitle: "HTML · CSS · JavaScript",
      body: `
        <p>This single-page portfolio website — dark theme, scroll animations, responsive design, and zero build step for easy GitHub Pages hosting.</p>
        <ul>
          <li>Sticky navigation with smooth scroll and active section highlighting</li>
          <li>Intersection Observer for fade-in animations on scroll</li>
          <li>Mobile hamburger menu and project detail modals</li>
          <li>Hosted at GitHub Pages with no frameworks required</li>
        </ul>
      `,
      links: [
        { label: "Live Site", url: "https://Murali-Madevan.github.io/" },
        { label: "Source", url: "https://github.com/Murali-Madevan/Murali-Madevan.github.io" },
      ],
    },
  };

  /* ---- Init ---- */
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---- Mobile nav toggle ---- */
  navToggle?.addEventListener("click", () => {
    navToggle.classList.toggle("active");
    navMenu.classList.toggle("active");
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      navToggle?.classList.remove("active");
      navMenu?.classList.remove("active");
    });
  });

  /* ---- Sticky header shadow ---- */
  window.addEventListener("scroll", () => {
    header?.classList.toggle("scrolled", window.scrollY > 50);
    updateActiveNav();
  });

  /* ---- Active nav link on scroll ---- */
  const sections = document.querySelectorAll("section[id]");

  function updateActiveNav() {
    const scrollY = window.scrollY + 120;
    sections.forEach((section) => {
      const id = section.getAttribute("id");
      const top = section.offsetTop;
      const height = section.offsetHeight;
      if (scrollY >= top && scrollY < top + height) {
        navLinks.forEach((link) => {
          link.classList.toggle("active", link.getAttribute("href") === `#${id}`);
        });
      }
    });
  }

  /* ---- Scroll fade-in animations ---- */
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
  );

  fadeElements.forEach((el) => observer.observe(el));

  /* ---- Counter animation (years of experience) ---- */
  function animateCounter(el) {
    const target = parseInt(el.dataset.target, 10);
    const duration = 1500;
    const start = performance.now();

    function step(now) {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.floor(eased * target);
      if (progress < 1) requestAnimationFrame(step);
      else el.textContent = target;
    }

    requestAnimationFrame(step);
  }

  if (statNumber) {
    const counterObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );
    counterObserver.observe(statNumber);
  }

  /* ---- Project modals ---- */
  document.querySelectorAll(".project-card").forEach((card) => {
    const id = card.dataset.project;
    const btn = card.querySelector(".project-card__link");
    btn?.addEventListener("click", () => openModal(id));
  });

  function openModal(id) {
    const project = projects[id];
    if (!project || !modal) return;

    modalTitle.textContent = project.title;
    modalSubtitle.textContent = project.subtitle;
    modalBody.innerHTML = project.body;
    modalLinks.innerHTML = project.links
      .map(
        (l) =>
          `<a href="${l.url}" target="_blank" rel="noopener">${l.label}</a>`
      )
      .join("");

    modal.classList.add("active");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closeModal() {
    modal?.classList.remove("active");
    modal?.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  modal?.querySelectorAll("[data-close]").forEach((el) => {
    el.addEventListener("click", closeModal);
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
  });

  /* ---- Contact form → mailto ---- */
  contactForm?.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = new FormData(contactForm);
    const name = data.get("name");
    const email = data.get("email");
    const message = data.get("message");
    const subject = encodeURIComponent(`Portfolio Contact from ${name}`);
    const body = encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\n${message}`);
    window.location.href = `mailto:muralimadevan82@gmail.com?subject=${subject}&body=${body}`;
  });
})();
