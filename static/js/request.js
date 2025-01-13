const requestButton = document.getElementById("btn-request");
const requestConfirm = document.getElementById("requestConfirm");

const requestModal = new bootstrap.Modal(document.getElementById("requestModal"));

/**
* Initializes request functionality for the provided button.
* 
* Retrieves the associated request ID upon click.
* Updates url.
* Opens Modal containing RequestForm.
* 
* *** CURRENTLY NON FUNCTIONAL ***
*/

requestButton.addEventListener("click", (e) => {
    let requestId = e.target.getAttribute("data-request_id");
    requestConfirm.href = `request-book/${requestId}`;
    requestModal.show();
});