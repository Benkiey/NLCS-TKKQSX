
let isSpinning = false;
let spinTimeout;

function startContinuousSpin() {
    isSpinning = true;
    spinCircles();

    // Tự động dừng sau 2 giây
    setTimeout(() => {
        stopContinuousSpin();
    }, 2000);
}

function stopContinuousSpin() {
    isSpinning = false;
    clearTimeout(spinTimeout); // Dừng đệ quy
}

function spinCircles() {
    if (!isSpinning) {
        return;
    }

    const circles = document.querySelectorAll('.circle');
    circles.forEach(circle => {
        const randomNumber = Math.floor(Math.random() * 10);
        circle.textContent = randomNumber;
        const randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
        circle.style.color = randomColor;

        circle.classList.add('spin');

        setTimeout(() => {
            circle.classList.remove('spin');
        }, 100); // Thời gian animation ngắn
    });

    // Tiếp tục nhảy sau một khoảng thời gian ngắn
    spinTimeout = setTimeout(spinCircles, 100);
}
  



        // Sử dụng JavaScript để thêm dữ liệu vào bảng
        // var table = document.getElementById("numberTable");

        // for (var i = 0; i < 100; i++) {
        //     var number = ("0" + i).slice(-2); // Định dạng số để có hai chữ số, ví dụ: 01, 02, ..., 99
        //     var row = table.insertRow();
        //     var cell1 = row.insertCell(0);
        //     var cell2 = row.insertCell(1);

        //     cell1.innerHTML = number;
        //     cell2.innerHTML = 0; // Số lần xuất hiện của mỗi số, bạn có thể thay đổi giá trị này tùy thuộc vào logic của bạn
        // }



// Tệp script3.js

// var ctx = document.getElementById('chart').getContext('2d');

// var data = {
//   labels: numbers_data.map(item => item.number),
//   datasets: [{
//     label: 'Số lần xuất hiện',
//     data: numbers_data.map(item => item.count),
//     backgroundColor: '#337ab7'
//   }]
// };

        
function getRandomNumber() {
    return Math.floor(Math.random() * 10);
}

// Hàm để tạo và hiển thị số ngẫu nhiên trong một khung
function generateRandomNumbers(randomNumbersDiv) {
    var numbers = [];
    for (var i = 0; i < 6; i++) {
        var randomNumber = getRandomNumber();
        numbers.push(randomNumber);
    }
    randomNumbersDiv.innerHTML = 'VÉ : ' + numbers.join('  ');
}

// Khung 1
var randomNumbersDiv1 = document.getElementById('randomNumbers1');
generateRandomNumbers(randomNumbersDiv1);

// Khung 2
var randomNumbersDiv2 = document.getElementById('randomNumbers2');
generateRandomNumbers(randomNumbersDiv2);

// Khung 3
var randomNumbersDiv3 = document.getElementById('randomNumbers3');
generateRandomNumbers(randomNumbersDiv3);

// Xử lý sự kiện khi nút được bấm
var generateButton = document.getElementById('generateNumbers');
generateButton.addEventListener('click', function () {
    generateRandomNumbers(randomNumbersDiv1);
    generateRandomNumbers(randomNumbersDiv2);
    generateRandomNumbers(randomNumbersDiv3);
});
