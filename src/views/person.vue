<template>
<div>
    <van-nav-bar
      title="核酸检测预约登记"
      fixed
      safe-area-inset-top
      placeholder
    />
    <van-form @submit="doSubmit">
    <van-cell-group>
        <van-cell is-link title="证件类别" :value="form.zjlb" @click="options.zjlb.show = true" />
        <van-action-sheet v-model="options.zjlb.show" :actions="options.zjlb.actions" @select="onZjlbSelect" />
        <van-field label="证件号码" placeholder="请输入证件号码" v-model="form.zjhm" 
        required
        :rules="[{ required: true, message: '请填写证件号码' }]"
        >
            <template #button>
                <van-button size="small" plain @click="doScan"><van-icon name="photo-o" /></van-button>
            </template>
        </van-field>
        <van-field label="姓名" placeholder="请输入姓名"  v-model="form.xm" 
        required
        :rules="[{ required: true, message: '请填写姓名' }]"
        />
        <van-cell title="性别" class="xb" style="text-align:left">
            <van-radio-group v-model="form.xb" direction="horizontal">
                <van-radio name="1" shape="square">男</van-radio>
                <van-radio name="2" shape="square">女</van-radio>
            </van-radio-group>
        </van-cell>
        <van-field label="电话" placeholder="请输入11位手机号"  v-model="form.lxdh" 
        required
        :rules="[{ required: true, message: '请填写电话' }]"
        />
        <van-field label="年龄" placeholder="请输入年龄"  v-model="form.nl" />
        <van-field label="户籍地址" placeholder="请输入身份证上的户籍地址"  v-model="form.hjdz" />
        <van-field label="居住地址" placeholder="请输入您的现住址"  v-model="form.jzdz" 
        required
        :rules="[{ required: true, message: '请填写居住地址' }]"
        />
        <van-field label="工作单位" placeholder="请输入您的工作单位"  v-model="form.dw" />
        <van-field label="体温" placeholder="请输入您目前体温"  v-model="form.tw" />
        <van-field label="备注" placeholder="其他备注信息"  v-model="form.bz" />
    </van-cell-group>
    <div style="margin: 1rem;">
        <van-button round block type="info" native-type="submit">提交</van-button>
    </div>
    </van-form>
</div>
</template>
<script>
import { personSubmit } from '@/api'
import { randomIdCard } from '@/utils/random'
export default {
    data() {
        return {
            form: {
                djrq: '',
                zjlb: '身份证',
                zjhm: '',
                xm: '',
                xb: '1',
                lxdh: '',
                nl: '',
                nldw: '年',
                hjdz: '',
                jzdz: '',
                dw: '',
                tw: '',
                bz: '',
            },
            options: {
                zjlb: {
                    show: false,
                    actions: [{name:'身份证'}, {name:'户口本'}, {name:'护照'}]
                }
            }
        }
    },
    mounted() {
        this.form.djrq = new Date()
        this.loadQrCode()
    },
    methods: {
        loadQrCode() {
             var personInfo = window.localStorage.getItem('personInfo')
             //如果信息已经注册了，跳转到二维码页面
            if (personInfo) {
                this.$router.replace('/qrcode')
            }
        },
        doScan() {
            const vData = {
                zjhm: randomIdCard(),  //随机18位数字
                xb: '1',
                xm: '三酷猫',
                nl: '35',
                hjdz: '贝克街211B',
                csrq: '1986-10-10 00:00:00',
            }
            this.$dialog.alert({
                message: '原系统中，调起摄像头拍摄身份证信息，使用”百度证件识别API“，将识别结果填入页面，本系统使用模拟数据演示功能',
            }).then(() => {
                Object.assign(this.form, vData)
                //为了使用模拟数据，将生成的伪身份证号记录到缓存中
                window.localStorage.setItem('v-card-id', vData.zjhm)
            });
        },
        onZjlbSelect(item) {
            this.options.zjlb.show = false;
            this.form.zjlb = item.name
        },
        doSubmit() {
            personSubmit(this.form).then(res=>{
                //提交成功后，将信息保存到本地缓存
                window.localStorage.setItem('personInfo', JSON.stringify(res))
                //跳转到二维码页面
                this.$router.push('/qrcode')
            })
        }
    }
}
</script>