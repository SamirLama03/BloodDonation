import RouteLayout from "./routes/RouteLayout"
import { BrowserRouter } from "react-router-dom"

// ! Configuration For Toaster 
import { ToastContainer } from "react-toastify"
import "react-toastify/dist/ReactToastify.css";


function App() {

  return (
    <>
      <BrowserRouter>
        <RouteLayout />
      </BrowserRouter>

      <ToastContainer />
    </>
  )
}

export default App
