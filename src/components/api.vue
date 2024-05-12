<template>
    <div class = main>
        <div class = box>
            <h1>非常感謝您的填寫，以下是您的分析</h1>
            <h1>{{ formData }}</h1>
            <p>{{ info }}</p>
            
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';


export default {
    data() {
        return {
            formData: 'please wait a sec',

            info:'',
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
                this.formData = '你的人格分析結果: M 型(Mechanics)';
                this.info = 'M型人格的人通常被歸類為INTP（直覺-思考-感覺-知覺）類型。他們是邏輯思維者，喜歡分析和解決複雜的問題。他們對技術和科學充滿好奇心，喜歡探索新的思維模式和理論。他們通常沉浸於自己的世界中，喜歡獨立思考，並通過創造性的方式找到解決方案。';
            } else if (maxScore === this.sumA) {
                this.formData = '你的人格分析結果: A 型(Aesthetics)';
                this.info = 'A型人格的人通常被歸類為ISFP（內向-感覺-情感-知覺）類型。他們是敏感和富有想象力的人，喜歡通過藝術和創造性的方式表達自己。他們注重個人價值觀和情感體驗，喜歡追求自己內心的真實感受。他們可能是藝術家、音樂家或設計師，擅長通過色彩和形式傳達情感和意義。';
                
            } else if (maxScore === this.sumD) {
                this.formData = '你的人格分析結果: D 型(Dynamics)';
                this.info = 'D型人格的人通常被歸類為ESFJ（外向-感覺-情感-判斷）類型。他們是熱情和富有同情心的人，喜歡與他人建立聯繫並關心他人的需求。他們擅長組織和協調，喜歡在團隊中發揮領導作用。他們在社交場合中表現出色，善於交流，能夠為他人提供支持和幫助。';
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

p{
    padding: 0 75px;
    font-size: 24px;
}
</style>