<template>

    <form class = "login">
        <div class = "box">
            <div class = "id_input">
                <label for = "ID"> 學號</label>
                <input id = "ID" type = "text" v-model= "password"/>
            </div>

            <div class = "radiobox">
                <label for = "gender"> 生理性別</label><br>
                <label><input id="term_gender1" type="radio" v-model="gender" value="male"/>男性</label>
                <label><input id="term_gender1" type="radio" v-model="gender" value="female"/>女性</label>    
                <label><input id="term_gender1" type="radio" v-model="gender" value="other"/>不願告訴</label>
            </div>

            <div class = "radiobox">
                <label for = "class"> 年級</label><br>
                <label><input id="term_class" type="radio" v-model="ord" value="1"/>大一</label>
                <label><input id="term_class" type="radio" v-model="ord" value="2"/>大二</label>
                <label><input id="term_class" type="radio" v-model="ord" value="3"/>大三</label>
                <label><input id="term_class" type="radio" v-model="ord" value="4"/>大四</label>
                <label><input id="term_class" type="radio" v-model="ord" value="5"/>畢業或其他</label>
            </div>

            <div class = "radiobox">
                <label for = "class"> 你是否嘗試做過遊戲</label><br>
                <label><input id="term_class" type="radio" v-model="trygame" value="1"/>是</label>
                <label><input id="term_class" type="radio" v-model="trygame" value="0"/>否</label>

            </div>
        </div>


        <div v-for = "(question,index) in question" :key = "index" class = "box">
            <div class = "radiobox">
                <label for = "q_form"> {{ question }} </label><br>
                <div class="ansblock">
                    <div class="ans">
                        <label for = "q_form"></label><br>
                        <label for = "q_form" >非常不同意</label>
                    </div>
                    <div class="ans">
                        <label for = "q_form"> 1 </label>
                        <label><input id="ans1" type="radio" v-model="q1_ans" value="1"/></label>
                    </div>
                    <div class="ans">
                        <label for = "q_form"> 2 </label>
                        <label><input id="ans2" type="radio" v-model="q1_ans" value="2"/></label>
                    </div>                
                    <div class="ans">
                        <label for = "q_form"> 3 </label>
                        <label><input id="ans3" type="radio" v-model="q1_ans" value="3"/></label>
                    </div>
                    <div class="ans">
                        <label for = "q_form"> 4 </label>
                        <label><input id="ans4" type="radio" v-model="q1_ans" value="4"/></label>
                    </div>
                    <div class="ans">
                        <label for = "q_form"> 5 </label>
                        <label><input id="ans5" type="radio" v-model="q1_ans" value="5"/></label>
                    </div>                
                    <div class="ans">
                        <label for = "q_form"> 6 </label>
                        <label><input id="ans6" type="radio" v-model="q1_ans" value="6"/></label>
                    </div>
                    <div class="ans">
                        <label for = "q_form"> 7 </label>
                        <label><input id="ans7" type="radio" v-model="q1_ans" value="7"/></label>
                    </div>
                    <div class="ans">
                        <label for = "q_form"></label><br>
                        <label for = "q_form">非常同意</label>
                    </div>
                </div>
            </div>
        </div>


        <div class = "box">
            <div class = "ans_input">
                    <label> 回饋區</label>
                    <input id = "ans" type = "text" v-model= "ans"/>
            </div>
        </div>
    </form>


</template>

<script>
  export default {
    data() {
      return {
        ans: "",
        ID: "",
        gender:"",
        ord:"",
        trygame:"",
        q1_ans:"",
        question:[
            "你知道怎麼寫程式-M",
            "你覺得自己可以用程式語言跟電腦溝通-M",
            "你覺得成程式碼像數學一樣難懂-M",
            "你不知道有什麼資源能解決你程式的問題-M",
            "你會好奇別人程式怎麼寫-M",
            "你喜歡想天馬行空的事-A",
            "你覺得自己很有想法-A",
            "在畫圖時你知道怎麼找參考-A",
            "你覺得自己沒辦法把想法做出來-A",
            "你常被說是細心的人-A",
            "你喜歡規劃自己的時間-D",
            "你平常會督促朋友一起做作業-D",
            "你能清楚表達自己的想法-D",
            "你不覺得自己是團隊的一份子-D",
            "比起聆聽你更想表達自己-D",
        ]
      };
    },

    methods:{

    }

  };
</script>


<style scoped>

.login{
    display: flex;
    flex-direction: column;
    justify-content: center; /* 水平居中 */
    align-items: center; /* 垂直居中 */
    background-color: #f7f7f7;
    height: 100vh;

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

.selectbox{
    display: flex;
    flex-direction: column;
    text-align: center;
    margin-bottom: 15px;
    padding: 0px 60px;
}

.ans_input{
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

.ansblock{
    display: flex;
    flex-direction: row;
    justify-content: center;
    
}

.ans{
    display: flex;
    flex-direction: column;
    text-align: center;
    margin:20px;
}

label{
    
    text-align: left;
    margin-bottom: 15px;
}
</style>