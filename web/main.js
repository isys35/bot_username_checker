window.addEventListener('load', init, false);

function init(e) {
    var submitButton = document.getElementById('submit');
    submitButton.addEventListener('click', save_api_config, false);
}

function save_api_config() {
        let api_id = document.getElementById('api_id').value;
        let api_hash = document.getElementById('api_hash').value;
        eel.save_api_config(api_id, api_hash)();
        document.location.href = 'http://localhost:8000/main.html?';
    }