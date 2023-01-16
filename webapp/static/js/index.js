let	div_ok = document.getElementById("terminal_ok");
let	div_ko = document.getElementById("terminal_ko");
let	url_path = window.location.pathname

if (url_path === "/" || url_path === "")
	document.querySelector('.home-content-container').classList.remove('d-none');

function getJson(json) { //prima era path
	console.log("222",json)
	if (url_path === "/tested")
    	printTerminal(json);
}

function closePopup() {
	let popCont = document.querySelector(".pop-container");
	popCont.classList.add('d-none')
}

function printTerminal(testsJson) {
	testsJson.map((fn) => {
		let isPercFail = false;
		div_ok.innerHTML += `
			<span>${fn.collectors[0].result[0].nodeid
				.replace("script_test/test/test_", "")
				.replace(".py", "")
				.toUpperCase()}</span>
			<div class="title">
				<div class="hr-container">
					<hr/>
					<hr/>
				</div>
				<span>test&nbsp;session&nbsp;started</span>
				<div class="hr-container">
					<hr/>
					<hr/>
				</div>
			</div>
			<span>collected ${fn.summary.collected} item</span>
			<div class="test">
				${fn.tests
					.map((test, i) => {
						const color =
							test.outcome === "passed" ? "green" : "red";
						isPercFail = color === "red" ? true : isPercFail;
						const perc = (100 / fn.summary.total) * (i + 1);
						return `
						<div>
							<span>${test.nodeid
								.substring(test.nodeid.indexOf(":") + 1)
								.replace(
									":",
									""
								)}<span style="margin-left: 10px;" class="${color}">${test.outcome.toUpperCase()}</span></span>
							<span class="${isPercFail ? "red" : "green"}">[${
							perc === 100 ? perc : "&nbsp;" + Math.round(perc)
						}%]</span>
						</div>
					`;
					})
					.join("")}
			</div>

			${
				fn.summary.failed
					? `
			<div class="title">
				<div class="hr-container">
					<hr/>
					<hr/>
				</div>
				<span>FAILURES</span>
				<div class="hr-container">
					<hr/>
					<hr/>
				</div>
			</div>
			` +
					  fn.tests
							.map((test, i) => {
								if (test.outcome === "failed")
									return `
						<div style="margin-bottom: 5px; margin-top: 5px">
							<div class="title red">
								<div class="hr-container">
									<hr/>
								</div>
								<span>${test.keywords[3].replace(/ /g, "&nbsp;")}</span>
								<div class="hr-container">
									<hr/>
								</div>
							</div>
							<span>Result obtained: ${test.call?.crash?.message.slice(
								7,
								test.call?.crash?.message.indexOf("=")
							)}</span><br>
							<span>Result expected: ${test.call?.crash?.message.substring(
								test.call?.crash?.message.indexOf("=") + 3
							)}</span>
						</div>
					`;
							})
							.join("")
					: ""
			}

			<div class="title summary ${fn.summary.failed ? "red" : "green"}">
				<div class="hr-container">
					<hr/>
					<hr/>
				</div>
				<span>${fn.summary.failed ? fn.summary.failed + "&nbsp;failed," : ""}${
			fn.summary.passed
				? '<span class="green">' +
				  fn.summary.passed +
				  "&nbsp;passed</span>"
				: "&nbsp;"
		}in&nbsp;${fn.duration > 0.009 ? fn.duration.toPrecision(1) : "0.01"}s
				</span>
				<div class="hr-container">
					<hr/>
					<hr/>
				</div>
			</div>
		`;
	});
	document.querySelector('.sld-trm-container').classList.remove('d-none')
}
