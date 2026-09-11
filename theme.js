(() => {
    const key = 'mangan-tako-theme';
    const system = window.matchMedia('(prefers-color-scheme: dark)');
    let preference = null;
    try {
        const saved = localStorage.getItem(key);
        if (saved === 'light' || saved === 'dark') preference = saved;
    } catch { /* Storage may be blocked; switching still works for this page. */ }
    const root = document.documentElement;
    const applyTheme = () => {
        const theme = preference || (system.matches ? 'dark' : 'light');
        root.dataset.theme = theme;
        const toggle = document.querySelector('.theme-toggle');
        if (toggle) toggle.setAttribute('aria-pressed', String(theme === 'dark'));
    };
    applyTheme();
    system.addEventListener('change', () => { if (!preference) applyTheme(); });
    window.addEventListener('storage', (event) => {
        if (event.key !== key && event.key !== null) return;
        preference = event.newValue === 'light' || event.newValue === 'dark' ? event.newValue : null;
        applyTheme();
    });
    document.addEventListener('DOMContentLoaded', () => {
        const toggle = document.querySelector('.theme-toggle');
        if (!toggle) return;
        toggle.hidden = false;
        applyTheme();
        toggle.addEventListener('click', () => {
            preference = root.dataset.theme === 'dark' ? 'light' : 'dark';
            try { localStorage.setItem(key, preference); } catch { /* In-memory fallback. */ }
            applyTheme();
        });
    });
})();
