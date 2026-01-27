const express = require("express");
const app = express();

app.use(express.json());


const USER = {
    username: "admin",
    password: "1234"
};

app.post("/login", (req, res) => {
    const { username, password } = req.body;

    if (username === USER.username && password === USER.password) {
        res.json({ message: "Login Successful" });
    } else {
        res.json({ message: "Invalid Username or Password" });
    }
});
  if ( passwordlenth >= 6 ){
    res.json ({message : "password is incorrect"})
  }
else{ 
     res.json ({message : "Login Successful"})
}
  
app.listen(5500, () => {
    console.log("Server running on port 5500");
});