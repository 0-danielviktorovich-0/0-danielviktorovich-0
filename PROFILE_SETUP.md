# Profile release setup

This package is designed to become Daniel Kamyshan's GitHub Profile README.

## Recommended public profile settings

- **Display name:** `Daniel Viktorovich Kamyshan`
- **Short public identity:** `Daniel Kamyshan`
- **Preferred username:** `danielkamyshan` if GitHub confirms it is available
- **Bio:** `Entrepreneur & product builder. AI automation, full-stack, web, mobile & desktop software. Building in Tokyo.`
- **Location:** `Tokyo, Japan`
- **Website:** `https://danielviktorovich.com/en/`
- **Public email:** add only after choosing and verifying the address you want exposed publicly

## Publishing order

1. In GitHub account settings, test whether `danielkamyshan` is available.
2. If available, change the username.
3. Update the old GitHub link on `danielviktorovich.com`.
4. Create a **public** repository whose name exactly matches the final username.
5. Upload the contents of this package to that repository root.
6. Preview `README.md` in both GitHub light and dark mode.
7. Pin **RimLoc**. Do not pin raw forks merely to fill space; the merged upstream PRs are already presented more honestly in the README.
8. When another owned project becomes public and presentable, add it as a second pin and move it into the `Selected work` section.

GitHub only displays a Profile README when the repository is public, has the same name as the username, and contains a non-empty root `README.md`.

## Why the profile is intentionally restrained

The profile does **not** include visitor counters, trophy walls, Spotify widgets, generic "top languages" cards, random quotes, or a contribution snake. Those elements add visual noise and external dependencies while contributing little evidence of product or engineering ability.

The strongest proof currently available is:
- a real public product: **RimLoc**;
- honest disclosure of **BookKeeper** as private development;
- merged upstream work in **RimSort** and **anylinuxfs**;
- a clear commercial capability map and direct CTA.

## After the username change

The RimLoc link in `README.md` currently points at the old owner path so it works today and benefits from GitHub's repository redirect after a username change. Once the username is final, update it to the new canonical URL.

Run:

```bash
python scripts/check_profile.py
```

before publishing changes.
