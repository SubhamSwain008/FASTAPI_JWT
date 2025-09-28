import { useState ,useRef } from "react"

export default function Signup(){

const userName=useRef(null);
const Userpassword=useRef(null);



    return (<>
    
    <div>
      <input ref={userName} type="text" placeholder="enter User Name" />
      <input ref={Userpassword} type="text" placeholder="enter password" />


    </div>

    </>)
}