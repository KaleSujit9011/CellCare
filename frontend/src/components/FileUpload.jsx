import React, { useState } from 'react'
import axios from 'axios'

function FileUpload({setPredictionData}) {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [selectedFile, setSelectedFile] = useState(null)
  
  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0])
    setError(null)
  }

  const handleUpload = async () => {
    if (!selectedFile) {
      setError('Please select a CSV file first')
      return
    }

    setLoading(true)
    setError(null)
    
    try {
      const formData = new FormData()
      formData.append('file', selectedFile)
      
      const singleResponse = await axios.post('http://localhost:8000/predict_csv', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      
      setPredictionData(singleResponse.data)
      try {
        const sequenceResponse = await axios.post('http://localhost:8000/predict_sequence_csv', formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        })
        setPredictionData(prev => ({
          ...prev,
          sequencePrediction: sequenceResponse.data
        }))
      
      } catch (seqErr) {
        console.log('Sequence prediction not available:', seqErr.response?.data?.detail)
      }
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to upload file. Make sure it has the required columns.')
    } finally {
      setLoading(false)
    }
  }

  const handleSamplePredict = async () => {
    setLoading(true)
    setError(null)
    
    try {
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
      setError('Failed to get prediction')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={styles.container}><div style={styles.instructionBox}>
        <h4 style={styles.instructionTitle}> CSV Upload Instructions</h4>
      
        <p style={styles.instructionText}>
          Your CSV file must contain these exact columns:
        </p>
      
        <code style={styles.codeBlock}>
          C1, C2, C3, C4, min_voltage
        </code>
      
        <p style={styles.instructionSubtext}>
        <strong>Tip:</strong> Download one of our demo files from <code>data/demo/</code> folder to see the correct format
        </p>
      </div>
      <div style={styles.uploadSection}>
        <input 
          type="file" 
          accept=".csv" 
          onChange={handleFileChange}
          style={styles.fileInput}
        />
        <button onClick={handleUpload} disabled={loading || !selectedFile} style={styles.button}>
          {loading ? 'Analyzing...' : 'Upload & Analyze CSV'}
        </button>
      </div>
      
      <div style={styles.divider}>OR</div>
      
      <button onClick={handleSamplePredict} disabled={loading} style={styles.sampleButton}>
        Try Sample Data
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
  instructionBox: {
    backgroundColor: '#e8f4f8',           
    border: '2px solid #3498db',          
    borderRadius: '8px',                  
    padding: '20px',                      
    marginBottom: '25px',                 
    textAlign: 'left',                    
  },
  
  instructionTitle: {
    
    margin: '0 0 10px 0',                 
    color: '#2c3e50',                     
    fontSize: '18px',                     
  },
  
  instructionText: {
    margin: '10px 0',                    
    color: '#34495e',                    
    fontSize: '14px',                     
  },
  
  codeBlock: {
    display: 'block',                     
    backgroundColor: '#2c3e50',
    color: '#ecf0f1',                     
    padding: '10px 15px',                
    borderRadius: '4px',                  
    margin: '10px 0',                     
    fontSize: '14px',                     
    fontFamily: 'monospace',              
  },
  
  instructionSubtext: {
   
    margin: '15px 0 0 0',                 
    fontSize: '13px',                     
    color: '#7f8c8d',                   
  },
  
  uploadSection: {
    display: 'flex',
    gap: '15px',
    justifyContent: 'center',
    alignItems: 'center',
  },
  fileInput: {
    padding: '10px',
    border: '2px dashed #0f3460',
    borderRadius: '5px',
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
  divider: {
    margin: '20px 0',
    color: '#666',
  },
  sampleButton: {
    padding: '12px 30px',
    fontSize: '14px',
    backgroundColor: '#16213e',
    color: 'white',
    border: 'none',
    borderRadius: '8px',
    cursor: 'pointer',
  },
  error: {
    color: 'red',
    marginTop: '10px',
  },
}

export default FileUpload