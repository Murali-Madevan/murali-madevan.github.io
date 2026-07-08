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

Your user site URL is **https://murali-madevan.github.io/** — the repo name must match your GitHub username exactly.

### Important: correct repo name

| Repo name | Result |
|-----------|--------|
| `Murali-Madevan.github.io` | ✅ `https://murali-madevan.github.io/` |
| `muralimadevan.github.io` | ❌ Project page only — **not** your root user site |

If you already have `muralimadevan.github.io`, rename it: **Settings → General → Repository name → `Murali-Madevan.github.io`**

### Steps

1. Create (or rename to) repo **`Murali-Madevan.github.io`** on GitHub
2. Push this folder:
   ```powershell
   cd "C:\Users\KK COMPUTERS\OneDrive\Documents\Murali-Madevan.github.io"
   git remote add origin https://github.com/Murali-Madevan/Murali-Madevan.github.io.git
   git push -u origin main
   ```
3. **Settings → Pages → Build and deployment**
   - Source: **Deploy from a branch**
   - Branch: **`main`** / **`/ (root)`**
   - Save
4. Wait 1–3 minutes, then open https://murali-madevan.github.io/

## Customize

- Update content in `index.html`
- Change accent color in `style.css` (`--accent` variable)
- Add `assets/resume.pdf` and replace `assets/profile.svg` with your photo
