const express = require("express");
const cors = require("cors");
const terminologyRoutes = require("./routes/terminologyRoutes");

const app = express();

app.use(cors());
app.use(express.json());
app.use((req,res,next)=>{
  console.log(`${req.method} ${req.url}`);
  next();
})
app.get("/", (req, res) => {
  res.json({
    message: "Custom FHIR Terminology API (MVC Version)",
  });
});

app.use("/", terminologyRoutes);

module.exports = app;
