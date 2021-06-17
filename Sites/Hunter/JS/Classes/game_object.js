class GameObject {
    constructor(name, hp, i, j, sprite){
        this.name = name
        this.hp = hp
        this.i = i
        this.j = j
        this.sprite = sprite
    }

    move(direction){
        if (direction == 'w'){
            if (this.i != 0){
                this.i -= 1
            }
        } else if (direction == 'a'){
            if (this.j == 0){
                this.j = M - 1
            } else {
                this.j -= 1
            }
        } else if (direction == 's'){
            if (this.i != N - 1){
                this.i += 1
            }
        } else if (direction == 'd'){
            if (this.j == M - 1){
                this.j = 0
            } else {
                this.j += 1
            }
        }
    }

    draw(matrix){
        // Отвечает за отрисовку игрока на матрице
        matrix[this.i][this.j] = this.sprite
    }
}
