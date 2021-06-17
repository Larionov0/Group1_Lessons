class Player extends GameObject {
    constructor(name, hp, i, j, sprite='https://i.pinimg.com/originals/d7/b3/da/d7b3da3d4b19b7f0c44673374158df0a.gif', main_weapon={}){
        super(name, hp, i, j, sprite)
        this.main_weapon = main_weapon
        this.details = 0
    }

    say_hi(){
        console.log(this.name + ': Hello! :)')
    } 

    check_if_kurka_catched(animals){
        for (var animal of animals){
            if (animal instanceof Chicken){
                if (animal.i == this.i && animal.j == this.j){
                    this.details += 3
                    animals.remove(animal)
                    break
                }
            }
        }
    }
}
