import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/page/Home';
import Random from '@/page/Random';
import Custom from '@/page/Custom';
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
    },
    {
      path: '/random',
      name: 'Random',
      component: Random,
    },
    {
      path: '/custom',
      name: 'Custom',
      component: Custom,
    }
  ],
});
