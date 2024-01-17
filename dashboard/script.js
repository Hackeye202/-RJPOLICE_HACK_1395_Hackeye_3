function addImage() {
    var table = document.getElementById('image-table');
    var index = table.rows.length - 1;

    var row = table.insertRow(table.rows.length);
    row.className = 'image-input';
    row.setAttribute('data-index', index);

    var cellIndex = row.insertCell(0);
    cellIndex.innerHTML = index;
    var cellName = row.insertCell(1);
    cellName.innerHTML = '<td><input type="text" name="names[]" required></td>';

    var cellFile = row.insertCell(2);
    cellFile.innerHTML = '<input type="file" name="images[]" accept="image/*" onchange="previewImage(this)" required>';

    var cellPreview = row.insertCell(3);
    cellPreview.innerHTML = '<img id="previewImage' + index + '" alt="Image Preview" style="max-width:100px; max-height:100px;">';

    var cellAction = row.insertCell(4);
    cellAction.innerHTML = '<button type="button" id="remove-button" onclick="removeImage(this)">Remove</button>';
}

function previewImage(input) {
    var index = input.closest('tr').getAttribute('data-index');
    var preview = document.getElementById('previewImage' + index);

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            preview.src = e.target.result;
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function removeImage(button) {
    var row = button.closest('tr');
    var index = row.getAttribute('data-index');

    row.remove();

    var table = document.getElementById('image-table');
    var rows = table.getElementsByClassName('image-input');

    for (var i = 0; i < rows.length; i++) {
        rows[i].setAttribute('data-index', i);
        rows[i].cells[0].innerHTML = i;
        rows[i].querySelector('input').setAttribute('name', 'names[]');
        rows[i].querySelector('img').setAttribute('id', 'previewImage' + i);
    }
}
