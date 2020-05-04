/************************************************************************************
 * JSON retrieval
 ************************************************************************************/
$( document ).ready(function() {
   var url = "https://canvasjs.com/services/data/datapoints.php?xstart=1&ystart=10&length=100&type=json";
   var modalMaster = document.getElementById('myMasterModal')
   var modalLine = document.getElementById('myLineModal');
   var modalBar = document.getElementById('myBarModal');
   var modalDonut = document.getElementById('myDonutModal');
   var modalScatter = document.getElementById('myScatterModal');
   var attributeClicked = false

   $('#attributeSel').click(function (){
      var select = document.getElementById("attributeSel").innerHTML;
      var select2 =  $('#attribute2').innerHTML;
      console.log(select);
      console.log(typeof select);
      var newOptions = select.split(",");
      console.log(newOptions);
      var selectedOption = newOptions[0];

      var select2 = document.getElementById("attributeSel");
      if (attributeClicked == false) {
         $.each(newOptions, function(text, value) {
            select2.appendChild(new Option(value, text));
         });
      }

      attributeClicked = true
      console.log(selectedOption);
   }); 

   var barfrm = $('#BarForm');
   $('#BarForm').submit(function () {
      var dataPoints = [];
      console.log("creating bar form");

      $.ajax({
         type: barfrm.attr('method'),
         url: barfrm.attr('action'),
         data: $("#BarForm").serialize(),
         success: function (formData) {
            $.getJSON('http://localhost:8000/regAnalysis/test.json&callback=?', function(data) {
               console.log("getting data");
               $.each(data, function(key, value){ // <=== Note, `data.results`, not just `data`
                  dataPoints.push({y: value[0], label: value[1]});// <=== Or `entry.from_user` would also work (although `entry['from_user']` is just fine)
               });
               barchart(dataPoints, true, $('#barTheme').val(), $('#bartitle').val() , $('#barYAxisTitle').val());
            });
         }
      });
      //close the modal
      modalBar.style.display = "none";
      modalMaster.style.display = "none";
      return false;
   });

   var donutfrm = $('#DonutForm');
   $('#DonutForm').submit(function () {
      var dataPoints = [];
      console.log("creating donut graph");

      $.ajax({
         type: donutfrm.attr('method'),
         url: donutfrm.attr('action'),
         data: $("#DonutForm").serialize(),
         success: function (formData) {
            $.getJSON(url, function(data) {
               console.log("getting data for donut graph");
               $.each(data, function(key, value){ // <=== Note, `data.results`, not just `data`
                  dataPoints.push({y: value[0], label: value[1]});// <=== Or `entry.from_user` would also work (although `entry['from_user']` is just fine)
               });
               donutchart(dataPoints, true,  $('#donutTheme').val(), $('#donuttitle').val());
            });
         }
      });
      //close the modal
      modalDonut.style.display = "none";
      modalMaster.style.display = "none";
      return false;
   });

   var scatterfrm = $('#ScatterForm');
   $('#ScatterForm').submit(function () {
      var dataPoints = [];
      console.log("creating donut graph");

      $.ajax({
         type: scatterfrm.attr('method'),
         url: scatterfrm.attr('action'),
         data: $("#ScatterForm").serialize(),
         success: function (formData) {
            $.getJSON(url, function(data) {
               console.log("getting data for donut graph");
               $.each(data, function(key, value){ // <=== Note, `data.results`, not just `data`
                  dataPoints.push({x: value[0], y: parseInt(value[1])});// <=== Or `entry.from_user` would also work (although `entry['from_user']` is just fine)
               });
               scatterchart(dataPoints, true,  $('#scatterTheme').val(), $('#scattertitle').val(), $('#scatterXAxisTitle').val(), $('#scatterYAxisTitle').val());
            });
         }
      });
      //close the modal
      modalScatter.style.display = "none";
      modalMaster.style.display = "none";
      return false;
   });

   var frm = $('#LineForm');
   $('#LineForm').submit(function () {
      var dataPoints = [];
      $.ajax({
         type: frm.attr('method'),
         url: frm.attr('action'),
         data: $("#LineForm").serialize(),
         success: function (formData) {
            $.getJSON(url, function(data) {
               $.each(data, function(key, value){ // <=== Note, `data.results`, not just `data`
                  dataPoints.push({x: value[0], y: parseInt(value[1])});// <=== Or `entry.from_user` would also work (although `entry['from_user']` is just fine)
               });
               linechart(dataPoints, true, $('#lineTheme').val(), $('#linetitle').val() , $('#lineXAxisTitle').val(), $('#lineYAxisTitle').val());
            });
         }
      });
      //close the modal
      modalLine.style.display = "none";
      modalMaster.style.display = "none";
      return false;
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
