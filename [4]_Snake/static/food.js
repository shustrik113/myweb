function Food(matrix) {
    this.matrix = matrix;

    randomCell = function() {
        var min = 1;
        var max = this.matrix.cols-1;
        var rand = min + Math.random() * (max + 1 - min);
        rand = Math.round(rand);
        return rand;
    }

    //Checking is food putted on body of snake or not
    var row, col;
    do {
        row = randomCell();
        col = randomCell();
    } while (this.matrix.getCell(row, col, "snake"))
    this.matrix.setFood(row, col, true);
}