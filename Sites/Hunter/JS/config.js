Array.prototype.random_choice = function(){
    return this[Math.floor(Math.random()*this.length)];
}
Array.prototype.remove = function (value) {
var index = this.indexOf(value);
    if (index > -1) {
        this.splice(index, 1);
    }
}


var N = 13
var M = 20

