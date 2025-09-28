import { useNavigate } from "react-router-dom"
import { useState,useRef } from "react"
import axios from 'axios';
export default function Login(){
    const password=useRef(null);
    const userName=useRef(null);
    
    const nav =useNavigate()

    const login=async()=>{

        console.log(password.current.value,userName.current.value);
        try{
            const response=await axios.post('http://127.0.0.1:8000/login/',{
                    username:userName.current.value,
                    password:password.current.value,
                    
                })
            if(response.data.access_token){

            console.log(response.data.access_token)
            localStorage.setItem("token", response.data.access_token);
            nav("/profile");
            }
            else{
                alert("user name or password is wrong")
            }
            
        }
        catch(e){
            console.error("error :",e)
        }
    }

    return(<>
    <div>
        <input type="text" placeholder="username" ref={userName}/>
        <input type="text" placeholder="password" ref={password}/>
        <button onClick={()=>{login()}}>Login</button><button onClick={()=>{nav("/")}}>signup</button>
    </div>
    </>)
}