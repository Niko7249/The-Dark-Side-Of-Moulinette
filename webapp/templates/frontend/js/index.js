// console.log(obj);
// localStorage.setItem("testsJson", JSON.stringify(obj));
let div = document.getElementById("prova");

function getJson(path) {
	console.log(window.location.origin + path)
	fetch(window.location.origin + path)
		.then((response) => response.json())
		.then((json) => {
			console.log(json);
			printTerminal(json);
		});
}

// let testsJson = JSON.parse(localStorage.getItem("testsJson"));
function printTerminal(testsJson) {
	testsJson.map((fn) => {
		let isPercFail = false;
		div.innerHTML += `
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
							perc === 100 ? perc : "&nbsp;" + perc
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

			<div class="title ${fn.summary.failed ? "red" : "green"}">
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
