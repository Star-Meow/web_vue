<template>

    <form class = "login">
          <div class = "box">
            <h1 for = "title"> 畢專三型人格調查</h1>
          </div>
        <div class = "box">
            <div class = "id_input">
                <label for = "ID"> 學號</label>
                <input id = "ID" type = "text" v-model= "ID"/>
            </div>
            <label class = "value1"> 生理性別</label>
            <div class = "radiobox1">
                <label><input id="term_gender1" type="radio" v-model="gender" value="male"/>男性</label>
                <label><input id="term_gender1" type="radio" v-model="gender" value="female"/>女性</label>    
                <label><input id="term_gender1" type="radio" v-model="gender" value="other"/>不願告訴</label>
            </div>

            <label class = "value1"> 年級</label>
            <div class = "radiobox1">
                <label><input id="term_class" type="radio" v-model="old" value="1"/>大一</label>
                <label><input id="term_class" type="radio" v-model="old" value="2"/>大二</label>
                <label><input id="term_class" type="radio" v-model="old" value="3"/>大三</label>
                <label><input id="term_class" type="radio" v-model="old" value="4"/>大四</label>
                <label><input id="term_class" type="radio" v-model="old" value="5"/>畢業或其他</label>
                
            </div>
            <label  class = "value1"> 你是否嘗試做過遊戲</label>
            <div class = "radiobox1">
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
                    <div class="ans" v-for="i in 7" :key="i">
                        <label>{{ i }}</label>
                        <input type="radio" :id="'ans' + i + '_' + index" :value="i" v-model="q_ans[index]"/>
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
                    <label> 回饋區(可不填寫)</label>
                    <input id = "ans1" type = "text" v-model= "ans[0]"/>
            </div>
        </div>
        <div class = "box">
            <div class = "ans_input">
                    <label> 在與人合作上是否有其他問題?(可不填寫)</label>
                    <input id = "ans2" type = "text" v-model= "ans[1]"/>
            </div>
            
        </div>

        <div >

                <button type="button" class="subbtn" @click="subForm">送出表單</button>

        </div>

    </form>


</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {

      ID: "",
      gender:"",
      old:"",
      trygame:"",
      q_ans: Array(14).fill(""),
      ans: Array(2).fill(""),
      formData: {}, // 將 formData 添加到 data 中
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
    subForm() {
        // 检查每个输入项目
        if (!this.ID || !this.gender || !this.old || !this.trygame) {

            alert("請檢查學號、性別、年級等是否漏填！");
            return;
        }
        for (let i = 0; i < this.q_ans.length; i++) {
            if (!this.q_ans[i]) {

                alert(`請檢查問題${i + 1}的答案！`);
                return;
            }
        }

      this.formData = { 
        ID: this.ID,
        gender: this.gender,
        old: this.old,
        trygame: this.trygame,
        q_ans: this.q_ans,
        ans: this.ans
      };
      
      this.$store.dispatch('updateFormData', { 
          ID: this.ID,
          gender: this.gender,
          old: this.old,
          trygame: this.trygame,
          q_ans: this.q_ans,
          ans: this.ans
          });
      
      this.$router.push({ name: 'api' });
      axios.post('http://127.0.0.1:5000/data', this.formData)
        .then(response => {
          console.log('表單提交成功:', response.data);
          
        })
        .catch(error => {
          console.error('表單提交失敗:', error);
        });   
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

.value1{
    display: flex;
    margin-bottom: 15px;
    padding: 0 60px;
}

.radiobox1 {
    display: flex;
    flex-direction: row;

    margin-bottom: 15px;
    padding: 0 60px;
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

.subbtn {
  position: fixed;
  bottom: 70px; /* 距离底部的距离 */
  right: 70px; /* 距离右侧的距离 */
}

/* 可以根据需要调整按钮的样式 */
.subbtn {
  padding: 15px 25px;
  font-size: 18px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 10px;
  cursor: pointer;
}

/* 可以添加其他样式，如 hover 效果等 */
.subbtn:hover {
  background-color: #0056b3;
}

/* 给输入框设置边框样式 */
input[type="text"] {
  /* 设置边框宽度、样式和颜色 */
  border: 2px solid #8f8f8f; /* 边框颜色为蓝色，可以根据需要调整 */
  /* 设置圆角 */
  border-radius: 8px; /* 圆角半径，越大越圆 */
  /* 设置输入框内边距 */
  padding: 10px 15px; /* 上下 10px，左右 15px */
  /* 设置输入框的字体大小和颜色 */
  font-size: 16px; /* 字体大小 */
  color: #333; /* 字体颜色 */
}

/* 悬停时改变输入框边框颜色 */
input[type="text"]:hover {
  border-color: #dfdfdf; /* 鼠标悬停时的边框颜色 */
}

/* 聚焦时改变输入框边框颜色 */
input[type="text"]:focus {
  outline: none; /* 移除默认的聚焦边框 */
  border-color: #8f8f8f; /* 输入框聚焦时的边框颜色 */
}

</style>