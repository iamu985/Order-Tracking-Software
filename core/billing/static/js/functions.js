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
            searchBar.val('');
        });

        /* Keypress Events*/
        $(document).keydown(function (event) {
            if (event.ctrlKey && event.which === 73) { // check for Ctrl+I
                event.preventDefault();
                searchBar.focus();

            }

            if (event.which === 27 || event.altKey) { // check for esc or alt
                event.preventDefault();
                searchTarget.animate({ height: 'hide' }, 200);
                searchBar.blur();
            }

            if (event.which === 9) { // Check for tab whole Search list is visible3
                if (searchTarget.is(':visible')) {
                    event.preventDefault();
                    menuItems();
                }
            }
        });


    }/* End of search Bar Function */

    searchBarFunction();

    function menuItems() {
        // alert('Please select');
        var max = $("#search-bar004-target ul li").length;
        var min = 0;
        var pointer = 0;

        $(document).keydown(function (event) {
            if (event.which === 40) { // check for Ctrl+I
                event.preventDefault();
                if (pointer < max - 1) {
                    $('#search-bar004-target ul li').eq(pointer).css({ 'background-color': '#fff' });
                    pointer++;
                }

            }

            $('#search-bar004-target ul li').eq(pointer).css({ 'background-color': 'red' });
        });

    }
});/* End of  document Ready Function */