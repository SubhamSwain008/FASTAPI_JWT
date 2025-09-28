import { useEffect } from "react"

export default function Profile(){

useEffect(()=>{
const token = localStorage.getItem("token"); // whatever you saved

fetch("http://localhost:8000/profile", {
  method: "GET",
  headers: {
    "Authorization": `Bearer ${token}`,
    "Content-Type": "application/json",
  },
})
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));
},[])

    return(<>
    <h1>User Profile</h1>
    </>)
}