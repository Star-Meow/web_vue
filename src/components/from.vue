<template>
    <form class = "login">
        <div class = "box">
            <div class = "email_input">
                <label for = "email"> Email(contact you)</label>
                <input id = "email" type = "text" v-model= "email"/>
            </div>

            
            <div class = "id_input">
                <label for = "ID"> ID(Student Number)</label>
                <input id = "ID" type = "text" v-model= "password"/>
            </div>
            <button @click="loginbtn">送出</button>

        </div>
    </form>

</template>

<script>
  export default {
    data() {
      return {
        email: "@example.com",
        ID: "",
      };
    },
    methods:{
    loginbtn(){
        this.$router.push('')
    }
  }
  };
</script>


<style scoped>
.login{
    display: flex;
    flex-direction: column;
    justify-content: center; /* 水平居中 */
    align-items: center; /* 垂直居中 */

}

.box{

    border: 2px solid #000; /* 黑色边框 */
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    height: 400px;
    width: 600px;;
}

.email_input{
    display: flex;
    flex-direction: column;
    text-align: center;
    margin-bottom: 15px;
    padding: 20px 60px;
    
}

.id_input{
    display: flex;
    flex-direction: column;
    text-align: center;
    margin-bottom: 15px;
    padding: 0 60px;

}

label{
    
    text-align: left;
    margin-bottom: 15px;
}
</style>