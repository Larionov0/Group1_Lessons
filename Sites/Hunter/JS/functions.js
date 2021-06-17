function create_matrix(n=N, m=M){
    // var grass_src = 'https://i.pinimg.com/originals/fa/29/d3/fa29d32e85cbc1c6e5277b1917fbeec5.jpg'
    var grass_src = 'https://images.unsplash.com/photo-1533460004989-cef01064af7e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1yZWxhdGVkfDd8fHxlbnwwfHx8fA%3D%3D&w=1000&q=80'
    var matrix = []
    var i = 0
    while (i < n) {
        var row = [];
        var j = 0
        while (j < m) {
            row.push(grass_src)
            j += 1
        }
        matrix.push(row)
        i += 1
    }
    return matrix
}


function draw_matrix(matrix){
    var game = document.getElementById('game')
    var table_html = '<table>'
    for (row of matrix){
        table_html += '<tr>'
        for (img_src of row){
            table_html += '<td><img class="sprite" src="' + img_src + '"></td>'
        }
        table_html += '</tr>'
    }
    table_html += '</table>'
    game.innerHTML = table_html
}


function draw_interface(player){
    var interface_panel = document.getElementById('interface_panel')

    var html = ''
    html += `<div id='img_place'><img src='${player.sprite}'></div>`
    html += '<div id="info"> <h3>' + player.name + '</h3>'
    html += `<p>Детали: ${player.details}</p> </div>`
    interface_panel.innerHTML = html
}

