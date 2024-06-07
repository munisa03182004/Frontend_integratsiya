const form = document.getElementById("login-form")
const usersContainer = document.getElementById("users-container")

async function onFormSubmit(event) {
    event.preventDefault()
    const email = event.target.email.value
    const password = event.target.password.value

    usersContainer.textContent = "Loading ..."

    const tokenResponse = await fetch("http://localhost:8000/api/v1/token/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({email: email, password: password})
    })

    const data = await tokenResponse.json()
    const accessToken = data.access

    const notesResponse = await fetch("http://localhost:8000/api/v1/notes/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + accessToken
        }
    })

    usersContainer.textContent = ""

    const notesData = await notesResponse.json()

    notesData.forEach(note => {
        usersContainer.innerHTML += `
            <p>${note.title} - ${note.body}</p>
        `
    })

}

form.addEventListener("submit", onFormSubmit)
