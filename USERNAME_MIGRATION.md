# GitHub username migration checklist

Use this if changing from `0-danielviktorovich-0` to a new professional username such as `danielkamyshan`.

## Before changing

- Confirm the new username in GitHub account settings.
- Record repositories, GitHub Pages sites, Actions variables/secrets, package metadata and external profile links that contain the old username.
- Keep a local backup of important repositories.

## Immediately after changing

- Create/rename the Profile README repository so its repository name **exactly matches the new username**.
- Update Git remotes to the new canonical URLs.
- Update `danielviktorovich.com` and social profiles.
- Update repository README links, badges and images that hard-code the old namespace.
- Check GitHub Pages projects. Do not assume every Pages URL will behave like a normal repository redirect.
- Update package metadata such as `repository`, `homepage`, crates/package links, CI references and documentation URLs.
- Review GitHub Sponsors / donation pages and any external services that reference the old GitHub handle.
- Sign out/in on GitHub Mobile if the old username remains cached there.

## Important redirect behavior

GitHub normally redirects old **repository** URLs after a username change, but the old **profile** URL does not redirect and can return 404. Treat redirects as a migration aid, not as the long-term canonical URL.
