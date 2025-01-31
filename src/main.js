import Vue from 'vue'
import App from './App.vue'
import Vant from 'vant';
import 'vant/lib/index.css';
import axios from 'axios'
import './styles/theme.less';
import dayjs from 'dayjs'
Vue.prototype.$http = axios
Vue.prototype.$bus = new Vue()
Vue.prototype.$dayjs = dayjs
import {router} from './router'

Vue.config.productionTip = false
import store from './store'
Vue.use(Vant)

//路由守卫
const whiteList = ['/login','/person', '/qrcode']

router.beforeEach(async(to, from, next) => {
    const hasToken = window.sessionStorage.getItem('Authorization')
    if (hasToken) {
        if (to.path === '/login') {
          next({ path: '/' })
        } else {
            next()
        }
    } else {
        if (whiteList.indexOf(to.path) !== -1) {
            next()
          } else {
            next('/login')
          }
    }
})

//应用实例
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App),
})
