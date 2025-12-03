# bhjupyter.github.io

```markdown
# Notebook Hub — GitHub Pages site with embedded Jupyter notebooks

How to use (entirely online):
1. Create a new GitHub repository (e.g., "my-notebooks-site") on github.com.
2. In the repo, use "Add file" → "Create new file" and create the files and paths shown in this repo:
   - docs/index.html
   - docs/notebooks.html
   - scripts/build_notebooks.py
   - .github/workflows/build_and_deploy.yml
   - requirements.txt (optional; list packages your notebooks need)
   - .gitignore
3. Upload your .ipynb files:
   - Click "Add file" → "Upload files".
   - Upload notebooks into a folder named notebooks_src (create folder by naming the uploaded path notebooks_src/your_notebook.ipynb).
   - Commit the upload.
4. Push/commit any remaining files via the web editor.
5. GitHub Actions will run on push to main:
   - It will install nbconvert/jupyter and any packages in requirements.txt,
   - Convert notebooks to HTML, write docs/notebooks/*.html and manifest.json,
   - Deploy the docs/ folder to the gh-pages branch (publish to GitHub Pages).
6. After the Action completes, visit the Pages URL shown in the repo's Settings → Pages (or on the Actions run page) to see your site.

Notes:
- If your notebooks require heavy or system-level deps (e.g., tensorflow, GDAL), the Actions runner might need extra configuration. For simple analysis notebooks (numpy/pandas/matplotlib) requirements.txt is usually enough.
- The exported HTML is static: outputs reflect the state when the notebook was last executed. For interactive widgets, consider Voilà or Binder links instead.
- If you prefer to host directly from main/docs (no gh-pages branch), you can skip the deploy step and set Pages source to branch main / folder /docs in repo Settings -> Pages.
