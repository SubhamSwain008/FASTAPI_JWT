import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function Profile() {
  const [username, setUsername] = useState("");
  const [useremail,setUsermail]=useState("");

  const nav=useNavigate();
  useEffect(() => {
    const fetchProfile = async () => {
      const token = localStorage.getItem("token"); // your JWT token
      if (!token) {
        alert("Login first");
        nav("/login")

      };

      try {
        const res = await axios.get("http://localhost:8000/profile", {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        });
        setUsername(res.data.username);
        setUsermail(res.data.email)
        console.log(res.data);
      } catch (err) {
        console.error("Error fetching profile:", err);
      }
    };

    fetchProfile();
  }, []);

  return (
    <>
      <h1>User Profile</h1>
      {username ? <p>User name: {username}</p> : <p>Loading...</p>}
      {useremail ? <p>User email: {useremail}</p> : <p>Loading...</p>}
      <button onClick={()=>{localStorage.setItem("token", "");}}>Logout</button>
    </>
  );
}
