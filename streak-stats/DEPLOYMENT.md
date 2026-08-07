# Deploying GitHub Readme Streak Stats on Vercel with Personal Access Token (PAT)

This directory contains the custom Vercel-compatible serverless build of `github-readme-streak-stats`. Deploying this to Vercel with your GitHub PAT allows your profile README streak badge to track private repository commits while keeping your code completely private!

---

## 🔑 Step 1: Generate a GitHub Personal Access Token (PAT)

1. Go to GitHub **Settings** ➔ **Developer settings** ➔ **Personal access tokens** ➔ **Tokens (classic)**.
   - *Quick link*: [Generate New Classic Token](https://github.com/settings/tokens/new?description=Streak%20Stats%20Token)
2. Give it a descriptive note (e.g. `Streak Stats Token`).
3. Set Expiration (e.g., `No expiration` or `90 days`).
4. Select Scopes:
   - Select **`repo`** (Full control of private repositories - required to fetch private activity).
   - Select **`user`** (Optional, for user data).
5. Click **Generate token** at the bottom.
6. **Copy the token immediately** (it looks like `ghp_...`).

---

## 🚀 Step 2: Deploy to Vercel

### Option A: Using Vercel Dashboard (Recommended)

1. Commit and push this `streak-stats` directory to your GitHub repository (`CodeCenturian`).
2. Log in to [Vercel](https://vercel.com/).
3. Click **Add New...** ➔ **Project**.
4. Import your **`CodeCenturian`** repository.
5. In the **Configure Project** section:
   - **Root Directory**: Click **Edit** and select the `streak-stats` folder.
   - **Framework Preset**: Select **Other**.
6. Expand **Environment Variables**:
   - **Name**: `TOKEN`
   - **Value**: Paste your GitHub PAT (`ghp_...`)
7. Click **Deploy**.

---

### Option B: Using Vercel CLI

1. Open your terminal and navigate to the `streak-stats` folder:
   ```bash
   cd streak-stats
   ```
2. Run Vercel CLI:
   ```bash
   npx vercel
   ```
3. Follow the prompts to set up the project.
4. Add the `TOKEN` environment variable in Vercel Dashboard under **Project Settings ➔ Environment Variables** with your PAT value.
5. Redeploy to apply environment variables:
   ```bash
   npx vercel --prod
   ```

---

## 🖼️ Step 3: Update `Readme.md`

Once deployment finishes, Vercel will provide your app URL (e.g., `https://streak-stats-xxxx.vercel.app`).

In your `Readme.md`, update the Streak Stats image source URL:

```html
<img src="https://<YOUR-VERCEL-APP-NAME>.vercel.app/?user=CodeCenturian&theme=github_dark&hide_border=true" height="180" alt="GitHub Streak"/>
```

Test the URL in your browser:
`https://<YOUR-VERCEL-APP-NAME>.vercel.app/?user=CodeCenturian&theme=github_dark&hide_border=true`
