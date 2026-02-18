# New Project Bootstrap Prompt (Cloudflare Pages + GitHub Actions)

Use this file to duplicate the exact workflow used in `stationeryobject`.

## One Prompt To Reuse

Copy/paste this into a new Codex thread after creating/opening the new repo folder:

```text
Set up a brand new website project using this exact deployment model:

Accounts to use:
- GitHub: rstephens1
- Cloudflare: rstephens1@gmail.com

Project details:
- Repo name: <REPO_NAME>
- Cloudflare Pages slug (lowercase): <PAGES_SLUG>
- Site display name: <SITE_TITLE>
- Menu must be exactly: Home, Submissions, Archive, About

Requirements:
1) Copy and adapt memory.md + PROJECT_GUARDRAILS.md from /Users/robertstephens/code/GitHub/rstephens1/website to this repo, replacing old project-specific values.
2) Create repo-local wrangler isolation:
   - wrangler.sh with WRANGLER_HOME=.wrangler-home
   - .gitignore entries: .wrangler-home/, .wrangler/, node_modules/, .DS_Store
3) Build Hugo site with:
   - Home feed
   - RSS enabled
   - About page
   - Archive page
   - Submissions page at /submissions/
   - Search page (JSON index + client-side search)
4) Create Cloudflare Pages project via Wrangler using slug <PAGES_SLUG> and production branch main.
5) Add GitHub Actions deploy workflow equivalent to website/.github/workflows/deploy-pages.yml, adapted for this repo and Hugo build command `hugo --gc --minify`.
6) Set these GitHub repo secrets in this order:
   - CLOUDFLARE_ACCOUNT_ID
   - CLOUDFLARE_PAGES_PROJECT
   - CLOUDFLARE_API_TOKEN
7) Trigger workflow on main and verify production deploy succeeds.
8) Disable GitHub repo email notifications for this repo (set subscription to ignored).
9) Commit and push all changes to main.

Safety:
- Always run account preflights before Cloudflare/GitHub actions:
  - git remote -v
  - gh auth status
  - bash wrangler.sh whoami
- Stop if account mismatch.
```

## Contacts / Inputs You Must Provide

- GitHub account owner: `rstephens1`
- Cloudflare login/account email: `rstephens1@gmail.com`
- Repo name: `<REPO_NAME>`
- Pages slug (must be lowercase): `<PAGES_SLUG>`
- Optional custom domain(s): `<DOMAIN>` / `www.<DOMAIN>`

## Secrets And Token Order

Set up secrets in this exact order.

1. `CLOUDFLARE_ACCOUNT_ID`
2. `CLOUDFLARE_PAGES_PROJECT` (slug, e.g. `stationeryobject`)
3. `CLOUDFLARE_API_TOKEN`

Why this order: first two remove slug/account ambiguity; token last enables deploy.

## Where To Create CLOUDFLARE_API_TOKEN

1. Open: <https://dash.cloudflare.com/profile/api-tokens>
2. Click `Create Token`
3. Use template `Edit Cloudflare Workers` (includes Pages deploy capability)
4. Scope to account: `Rstephens1@gmail.com's Account`
5. Create token and copy it (shown once)
6. Save to GitHub secret:
   - `gh secret set CLOUDFLARE_API_TOKEN --repo rstephens1/<REPO_NAME>`

## Required Repo Secrets Commands

```bash
gh secret set CLOUDFLARE_ACCOUNT_ID --repo rstephens1/<REPO_NAME> --body "fb5bfb2bcc149dfb0e63a850b5c0d346"
gh secret set CLOUDFLARE_PAGES_PROJECT --repo rstephens1/<REPO_NAME> --body "<PAGES_SLUG>"
gh secret set CLOUDFLARE_API_TOKEN --repo rstephens1/<REPO_NAME>
```

## Verification Commands

```bash
# Account preflight
git remote -v
gh auth status
bash wrangler.sh whoami

# Build check
hugo

# Trigger CI deploy
gh workflow run "Deploy Hugo to Cloudflare Pages" --repo rstephens1/<REPO_NAME> --ref main

# Watch latest runs
gh run list --repo rstephens1/<REPO_NAME> --limit 3

# Disable repo notifications/email for this repo
gh api --method PUT /repos/rstephens1/<REPO_NAME>/subscription -f ignored=true

# Verify notification state
gh api /repos/rstephens1/<REPO_NAME>/subscription
```

## Expected End State

- GitHub repo exists under `rstephens1/<REPO_NAME>`
- Cloudflare Pages project exists as `<PAGES_SLUG>`
- Workflow file exists at `.github/workflows/deploy-pages.yml`
- Secrets set: `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_PAGES_PROJECT`, `CLOUDFLARE_API_TOKEN`
- `main` branch deploy passes and publishes `https://<PAGES_SLUG>.pages.dev`
- GitHub repo subscription returns `"ignored": true` (email notifications off)
