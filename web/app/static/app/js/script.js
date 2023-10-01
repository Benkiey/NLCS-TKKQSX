function spinCircles() {
    const circles = document.querySelectorAll('.circle'); // Lấy tất cả các hình tròn
    circles.forEach(circle => {
    const randomNumber = Math.floor(Math.random() * 10); // Tạo số ngẫu nhiên từ 0 đến 9
    circle.textContent = randomNumber; // Gán số ngẫu nhiên vào nội dung của hình tròn
          // Tạo một số ngẫu nhiên từ 0 đến 9 cho màu chữ
    const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
    circle.style.color = randomColor; // Áp dụng màu chữ ngẫu nhiên



    });
  }
  