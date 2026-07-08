# Murali Madevan — Portfolio

Personal portfolio website hosted on GitHub Pages.

**Live:** [Murali-Madevan.github.io](https://Murali-Madevan.github.io/)

## Structure

```
├── index.html      # Main page
├── style.css       # Styles
├── script.js       # Interactions
└── assets/         # Images, resume PDF
```

## Local preview

```bash
# Option 1: Python
python -m http.server 8080

# Option 2: Node (if installed)
npx serve .

# Option 3: VS Code / Cursor Live Server extension
# Right-click index.html → "Open with Live Server"
```

Open http://localhost:8080 in your browser.

## Deploy to GitHub Pages

1. Create repo named `Murali-Madevan.github.io` on GitHub
2. Push this folder to the `main` branch
3. Settings → Pages → Source: **Deploy from branch** → `main` / `/ (root)`
4. Site goes live at https://Murali-Madevan.github.io/

## Customize

- Update content in `index.html`
- Change accent color in `style.css` (`--accent` variable)
- Add `assets/resume.pdf` and replace `assets/profile.svg` with your photo
