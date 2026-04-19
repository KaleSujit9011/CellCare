import { useState } from 'react'
import './App.css'
import NavBar from './components/NavBar'
import HealthDashboard from './components/HealthDashboard'
import TechnicalDashboard from './components/TechnicalDashboard'

function App() {
  const [currentPage, setCurrentPage] = useState('health')
  const [predictionData, setPredictionData] = useState(null)

  return (
    <div className="App">
      <NavBar currentPage={currentPage} setCurrentPage={setCurrentPage} />
      
      {currentPage === 'health' ? (
        <HealthDashboard 
          predictionData={predictionData} 
          setPredictionData={setPredictionData} 
        />
      ) : (
        <TechnicalDashboard />
      )}
    </div>
  )
}

export default App