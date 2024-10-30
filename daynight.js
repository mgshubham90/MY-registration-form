const toggleButton = document.getElementById('toggle-button');
const body = document.body;

// Set initial mode based on local storage or default to day mode
if (localStorage.getItem('mode') === 'night') {
    body.classList.add('night-mode');
    toggleButton.textContent = 'Switch to Day Mode';
} else {
    body.classList.add('day-mode');
    toggleButton.textContent = 'Switch to Night Mode';
}

// Toggle between day and night mode
toggleButton.addEventListener('click', () => {
    if (body.classList.contains('day-mode')) {
        body.classList.remove('day-mode');
        body.classList.add('night-mode');
        toggleButton.textContent = 'Switch to Day Mode';
        localStorage.setItem('mode', 'night');
    } else {
        body.classList.remove('night-mode');
        body.classList.add('day-mode');
        toggleButton.textContent = 'Switch to Night Mode';
        localStorage.setItem('mode', 'day');
    }
});
