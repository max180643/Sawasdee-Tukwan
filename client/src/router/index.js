import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/Page/Home';
import Ping from '@/components/Ping';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    }
  ],
});
