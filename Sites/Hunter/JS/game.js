var player = new Player('Bob', 4, 3, 3)
var animals = [
    new Chicken('Ryaba', 3, 5, 5),
    new Chicken('Biba', 3, 6, 5),
    new Chicken('Boba', 3, 5, 6),
]


function game_cicle(){
    // не поймал ли игрок курицу
    player.check_if_kurka_catched(animals)

    // все животные ходят
    for (animal of animals){
        animal.make_move(animals, player)
    }

    player.check_if_kurka_catched(animals)

    // все отрисовываются
    var matrix = create_matrix()  // создали пустую матрицу (с травинками)
    player.draw(matrix)  // отрисовали героя
    for (animal of animals){  // перебрали всех животных
        animal.draw(matrix)  // отрисовали каждое животное
    }
    draw_matrix(matrix)  // вывели матрицу на экран в виде таблички с картинками
    draw_interface(player) // рисуем панель с интерфейсом
}


function onKeyPress(event) {
    if (['w', 'a', 's', 'd'].includes(event.key)){
        player.move(event.key)
        game_cicle()
    }
}


game_cicle()
document.addEventListener('keypress', onKeyPress);