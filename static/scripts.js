// Function to search a book by ISBN and navigate to a page
function searchBookByISBN(isbn) {
    // This function is optional now since the link is already set
    var googleSearchURL = `https://www.google.com/search?q=${isbn}`;
    const link = document.querySelector(`a[data-isbn="${isbn}"]`);
    
    // Open the link in a new window when clicked
    window.open(googleSearchURL, '_blank');
}

// Add event listeners for each book title
document.querySelectorAll('.book-title').forEach(function (element) {
    element.addEventListener('click', function (event) {
        // Get the ISBN from the data attribute
        const isbn = event.target.getAttribute('data-isbn');

        // Call the search function (if you want to open in a new window too)
        searchBookByISBN(isbn);
    });
});

// Function to show error modal
function showErrorModal(message) {
    const modal = document.getElementById("errorModal");
    const modalMessage = document.getElementById("errorMessage");

    modal.style.display = "block";
    modalMessage.textContent = message;

    // Close modal when clicking outside the modal
    modal.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };

    // Close button logic
    const closeButton = modal.querySelector("button");
    closeButton.onclick = function() {
        modal.style.display = "none";
    };
}

// Check if there are any flash messages and show modal if there are
if (window.flashMessages && window.flashMessages.length > 0) {
    showErrorModal(window.flashMessages[0]); // Show the first message
}

