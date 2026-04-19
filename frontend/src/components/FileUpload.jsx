import React, { useState } from 'react';
import axios from 'axios';

function FileUpload({ setPredictionData }) {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handlePredict = async () => {
    setLoading(true)
    setError(null)
    
    try {
      // Sample battery features for demo
      const sampleData = {
        C1: 0.000032,
        C2: 0.010484,
        C3: -0.717731,
        C4: 95.203672,
        min_voltage: 2.612467
      }
      
      const response = await axios.post('http://localhost:8000/predict', sampleData)
      setPredictionData(response.data)
    } catch (err) {
      setError('Failed to get prediction. Make sure FastAPI is running.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={styles.container}>
      <button onClick={handlePredict} disabled={loading} style={styles.button}>
        {loading ? 'Analyzing...' : 'Get Battery Health Prediction'}
      </button>
      {error && <p style={styles.error}>{error}</p>}
    </div>
  )
}

const styles = {
  container: {
    textAlign: 'center',
    margin: '30px 0',
  },
  button: {
    padding: '15px 40px',
    fontSize: '16px',
    backgroundColor: '#0f3460',
    color: 'white',
    border: 'none',
    borderRadius: '8px',
    cursor: 'pointer',
    fontWeight: 'bold',
  },
  error: {
    color: 'red',
    marginTop: '10px',
  },
}

export default FileUpload