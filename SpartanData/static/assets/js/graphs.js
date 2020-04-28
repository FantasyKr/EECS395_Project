/************************************************************************************
 * JSON retrieval
 ************************************************************************************/
$( document ).ready(function() {   
   var url = "https://canvasjs.com/services/data/datapoints.php?xstart=1&ystart=10&length=100&type=json";

   $("#BarForm").submit(function() {
      alert("you reached here 1");
      var dataPoints = [];
      $.getJSON(url , function(data) {  
         alert("you reached spot 3");
         $.each(data, function(key, value){
            dataPoints.push({y: value[0], label: value[1]});
         });	
         barchart(true, "light2", "NEWB", "yBitch");
      }); 
   });
   $("#DonutForm").submit(function() {
      var dataPoints = [];
      $.ajax({
         url:        url,
         dataType:   "jsonp", // <== JSON-P request
         success:    function(data){
            $.each(data, function(key, value){ // <=== Note, `data.results`, not just `data`
               dataPoints.push({y: value[0], label: value[1]});// <=== Or `entry.from_user` would also work (although `entry['from_user']` is just fine)
            });
            donutchart(dataPoints, true, "light2", "NEWB");
            alert("hi"); // <== Note I've moved this (see #2 above)
         }
      });
   });

   $("#scattersubmit").onclick(function() {
      alert("You did it!");
      var dataPoints = [];
      $.getJSON(url, function(data) {  
         $.each(data, function(key, value){
            dataPoints.push({x: value[0], y: parseInt(value[1])});
         });	
         scatterchart(dataPoints, true, "light2", "NEWB", "xBitch", "yBitch");
      });
   });

   $("#LineForm").submit(function() {
      var dataPoints = [];
      $.getJSON(url, function(data) {  
         $.each(data, function(key, value){
            dataPoints.push({x: value[0], y: parseInt(value[1])});
         });	
         linechart(dataPoints, true, "dark1", "NEWB", "suck", "that") ;
      });
   });
});

/************************************************************************************
 * Graph Functions:
 * linechart()
 * barchart()
 * donutchart()
 * scatterchart()
 ************************************************************************************/

/** 
 * linechart
 * @param isInteractive Boolean. true if want chart to be interactive
 * @param theme   String of desired theme. The options are : “light1″, ”light2”, “dark1”, or “dark2”
 * @param title   String of the desired title
 * @param xAxisTitle String of the desired x-axis title
 * @param yAxisTitle String of the desired y-axis title
*/
function linechart(data, isInteractive, theme, title, xAxisTitle, yAxisTitle) {
   //setup the div that the graph is going to be rendered at
   setupGraphDiv();

   var chart = new CanvasJS.Chart("Graph" + idGraph.toString(), {
      animationEnabled: isInteractive,
      theme: theme,
      title:{
         text: title.toString()
      },
      axisX:{
         title : xAxisTitle.toString(),
      },
      axisY: {
         title: yAxisTitle.toString(),
      },
      legend:{
         cursor:"pointer",
         verticalAlign: "bottom",
         horizontalAlign: "left",
         dockInsidePlotArea: true,
         itemclick: toogleDataSeries
      },
      data: [{
         type: "line",
         showInLegend: true,
         name: "Total Visit",
         markerType: "square",
         xValueFormatString: "DD MMM, YYYY",
         color: "#F08080",
         dataPoints: data
      }]
   });
   
   getData(chart);

   function toogleDataSeries(e){
      if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
         e.dataSeries.visible = false;
      } else{
         e.dataSeries.visible = true;
      }
      chart.render();
   }
}

/** 
 * barchart
 * @param isInteractive Boolean. true if want chart to be interactive
 * @param theme   String of desired theme. The options are : “light1″, ”light2”, “dark1”, or “dark2”
 * @param title   String of the desired title
 * @param xAxisTitle String of the desired x-axis title
 * @param yAxisTitle String of the desired y-axis title
*/
function barchart(isInteractive, theme, title, yAxisTitle){
   setupGraphDiv();
   var chart = new CanvasJS.Chart("Graph" + idGraph.toString(), {
      animationEnabled: isInteractive,
      theme: theme,
      title:{
         text: title.toString()
      },
      axisY: {
         title: yAxisTitle.toString()
      },
      data: [{        
         type: "column",  
         dataPoints: [      
            { y: 300878, label: "Venezuela" },
            { y: 266455,  label: "Saudi" },
            { y: 169709,  label: "Canada" },
            { y: 158400,  label: "Iran" },
            { y: 142503,  label: "Iraq" },
            { y: 101500, label: "Kuwait" },
            { y: 97800,  label: "UAE" },
            { y: 80000,  label: "Russia" }
         ]
      }]
   });
   chart.render();
}

