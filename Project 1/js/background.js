window.x = {}
chrome.runtime.onMessage.addListener(function (request) {
        window.x[request.url] = request.count
    })
window.e = {}
chrome.runtime.onMessage.addListener(function (request) {
        window.e[request.url] = request.count2
        })

chrome.browserAction.onClicked.addListener(function () {
    chrome.tabs.create({url: 'popup.html'})
})