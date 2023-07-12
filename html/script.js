// document.getElementById("add-row").addEventListener("click", function(){
//     table.rowManager.addRow({}, 0);
// });
// document.getElementById("clear").addEventListener("click", function(){
//     table.clearData()
// });

$('#input').on('change', function (e) { // element.addEventListener
    message.commands['input'] = $(this).val(); //element.value
    SendMessage();
})

// data = getDataFromRB({module_name:"odbc", command_name:"get_drivers"})
// .then(data => {
//     drivers = data["drivers"]
// })

function addOptions(theArray) {
    
    let mytable = "<table id=\"theTable\"><tr>";
    
    for (let eachKey of Object.keys(theArray)) {
        let eachValue = theArray[eachKey]
        console.log(typeof eachValue)
        if (typeof eachValue == "object") {
            eachValue = JSON.stringify(eachValue)
        }
        console.log(eachKey, eachValue)
        mytable += "<td> " + eachKey + " </td><td> " + eachValue + " </td> </tr>";
    }
    
    mytable += "</tr></table>";
    document.getElementById("theTable").innerHTML = mytable

}

data = getDataFromRB({module_name:"2Captcha", command_name:"getCallback"})
.then(data => {
    if (data) {
    addOptions(data)
} else {
    not_browser = {'Error': 'The browser is not opened or does not contain a valid captcha'}
    addOptions(not_browser)
}
})
