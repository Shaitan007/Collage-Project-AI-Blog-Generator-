// script.js
document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const searchButton = document.getElementById("searchButton");
    const searchResultsContainer = document.getElementById("searchResultsContainer");

    function displaySearchResults(searchTerm) {
       
        searchResultsContainer.innerHTML = `<p>Search results for: ${searchTerm}</p>`;
    }

    function handleSearch() {
        const searchTerm = searchInput.value.trim();
        if (searchTerm !== "") {
            displaySearchResults(searchTerm);
        }
    }

    searchButton.addEventListener("click", handleSearch);

    searchInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            handleSearch();
        }
    });
});
