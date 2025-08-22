import { jwtDecode } from "jwt-decode"
import api from "../../../api/api"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../../../constant"
import { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom"



// ! For Protecting Route 
export default function ProtectedRoute({ children }) {
    /*  
    This function helps to protect unauthenticated user to access the childen
    Component
    */
    const navigate = useNavigate()
    const [isAuthorized, setIsAuthorized] = useState(null);

    // ! Runs At First which call the auth function
    useEffect(() => {
        // !If it catch error set the isAuthorized to false 
        auth().catch(() => setIsAuthorized(false))
    }, [])

    // ! For Refreshing the access token
    const refreshToken = async () => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN);
        try {
            const res = await api.post("/api/token/refresh/", {
                refresh: refreshToken,
            });
            if (res.status === 200) {
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                setIsAuthorized(true)
            } else {
                setIsAuthorized(false)
            }
        } catch (error) {
            console.log(error);
            setIsAuthorized(false);
        }
    };

    // ! For Checking User Authentication Status and Calling refreshToken function
    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN);

        // ! If no token is found set the state false and return the function which then navigate to home route
        if (!token) {
            setIsAuthorized(false);
            return;
        }
        const decoded = jwtDecode(token);
        const tokenExpiration = decoded.exp;
        const now = Date.now() / 1000;

        if (tokenExpiration < now) {
            await refreshToken();
        } else {
            setIsAuthorized(true);
        }
    };

    if (isAuthorized === null) {
        return <div>Loading...</div>;
    }

    // Routes to /login if the user is not logged in 
    return isAuthorized ? children : navigate('/login')
}