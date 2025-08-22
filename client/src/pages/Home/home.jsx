import { Link, useNavigate } from 'react-router-dom';
import ToastMessage from '../../utils/toaster/toaster';
import { userDetail } from '../../utils/userDetail/userDetail';
import Header from '../../components/Header/header';
import Footer from '../../components/Footer/footer';

export default function Home() {
    const navigate = useNavigate()

    const userData = userDetail();
    console.log("This is user data", userData)

    // ! For Handeling User Logout
    const logoutClick = () => {
        localStorage.clear()
        ToastMessage.success("Successfully Logged Out")
        return navigate('/login')
    }

    return (
        <>
            <Header />
            <br />

            {/*For User Logout */}
            <div >
                <button onClick={logoutClick}>Logout</button>
                <button><Link to={'/change-password'}>Change Password</Link></button>

                <div>Welcome {userData.username}</div>
            </div>

            <Footer />
        </>
    )
}