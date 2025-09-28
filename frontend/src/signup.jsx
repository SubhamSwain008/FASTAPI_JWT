import { useState ,useRef } from "react"
import axios from 'axios';
import { useNavigate } from "react-router-dom";

export default function Signup(){

const userName=useRef(null);
const Userpassword=useRef(null);
const Useremail=useRef(null);
const [message,setMessage]=useState("");
const nav=useNavigate();

const signup=async()=>{

    console.log(userName.current.value,Userpassword.current.value)
    if(userName.current.value!=null && Userpassword.current.value !=null){

        try{
                const response=await axios.post('http://127.0.0.1:8000/signup/',{
                    username:userName.current.value,
                    password:Userpassword.current.value,
                    email:Useremail.current.value,
                })
                console.log(response.data.message);
                setMessage(response.data.message," now log in");
            }
            catch (error){
                console.error("Error",error)
            }
    
        }
    else{
        alert("new username and password are required");
    }
    }
    

    return (<>
    
    <div>
      <input ref={userName} type="text" placeholder="enter User Name" />
      <input ref={Userpassword} type="text" placeholder="enter password" />
      <input ref={Useremail} type="text" placeholder="enter email" />
      <button
      onClick={()=>{signup()}}
      > Sign up</button>
      <h3 style={{color:"red"}}>{message}</h3>
      <button onClick={()=>{nav("/login")}}>Login</button>


    </div>

    </>)
}