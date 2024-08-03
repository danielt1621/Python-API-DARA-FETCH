<!--Log in handler-->
<?php
// Start the session to maintain user session data across pages
session_start();

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve the password from the POST request
    $password = $_POST['password'];
    
    // Check if the provided password matches the hardcoded password
    if ($password === '0000') { // If you are using a database, it would be recommended to enrypt and store the string there.
        // Set session variable to indicate the user is logged in
        $_SESSION['logged_in'] = true;
        // Redirect to the main.html page
        header('Location: main.html');
        exit;
    } else {
        // Set an error message if the password is invalid
        $error = 'Invalid password.'.'<br>'.'If forgot your password, contact your admin.';
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Specify the character encoding for the HTML document -->
    <meta charset="UTF-8">
    <!-- Set the viewport to ensure proper scaling on different devices -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Define the title of the webpage -->
    <title>Login - BS API Tool</title>
    <!-- Link to the favicon for the webpage -->
    <link rel="icon" type="image/png" href="your/logo.JPG">
    <!-- CSS styles for the login page -->
    <style>
        /* Apply styles to the body element */
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-image: linear-gradient(to right, #27398F, #4557B3);
            color: #003d82;
        }

        /* Style the login container */
        .login-container {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2), 0 6px 6px rgba(0, 0, 0, 0.2);
            animation: fadeIn 1s ease-in-out forwards;
        }

        /* Define the keyframes for the fadeIn animation */
        @keyframes fadeIn {
            0% {
                opacity: 0;
                transform: scale(0.9);
            }
            100% {
                opacity: 1;
                transform: scale(1);
            }
        }

        /* Style the heading */
        h1 {
            text-align: center;
            color: #333;
        }

        /* Style the form element */
        form {
            display: flex;
            flex-direction: column;
        }

        /* Style the input elements */
        input {
            margin: 0.5rem 0;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        /* Style the button element */
        button {
            margin-top: 1rem;
            padding: 0.5rem;
            background-color: #0056b3;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        /* Style the button on hover */
        button:hover {
            background-color: #003d82;
        }

        /* Center images */
        img {
            margin: auto;
        }

        /* Style for copyright notice at the bottom */
        .copyright-notice {
            position: fixed;
            bottom: 0;
            left: 0;
            font-size: 12px;
            color: #ffffff;
            padding: 5px;
            background-color: #003d82;
            border-top: 1px solid #ddd;
            width: 100%;
            text-align: left;
        }
    </style>
</head>
<body>
    <!-- Login container content -->
    <div class="login-container">
        <!-- Logo image -->
        <img src="yourimg/path.JPG" alt="" class="logo">
        <!-- Page heading -->
        <h1 style="color: #003d82;">API Tool</h1>
        <!-- Display error message if set -->
        <?php if (isset($error)): ?> <!--Error handling in case the user inputs a wrong password-->
            <p style="color: red;"><?php echo $error; ?></p>
        <?php endif; ?>
        <!-- Login form -->
        <form method="post">
            <input type="password" name="password" placeholder="Enter password" required>
            <button type="submit">Login</button>
        </form>
    </div>

    <!-- Footer content -->
    <footer class="copyright-notice">
        &copy; BS API TOOL v1, Daniel Tsavalos
    </footer>
</body>
</html>
