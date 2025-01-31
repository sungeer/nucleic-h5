<template>
<div>
    <van-nav-bar
      :title="title[active]"
      fixed
      safe-area-inset-top
      placeholder
      @click-left="onClickLeft"
    >
      <!-- <template #right>

        <van-popover
        v-model="showPopover"
        theme="dark"
        trigger="click"
        placement="bottom-end"
        @select="selectMenu"
        :actions="actions"
      >
        <template #reference>
          <van-icon name="ellipsis" size="18" />
        </template>
      </van-popover>
      </template> -->
    </van-nav-bar>
    <new-label v-show="active == 0" @switchTab="handleSwitchTab"/>
    <regist ref="regist" v-show="active == 1" @close="handleNewLabel(0)"/>
    <query v-show="active == 2" @close="handleClosePrint"/>

    <van-tabbar v-model="active">
      <van-tabbar-item icon="orders-o">标签管理</van-tabbar-item>
      <van-tabbar-item icon="home-o">登记采集</van-tabbar-item>
      <van-tabbar-item icon="search">查询</van-tabbar-item>
      <!-- <van-tabbar-item icon="setting-o">设置</van-tabbar-item> -->
    </van-tabbar>

  <van-dialog v-model="showMode" title="采集模式设定" show-cancel-button @confirm="confirmMode">
      <van-row style="margin-top:0.5rem">
        <van-col span="10">采集模式</van-col>
        <van-col span="14">
          <van-radio-group v-model="form.mode" direction="horizontal">
              <van-radio name="1" >单采</van-radio>
              <van-radio name="2" >团采</van-radio>
          </van-radio-group>
        </van-col>
      </van-row>
  </van-dialog>

</div>
</template>
<script>
import Regist from '@/components/regist.vue'
import Query from '@/components/query.vue'
import newLabel from '@/components/newLabel.vue'
var exitAppTicker = 0;
export default {
  name: 'App',
  components: {
    Regist, Query, newLabel
  },
  data() {
    return {
      title: [
        '标签管理',
        '核酸检测登记',
        // '补打标签',
        '记录查询',
        '功能设置'
      ],
      active: 0,
      showMode: false,
      showPopover: false,
      actions: [{ text: '新建标签' }, { text: '打印标签' }],
      form: {
        mode: '1'
      },
      readerIsReady: false,
    }
  },
  watch: {
    active(val) {
      window.localStorage.setItem('active-tab', val)
      if (val == 2) {
        this.$bus.$emit('query')
      }
    }
  },
  mounted() {
    var self = this
    var mode = window.sessionStorage.getItem('gather-mode') || '0'
    console.log('gather-mode', mode)
    // this.showMode = mode == '0';
    document.addEventListener("backbutton", function(){
      if(exitAppTicker == 0){
          exitAppTicker++;
          self.$toast("再点一次退出");
          setTimeout(function(){
                  exitAppTicker = 0;
          },1000);
      }else if(exitAppTicker == 1){
          navigator.app.exitApp(); //退出app
      }
    }, false);
  },

  methods: {

    /**
     * 核心服务， 从标签库中创建一个标签
     * 1、首次打开页面时
     * 2、标签配额完成时
     * 3、主动创建标签时
     */
    serviceNewLabel() {
      // var sbid = window.localStorage.getItem('device-uuid')

    },
    /**
     * 核心服务， 登记标签
     * 判断标签配额，如果未到数量，增加计数, 否则创建下个标签
     *
     */
    serviceRegist() {

    },

    handleSwitchTab(index) {
      this.active = index
      // this.$store.dispatch('active', index)
      // window.localStorage.setItem('active-tab', index)
    },
    onClickLeft() {},
    confirmMode() {
      //确认采集模式后
      window.sessionStorage.setItem('gather-mode', this.form.mode)
    },
    selectMenu(t,index) {
      //console.log(t,i)
      if (index === 0) {
        // 新建标签
      } else if (index === 1) {
        //打印标签

      }
    },
    //关闭新建页面
    handleNewLabel(val) {
      // this.serviceNewLabel()
      this.active = val
    },
    //关闭补打页面
    handleClosePrint() {
      //啥也不做
    }
  }
}
</script>

<style>

</style>