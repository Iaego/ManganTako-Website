# Portfolio redesign and bug fixes

## Suggested commit message

```text
Redesign Mangan Tako restaurant site and add persistent light and dark modes

- Introduce a shared ivory, forest green, and terracotta visual system
- Rebuild home, story, menu, and contact layouts for desktop and mobile
- Feature Cordilleran dishes and replace informal testimonial content
- Add accessible theme switching with system and saved preferences
- Improve navigation, semantic structure, image captions, and focus states
- Retain the disabled contact form until delivery is configured
- Add dependency-free structural and theme regression checks
- Update preview instructions and document remaining launch setup
```

## Changes

- **styles.css:** Replaced the previous stylesheet with consistent theme variables, typography, spacing, button treatments, responsive grids, and mobile breakpoints. Added image crops, an arched hero photo, signature dish cards, an editorial story section, and permanent gallery captions. Includes reduced-motion support and keyboard focus outlines.
- **index.html:** Rebuilt the home page around existing photography and Cordilleran dishes. Replaced the informal review cards with menu highlights. Added clear menu and story links, without inventing reviews, awards, hours, or contact information.
- **menu.html:** Retained the existing dishes and prices. Added category anchors, a single page heading, compact food thumbnails, and layouts for narrow screens.
- **about.html:** Expanded the story into a photo-and-copy layout and three short brand values. User zoom remains available.
- **contact.html:** Added a matching photo and form layout. Retained corrected labels, a multiline message field, disabled fields, and the unavailable notice as requested. No submissions are sent.
- **All pages:** Share navigation, active-page indicators, a theme toggle, skip link, main landmark, descriptive titles, meta descriptions, and footer. Navigation uses normal links. Removed placeholder social icons and the Font Awesome CDN; fonts use installed system families. The footer identifies the site as a restaurant concept.
- **theme.js:** Applies the saved theme before CSS loads, or follows the system preference. Keeps the toggle's accessible pressed state in sync. Supports system changes, cross-tab preference updates, invalid saved values, and blocked storage. The toggle stays hidden without JavaScript, while CSS still follows system preference.
- **tests/:** Added repeatable Python page checks and Node theme behavior tests. Neither needs external packages.
- **README.md:** Updated the project overview, preview steps, theme behavior, tests, and remaining launch setup.

## Verification

Passed:

```sh
python tests/check_site.py
node --check theme.js
node tests/theme.test.cjs
git diff --check
```

The page checker validates all four HTML pages: nesting, IDs, form label targets, local files and fragment links, image descriptions, one main heading, and active navigation. The theme tests cover system preference changes, explicit overrides, saving preferences, storage synchronization, invalid values, blocked storage, and toggle state.

Rendered browser verification is still pending. Edge previously crashed during headless startup; a second attempt with an in-process GPU did not produce a screenshot and was stopped. The automated checks above do not verify visual layout.

## Visual checklist before pushing

- Open every page at 1440px, 768px, 390px, and 320px in both themes. Check wrapping, photo crops, readable contrast, and horizontal overflow.
- Switch themes, navigate to another page, and reload to verify persistence using the local server.
- Tab through navigation, theme toggle, menu categories, and footer. Verify visible focus and the skip link.
- Check the layout at 200% zoom and with reduced motion enabled.
- Confirm the contact form remains disabled and its notice is visible.

## Remaining launch setup

- Add a real contact endpoint and test delivery, validation, success, and failure states before enabling the form.
- Supply verified restaurant details and any real social profile links.
- Review existing menu information and image permissions before commercial use.

No commit or push was performed.
