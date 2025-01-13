const requestButton = document.getElementById("btn-request");
const requestForm = document.getElementById("requestForm");
const requestConfirm = document.getElementById("requestConfirm")

const requestModal = new bootstrap.Modal(document.getElementById("requestModal"));

/**
* Initializes request functionality for the provided button.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

requestButton.addEventListener("click", (e) => {
    let requestId = e.target.getAttribute("data-request_id");
    requestConfirm.href = `request-book/${requestId}`;
    requestModal.show();
});