// Ensure the page content is loaded
window.addEventListener('DOMContentLoaded', function () {
    // Get the game card element
    var cardElement = document.getElementById('card');

    // Create a Hammer manager to handle the gestures
    var hammerManager = new Hammer(cardElement);

    // Enable only horizontal swipes
    hammerManager.get('swipe').set({direction: Hammer.DIRECTION_HORIZONTAL});

    // Handle swipe left
    hammerManager.on('swipeleft', function () {
        navigate(1); // Next card
    });

    // Handle swipe right
    hammerManager.on('swiperight', function () {
        navigate(-1); // Previous card
    });
});