import Vue from 'vue'
import Vuex from 'vuex'

//挂载Vuex
Vue.use(Vuex)

//创建VueX对象
const store = new Vuex.Store({
    state:{
        //存放的键值对就是所要管理的状态
        bqsl: 1,
        lableCode: '',
        active: 0
    },
    mutations:{
        //es6语法，等同edit:funcion(){...}
        bqsl(state, val){
            state.bqsl = val
            window.localStorage.setItem('bqsl', val);
        },
        labelCode(state, val) {
            state.labelCode = val
            window.localStorage.setItem('labelCode', val)
        },
        active(state, val) {
            state.active = val
        }
    },
    actions: {
        bqsl(context, payload) {
            context.commit('bqsl', payload)
        },
        labelCode(context, payload) {
            context.commit('labelCode', payload)
        },
        active(context, val) {
            context.commit('active', val)
        }
    },
    getters: {
        bqsl(state) {
            console.log('>>>'+state.bqsl)
            return Number(window.localStorage.getItem('bqsl'))
        },
        labelCode(state) {
            console.log('>>>'+state.lableCode)
            return window.localStorage.getItem('labelCode')
        },
        active(state) {
            return state.active
        }
    }
})

export default store