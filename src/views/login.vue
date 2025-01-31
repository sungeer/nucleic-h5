<template>
<div>
    <van-nav-bar
      title="登录"
      fixed
      safe-area-inset-top
      placeholder
    />
    <van-row style="font-size:1.2rem;padding:0.5rem" type="flex" justify="center">
        <van-col>核酸采集系统登记平台</van-col>
    </van-row>
    <van-cell-group title="">
        <van-field v-model="username" type="text" label="用户名" class="labelCode">
            </van-field>
         <van-field v-model="password" type="password" label="密码" class="labelCode">
            </van-field>
    </van-cell-group>
    <van-cell-group :border="false">
        <div style="display:flex;justify-content:center;padding-top:2rem">
            <van-button style="width:30%" round block type="info" @click="doSubmit">登录</van-button>
        </div>
    </van-cell-group>
</div>
</template>
<script>
import { login, userInfo } from '@/api'
export default {
    data() {
        return {
            loading: false,
            username: '',
            password: '',
        }
    },
    methods: {
        doSubmit() {
            this.loading = true;
            login({username: this.username, password: this.password})
            .then(res => {
                window.sessionStorage.setItem('Authorization',res.access_token)
                //登记成功后，获取当前登录用户信息
                userInfo().then(info=>{
                    window.sessionStorage.setItem('userid',info.id)
                    this.$router.push({ path: '/checkin'})
                this.loading = false
                })
                
            })
            .catch((e) => {
                console.log(e)
              this.loading = false
            })
        }
    }
}
</script>