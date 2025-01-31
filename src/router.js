import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

const routes = [
  {
    path: '*',
    redirect: '/login'
  },
  {
    name: 'login',
    component: () => import('./views/login'),
    meta: { title: '登录'}
  },
  {
    name: 'person',
    component: () => import('./views/person'),
    meta: { title: '预约'}
  },
  {
    name: 'qrcode',
    component: () => import('./views/qrcode'),
    meta: { title: '预约信息'}
  },
  {
    name: 'checkin',
    component: () => import('./views/checkin'),
    meta: { title: '登记' }
  }
];

routes.forEach(route => {
  route.path = route.path || '/' + (route.name || '');
});

const router = new Router({ routes });

router.beforeEach((to, from, next) => {
  // const title = to.meta && to.meta.title;
  // if (title) {
  //   document.title = title;
  // }
  next();
});

export {
  router
};