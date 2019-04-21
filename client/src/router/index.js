import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/page/Home';
import Today from '@/page/Today';
import Random from '@/page/Random';
import Custom from '@/page/Custom';
import Ping from '@/components/Ping';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/custom',
      name: 'custom',
      component: Custom,
    },
    {
      path: '/today',
      name: 'today',
      component: Today,
    },
    {
      path: '/random',
      name: 'random',
      component: Random,
    },
  ],
});
