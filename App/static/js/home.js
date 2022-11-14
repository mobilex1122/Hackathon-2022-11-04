navbuttons = document.getElementsByName("nab")

function navb(select) {
    navbuttons.forEach(element => {
        console.log(element, element.innerHTML)
        if (select == element.innerHTML) {
            element.className = "selected";
        } else {
            element.className = "";
        }
    });
}