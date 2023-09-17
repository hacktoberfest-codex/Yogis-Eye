import { useState } from 'react'

import './App.css'
import NavBar from './pages/NavBar'
import { Route, Routes } from 'react-router-dom'
import About from './pages/About'
import Home from './pages/Home'
import ImageUploadWithForm from './pages/ImageUploadForm'
import Footer from './pages/footer'



function App() {
  const [count, setCount] = useState(0)


  return (
    <div className='bg-[#b2d8d8]'>
      <NavBar />
      <Routes>
        <Route path='/' element={<Home />} />

        <Route path='/about' element={<About />} />

   <Route path='/upload' element={<ImageUploadWithForm/>}/>
   

      </Routes>
      {/* <ImageUploadWithForm /> */}
      < Footer />



    </div>
  )
}

export default App
