import { useState } from 'react'
import {BrowserRouter  as Router, Routes, Route} from "react-router-dom";
import Signup from './signup';
import Login from './login';
import Profile from './profile';

function App() {
  

  return (
    <>
    <Router>

        <Routes>

          <Route path='/' element={<Signup/>}/>
          <Route path='/login' element={<Login/>}/>
          <Route path='/profile' element={<Profile/>}/>

        </Routes>

    </Router>

      
    </>
  )
}

export default App
