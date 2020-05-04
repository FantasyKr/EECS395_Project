/************************************************************************************
 * JSON retrieval
 ************************************************************************************/

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
      theme: "light2",
      title:{
         text: title
      },
      axisX:{
         title : xAxisTitle,
      },
      axisY: {
         title: yAxisTitle,
      },
      data: [{
         type: "line",
         dataPoints: data
      }]
   });
   
   chart.render();
}

/** 
 * barchart
 * @param isInteractive Boolean. true if want chart to be interactive
 * @param theme   String of desired theme. The options are : “light1″, ”light2”, “dark1”, or “dark2”
 * @param title   String of the desired title
 * @param xAxisTitle String of the desired x-axis title
 * @param yAxisTitle String of the desired y-axis title
*/
function barchart(data, isInteractive, theme, title, yAxisTitle){
   setupGraphDiv();
   var chart = new CanvasJS.Chart("Graph" + idGraph.toString(), {
      animationEnabled: isInteractive,
      theme: theme,
      title:{
         text: title
      },
      axisY: {
         title: yAxisTitle
      },
      data: [{        
         type: "column",  
         dataPoints: data
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
function donutchart(data, isInteractive, theme, title){
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
         dataPoints: data
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
function scatterchart(data, isInteractive, theme, title, xAxisTitle, yAxisTitle){
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
         dataPoints: data
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
   button.setAttribute("value", "Remove");

   button.onclick = (function(){ 
       var graphDiv = document.getElementById("Graph" + this.id.toString());
       var buttonDiv = document.getElementById(this.id.toString());
       buttonDiv.parentNode.removeChild(buttonDiv);
       graphDiv.parentNode.removeChild(graphDiv); 
        
    })
    return button;
}