document.addEventListener('DOMContentLoaded', function () {

    const bg = chrome.extension.getBackgroundPage()
    Object.keys(bg.x).forEach(function (url) {
        const div = document.createElement('div')
        div.textContent = `${url}: # of X's- ${bg.x[url]}, # of E's- ${bg.e[url]}`
        document.body.appendChild(div)
    })
    
}, false)

// X icon image: https://www.pngall.com/wp-content/uploads/5/X-Letter-PNG.png