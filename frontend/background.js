// Our temporary brain for storing what's happening in each tab
let pageData = {};

// Listen for our content script gossiping about the current page
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "pageAnalysis" && sender.tab) {
    pageData[sender.tab.id] = { 
        url: message.url, 
        hasLoginForm: message.hasLoginForm,
        hasCrossSiteAction: message.hasCrossSiteAction
    };
  }
});

// When the popup asks "What are we looking at?", we answer here
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "getTabData") {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      if(tabs && tabs.length > 0) {
        const tabId = tabs[0].id;
        // hand over the data, or default if we missed the memo
        sendResponse(pageData[tabId] || { url: tabs[0].url, hasLoginForm: false, hasCrossSiteAction: false });
      } else {
        sendResponse(null);
      }
    });
    return true; // gotta keep the channel alive for async stuff
  }
});
