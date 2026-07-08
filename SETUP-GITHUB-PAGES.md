# Fix GitHub Pages 404 — Do This Now

Your site **works** here (wrong URL):
**https://murali-madevan.github.io/muralimadevan.github.io/**

Your root URL **404s** because the repo name is wrong:
**https://murali-madevan.github.io/** ← needs repo `Murali-Madevan.github.io`

---

## Step 1: Rename repo (2 minutes)

1. Open: https://github.com/Murali-Madevan/muralimadevan.github.io/settings
2. Scroll to **Repository name**
3. Change `muralimadevan.github.io` → **`Murali-Madevan.github.io`**
4. Click **Rename**

GitHub will warn you about redirects — that's OK. Click confirm.

---

## Step 2: Confirm Pages settings

1. Open: https://github.com/Murali-Madevan/Murali-Madevan.github.io/settings/pages
2. Set:
   - **Source:** Deploy from a branch
   - **Branch:** `main`
   - **Folder:** `/ (root)`
3. Click **Save**

Wait 2–5 minutes. Your site should appear at:
**https://murali-madevan.github.io/**

---

## Step 3: Push the new portfolio (optional)

After rename, run in PowerShell:

```powershell
cd "C:\Users\KK COMPUTERS\OneDrive\Documents\Murali-Madevan.github.io"
git remote remove origin
git remote add origin https://github.com/Murali-Madevan/Murali-Madevan.github.io.git
git push -u origin main --force
```

This replaces the old skin-cancer page with your new portfolio design.

---

## Still 404?

- Clear browser cache or try incognito
- Check **Actions** tab for failed Pages builds
- Ensure `index.html` is at the **root** of the repo (not in a subfolder)
- Repo must be **Public**
