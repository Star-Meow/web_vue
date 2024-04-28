<template>
    <p>api</p>

</template>

<script>
    export default {
    created() {

        const formData = this.$route.params.formData;

        console.log(formData);
    }
    }
</script>