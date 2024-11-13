// frontend/src/components/Dashboard.js

import React, { useEffect, useState } from 'react';  // Importa React e hooks
import axios from 'axios';  // Importa biblioteca para requisições HTTP
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, PieChart, Pie, Cell
} from 'recharts';  // Importa componentes de gráficos
import { API_URL } from '../config';  // Importa a URL da API

function Dashboard() {
  const [monthlyBills, setMonthlyBills] = useState([]);  // Estado para faturas mensais
  const [monthlyIncome, setMonthlyIncome] = useState([]);  // Estado para entradas mensais
  const [monthlyExpenses, setMonthlyExpenses] = useState([]);  // Estado para despesas mensais
  const [categoryData, setCategoryData] = useState([]);  // Estado para dados por categoria

  useEffect(() => {
    const token = localStorage.getItem('token');  // Obtém o token armazenado
    const config = { headers: { Authorization: `Bearer ${token}` } };  // Configura os headers

    // Função assíncrona para buscar dados da API
    const fetchData = async () => {
      try {
        const billsResponse = await axios.get(`${API_URL}/api/monthly-bills`, config);
        setMonthlyBills(billsResponse.data);  // Atualiza estado das faturas

        const incomeResponse = await axios.get(`${API_URL}/api/monthly-income`, config);
        setMonthlyIncome(incomeResponse.data);  // Atualiza estado das entradas

        const expensesResponse = await axios.get(`${API_URL}/api/monthly-expenses`, config);
        setMonthlyExpenses(expensesResponse.data);  // Atualiza estado das despesas

        const categoryResponse = await axios.get(`${API_URL}/api/category-analysis`, config);
        setCategoryData(categoryResponse.data);  // Atualiza estado das categorias
      } catch (error) {
        console.error('Erro ao obter dados do dashboard:', error);  // Log de erro
      }
    };

    fetchData();  // Chama a função para buscar dados
  }, []);

  const COLORS = ['#8884d8', '#82ca9d', '#ffc658', '#ff8042', '#8dd1e1'];  // Paleta de cores

  return (
    <div className="dashboard">
      <h2>Dashboard Financeiro</h2>

      {/* Gráfico de Entradas e Despesas Mensais */}
      <BarChart
        width={600}
        height={300}
        data={monthlyIncome}  // Dados para o gráfico
        margin={{ top: 5, right: 30, left: 20, bottom: 5 }}  // Margens do gráfico
      >
        <CartesianGrid strokeDasharray="3 3" />  // Grades do gráfico
        <XAxis dataKey="month" />  // Eixo X com o mês
        <YAxis />  // Eixo Y
        <Tooltip />  // Tooltip ao passar o mouse
        <Legend />  // Legenda do gráfico
        <Bar dataKey="income" fill="#82ca9d" />  // Barras das entradas
        <Bar dataKey="expenses" fill="#8884d8" />  // Barras das despesas
      </BarChart>

      {/* Gráfico de Faturas do Cartão de Crédito */}
      <PieChart width={400} height={400}>
        <Pie
          data={monthlyBills}  // Dados para o gráfico
          dataKey="amount"  // Chave para o valor
          nameKey="creditCard"  // Chave para o nome do cartão
          cx="50%"  // Posição X
          cy="50%"  // Posição Y
          outerRadius={100}  // Raio externo
          fill="#8884d8"  // Cor de preenchimento
          label  // Exibe labels
        >
          {monthlyBills.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />  // Células coloridas
          ))}
        </Pie>
        <Tooltip />
        <Legend />
      </PieChart>

      {/* Gráfico de Análise por Categoria */}
      <PieChart width={400} height={400}>
        <Pie
          data={categoryData}  // Dados para o gráfico
          dataKey="value"  // Chave para o valor
          nameKey="category"  // Chave para o nome da categoria
          cx="50%"
          cy="50%"
          outerRadius={100}
          fill="#82ca9d"
          label
        >
          {categoryData.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />  // Células coloridas
          ))}
        </Pie>
        <Tooltip />
        <Legend />
      </PieChart>
    </div>
  );
}

export default Dashboard;