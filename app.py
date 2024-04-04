from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clipping Automatizado</title>
</head>
<body>
    <h1>Clipping Automatizado</h1>
    <form action="/" method="post">
        <label>Termo de Busca:</label><br>
        <input type="text" name="termo"><br>
        <label>Seu E-mail:</label><br>
        <input type="email" name="email"><br><br>
        <input type="submit" value="Buscar">
    </form>
</body>
</html>
