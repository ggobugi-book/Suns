

/*
// Themes begin
am4core.useTheme(am4themes_animated);
// Themes end

var chart = am4core.create("chartdiv", am4plugins_forceDirected.ForceDirectedTree);
var networkSeries = chart.series.push(new am4plugins_forceDirected.ForceDirectedSeries())

var data = []
for(var i = 0; i < 15; i++){
  data.push({name: "Node " + i, value:Math.random() * 50 + 10});
}

chart.data = data;

networkSeries.dataFields.value = "value";
networkSeries.dataFields.name = "name";
networkSeries.dataFields.children = "children";
networkSeries.nodes.template.tooltipText = "{name}:{value}";
networkSeries.nodes.template.fillOpacity = 1;
networkSeries.dataFields.id = "name";
networkSeries.dataFields.linkWith = "linkWith";


networkSeries.nodes.template.label.text = "{name}"
networkSeries.fontSize = 10;

var selectedNode;

*//*var label = chart.createChild(am4core.Label);
label.text = "Click on nodes to link"
label.x = 50;
label.y = 50;
label.isMeasured = false;*//*


networkSeries.nodes.template.events.on("up", function (event) {
  var node = event.target;
  if (!selectedNode) {
    node.outerCircle.disabled = false;
    node.outerCircle.strokeDasharray = "3,3";
    selectedNode = node;
  }
  else if (selectedNode == node) {
    node.outerCircle.disabled = true;
    node.outerCircle.strokeDasharray = "";
    selectedNode = undefined;
  }
  else {
    var node = event.target;

    var link = node.linksWith.getKey(selectedNode.uid);

    if (link) {
      node.unlinkWith(selectedNode);
    }
    else {
      node.linkWith(selectedNode, 0.2);
    }
  }
})*/
window.onload=function(){
Highcharts.chart('container', {

    title: {
        text: 'Highcharts Dependency Wheel'
    },

    accessibility: {
        point: {
            descriptionFormatter: function (point) {
                var index = point.index + 1,
                    from = point.from,
                    to = point.to,
                    weight = point.weight;

                return index + '. From ' + from + ' to ' + to + ': ' + weight + '.';
            }
        }
    },

    series: [{
        keys: ['from', 'to', 'weight'],
        data: [
            ['Brazil', 'Portugal', 5],
            ['Brazil', 'France', 1],
            ['Brazil', 'Spain', 1],
            ['Brazil', 'England', 1],
            ['Canada', 'Portugal', 1],
            ['Canada', 'France', 5],
            ['Canada', 'England', 1],
            ['Mexico', 'Portugal', 1],
            ['Mexico', 'France', 1],
            ['Mexico', 'Spain', 5],
            ['Mexico', 'England', 1],
            ['USA', 'Portugal', 1],
            ['USA', 'France', 1],
            ['USA', 'Spain', 1],
            ['USA', 'England', 5],
            ['Portugal', 'Angola', 2],
            ['Portugal', 'Senegal', 1],
            ['Portugal', 'Morocco', 1],
            ['Portugal', 'South Africa', 3],
            ['France', 'Angola', 1],
            ['France', 'Senegal', 3],
            ['France', 'Mali', 3],
            ['France', 'Morocco', 3],
            ['France', 'South Africa', 1],
            ['Spain', 'Senegal', 1],
            ['Spain', 'Morocco', 3],
            ['Spain', 'South Africa', 1],
            ['England', 'Angola', 1],
            ['England', 'Senegal', 1],
            ['England', 'Morocco', 2],
            ['England', 'South Africa', 7],
            ['South Africa', 'China', 5],
            ['South Africa', 'India', 1],
            ['South Africa', 'Japan', 3],
            ['Angola', 'China', 5],
            ['Angola', 'India', 1],
            ['Angola', 'Japan', 3],
            ['Senegal', 'China', 5],
            ['Senegal', 'India', 1],
            ['Senegal', 'Japan', 3],
            ['Mali', 'China', 5],
            ['Mali', 'India', 1],
            ['Mali', 'Japan', 3],
            ['Morocco', 'China', 5],
            ['Morocco', 'India', 1],
            ['Morocco', 'Japan', 3],
            ['Japan', 'Brazil', 1]
        ],
        type: 'dependencywheel',
        name: 'Dependency wheel series',
        dataLabels: {
            color: '#333',
            textPath: {
                enabled: true,
                attributes: {
                    dy: 5
                }
            },
            distance: 10
        },
        size: '95%'
    }]

});


}




