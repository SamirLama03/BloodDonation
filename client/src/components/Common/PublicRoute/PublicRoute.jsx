import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN } from "../../../constant";


// ! Publlic Route Function
export default function PublicRoute({ children }) {
    /* 
    Public Route function To Make Only the Unauthenticated users to access 
    Endpoinsts
    */
    const navigate = useNavigate();
    const [isChecking, setIsChecking] = useState(true);

    useEffect(() => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            navigate('/');
        } else {
            setIsChecking(false);
        }
    }, [navigate]);

    if (isChecking) {
        return <div>Loading...</div>;
    }

    return children;
}
