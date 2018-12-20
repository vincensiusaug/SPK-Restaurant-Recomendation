
let rank = ['MCD', 'KFC', 'A&W'];
let percent = [0.6, 0.3, 0.1];
let y_location;
let size = [];
let sizeAnimation = [];
let speed = 0.01;
let spacing = 10;


function setup() {
    createCanvas(1200, 600);
    y_location = height/rank.length;
    for(let i=0; i<rank.length; ++i){
        size.push(width*percent[i]);
        sizeAnimation.push(0);
    }
    console.log(height/rank.length-spacing*2);
}

function draw() {
    background(51);
    for(let i=0; i<rank.length; ++i){
        sizeAnimation[i] = sizeAnimation[i] + size[i] * speed
        if(sizeAnimation[i]>size[i]){
            sizeAnimation[i] = size[i];
        }
        fill(129, 206, 15);
        rect(spacing, i*y_location+spacing, sizeAnimation[i], height/rank.length-spacing*2);
        fill(0);
        textSize((height/rank.length-spacing*2)/10);
        text(rank[i], spacing+sizeAnimation[i]/2, i*y_location+height/(rank.length*2));
    }
}
