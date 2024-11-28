// frontend/src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Login';
import Register from './Register';
import Dashboard from './Dashboard';
import Header from './Header';
import Footer from './Footer';
import Faturas from './Faturas';
import Faturamento from './Faturamento';
import Despesas from './Despesas';
import './App.css';

function App() {
  const [auth, setAuth] = useState(false);
  const [message, setMessage] = useState('');
  const [showRegister, setShowRegister] = useState(false);

  useEffect(() => {
    if (auth) {
      const token = localStorage.getItem('token');
      axios.get(`${process.env.REACT_APP_API_URL}/user-info`, {
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
    <Router>
      <Header auth={auth} />
      <div className="App">
        {auth ? (
          <>
            <h1>{message}</h1>
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/faturas" element={<Faturas />} />
              <Route path="/faturamento" element={<Faturamento />} />
              <Route path="/despesas" element={<Despesas />} />
            </Routes>
          </>
        ) : showRegister ? (
          <>
            <Register />
            <p>Já possui conta? <button onClick={() => setShowRegister(false)}>Login</button></p>
          </>
        ) : (
          <>
            <Login setAuth={setAuth} />
            <p>Não possui conta? <button onClick={() => setShowRegister(true)}>Registrar</button></p>
          </>
        )}
      </div>
      <Footer />
    </Router>
  );
}

export default App;