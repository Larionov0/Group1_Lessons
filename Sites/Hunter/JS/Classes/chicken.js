class Chicken extends GameObject{
    constructor(name, hp, i, j, sprite='https://media.tenor.com/images/c92bbe75ae5819e5bd77db2dc1dd272c/tenor.gif'){
        super(name, hp, i, j, sprite)
    }

    make_move(animals, player){
        var dir = ['w', 'a', 's', 'd'].random_choice()
        this.move(dir)
    }
}