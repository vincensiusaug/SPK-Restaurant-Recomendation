
let rank = ['mcd', 'kfc', 'a&w'];
let percent = [0.6, 0.3, 0.1];
let y_location;
let size = [];
let sizeAnimation = [];
let speed = 0.01;


function setup() {
    createCanvas(1200, 600);
    y_location = height/rank.length;
    for(let i=0; i<rank.length; ++i){
        size.push(width*percent[i]);
        sizeAnimation.push(0);
    }

}

function draw() {
    background(51);
    for(let i=0; i<rank.length; ++i){
        sizeAnimation[i] = sizeAnimation[i] + size[i] * speed
        if(sizeAnimation[i]>size[i]){
            sizeAnimation[i] = size[i];
        }
    }
    for(let i=0; i<rank.length; ++i){
        fill(129, 206, 15);
        rect(0, i*y_location, sizeAnimation[i], height/rank.length);
    }
}
