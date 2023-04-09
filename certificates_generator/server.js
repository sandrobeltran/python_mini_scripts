const express = require("express")
const colors = require("colors")
const app = express()
const path = require("path")
const router = require("./router")

// Settings
app.set("PORT", 3000)

// Midlewares
app.use(express.json())
app.use(express.static(path.join(__dirname, "static")))
app.use(express.static(path.join(__dirname, "certificates")))

// Routes
app.use("/", router)

app.listen(app.get("PORT"), ()=>{
	console.log(`Server listening on port ${app.get("PORT")}`.green)
})