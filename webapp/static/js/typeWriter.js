let span1 = document.querySelectorAll(".span1");
let span2 = document.querySelectorAll(".span2");
const waitTime = 3000;
const wrtSpeed = 80;

setTimeout(textInit, waitTime);
function textInit() {
	changeText();
}
function changeText(i = 0) {
	if (span2[i].textContent.length > 0) {
		span1[i].innerHTML += span2[i].textContent.slice(0, 1);
		span2[i].innerHTML = span2[i].textContent.slice(
			1,
			span2[i].textContent.length
		);
		setTimeout(changeText, wrtSpeed);
	} else if (i != span2.length - 1) setTimeout(changeText(i + 1), wrtSpeed);
}
