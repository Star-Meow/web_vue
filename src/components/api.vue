<template>
    <div>
        <h1>{{ message }}</h1>
        <h1>api</h1>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    data() {
        return {
            message: ''
        };
    },
    created() {
        axios.get('http://127.0.0.1:5000/data')
            .then(response => {
                this.message = response.data.message;
                
            })
            .catch(error => {
                this.message = 'error';
                console.error('Error fetching data from Flask API:', error);
            });
    }
}
</script>