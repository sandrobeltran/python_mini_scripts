const genForm = document.querySelector(".generate-form")


genForm.addEventListener("submit", async (e)=>{
	e.preventDefault()

	const student = e.target.student
	const course = e.target.course
	const teacher = e.target.teacher

	const request = await fetch("/generate", {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify({ 
			student: student.value,
			course: course.value,
			teacher: teacher.value,
		})
	})

	const response = await request.blob()

	const a = document.createElement("a")

	a.download = `${student.value}_${course.value}.pdf`
	a.href = URL.createObjectURL(response)
	a.click()
	a.remove()
})