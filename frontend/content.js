// Sniffing around for password fields. Pls don't enter your bank details if it's shady.
const passwordInput = document.querySelector('input[type="password"]');
const hasLoginForm = passwordInput !== null;
let hasCrossSiteAction = false;

// Check if the form is secretly sending data to a completely different server
if (hasLoginForm) {
    const form = passwordInput.closest('form');
    if (form && form.action) {
        try {
            const actionUrl = new URL(form.action, window.location.href);
            if (actionUrl.hostname !== window.location.hostname) {
                hasCrossSiteAction = true;
            }
        } catch(e) {
            // failed to parse URL, silently ignore
        }
    }
}

// Yeet this info over to the background script
chrome.runtime.sendMessage({
  action: "pageAnalysis",
  url: window.location.href,
  hasLoginForm: hasLoginForm,
  hasCrossSiteAction: hasCrossSiteAction
});
