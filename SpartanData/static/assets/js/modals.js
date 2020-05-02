
(function() {
    /* Modal */   
    var modalMaster = document.getElementById('myMasterModal')
    var modalLine = document.getElementById('myLineModal');
    var modalBar = document.getElementById('myBarModal');
    var modalDonut = document.getElementById('myDonutModal');
    var modalScatter = document.getElementById('myScatterModal');

    /* Launch Button */
    // Get the button that opens the modal
    var btnMaster = document.getElementById("myMasterBtn")
    var btnLine = document.getElementById("myLineBtn");
    var btnBar = document.getElementById("myBarBtn");
    var btnDonut = document.getElementById("myDonutBtn");
    var btnScatter = document.getElementById("myScatterBtn");

    // When the user clicks on the button, open the modal
    btnMaster.onclick = function() { modalMaster.style.display = "block"}
    btnLine.onclick = function() { modalLine.style.display = "block"; }
    btnBar.onclick = function() { modalBar.style.display = "block"; }
    btnDonut.onclick = function() { modalDonut.style.display = "block"; }
    btnScatter.onclick = function() { modalScatter.style.display = "block"; }
    
    // Get the <span> element that closes the modal
    var spanMaster = document.getElementById("closeMaster")
    var spanLine = document.getElementById("closeLine");
    var spanBar = document.getElementById("closeBar");
    var spanDonut = document.getElementById("closeDonut");
    var spanScatter = document.getElementById("closeScatter");
    
    // When the user clicks on <span> (x), close the modal
    spanMaster.onclick = function() { modalMaster.style.display = "none";}
    spanLine.onclick = function() { modalMaster.style.display = "none";
                                    modalLine.style.display = "none"; }
    spanBar.onclick = function() { modalMaster.style.display = "none";
                                    modalBar.style.display = "none"; }
    spanDonut.onclick = function() { modalMaster.style.display = "none";
                                    modalDonut.style.display = "none"; }
    spanScatter.onclick = function() { modalMaster.style.display = "none";
                                    modalScatter.style.display = "none"; }
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modalLine) {
            modalMaster.style.display = "none";
            modalLine.style.display = "none";
        } else if (event.target == modalBar) {
            modalMaster.style.display = "none";
            modalBar.style.display = "none";
        } else if (event.target == modalDonut) {
            modalMaster.style.display = "none";
            modalDonut.style.display = "none";
        } else if (event.target == modalScatter) {
            modalMaster.style.display = "none";
            modalScatter.style.display = "none";
        } else if(event.target == modalMaster){
            modalMaster.style.display = "none";
        }
    }
    })();