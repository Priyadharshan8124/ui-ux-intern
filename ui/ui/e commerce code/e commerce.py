<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colorful Bookstore</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2; /* Light gray background */
            color: #333;
        }

        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
        }

        main {
            max-width: 1200px;
            margin: 20px auto;
        }

        .book-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
        }

        .book {
            background-color: #ffffff; /* White background */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .book:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .book img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
            margin-bottom: 10px;
        }

        .book h3 {
            margin-top: 10px;
            color: #004080; /* Dark blue text */
            font-size: 1.2em;
        }

        .book p {
            color: #666; /* Dark gray text */
            margin-bottom: 8px;
        }

        .book button {
            background-color: #006600; /* Dark green button */
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .book button:hover {
            background-color: #004d00; /* Darker green on hover */
        }

        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0, 0, 0, 0.7);
            padding-top: 60px;
        }

        .modal-content {
            background-color: #fafafa; /* Light gray modal background */
            margin: 5% auto;
            padding: 20px;
            border: 1px solid #888;
            width: 80%;
            border-radius: 8px;
            text-align: center;
        }

        .close {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
        }

        .close:hover,
        .close:focus {
            color: black;
            text-decoration: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <header>
        <h1>Colorful Bookstore</h1>
    </header>

    <main>
        <div class="book-grid">
            <div class="book" onclick="openModal('The Great Gatsby', 'F. Scott Fitzgerald', 12.99)">
                <img src="book1.jpg" alt="The Great Gatsby">
                <h3>The Great Gatsby</h3>
                <p>by F. Scott Fitzgerald</p>
                <p>$12.99</p>
                <button>Add to Cart</button>
            </div>

            <div class="book" onclick="openModal('To Kill a Mockingbird', 'Harper Lee', 14.99)">
                <img src="book2.jpg" alt="To Kill a Mockingbird">
                <h3>To Kill a Mockingbird</h3>
                <p>by Harper Lee</p>
                <p>$14.99</p>
                <button>Add to Cart</button>
            </div>

            <!-- Add more books as needed -->
        </div>
    </main>

    <!-- Modal for Book Details -->
    <div id="bookModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal()">&times;</span>
            <h2 id="modalTitle"></h2>
            <p id="modalAuthor"></p>
            <p id="modalPrice"></p>
            <button onclick="addToCart()">Add to Cart</button>
        </div>
    </div>

    <script>
        function openModal(title, author, price) {
            document.getElementById('modalTitle').innerHTML = title;
            document.getElementById('modalAuthor').innerHTML = 'by ' + author;
            document.getElementById('modalPrice').innerHTML = '$' + price.toFixed(2);
            document.getElementById('bookModal').style.display = 'block';
        }

        function closeModal() {
            document.getElementById('bookModal').style.display = 'none';
        }

        function addToCart() {
            // Implement your cart logic here
            alert
