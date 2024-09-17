$.ajax(
    {
        url: "/pm25-data",
        type: "GET",
        dataType: "json",
        success: (data) => {
            console.log(data);
            drawChart(chart1, data["site"], data["pm25"], title = "pm2.5數據", name = "pm2.5");
        }
    }
);


// 基于準備好的dom，初始化echarts實例
let chart1 = echarts.init(document.getElementById('main'));

function drawChart(chart, xdata, ydata, title = "圖表", name = "數值") {


    // 指定圖表的配置项和數據
    let option = {
        title: {
            text: title
        },
        tooltip: {},
        legend: {
            data: [name]
        },
        xAxis: {
            data: xdata
        },
        yAxis: {},
        series: [
            {
                name: name,
                type: 'bar',
                data: ydata
            }
        ]
    };

    // 使用刚指定的配置项和数据显示图表。
    chart.setOption(option);
}

// document.querySelector("h1").innerText = "123"
// 使用jquery的寫法
$("h1").css("color", "green")
$("h1").click(() => {
    alert("test!")
})