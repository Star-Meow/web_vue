<template>
    <div class = main>
        <div class = box>
            <h1>{{ formData }}</h1>
            <h1>非常感謝您的填寫</h1>
            
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';


export default {
    data() {
        return {
            formData: 'please wait a sec',
            sumM:0,
            sumA:0,
            sumD:0,
        };
    },
    computed: {
        formDataComputed() {
            const message = this.$store.getters.formData
            console.log(message.q_ans)
            this.formData = '你的人格分析結果是x型'
            this.sumM = parseInt(message.q_ans.slice(0, 5).reduce((acc, cur) => acc + cur, 0));
            this.sumA = parseInt(message.q_ans.slice(5, 10).reduce((acc, cur) => acc + cur, 0));
            this.sumD = parseInt(message.q_ans.slice(10, 15).reduce((acc, cur) => acc + cur, 0));
            
            const maxScore = Math.max(this.sumM, this.sumA, this.sumD);
            
            if (maxScore === this.sumM) {
                this.formData = '你的人格分析結果是M型';
            } else if (maxScore === this.sumA) {
                this.formData = '你的人格分析結果是A型';
            } else if (maxScore === this.sumD) {
                this.formData = '你的人格分析結果是D型';
            }
            console.log(this.formData)
            console.log(this.formData)
            console.log(this.formData)
            console.log(this.formData)
            return this.$store.getters.formData;

        }
    },
    watch: {
        formDataComputed(newFormData, oldFormData) {

            console.log('test2')
            this.formData = newFormData;
            
        }
    }
};


</script>


<style scoped>
.main{
    display: flex;
    flex-direction: column;
    justify-content: center; /* 水平居中 */
    align-items: center; /* 垂直居中 */
    background-color: #ffffff;
    height: auto;

}

.box{

border: 2px solid #ffffff; /* 黑色边框 */
border-radius: 8px;
padding: 20px;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
height: auto;
width: 800px;;
background-color: #ffffff;
margin: 20px;
}

.score{
    display: flex;
    flex-direction: row; /* 将子元素水平排列 */
    justify-content: space-between; /* 设置子元素之间的间隔为 10，并且居中对齐 */
    text-align: center;
    margin: 20px;
}
</style>