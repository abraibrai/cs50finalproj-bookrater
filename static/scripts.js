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
