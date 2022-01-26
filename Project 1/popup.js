document.addEventListener('DOMContentLoaded', function () {

    const bg = chrome.extension.getBackgroundPage()
    Object.keys(bg.x).forEach(function (url) {
        const div = document.createElement('div')
        const divx = document.createElement('div')
        const dive = document.createElement('div')
        const divd = document.createElement('div')
        const br = document.createElement('br')
        let dif = `${bg.e[url]}` - `${bg.x[url]}`
        div.textContent = `Webpage: ${url}`
        document.body.appendChild(div)
        document.body.appendChild(br)
        divx.textContent = `# of X's - ${bg.x[url]}`
        document.body.appendChild(divx)
        document.body.appendChild(br)
        dive.textContent = `# of E's - ${bg.e[url]}`
        document.body.appendChild(dive)
        document.body.appendChild(br)
        divd.textContent = `Difference(E-X): `+dif
        document.body.appendChild(divd)
        document.body.appendChild(br)
    })
    
}, false)

// X icon image: https://www.pngall.com/wp-content/uploads/5/X-Letter-PNG.png
// Youtube video reference: https://www.youtube.com/watch?v=Ipa58NVGs_c
