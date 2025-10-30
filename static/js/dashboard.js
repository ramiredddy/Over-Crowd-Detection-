document.addEventListener('DOMContentLoaded', function() {
    const alertList = document.getElementById('alert-list');
    const zonesDiv = document.getElementById('zones');
    const ctx = document.getElementById('densityChart').getContext('2d');
    let densityChart;

    function updateAlerts() {
        fetch('/alerts')
            .then(response => response.json())
            .then(data => {
                alertList.innerHTML = '';
                data.forEach(alert => {
                    const li = document.createElement('li');
                    li.textContent = `${new Date(alert.timestamp * 1000).toLocaleString()}: ${alert.message}`;
                    alertList.appendChild(li);
                });
            });
    }

    function updateDashboard() {
        fetch('/dashboard')
            .then(response => response.json())
            .then(data => {
                zonesDiv.innerHTML = '';
                const labels = [];
                const densities = [];

                for (const [zone, info] of Object.entries(data)) {
                    labels.push(zone);
                    densities.push(info.avg_density);

                    const zoneDiv = document.createElement('div');
                    zoneDiv.className = `zone ${info.high_risk_count > 0 ? 'high-risk' : ''}`;
                    zoneDiv.innerHTML = `
                        <h3>${zone}</h3>
                        <p>Average Density: ${info.avg_density.toFixed(2)}</p>
                        <p>High Risk Incidents: ${info.high_risk_count}</p>
                    `;
                    zonesDiv.appendChild(zoneDiv);
                }

                if (densityChart) {
                    densityChart.destroy();
                }
                densityChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Average Density',
                            data: densities,
                            backgroundColor: 'rgba(54, 162, 235, 0.2)',
                            borderColor: 'rgba(54, 162, 235, 1)',
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
            });
    }

    // Update every 5 seconds
    setInterval(() => {
        updateAlerts();
        updateDashboard();
    }, 5000);

    // Initial load
    updateAlerts();
    updateDashboard();
});
