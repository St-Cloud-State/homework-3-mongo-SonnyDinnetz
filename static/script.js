function add_application() {
    const name = document.getElementById('name').value;
    const address = document.getElementById('address').value;

    const application = {
        name: name,
        address: address,
    };

    fetch('/api/add_application', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(application)
    })
        .then(response => response.json())
        .then(data => {
            alert(`${data['status']}!\nApplication Number: ${data['app_num']}\n${data['message']}`);
        })
        .catch(error => {
            console.error('Error adding application:', error);
        });
}

function check_status() {
    const number = document.getElementById('app_num').value;
    let send = {'app_num': number}

    fetch('/api/check_status', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(send)
    })
        .then(response => response.json())
        .then(data => {
            alert(`${data['status']}!\nApplication Number: ${data['app_num']}\n${data['message']}`);
        })
        .catch(error => {
            console.error('Error fetching application:', error);
        });
}

function change_status() {
    const number = document.getElementById('app_num').value;
    const status = document.getElementById('new_status').value;
    let send = {'app_num': number, 'status': status}

    fetch('/api/change_status', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(send)
    })
        .then(response => response.json())
        .then(data => {
            alert(`${data['status']}!\nApplication Number: ${data['app_num']}\n${data['message']}`);
        })
        .catch(error => {
            console.error('Error fetching application:', error);
        });
}

function add_note() {
    const number = document.getElementById('app_num').value;
    const note = document.getElementById('note').value;
    let send = {'app_num': number, 'note': note}

    fetch('/api/add_note', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(send)
    })
        .then(response => response.json())
        .then(data => {
            alert(`${data['status']}!\nApplication Number: ${data['app_num']}\n${data['message']}`);
        })
        .catch(error => {
            console.error('Error fetching application:', error);
        });
}

function get_application() {
    const number = document.getElementById('app_num').value;
    let send = {'app_num': number}

    fetch('/api/get_application', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(send)
    })
        .then(response => response.json())
        .then(data => {
            alert(`${data['status']}!\nApplication Number: ${data['app_num']}\n${data['message']}`);
        })
        .catch(error => {
            console.error('Error fetching application:', error);
        });
}