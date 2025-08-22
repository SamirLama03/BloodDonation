import "./header.css"
import { userDetail } from '../../utils/userDetail/userDetail';
import ToastMessage from '../../utils/toaster/toaster';
import { Link, useNavigate } from 'react-router-dom';
import React from 'react';



export default function Header() {
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
            <header className="navbar-dark bg-dark fixed-top text-white ">
                <div className="container container-fluid ">
                    <div className="row">

                        <div className="d-flex justify-content-between text-white">
                            <div className="d-flex justify-content-evenly col-8">
                                <div className="nav-item cursor-pointer" onClick={() => navigate('/')}>Home</div>
                                <div className="nav-item">About Us</div>
                                <div className="nav-item">Our Team</div>
                                <div className="nav-item">Contact Us</div>
                            </div>
                            <div className="d-flex justify-content-end col-4">
                                <div onClick={logoutClick} className="nav-item cursor-pointer">
                                    Logout
                                </div>

                                <button className="navbar-toggler p-3" type="button" data-bs-toggle="offcanvas"
                                    data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar">
                                    <span className="navbar-toggler-icon"></span>
                                </button>
                            </div>

                            {/* DropDown Items */}
                            <div className="offcanvas offcanvas-end text-bg-dark" tabIndex="-1" id="offcanvasDarkNavbar"
                                aria-labelledby="offcanvasDarkNavbarLabel">
                                <div className="offcanvas-header">
                                    <h5 className="offcanvas-title" id="offcanvasDarkNavbarLabel">Hamburger</h5>
                                    <button type="button" className="btn-close btn-close-white" data-bs-dismiss="offcanvas"
                                        aria-label="Close"></button>
                                </div>
                                <div className="offcanvas-body">
                                    <ul className="navbar-nav justify-content-end flex-grow-1 pe-3">
                                        <li className="nav-item">
                                            <a className="nav-link active cursor-pointer" aria-current="page" onClick={() => navigate('/change-password')} >

                                                Change Password
                                            </a>
                                        </li>
                                        <li className="nav-item">
                                            <a className="nav-link" href="#">Link</a>
                                        </li>
                                        <li className="nav-item dropdown">
                                            <a className="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                                                aria-expanded="false">
                                                Dropdown
                                            </a>
                                            <ul className="dropdown-menu dropdown-menu-dark">

                                                <li><a className="dropdown-item" href="#">Another action</a></li>
                                                <li>
                                                    <hr className="dropdown-divider" />
                                                </li>
                                                <li><a className="dropdown-item" href="#">Something else here</a></li>
                                            </ul>
                                        </li>
                                    </ul>
                                    <form className="d-flex mt-3" role="search">
                                        <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
                                        <button className="btn btn-success" type="submit">Search</button>
                                    </form>
                                </div>
                            </div>

                        </div>

                    </div>
                </div>
            </header >
            <div className='mb-5'></div>
        </>
    );
}
