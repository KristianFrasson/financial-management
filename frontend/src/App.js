// src/App.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Login from './Login';

function App() {
  const [auth, setAuth] = useState(false);
  const [message, setMessage] = useState('');

  useEffect(() => {
    if (auth) {
      const token = localStorage.getItem('token');
      axios.get('http://localhost:5000/protected', {
        headers: { Authorization: `Bearer ${token}` }
      })
        .then(response => {
          setMessage(`Bem-vindo, ${response.data.logged_in_as}`);
        })
        .catch(error => {
          console.error('Erro ao acessar rota protegida:', error);
          setAuth(false);
        });
    }
  }, [auth]);

  return (
    <div className="App">
      {auth ? (
        <h1>{message}</h1>
      ) : (
        <Login setAuth={setAuth} />
      )}
    </div>
  );
}

export default App;