/** 
 * donutchart
 * @param isInteractive Boolean. true if want chart to be interactive
 * @param theme   String of desired theme. The options are : “light1″, ”light2”, “dark1”, or “dark2”
 * @param title   String of the desired title
 * @param xAxisTitle String of the desired x-axis title
 * @param yAxisTitle String of the desired y-axis title
*/
function donutchart(isInteractive, theme, title){
   setupGraphDiv();
   var chart = new CanvasJS.Chart("Graph" + idGraph.toString(), {
      animationEnabled: isInteractive,
      theme: theme,
      title:{
         text: title,
      },
      data: [{
         type: "doughnut",
         startAngle: 60,
         indexLabelFontSize: 17,
         indexLabel: "{label} - #percent%",
         toolTipContent: "<b>{label}:</b> {y} (#percent%)",
         dataPoints: [
            { y: 67, label: "Inbox" },
            { y: 28, label: "Archives" },
            { y: 10, label: "Labels" },
            { y: 7, label: "Drafts"},
            { y: 15, label: "Trash"},
            { y: 6, label: "Spam"}
         ]
      }]
   });
   chart.render();
}

/** 
 * scatterchart
 * @param isInteractive Boolean. true if want chart to be interactive
 * @param theme   String of desired theme. The options are : “light1″, ”light2”, “dark1”, or “dark2”
 * @param title   String of the desired title
 * @param xAxisTitle String of the desired x-axis title
 * @param yAxisTitle String of the desired y-axis title
*/
function scatterchart(isInteractive, theme, title, xAxisTitle, yAxisTitle){
   setupGraphDiv();
   var chart = new CanvasJS.Chart("Graph" + idGraph.toString(), {
      animationEnabled: isInteractive,
      zoomEnabled: true,
      theme: theme,
      title:{
         text: title
      },
      axisX: {
         title:xAxisTitle
      },
      axisY:{
         title: yAxisTitle
      },
      data: [{
         type: "scatter",
         dataPoints: [
            { x: 800, y: 350 },
            { x: 900, y: 450 },
            { x: 850, y: 450 },
            { x: 1250, y: 700 },
            { x: 1100, y: 650 },
            { x: 1350, y: 850 },
            { x: 1200, y: 900 },
            { x: 1410, y: 1250 },
            { x: 1250, y: 1100 },
            { x: 1400, y: 1150 },
            { x: 1500, y: 1050 },
            { x: 1330, y: 1120 },
            { x: 1580, y: 1220 },
            { x: 1620, y: 1400 },
            { x: 1250, y: 1450 },
            { x: 1350, y: 1600 },
            { x: 1650, y: 1300 },
            { x: 1700, y: 1620 },
            { x: 1750, y: 1700 },
            { x: 1830, y: 1800 },
            { x: 1900, y: 2000 },
            { x: 2050, y: 2200 },
            { x: 2150, y: 1960 },
            { x: 2250, y: 1990 }
         ]
      }]
   });
   chart.render();
}
/************************************************************************************
 * Setup of the Div element that the graphs will be rendered into 
 ************************************************************************************/

// Tracks the id of the graph
var idGraph = 0;

/**
 * Call prior to creating graph in order to create new div for the new graph to be placed in
 * Otherwise graphs will be added to current div.
 */
function setupGraphDiv(){
   ++idGraph;

   //creating div and remove button
   div = createGraphDiv();
   button = createRemoveButton(); 

   //add to the div with the id graphContainer
   $("#graphContainer").append(div).append(button);
}

/**
 * Should NEVER call except in setupGraphDiv()
 */
function createGraphDiv(){
   div = document.createElement('div');
        div.id = "Graph" + idGraph.toString();
        div.style = "height: 300px; width: 100%;";
        div.class = 'remove';
   return div;
}

/**
 * Should NEVER call except in setupGraphDiv()
 */
function createRemoveButton(){
   button = document.createElement('button'); 
   button.id = idGraph.toString();
   button.onclick = (function(){ 
       var graphDiv = document.getElementById("Graph" + this.id.toString());
       var buttonDiv = document.getElementById(this.id.toString());
       buttonDiv.parentNode.removeChild(buttonDiv);
       graphDiv.parentNode.removeChild(graphDiv); 
        
    })
    return button;
}