import Home from "../pages/Home/home";
import Login from "../pages/Login/login";
import Register from "../pages/Register/register";
import NotFound from "../pages/NotFound/notFound";
import { Routes, Route } from "react-router-dom";
import ProtectedRoute from "../components/Common/ProtectedRoute/ProtectedRoute";
import PublicRoute from "../components/Common/PublicRoute/PublicRoute";
import { ChangePassword } from "../pages/ChangePassword/changePassword";
import ForgotPassword from "../pages/ForgotPassword/forgotPassword";
import { ResetPassword } from "../pages/ResetPassword/resetPassword";


function RegisterAndLogout() {
    localStorage.clear()
    return <Register />;
}


// ! Projects Route Layout 
export default function RouteLayout() {
    return (
        <div>
            <Routes>
                <Route path="/login" element={
                    <PublicRoute>
                        <Login />
                    </PublicRoute>}
                />

                <Route path="/register" element={
                    <PublicRoute>
                        <RegisterAndLogout />
                    </PublicRoute>
                } />
                <Route path="/change-password" element={
                    <ProtectedRoute>
                        <ChangePassword />
                    </ProtectedRoute>
                } />
                <Route path="/forgot-password" element={
                    <PublicRoute>
                        <ForgotPassword />
                    </PublicRoute>
                } />
                <Route path="/reset-password/:uid/:token" element={
                    <PublicRoute>
                        <ResetPassword />
                    </PublicRoute>
                } />
                <Route path="/" element={
                    <ProtectedRoute>
                        <Home />
                    </ProtectedRoute>}>
                </Route>


                {/* ! If the Route Other than the specified one are mapped this NotFound Component Will be Called */}
                <Route path="*" element={<NotFound />} />
            </Routes>
        </div >
    )
}