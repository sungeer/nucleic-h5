<template>
    <div>
        <van-nav-bar
      title="我的预约二维码"
      fixed
      safe-area-inset-top
      placeholder
    />
     <van-cell-group :border="false" style="text-align:center;font-size:1.1rem">
         <span>预约日期：{{ djrq }}</span>
     </van-cell-group>
    <van-cell-group style="text-align:center">
        
        <vue-qr :text="text" :size="200"></vue-qr>
    </van-cell-group>
    <van-cell-group :border="false" style="text-align:center;font-size:1.1rem; padding-top:1rem">
        <van-button plain @click="doRedo">重新填写</van-button>
     </van-cell-group>
    </div>
</template>
<script>
import vueQr from 'vue-qr'
export default {
    components: {vueQr},
    data() {
        return {
            text: '',
            djrq: ''
        }
    },
    mounted() {
        this.loadQrCode()
    },
    methods: {
        loadQrCode() {
            var personInfo = window.localStorage.getItem('personInfo')
            if (personInfo) {
                var person = JSON.parse(personInfo)
                //将注册信息的主要内容组合成字符串，然后使用Base64编码进行加密
                this.djrq = this.$dayjs(person.djrq).format('YYYY年MM月DD日')
                this.text = btoa([person.id, person.zjhm, person.lxdh, person.xm].join('|'))
            } else {
                this.$router.replace('/person')
            }
        },
        doRedo() {
            this.$dialog.confirm({
                title: '确认',
                message: '是否清除当前二维码，重新填写信息',
            })
            .then(() => {
                window.localStorage.removeItem('personInfo')
                this.$router.replace('/person')
            })
            .catch(() => {
                // on cancel
            });
            
        }
    }
}
</script>