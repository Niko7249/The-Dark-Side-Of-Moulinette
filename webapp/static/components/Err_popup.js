class Err_popup extends HTMLElement {
    constructor() {
        super();

    }
    connectedCallback() {

        this.innerHTML = `
            <style>
                .pop-container {
                    width: 350px;
                    background-color: #0257df;
                    padding: 3px;
                    border-radius: 5px 5px 0 0;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    position: fixed;
                    top: 40vh;
                    left: 30%;
                    transform: scale(1.5);
                }
                .pop-container .pop-header {
                    padding-left: 5px;
                    padding-bottom: 3px;
                    font-size: 10px;
                    color: white;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                .pop-container .esc-btn {
                    color: white;
                    background-color: #E94A11;
                    border: 1.5px solid white;
                    border-radius: 3px;
                    font-weight: 900;
                    padding: 1px 3.5px;
                }
                .pop-container .esc-btn:active {
                    background-color: #cc410e;
                }
                .pop-container .pop-content {
                    background-color: #F8F6E6;
                    width: 100%;
                    height: 80px;
                    color: black;
                    display: flex;
                    flex-direction: column;
                }
                .pop-content .pop-mess {
                    font-size: 9px;
                    display: flex;
                    align-items: center;
                    padding: 7px 16px 5px 8px;
                }
                .pop-content .pop-mess span {
                    margin-left: 5px;
                }
                .pop-content .ok-btn {
                    margin: 0 auto;
                    border-color: black;
                    background-color: transparent;
                    padding: 2px;
                    font-size: 10px;
                }
                .pop-content .ok-btn > div {
                    border: 1.4px dotted black;
                    padding: 0px 18px;
                    border-radius: 2px;
                }
            </style>
            <div class="pop-container">
                <div class="pop-header">
                    <span>${this.getAttribute('title')}</span>
                    <button class="esc-btn" onclick="closePopup()">&#9747;</button>
                </div>
                <div class="pop-content">
                    <div class="pop-mess">
                        <img src="./static/assets/image/Removal-784.png" alt="Removal-784">
                        <span>${this.getAttribute('description')}</span>
                    </div>
                    <button class="ok-btn" onclick="closePopup()"><div>OK</div></button>
                </div>
            </div>
        `;
    }
}
customElements.define("err-popup", Err_popup);
