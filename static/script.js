async function ask(){
    let question=document.getElementById("question").value;
    let chat=document.getElementById("chatbox");
    chat.innerHTML+= "<p><b>You:</b> "+question+"</p>";

    let res=await fetch("/ask",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({question:question})
    });

    let data=await res.json();
    chat.innerHTML+= "<p><b>AI:</b> "+data.answer+"</p>";
}