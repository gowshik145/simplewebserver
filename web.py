from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login website</title>
 <style>
    .frm{
    background-color: rgba(190, 195, 197, 0.756);
    color: rgb(31, 27, 27); 
    
}
.frm{
    border: 10px solid black;
    width: 60%;
    margin-left: 250px;
    padding: 60px;
}

input{
    border-radius: 20px;
    text-align: center;
    padding: 13px;
   
}

input:hover{
    background-color: rgb(128, 77, 195);
}
::placeholder{
    color:rgb(134, 37, 73);
}
a{
    text-decoration: none;
}

.homepage{
    background-color: red;
    width: 100%;
    height: 60px;
    
}
#srcbx{
    background-color: white;
    color: black;
    background-image: url(search.png);
    background-size: contain;
    background-repeat: no-repeat;
    padding-left: 15px;
    background-position: 95%;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;


}
</style>
</head>

<body>
    <div class="frm">
        <form method="get">
            <h1 style="text-align: center;">LOGIN</h1>
            <input type="text" name="searchbox" id="srcbx"><br>
            <br>
            <input type="text" name="name" required placeholder="Enter Name"><br>
            <br>
            <input type="number" name="num" placeholder="roll number"><br>
            <br>
            <input type="date" name="dob"><br>
            <br>
            <input type="number" name="Age" min="18" max="60" placeholder="enter Age"><br>
            <br>
            <input type="email" id="email" name="aemail" placeholder="Enter email"
                pattern="[a-z0-9._]+@[a-z0-9.\-.]+\.[a-z]{2,4}$"><br>
            <br>
            <input type="password" name="Pass" placeholder="password"><br>
            <br>
            Gender:<br>
            <input type="radio" name="gender" style="accent-color:green;" value="M">Male<br>
            <input type="radio" name="gender" style="accent-color: rgb(235, 16, 180);" value="F">Femlae<br>
            <br>
            Department: <br>
            <input type="checkbox" name="dep" value="CSE">computer science Engineering<br>
            <input type="checkbox" name="dep" value="IT">Information Technology<br>
            <input type="checkbox" name="dep" value="AIDS">Artificial intelligence and Data Science<br>
            <input type="checkbox" name="dep" value="AIML">Artificial intelligence and Mechine Learning<br>
            <br>
            select the College: <select name="college" multiple>
                <option value="none">---Select the college</option>
                <option value="SEC">Saveetha engineering college</option>
                <option value="pec">panimalar enigneering college</option>
                <option value="REC">rajalakshmi engineering college</option>
            </select><br>
            <br>
            select the College: <select name="college">
                <option value="none">---Select the college</option>
                <option value="SEC">Saveetha engineering college</option>
                <option value="pec">panimalar enigneering college</option>
                <option value="REC">rajalakshmi engineering college</option>
            </select><br>
            <br>
            <textarea name="Your Comments" cols="30" rows="10"></textarea><br>
            <br>
            <input type="file" value="save"><br>
            <br>
            <input type="submit" class="Subbtn" name="save">
        </form>
    </div>
</body>

</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()