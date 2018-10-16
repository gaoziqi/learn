var gzq;
(function (gzq) {
    function add(x, y) {
        return x + y;
    }
    gzq.add = add;
})(gzq || (gzq = {}));
console.log(gzq.add(1, 2));
