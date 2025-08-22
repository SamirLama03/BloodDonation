import './forgotPassword.css'
import api from "../../api/api"
import { useState } from "react"
import { useNavigate } from "react-router-dom"
import InputField from "../../components/Common/InputField/InputField"
import ToastMessage from "../../utils/toaster/toaster"
import { isAxiosError } from "axios";


export default function ForgotPassword() {
    const [email, setEmail] = useState('')


    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await api.post('api/auth/forgot-password/', { email })
            const response = res.data;
            if (response.success) {
                ToastMessage.success(response.message)
                setEmail("");
            }

        } catch (error) {
            if (isAxiosError(error)) {
                console.log(error.response)
                ToastMessage.error(error.response.data.message);
            } else {
                ToastMessage.error("An unexpected error occurred.", error);
            }
        }
    }


    return (
        <>
            <form onSubmit={handleSubmit} className="form-container" method="post">

                <h1>Forgot Password</h1>
                <InputField
                    type="email"
                    name="email"
                    placeholder="Enter your email"
                    value={email}
                    change={(e) => {
                        setEmail(e.target.value)
                    }}
                />

                <button className="form-button" type="submit">
                    Send Email
                </button>

            </form>
        </>
    )
}