// src/Register.js
import React, { useState } from 'react';
import axios from 'axios';

function Register() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('https://probable-palm-tree-vxwx9v564j9hp95-5000.app.github.dev/auth/register', { username, password })
      .then(response => {
        alert('Usuário criado com sucesso!');
      })
      .catch(error => {
        console.error('Erro ao registrar:', error);
        alert('Erro ao registrar usuário');
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Registrar</h2>
      <input
        type="text"
        placeholder="Usuário"
        value={username}
        onChange={e => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Senha"
        value={password}
        onChange={e => setPassword(e.target.value)}
      />
      <button type="submit">Registrar</button>
    </form>
  );
}

export default Register;