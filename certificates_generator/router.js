const { Router } = require("express")
const router = Router()
const fs = require("fs").promises
const { spawn } = require("child_process")

router.get("/", (req, res)=>{
	return res.sendFile("index.html")
})

router.post("/generate", async (req, res) => {
	const { body } = req

	// Write data.csv file
	console.log("Writting file...".grey)
	await fs.writeFile("./data.csv", `${body.student},${body.course},${body.teacher}`)
	console.log("File written!".green)

	// Execute python script
	console.log("Executing script...".grey)
	await spawn('cmd.exe', ["/c", __dirname + "/generate.bat"]);
	console.log("Script executed!".green)

	console.log(`Certificate for ${body.student} generated!`.green)

	await setTimeout(()=>{
	return res.status(200).sendFile(__dirname + `/certificates/${body.student}_${body.course}.pdf`)

	}, 2000)

})

module.exports = router