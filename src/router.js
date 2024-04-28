import { createRouter, createWebHistory } from 'vue-router';
import Form from './components/form.vue'; // 導入表單組件
import Api from './components/api.vue'; // 導入API組件
import Ans from './components/ans.vue'; 

const routes = [
    { path: '/', component: Form }, // 將表單組件設置為首頁路由
    { path: '/api', name: 'api', component: Api }, // 添加API組件的路由
    { path: '/ans', component: Ans },

  ];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;