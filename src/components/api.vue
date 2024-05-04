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
    mounted() {
        const message = this.$route.params.data;
        console.log(message);
        console.log('mounted觸發');
    }
    
}
</script>