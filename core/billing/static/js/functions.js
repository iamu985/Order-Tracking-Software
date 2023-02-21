$(document).ready(function () {

    function searchBarFunction() {

        /*----------------------------------------------------------------
        Function for search bar
        1. List will be automatically dropped when Searchbar is focused
        2. When Focused is automatically shift focus to last instantly added item
        3. Shortcut to focus Searchbar CTRL + I
        4. Shortcut to Focus Out ESC or ALT
        ----------------------------------------------------------------*/
        var instantlyAdded = $('#instantly-added');
        const searchBar = $("#search-bar004");
        const searchTarget = $("#search-bar004-target");
        // Search Bar on Focus
        searchBar.on('focus', function () {
            searchTarget.animate({ height: 'show' }, 200);
        });
        // Search Bar on Focusout
        searchBar.on('blur', function () {
            searchTarget.animate({ height: 'hide' }, 200);
            searchBar.val('');
            instantlyAdded.focus();
        });
        // Search Bar focus shortcuts ==> Ctrl + I
        $(document).keydown(function (event) {
            if (event.ctrlKey && event.which === 73) { // check for Ctrl+I
                event.preventDefault();
                searchBar.focus();

            }
        });
        // Function focusout on key press Esc or Alt and focus to instantly added element
        $(document).keydown(function (event) {
            if (event.which === 27 || event.altKey) { // check for esc or alt
                event.preventDefault();
                searchBar.blur();
            }

        });


    }/* End of search Bar Function */

    searchBarFunction();
});/* End of  document Ready Function */