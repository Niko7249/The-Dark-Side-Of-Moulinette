console.log(obj);
let	div = document.getElementById('prova');
let	isPercFail = false;
div.innerHTML += `
<span>${obj.collectors[0].result[0].nodeid.replace('script_test/test/test_', '').replace('.py', '').toUpperCase()}</span>
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
<span>collected ${obj.summary.collected} item</span>
<div class="test">
	${obj.tests.map((test, i) => {
		const	color = test.outcome === 'passed' ? 'green' : 'red';
		isPercFail = color === 'red' ? true : isPercFail;
		const	perc = (100 / obj.summary.total) * (i + 1);
		return (`
			<div>
				<span>${test.nodeid.substring(test.nodeid.indexOf(':') + 2)}<span style="margin-left: 10px;" class="${color}">${test.outcome.toUpperCase()}</span></span>
				<span class="${isPercFail ? 'red' : 'green'}">[${perc === 100 ? perc : '&nbsp;' + perc}%]</span>
			</div>
		`);
	}).join('')}
</div>

${obj.summary.failed ? `
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
` + obj.tests.map((test, i) => {
	if (test.outcome === "failed")
		return (`
			<div style="margin-bottom: 5px; margin-top: 5px">
				<div class="title red">
					<div class="hr-container">
						<hr/>
					</div>
					<span>${test.keywords[0]}</span>
					<div class="hr-container">
						<hr/>
					</div>
				</div>
				<span>Result obtained: ${test.call?.crash?.message.slice(7, test.call?.crash?.message.indexOf('='))}</span><br>
				<span>Result expected: ${test.call?.crash?.message.substring(test.call?.crash?.message.indexOf('=') + 3)}</span>
			</div>
		`)
}).join('') : ''}

<div class="title ${obj.summary.failed ? 'red' : 'green'}">
	<div class="hr-container">
		<hr/>
		<hr/>
	</div>
	<span>${obj.summary.failed ? obj.summary.failed + '&nbsp;failed,' : ''}${obj.summary.passed ? '<span class="green">' + obj.summary.passed + '&nbsp;passed</span>' : '&nbsp;'}in&nbsp;${obj.duration > 0.009 ? obj.duration.toPrecision(1) : '0.01'}s
	</span>
	<div class="hr-container">
		<hr/>
		<hr/>
	</div>
</div>
`
