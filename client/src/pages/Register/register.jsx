import api from "../../api/api";
import { useState } from "react";
import "./register.css"; // Ensure this file exists for styling
import { useNavigate } from "react-router-dom";
import InputField from "../../components/Common/InputField/InputField";
import { Link } from 'react-router-dom';
import ToastMessage from "../../utils/toaster/toaster";

export default function Register() {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [passwordConfirmation, setPasswordConfirmation] = useState('');
    const [error, setError] = useState({});
    const [errorMessage, setErrorMessage] = useState("");
    const [isLoading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError({});
        setErrorMessage('');
        try {
            const res = await api.post(
                'api/auth/register/',
                {
                    first_name: firstName,
                    last_name: lastName,
                    username: username,
                    email: email,
                    password: password,
                    password_confirmation: passwordConfirmation
                }
            );
            const response = res.data;

            if (response.success) {
                setLoading(false);
                ToastMessage.success(response.message);
                return navigate('/login');
            }
        } catch (error) {
            const errorMessage = error.response.data.message;
            setErrorMessage(errorMessage);
            setError(error.response.data.errors);
            ToastMessage.error(errorMessage);

        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            <form onSubmit={handleSubmit} className="register-form">
                <h1>User Register</h1>

                <InputField
                    type="text"
                    name="firstName"
                    placeholder="Enter your first name"
                    value={firstName}
                    className="form-input"
                    change={(e) => setFirstName(e.target.value)}
                    error={error.first_name}
                />

                <InputField
                    type="text"
                    name="lastName"
                    placeholder="Enter your last name"
                    value={lastName}
                    className="form-input"
                    change={(e) => setLastName(e.target.value)}
                    error={error.last_name}
                />

                <InputField
                    type="text"
                    name="username"
                    placeholder="Enter your username"
                    value={username}
                    className="form-input"
                    change={(e) => setUsername(e.target.value)}
                    error={error.username}
                />

                <InputField
                    type="email"
                    name="email"
                    placeholder="Enter your email"
                    value={email}
                    className="form-input"
                    change={(e) => setEmail(e.target.value)}
                    error={error.email}
                />

                <InputField
                    type="password"
                    name="password"
                    placeholder="Enter your password"
                    value={password}
                    className="form-input"
                    change={(e) => setPassword(e.target.value)}
                    error={error.password}
                />

                <InputField
                    type="password"
                    name="passwordConfirmation"
                    placeholder="Enter your password confirmation"
                    value={passwordConfirmation}
                    className="form-input"
                    change={(e) => setPasswordConfirmation(e.target.value)}
                    error={error.password_confirmation}
                />

                <button type="submit" className="form-button">
                    Register
                </button>
                <div>Already have an account? <Link to="/login">Login</Link></div>
            </form>
        </>
    );
}
