document.addEventListener('DOMContentLoaded', () => {
    const symptomsTextarea = document.getElementById('symptoms');
    const analyzeBtn = document.getElementById('analyze-btn');
    const possibleDiagnoses = document.getElementById('possible-diagnoses');
    const recommendations = document.getElementById('recommendations');

    analyzeBtn.addEventListener('click', async () => {
        const symptoms = symptomsTextarea.value.split(',').map(s => s.trim());
        
        try {
            const response = await axios.post('http://localhost:5000/api/analyze_symptoms', { symptoms });
            const result = response.data;

            possibleDiagnoses.innerHTML = `
                <h3>Possible Diagnoses:</h3>
                <ul>
                    ${result.possible_diagnoses.map(d => `<li>${d.name} (${(d.probability * 100).toFixed(1)}%)</li>`).join('')}
                </ul>
            `;

            recommendations.innerHTML = `
                <h3>Recommendations:</h3>
                <ul>
                    ${result.recommendations.map(r => `<li>${r}</li>`).join('')}
                </ul>
            `;
        } catch (error) {
            console.error('Error:', error);
            let errorMessage = 'An error occurred while analyzing symptoms. ';
            if (error.response) {
                // The request was made and the server responded with a status code
                // that falls out of the range of 2xx
                errorMessage += `Server responded with status ${error.response.status}: ${error.response.data}`;
            } else if (error.request) {
                // The request was made but no response was received
                errorMessage += 'No response received from the server. Check if the server is running.';
            } else {
                // Something happened in setting up the request that triggered an Error
                errorMessage += error.message;
            }
            alert(errorMessage);
        }
    });
});