
<!DOCTYPE html>
    <html>
        <head>
            <title>Login Form</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <div class="Login">
                <form action="">
                    <h1>Login</h1>
                    <br>
                    <input type="email" placeholder="Email">
                    <br>
                    <input type="password" placeholder="Password">
                    <br>
                    <button type="submit">Login</button>
                    <br>
                    <a href="#">Froget Password?</a>
                    <br>
                   <p>don't have accuont?<a href="#">Sign up</a></p>
                </form>
            </div>
        </body>
    </html>
HTML ⬇
*{
    margin: 0;
    padding: 0;
}
body{
    background-image:linear-gradient(rgba(0,0,0,0.5),rgba(0,0,0,0.5)), url(b1.jpg); background-attachment: fixed;
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    height: 100vh;
}
.Login{
    width: 260px;
    height: 350px;
    text-align: center;
    background: rgba(0,0,0,0.5);
    border-radius: 10px;
    margin-top: 15%;
    margin-left: 40%;
}
.Login h1{
    font-family: Arial, Helvetica, sans-serif;
    color: #fff;
    margin-top:10%;
}
.Login input{
    width: 190px;
    height: 35px;
    border-radius: 7px;
    border: none;
    margin-top: 20px;
}
.Login button{
    width:190px;
    height:35px;
    margin-top: 20px;
    background:#39C;
    border-radius: 7px;
    border: none;
    color: #fff;
    cursor: pointer;
    font-size: 18px;
    margin-bottom: 10px;
}
.Login a{
    color: #fff;
    text-align: center;
}
.Login p{
    color: #fff;
    margin-left: 10px;
    margin-top: 20px;
}
.Login p a{
    color: #39C;
}