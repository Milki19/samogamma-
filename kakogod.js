console.log("Script loaded");
window.addEventListener("load", function(){
    
document.getElementById('chart1-button').addEventListener('click', function () {
    console.log("Uhvatio dugme")
    fetch('/api/chart1-data')
        .then(response => response.json())
        .then(data => {
            drawChart(data);
        })
        .catch(error => console.error("Greška prilikom poziva API endpointa:", error));
});

document.getElementById('chart2-button').addEventListener('click', function () {
    fetch('/api/chart2-data')
        .then(response => response.json())
        .then(data => {
            drawChart(data);
        })
        .catch(error => console.error("Greška prilikom poziva API endpointa:", error));
});

document.getElementById('chart3-button').addEventListener('click', function () {
    fetch('/api/chart3-data')
        .then(response => response.json())
        .then(data => {
            drawChart(data);
        })
        .catch(error => console.error("Greška prilikom poziva API endpointa:", error));
});

});

function drawChart(chartData) {
    const labels = chartData.map(item => item.Course);
    const scores = chartData.map(item => item.total_points_scored);
    const ctx = document.getElementById('student-chart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Total Points Scored',
                data: scores,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
