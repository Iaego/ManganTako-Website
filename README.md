# Mangan Tako

A responsive restaurant website concept celebrating Cordilleran food. Built as a portfolio project with HTML, CSS, and a small vanilla JavaScript theme controller.

## Pages and features

- Home: editorial hero, signature dishes, restaurant story, and photo gallery.
- Menu: existing dishes and prices, thumbnail layouts, and category links.
- Our story: brand introduction and food philosophy.
- Contact: styled inquiry form with a clear unavailable state until a delivery service is configured.
- Light and dark palettes, system preference detection, and saved theme selection.
- Responsive layouts, keyboard focus indicators, skip links, reduced-motion support, and semantic landmarks.
- Local images and system fonts; no framework, build step, or external icon/font service.

## Preview

Open `index.html`, or use a local server for consistent theme persistence across pages:

```sh
python -m http.server 8000
```

Visit `http://localhost:8000`. Use the Dark mode toggle in the header. Its pressed state means dark mode is enabled. A saved choice overrides the operating system setting; clear the `mangan-tako-theme` local storage entry to follow the system again. If storage is blocked, switching still works on the current page. With JavaScript disabled, the site follows the system palette and hides the toggle.

## Checks

Requires Python 3 and Node.js, with no extra packages:

```sh
python tests/check_site.py
node --check theme.js
node tests/theme.test.cjs
```

These checks cover page structure and theme logic; they do not replace visual browser testing.

## Before using this for a real restaurant

Configure and test message delivery before enabling the contact form. Add verified location, hours, contact information, and any real social profiles. Confirm the menu, pricing, ingredient information, and rights to the existing photos. The footer identifies this as a restaurant website concept.

See [CHANGES.md](CHANGES.md) for the commit summary and verification notes.
