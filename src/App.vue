<template>
  <RouterView />

</template>

<script>


import { RouterView } from 'vue-router';
export default {
name: 'App',
components: {

  RouterView // 使用 RouterView 來顯示匹配的路由組件
}
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100..900&display=swap');
#app {



  font-family: Noto Sans TC, Helvetica, Arial, sans-serif;
  font-size: 20px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
