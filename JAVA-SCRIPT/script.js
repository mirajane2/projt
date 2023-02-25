var cobra;
var goldenApple;
var game;
window.onload = function()
{
    game = new Snakegame(900, 600, 30, 100);
    cobra =  new Snake([[6,4], [5,4], [4,4]], "right");
    goldenApple = new Apple([10, 10]);
    game.init(cobra, goldenApple);
}
document.onkeydown = function handleKeyDown(e) 
{
    var key = e.keyCode;
    var newDirection;
    switch (key) {
        case 37:
            newDirection = "left";
            break;
        case 40 :
            newDirection = "up"
            break;
        case 39:
            newDirection = "right";
            break;
        case 38:
            newDirection = "down";
            break;
        case 32:
            cobra =  new Snake([[6,4], [5,4], [4,4]], "right");
            goldenApple = new Apple([10, 10]);
            game.init(cobra, goldenApple);
            break;
        default:
            return;    
    }
    game.cobra.setDirection(newDirection);
}
function Snakegame(canvasWidth, canvasHeight, blocSize, delay) {
    this.canvas = document.createElement("canvas");
    this.canvas.width = canvasWidth;
    this.canvas.height = canvasHeight;
    this.canvas.style.border = "30px solid gray";
    this.canvas.style.margin = "50px auto";
    this.canvas.style.display = "block";
    this.canvas.style.backgroundColor = "#ddd";
    document.body.appendChild(this.canvas);
    this.ctx =this.canvas.getContext("2d"); ;
    this.blocSize = blocSize;
    this.delay = delay;
    this.cobra;
    this.goldenApple;
    this.widthInBlock = canvasWidth/blocSize;
    this.heightInBlock = canvasHeight/blocSize;
    this.score;
    var instance = this;
    var timeout;

    this.init =  function(cobra,goldenApple) {  
        this.cobra = cobra;
        this.goldenApple =goldenApple;
        this.score = 0;
        clearTimeout(timeout);
        refresh();
    }
    var refresh = function() {
        instance.cobra.advance();
        if(instance.checkCollision()) {  
            instance.gameOver();         
        }
        else {
            if(instance.cobra.eatApple(instance.goldenApple)) {
                instance.score +=1
                instance.cobra.ateApple = true;
                do {
                    instance.goldenApple.setNewPosition(instance.widthInBlock, instance.heightInBlock);
                }
                while(instance.goldenApple.onApple(instance.cobra))
            }
            instance.ctx.clearRect(0, 0, instance.canvas.width, instance.canvas.height);
            instance.drawScore();    
            instance.cobra.draw(instance.ctx, instance.blocSize);
            instance.goldenApple.draw(instance.ctx, instance.blocSize);  
            timeout = setTimeout(refresh, delay);
        }
    }
    this.checkCollision = function() {
        var wall = false;
        var cobraCollision =  false;
        var head = this.cobra.body[0];
        var rest = this.cobra.body.slice(1);
        var cobraX = head[0];
        var cobraY = head[1];
        var minX = 0;
        var minY = 0;
        var maxX = this.widthInBlock - 1;
        var maxY = this.heightInBlock -1;
        var noCanvas = cobraX < minX || cobraX > maxX;
        var noCanvas2 = cobraY < minY || cobraY > maxY;

        if(noCanvas || noCanvas2){
            wall = true;
        }
        for(var i = 0; i < rest.length; i++) {
            if(cobraX === rest[i][0] && cobraY === rest[i][1]) {
                cobraCollision = true;
            }
        }
        return wall || cobraCollision;
    };
    this.gameOver =  function() {
        this.ctx.save();
        this.ctx.font = "bold 70px sans-serif";
        this.ctx.fillStyle = "#000"
        this.ctx.textAlign = "center";
        this.ctx.textBaseline = "middle";
        this.ctx.strokeStyle = "white"
        this.ctx.lineWidth = 5;
        var centreX = this.canvas.width/2 ;
        var centreY = this.canvas.height/2 ;
        this.ctx.strokeText("Game Over", centreX, centreY-180);
        this.ctx.fillText("Game Over", centreX, centreY-180);
        this.ctx.font = "bold 30px sans-serif";
        this.ctx.strokeText("Reessayer", centreX, centreY-120);
        this.ctx.fillText("Reessayer", centreX, centreY-120)
        this.ctx.restore();
    }
    this.drawScore = function() {
        this.ctx.save();
        this.ctx.font = "bold 200px sans-serif";
        this.ctx.fillStyle = "gray"
        this.ctx.textAlign = "center";
        this.ctx.textBaseline = "middle";
        var centreX = this.canvas.width/2 ;
        var centreY = this.canvas.height/2 ;
        this.ctx.fillText(this.score.toString(), centreX, centreY);
        this.ctx.restore();
    }
}
function Snake(body, direction) {
    this.body = body;
    this.direction = direction;
    this.ateApple =  false;
    this.draw = function(ctx, blocSize) {
        ctx.save();
        ctx.fillStyle = "#ff0000";
        for(var i = 0; i < this.body.length; i++) {
            var x = this.body[i][0] * blocSize;
            var y = this.body[i][1] * blocSize;
            ctx.fillRect(x, y, blocSize, blocSize);
        }
        ctx.restore();       
    };
    this.advance = function() {
        var next = this.body[0].slice();
        switch (this.direction) {
            case "left":
                next[0] -= 1;
                break;
            case "right" : 
                next[0] += 1;
                break;
            case "down":
                next[1] -= 1;
                break;
            case "up":
                next[1] += 1;
                break;
            default:
                throw("Invalid Direction");
        }
        this.body.unshift(next);
        if(!this.ateApple)
            this.body.pop()
        else
            this.ateApple = false;     
    };
    this.setDirection = function(newDirection) {
        var allowedDirection;
        switch (this.direction) {
            case "left":
            case "right" : 
                allowedDirection = ["up", "down"];
                break;
            case "down":
            case "up":
                allowedDirection = ["left", "right"];
                break;
            default:
                throw("Invalid Direction");
        }
        if(allowedDirection.indexOf(newDirection) > -1){
            this.direction = newDirection;
        }
    };
    this.eatApple = function(appleToEat) {
        var head = this.body[0];
        if(head[0] === appleToEat.position[0] && head[1] === appleToEat.position[1])
            return true;
        else 
            return false;
    };  
}
function Apple(position){
    this.position = position;
    this.draw =  function(ctx, blocSize){
        ctx.save();
        ctx.fillStyle = "#33cc33";
        ctx.beginPath();
        var radius = blocSize/2;
        var x = this.position[0]*blocSize + radius;
        var y = this.position[1]*blocSize + radius;
        ctx.arc(x, y, radius, 0, Math.PI*2, true);
        ctx.fill();
        ctx.restore();
    };
    this.setNewPosition = function(widthInBlock,heightInBlock) {
        var newX = Math.round(Math.random()*(widthInBlock-1));
        var newY = Math.round(Math.random()*(heightInBlock-1));
        this.position = [newX, newY];
    };
    this.onApple = function(cobra) {
        var oncobra = false;
        for (var i = 0; i < cobra.body.length; i++) {
            if(this.position[0] === cobra.body[i][0] && this.position[1] === cobra.body[i][1] ) {
                oncobra = true;
            }               
        }
        return oncobra;
    };

}

 


