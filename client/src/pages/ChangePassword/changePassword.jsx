import './changePassword.css'
import api from '../../api/api'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import ToastMessage from '../../utils/toaster/toaster'
import InputField from '../../components/Common/InputField/InputField'
import { isAxiosError } from "axios";

export function ChangePassword() {
    const navigate = useNavigate()
    const [oldPassword, setOldPassword] = useState("")
    const [newPassword, setNewPassword] = useState("")
    const [newPasswordConfirmation, setNewPasswordConfirmation] = useState("")
    // const [errorResponse, setError] = useState({})

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const res = api.post(
                'api/auth/change-password/',
                {
                    old_password: oldPassword,
                    new_password: newPassword,
                    new_password_confirmation: newPasswordConfirmation
                }
            )
            const response = (await res).data;
            if (response.success) {
                localStorage.clear()
                ToastMessage.success(response.message)
                navigate('/login')
            }
        }
        catch (error) {
            if (isAxiosError(error)) {
                ToastMessage.error(error.response.data.message);

                // ! Doing It later
                // const errors = error.response.data.errors
                // if (error != null) {
                //     setError(errors)
                // }
            } else {
                ToastMessage.error("An unexpected error occurred.", error);
            }
        }
    }

    return (
        <>
            <form method="post" onSubmit={handleSubmit}>
                <InputField
                    type="password"
                    name="old_password"
                    placeholder="Enter your old password"
                    value={oldPassword}
                    className="form-input"
                    change={(e) => setOldPassword(e.target.value)}
                // error={errorResponse.old_password ? errorResponse.old_password : null}
                />
                <InputField
                    type="password"
                    name="new_password"
                    placeholder="Enter your new password"
                    value={newPassword}
                    className="form-input"
                    change={(e) => setNewPassword(e.target.value)}
                // error={errorResponse.new_password ? errorResponse.new_password : null}
                />
                <InputField
                    type="password"
                    name="new_password_confirmation"
                    placeholder="Enter your new password confirmation"
                    value={newPasswordConfirmation}
                    className="form-input"
                    change={(e) => setNewPasswordConfirmation(e.target.value)}
                // error={errorResponse.new_password_confirmation ? errorResponse.new_password_confirmation : null}
                />

                <button type="submit" className="form-button">
                    Change Password
                </button>
            </form>
        </>
    )
}
