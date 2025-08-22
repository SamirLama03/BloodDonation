import api from "../../api/api"
import { useState } from "react"
import "./login.css"
import { useNavigate } from "react-router-dom"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../../constant"
import InputField from "../../components/Common/InputField/InputField"
import { Link } from 'react-router-dom';
import ToastMessage from "../../utils/toaster/toaster"


export default function Login() {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [isLoading, setLoading] = useState(false)
    const navigate = useNavigate()


    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        try {
            const res = await api.post('api/auth/login/', { email, password })
            console.log(res);
            const response = res.data;
            console.log(response);
            if (response.success) {
                // ! If Success Setting Access And Refresh Token At Local Storage 
                localStorage.setItem(ACCESS_TOKEN, response.data.access)
                localStorage.setItem(REFRESH_TOKEN, response.data.refresh)
                // ! Navigating To Root
                ToastMessage.success(response.message)
                navigate('/')
            }

            // ! If Response Has Succes To False Navigating To Login
        } catch (error) {
            ToastMessage.error("Invalid Credential provided")
        } finally {
            setLoading(false);
        }
    }


    return (
        <>
            <form onSubmit={handleSubmit} className="form-container" method="post">
                <h1>Login</h1>
                <InputField
                    type="email"
                    name="email"
                    placeholder="Enter your email"
                    value={email}
                    change={(e) => {
                        setEmail(e.target.value)
                    }}
                />
                <InputField
                    type="password"
                    name="password"
                    placeholder="Enter your password"
                    value={password}
                    change={(e) => {
                        setPassword(e.target.value)
                    }}
                />

                <button className="form-button" type="submit">
                    Login
                </button>

                <div><Link to="/forgot-password">Forgot Password? </Link> </div >
                <div>Don't have a account? <Link to="/register">Register</Link> </div >

            </form>
        </>
    )
}