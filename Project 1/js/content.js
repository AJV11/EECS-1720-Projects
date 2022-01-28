const re = new RegExp('x', 'gi')
const re2 = new RegExp('e', 'gi')
const matches = document.documentElement.innerHTML.match(re)
const matches2 = document.documentElement.innerHTML.match(re2)
chrome.runtime.sendMessage({
    url: window.location.href,
    count: matches.length,
    count2: matches2.length
})