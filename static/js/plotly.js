$(document).ready(function() {
	// var trace1;
	function displayChart() {
		fetch('/asset_chart')
			.then(res => {
				return res.json();
			})
			.then(data => {
				let allValues = [[], []];
				let allLabels = [];
				let chartData = [
					{
						labels: allLabels,
						values: allValues[0],
						type: 'pie',
						name: 'Value',
						domain: {
							row: 1,
							column: 0
						},
						hoverinfo: 'label+value+name',
						title: 'Value per box'
					},
					{
						labels: allLabels,
						values: allValues[1],
						type: 'pie',
						name: 'Count',
						domain: {
							row: 1,
							column: 1
						},
						hoverinfo: 'label+value+name',
						title: 'Items per box'
					}
				];
				for (let i = 0; i < data.length; i++) {
					let row = data[i];
					console.log(row);
					allLabels.push(row['location']);
					allValues[0].push(row['inventoryValue']);
					allValues[1].push(row['inventoryCount']);
				}
				const layout = {
					title: 'Asset Inventory!',
					font: { size: 18 },
					grid: { rows: 1, columns: 2 }
				};
				console.log(chartData);
				Plotly.newPlot('myDiv', chartData, layout);
				// console.log('chartData', chartData);
				// return data;

				let myPlot = document.getElementById('myDiv');
				let d3 = Plotly.d3;
				let N = 16;
				let x = d3.range(N);
				let y = d3.range(N).map(d3.random.normal());

				myPlot.on('plotly_click', function(data) {
					var pts = '';
					for (var i = 0; i < data.points.length; i++) {
						pts =
							'x = ' +
							data.points[i].x +
							'\ny = ' +
							data.points[i].y.toPrecision(4) +
							'\n\n';
					}
					alert('Closest point clicked:\n\n' + 'abc');
				});
			});
	}
	displayChart();
});
