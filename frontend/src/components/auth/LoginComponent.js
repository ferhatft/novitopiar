import React, { useState } from 'react';
import axios from 'axios';

function LoginComponent() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleLogin = async () => {
        try {
            const response = await axios.post('http://localhost:8000/dj-rest-auth/login/', {
                username: email,
                email,
                password
            });
            localStorage.setItem('token', response.data.key);
        } catch (err) {
            setError(err.response && err.response.data.email ? err.response.data.email : 'Giriş başarısız oldu. Lütfen bilgilerinizi kontrol edin.');
        }
    };
    

    return (
        <div>
            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <input
                type="password"
                placeholder="Şifre"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={handleLogin}>Giriş Yap</button>
            {error && <p>{error}</p>}
        </div>
    );
}

export default LoginComponent;
