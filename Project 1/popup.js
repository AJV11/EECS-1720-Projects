document.addEventListener('DOMContentLoaded', function () {

    const bg = chrome.extension.getBackgroundPage()
    Object.keys(bg.x).forEach(function (url) {
        const div = document.createElement('div')
        const divx = document.createElement('div')
        const dive = document.createElement('div')
        const br = document.createElement('br')
        div.textContent = `Webpage: ${url}`
        document.body.appendChild(div)
        document.body.appendChild(br)
        divx.textContent = `# of X's - ${bg.x[url]}`
        document.body.appendChild(divx)
        document.body.appendChild(br)
        dive.textContent = `# of E's - ${bg.e[url]}`
        document.body.appendChild(dive)
        document.body.appendChild(br)
    })
    
}, false)

// X icon image: https://www.pngall.com/wp-content/uploads/5/X-Letter-PNG.png
