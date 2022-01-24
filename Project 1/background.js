window.x = {}
chrome.runtime.onMessage.addListener(function (request,
    sender, sendResponse) {
        window.x[request.url] = request.count
    })
window.e = {}
chrome.runtime.onMessage.addListener(function (request,
    sender, sendResponse) {
        window.e[request.url] = request.count2
        })

chrome.browserAction.onClicked.addListener(function (tab) {
    chrome.tabs.create({url: 'popup.html'})
})