<template>
    <p>api</p>

</template>

<script>
    export default {
    created() {

        const data = this.$route.params.data;

        console.log(data);
    }
    }
</script>