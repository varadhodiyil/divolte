google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(loadData);

function loadData()
{
	var json_data=[];
	$.getJSON( "/getData/", function( data ) 
	{
		json_data.push(['Events', 'Events']);
		  $.each( data.result, function( key, val ) 
		  {
			   	json_data.push([key,val]);
		  });
		  drawAxisTickColors(json_data);
	});

}
var data=[];

function drawAxisTickColors(json_data) 
{
  var data = google.visualization.arrayToDataTable(json_data);
	var options = 
	{
	    title: 'Event Clicks',
	    chartArea: {width: '50%'},
	    hAxis: {
	      title: 'Count',
	      minValue: 0
	    },
	    vAxis: {
	      title: 'Events'
	    }
	};
	var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
	chart.draw(data, options);
}