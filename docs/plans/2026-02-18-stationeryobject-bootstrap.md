# StationeryObject Bootstrap Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Bootstrap a new Hugo + Cloudflare Pages blog named StationeryObject with home feed, RSS, About, Search, Archive, and Submit navigation.

**Architecture:** Use Hugo with PaperMod as theme base and lightweight template overrides for homepage feed and custom pages. Keep Cloudflare deployment safe via repo-local Wrangler isolation and account preflight checks.

**Tech Stack:** Hugo, PaperMod theme, Cloudflare Pages, Wrangler CLI, Markdown content.

---

### Task 1: Adapt project memory and guardrails

**Files:**
- Modify: `memory.md`
- Modify: `PROJECT_GUARDRAILS.md`

**Step 1: Update memory for StationeryObject specifics and replace legacy /website references.**

**Step 2: Update guardrails to single confirmed account pair and StationeryObject project metadata.**

### Task 2: Add Cloudflare account isolation scaffold

**Files:**
- Create: `.gitignore`
- Create: `wrangler.sh`

**Step 1: Add repo-local Wrangler and ignore local auth/build artifacts.**

**Step 2: Make wrapper executable and validate shell syntax.**

### Task 3: Scaffold Hugo site and theme baseline

**Files:**
- Create: `hugo.toml`
- Create: `themes/PaperMod/` (git submodule or clone)
- Create: `content/_index.md`, `content/about.md`, `content/search.md`, `content/archive.md`, `content/submit.md`
- Create: `layouts/index.html`
- Create: `static/css/base.css`

**Step 1: Configure site menus and output formats including RSS.**

**Step 2: Add content pages and homepage feed template.**

**Step 3: Add minimal styling so nav and feed are readable on desktop/mobile.**

### Task 4: Verify build and Cloudflare preflight

**Files:**
- Verify: local build output

**Step 1: Run `hugo` and confirm successful generation.**

**Step 2: Run `bash wrangler.sh whoami` and verify account matches `rstephens1@gmail.com`.**

**Step 3: Record any follow-up needed for `wrangler pages project create StationeryObject` if auth is missing.**
