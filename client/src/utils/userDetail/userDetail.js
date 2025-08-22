import { decodeToken } from "react-jwt";
import { ACCESS_TOKEN } from '../../constant.js'


export function userDetail() {
    const access_token = localStorage.getItem(ACCESS_TOKEN);
    const decoded_data = decodeToken(access_token);
    return decoded_data;;
}