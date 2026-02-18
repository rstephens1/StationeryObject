# Project Guardrails

Use this checklist at the start of any new Codex thread for this repo.

Scope of this file:
- Account isolation, deployment safety, and stop conditions.

## Account Confirmation

Before any work, confirm:
- GitHub account: `rstephens1`
- Cloudflare account: `rstephens1@gmail.com`

If either account is not confirmed, stop and ask.

## Cloudflare Isolation

Always isolate Wrangler per repo:

- Use local wrapper script `wrangler.sh` with `WRANGLER_HOME=.wrangler-home`.
- Add `.wrangler-home/`, `.wrangler/`, `node_modules/`, and `.DS_Store` to `.gitignore`.
- Always run Wrangler with `bash wrangler.sh ...`.
- Before any Cloudflare command, run `bash wrangler.sh whoami`.
- If account is wrong or unauthenticated, run:
  - `bash wrangler.sh logout`
  - `bash wrangler.sh login`
  - re-run `bash wrangler.sh whoami`

## GitHub Safety

- Verify expected remote before push/pull: `git remote -v`.
- If remote does not match `rstephens1`, stop and ask.

## Cloudflare Pages Safety

- Use Pages project slug: `StationeryObject`.
- Prefer GitHub-connected Pages deploys from `main`.
- Do not deploy stale local build artifacts as production source of truth.

## Stop Conditions

If any account ambiguity appears, stop and ask for clarification.

## Final Confirmation

Repeat back before sensitive actions:
- Repo path
- GitHub account
- Cloudflare account
