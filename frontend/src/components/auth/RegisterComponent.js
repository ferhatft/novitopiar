import React, { useState } from 'react';
import axios from 'axios';

function RegisterComponent() {
    const [email, setEmail] = useState('');
    const [password1, setPassword1] = useState('');
    const [password2, setPassword2] = useState('');
    const [error, setError] = useState('');

    const handleRegister = async () => {
        try {
            await axios.post('http://localhost:8000/dj-rest-auth/registration/', {
                email,
                password1,
                password2
            });
            // Kayıt başarılı ise kullanıcıyı giriş sayfasına yönlendirebilirsiniz.
        } catch (err) {
            setError('Kayıt başarısız. Lütfen bilgilerinizi kontrol edin.');
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
                value={password1}
                onChange={(e) => setPassword1(e.target.value)}
            />
            <input
                type="password"
                placeholder="Şifre Tekrar"
                value={password2}
                onChange={(e) => setPassword2(e.target.value)}
            />
            <button onClick={handleRegister}>Kayıt Ol</button>
            {error && <p>{error}</p>}
        </div>
    );
}

export default RegisterComponent;
