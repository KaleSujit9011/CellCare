import React, { useState } from 'react';
import axios from 'axios';
import FileUpload from './FileUpload';

function HealthDashboard({ predictionData, setPredictionData }) {
  const [sequencePrediction, setSequencePrediction] = useState(null)
  //LSTM endpoint
  const handleSequencePrediction = async () => {
  try {
    // Sample 10 cycles of data
    const sampleSequence = [
      {"C1": 0.000032, "C2": 0.010484, "C3": -0.717731, "C4": 95.203672, "min_voltage": 2.612467},
      {"C1": 0.000031, "C2": 0.010477, "C3": -0.680330, "C4": 94.682301, "min_voltage": 2.587209},
      {"C1": 0.000033, "C2": 0.010529, "C3": -0.702891, "C4": 94.193666, "min_voltage": 2.651917},
      {"C1": 0.000030, "C2": 0.010572, "C3": -0.603656, "C4": 93.639877, "min_voltage": 2.592948},
      {"C1": 0.000029, "C2": 0.010587, "C3": -0.695410, "C4": 93.688447, "min_voltage": 2.547420},
      {"C1": 0.000032, "C2": 0.010581, "C3": -0.689567, "C4": 93.234567, "min_voltage": 2.520948},
      {"C1": 0.000031, "C2": 0.010567, "C3": -0.712345, "C4": 92.876543, "min_voltage": 2.487927},
      {"C1": 0.000034, "C2": 0.010623, "C3": -0.734567, "C4": 92.456789, "min_voltage": 2.665205},
      {"C1": 0.000035, "C2": 0.010645, "C3": -0.756789, "C4": 92.123456, "min_voltage": 2.603858},
      {"C1": 0.000036, "C2": 0.010678, "C3": -0.765432, "C4": 91.987654, "min_voltage": 2.552854}
    ]
    
    const response = await axios.post('http://localhost:8000/predict_sequence', sampleSequence)
      setSequencePrediction(response.data)
    } catch (err) {
      console.error('Sequence prediction failed:', err)
    }
  }
  const getStatusColor = (status) => {
    if (status === 'Safe') return '#4CAF50'
    if (status === 'Warning') return '#FF9800'
    return '#F44336'
  }

  return (
    <div style={styles.container}>
      <h2 style={styles.header}>Battery Health Dashboard</h2>
      
      <FileUpload setPredictionData={setPredictionData} />
      
      {predictionData ? (
        <div style={styles.resultsGrid}>
          {/* Health Status Card */}
          <div style={{
            ...styles.card,
            backgroundColor: getStatusColor(predictionData.health_status),
            color: 'white',
          }}>
            <h3>Health Status</h3>
            <p style={styles.bigNumber}>{predictionData.health_status}</p>
          </div>

          {/* Remaining Life Card */}
          <div style={styles.card}>
            <h3>Remaining Useful Life</h3>
            <p style={styles.bigNumber}>{predictionData.RUL}</p>
            <p>cycles remaining</p>
          </div>

          {/* Capacity Card */}
          <div style={styles.card}>
            <h3>Current Capacity</h3>
            <p style={styles.bigNumber}>{predictionData.capacity.toFixed(2)}</p>
            <p>Ah</p>
          </div>

          {/* Stress Level Card */}
          <div style={styles.card}>
            <h3>Stress Level</h3>
            <p style={styles.bigNumber}>{predictionData.stress_level}</p>
          </div>
          <button onClick={handleSequencePrediction} style={styles.sequenceButton}>
          Predict Next 10 Cycles (LSTM)
          </button>
          {sequencePrediction && (
            <div style={styles.sequenceCard}>
              <h3>Future Capacity Predictions (Next 10 Cycles)</h3>
              <div style={styles.predictionList}>
                {sequencePrediction.predicted_capacities.map((cap, idx) => (
                  <span key={idx} style={styles.predictionValue}>
                    Cycle +{idx+1}: {cap} Ah<br/>
                  </span>
                ))}
              </div>
            </div>
          )}  
        </div>
        
      ) : (
        <p style={styles.placeholder}>Click the button above to analyze battery health</p>
      )}
    </div>
  )
}

const styles = {
  container: {
    padding: '40px',
    maxWidth: '1200px',
    margin: '0 auto',
  },
  header: {
    textAlign: 'center',
    color: '#1a1a2e',
    marginBottom: '20px',
  },
  resultsGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
    gap: '20px',
    marginTop: '30px',
  },
  card: {
    backgroundColor: 'white',
    padding: '30px',
    borderRadius: '10px',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
    textAlign: 'center',
  },
  bigNumber: {
    fontSize: '48px',
    fontWeight: 'bold',
    margin: '10px 0',
  },
  placeholder: {
    textAlign: 'center',
    color: '#666',
    fontSize: '18px',
    marginTop: '50px',
  },
  sequenceButton: {
  width:'10rem',
  height:'5rem',
  marginTop: '20px',
  padding: '12px 30px',
  backgroundColor: '#e74c3c',
  color: 'white',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
  fontSize: '16px',
  },
  sequenceCard: {
  marginTop: '30px',
  backgroundColor: 'white',
  padding: '30px',
  borderRadius: '10px',
  boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
  },
  predictionList: {
  display: 'inline-block',
  gridTemplateColumns: 'repeat(5, 1fr)',
  gap: '15px',
  marginTop: '20px',
  },
  predictionValue: {
  padding: '0.2rem',
  // backgroundColor: '#ecf0f1',
  // borderRadius: '5px',
  textAlign: 'center',
  fontSize: '14px',
  }
}

export default HealthDashboard