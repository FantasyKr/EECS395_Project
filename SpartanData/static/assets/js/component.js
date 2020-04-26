

//slider js information
function slider(){
    var slider = document.getElementById("myRange");
    var output = document.getElementById("demo");
    output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
    slider.oninput = function() {
        output.innerHTML = this.value;
    }
}

<style>
/* Slider */

.slidecontainer {
	width: 100%; /* Width of the outside container */
  }
  
/* The slider itself */
.slider {
	-webkit-appearance: none;  /* Override default CSS styles */
	appearance: none;
	width: 100%; /* Full-width */
	height: 25px; /* Specified height */
	background: #d3d3d3; /* Grey background */
	outline: none; /* Remove outline */
	opacity: 0.7; /* Set transparency (for mouse-over effects on hover) */
	-webkit-transition: .2s; /* 0.2 seconds transition on hover */
	transition: opacity .2s;
  }
  
  /* Mouse-over effects */
  .slider:hover {
	opacity: 1; /* Fully shown on mouse-over */
  }
  
  /* The slider handle (use -webkit- (Chrome, Opera, Safari, Edge) and -moz- (Firefox) to override default look) */
  .slider::-webkit-slider-thumb {
	-webkit-appearance: none; /* Override default look */
	appearance: none;
	width: 25px; /* Set a specific slider handle width */
	height: 25px; /* Slider handle height */
	background: #4CAF50; /* Green background */
	cursor: pointer; /* Cursor on hover */
  }
  
  .slider::-moz-range-thumb {
	width: 25px; /* Set a specific slider handle width */
	height: 25px; /* Slider handle height */
	background: #4CAF50; /* Green background */
	cursor: pointer; /* Cursor on hover */
  }
  </style>