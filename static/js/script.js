active = ''
function selDoc() {
    document.getElementById("doctor").style.backgroundColor = '#198754';
    document.getElementById("patient").style.backgroundColor = 'white';
    document.getElementById("rad-doctor").checked = true
    document.getElementById("apply").disabled = false;
    
    console.log("doctor selected")
}
function selPat(){
    document.getElementById("patient").style.backgroundColor = '#198754';
    document.getElementById("doctor").style.backgroundColor = 'white';
    document.getElementById("rad-patient").checked = true
    document.getElementById("apply").disabled = false;

    console.log("patient selected")
}
// document.addEventListener('DOMContentLoaded', {

// });
// document.getElementById("rad-doctor").onclick() = selDoc;

// document.getElementById("rad-doctor").addEventListener("change", function () { console.log("button click") });
// document.getElementById("doctor").onclick = selDoc;
document.addEventListener('DOMContentLoaded', ()=>{
    document.getElementById("doctor").onclick = selDoc;
    document.getElementById("patient").onclick = selPat;
    document.getElementById("apply").disabled = true;
    document.getElementById("apply").onclick = () => {
        console.log("click")
    };

});
