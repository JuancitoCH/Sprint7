var ctx = document.getElementById('myChart')
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Venta',
            data: [],
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
})

const url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
fetch(url)
.then(response=>response.json())
.then(data=>mostrar(data))

function mostrar(data){
    console.log(data)
    data.forEach(element => {
        myChart.data['labels'].push(element.casa.nombre)
        myChart.data.datasets[0].data.push(Number.parseFloat(element.casa.venta))
        myChart.update()
        
    })
}