import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'
import router from './router';


const store = createStore({
    state: {
      formData: {} // 初始化表单数据为空对象
    },
    mutations: {
      setFormData(state, data) {
        state.formData = data;
      }
    },
    actions: {
      updateFormData({ commit }, data) {
        commit('setFormData', data);
      }
    },
    getters: {
      formData(state) {
        return state.formData;
      }
    }
  });

createApp(App).use(store).use(router).mount('#app')
