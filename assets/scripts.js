
// var hamburger = document.querySelector(".hamburger");
// const sidebar = document.querySelector(".sidebar");
// const resizer = document.querySelector(".resizer");

var sidebar = document.getElementsByClassName("sidebar")[0];
var hamburger = document.getElementsByClassName("hamburger")[0];
var SIDEBAR_INITIAL_WIDTH='300px'
console.log(sidebar)
sidebar.style.width = SIDEBAR_INITIAL_WIDTH
hamburger.addEventListener("click", () => {
	const width = Number(sidebar.style.width.slice(0,-2))		
	if(width<250)
		sidebar.style.width =SIDEBAR_INITIAL_WIDTH;
	else
		sidebar.style.width="50px";
})


/// Sidebar Resize
const resizer = document.getElementsByClassName("resizer")[0];
console.log(resizer)
resizer.addEventListener("mousedown",
	(event) => {
			document.addEventListener("mousemove",resize  , false);
			document.addEventListener("mouseup", 
			() => {
				document.removeEventListener("mousemove", resize, false);
			}, false);	
	}
);
resize= (e) =>{
	let size="";
	if(e.x<=250)size = "50px";
	else size = `${e.x}px`;
	sidebar.style.width = size;
	console.log(e.x)
}




document.onkeydown = (keyDownEvent) => { 
 
	isKeyPressed[keyDownEvent.key] = true;
	if (isKeyPressed["a"] && isKeyPressed["b"]) {
	console.log("980000")
	};
}
