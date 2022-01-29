# EECS-1720-Projects
EECS 1720 Projects - Anthony Venditti


**Lab Project 1 - Lens for the Internet:**

*The Letter X vs. The Letter E*

manifest.json: This file consists of the typical json code for an extension. This is where I set the extension title, description, icons, version, scripts, and permissions.

popup.html: This file consists of all the aspects that are seen when the extension tab opens up. The popup.js and style.css files are linked through this html inside of the element. This file is also where I wrote the text that displays in the extension, along with a thematic break to divide the html text from the actual content text of the extension.

style.css: This file consists of the changes to the visual appearances of the extensions content. This file is where I altered the colour, fonts, sizes, margins, and images (the X icon at the top right) of the content in the extension.

content.js: This file consists of the content that is captured when webpages are visited while this extension is active. This file is where I created four important variables; one RegExp variable that searches the webpage for all the instances of the letter 'X', another variable that does the same but for the letter 'E', and two other variables that count the amount of matches for each corresponding letter. Then, at chrome runtime, a message is sent that contains the webpage's URL and the total count of each letter.

background.js: This file consists of the background action that takes place while on chrome. This file is where I set it so that when a new window is opened on chrome, the extension requests to access the webpage's URL and counts of each letter. Also, when the extension icon at the top right is clicked, a new tab is created using the popup.html.

popup.js: This file consists of the content that is displayed in the extension with the help of the other js files. First, before any of this code runs, the 'DOMContentLoaded' event is called which waits for all content in the html to load before running. This file is where I created 'div' and 'br' elements, along with a variable that calculates the difference between E's and X's in each webpages. Here is where I listed the necessary information that gives my extension purpose. The div's display the text of the webpage's URL, the number of X's, the number of E's, and the difference. Also, between each div, there is a line break to help seperate the data, all of which is implemented into the html through the appendChild() function.

Note!!!: In order to get rid of the list of webpages that are displayed in the extension tab, you must refresh the extension in the 'manage extensions' setting on chrome.
