import "./InputField.css"


import React from "react";
import "./InputField.css";

export default function InputField({
    type,
    value,
    placeholder,
    change,
    error = null,
    name,
    className = "form-input",
}) {

    return (
        <>
            <input
                id={name}
                type={type}
                placeholder={placeholder}
                value={value}
                name={name}
                onChange={change}
                className={className}
                required
            />
            {error && <p className="error">{error}</p>}
        </>
    );
}
