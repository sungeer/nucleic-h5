<template>
    <div>
        <van-notice-bar :scrollable="false" wrapable text="请扫描标签号，或手工录入标签号" />
        <van-row>
            <van-col span="6"></van-col>
        <van-col span="12"></van-col>
        </van-row>
        <van-field  v-model="cjdd" class="cjdd" readonly label="采集地点">
            <template #button>
                <van-button :disabled="isGathering" size="small" type="info" plain @click="editCjdd">修改地点</van-button>
            </template>
        </van-field>
        <van-field v-model="labelCount" type="number" :disabled="isGathering" label="分组数量" class="labelCount"></van-field>
        <van-field v-model="labelCode" :disabled="isGathering" required type="tel" label="标签内容" class="labelCode" clearable placeholder="请录入或扫描标签码">

        </van-field>
        <van-cell-group style="padding: 1rem">
        
             <!-- <van-button block round type="primary" @click="gotoRegist">开始登记</van-button> -->
        <van-row type="flex" justify="center" style="margin-top:2rem">
            <van-col span="18">
                <van-button :disabled="isGathering" block round plain type="info" @click="doScan">扫描标签</van-button>
            </van-col>
        </van-row>
        <van-row type="flex" justify="center" style="margin-top:2rem">
            <van-col span="18">
                <van-button :disabled="isGathering" block round type="primary" @click="gotoRegist">开始登记</van-button>
            </van-col>
        </van-row>
        </van-cell-group>
        <van-dialog v-model="showCjdd" title="修改采集地点" show-cancel-button @confirm="confirmNewCjdd">
            <van-field v-model="newCjdd" clearable placeholder="请输入采集地点，小于10字"></van-field>
        </van-dialog>
    </div>
</template>
<script>
import { randomString } from '@/utils/random'
export default {
    name: 'newLabel',
    data() {
        return {
            cjdd: '',
            newCjdd: '',
            showCjdd: false,
            labelCount: 1,
            labelCode: '',
            isGathering: false,
        }
    },
    mounted() {
        window.vm = this;
        this.cjdd = window.localStorage.getItem('cjdd') || ''
        this.labelCode = window.localStorage.getItem('labelCode') || ''
        this.labelCount = window.localStorage.getItem('labelCount') || 5
         this.isGathering = this.getGathering()
        this.$bus.$on('labelCountChange', (v)=>{
            this.labelCount = v;
        })
        this.$bus.$on('labelCodeClear', ()=>{
            window.localStorage.setItem('labelCode', '')
            this.labelCode = ''
        })
        this.$bus.$on('finishGather', ()=>{
            this.isGathering = false
            window.localStorage.setItem('isGathering', 0)
        })
        // var bqsl = window.localStorage.getItem('bqsl') || 1
        // this.value = Number(bqsl);
    },
    methods: {
        getGathering() {
            if (this.labelCode == '') {
                return false;
            }
            var g = window.localStorage.getItem('isGathering')
            if (g == null) {
                var a = window.localStorage.getItem('labelCount')
                var b = window.localStorage.getItem('labelCounter')
                if (a > b) {
                    g = 1
                }
            }
            return g == 1;
        },
        editCjdd() {
            this.newCjdd = this.cjdd;
            this.showCjdd = true;
        },
        confirmNewCjdd() {
            window.localStorage.setItem('cjdd', this.newCjdd)
            this.cjdd = this.newCjdd
            this.showCjdd = false;
        },
        doClear() {
            this.labelCode = ''
        },
        doScan() {
            this.$dialog.alert({
            message: '原系统中，调起摄像头拍摄试剂盒上的条码，使用”百度条码识别API“，将识别结果填入标签编号，本系统使用模拟数据演示功能',
            }).then(() => {
                this.labelCode = randomString(8)
            });
        },
        gotoRegist() {
            if (this.labelCode == '') {
                this.$toast('请录入或扫描标签')
                return;
            }
            if (this.cjdd == '') {
                this.$toast('请选择采集地点')
                return;
            }
            this.$emit('switchTab', 1)
            window.localStorage.setItem('isGathering',1)
            window.localStorage.setItem('labelCode', this.labelCode)
            window.localStorage.setItem('labelCount', this.labelCount)
            this.isGathering = true;
            this.$bus.$emit('lableCodeChange', this.labelCode)
        },
    }
}
</script>

<style>
  .labelCount input {
      color: #059b00;
      font-size: 1.2rem;
  }
  .labelCode input {
      color: #cc0a0a;
      font-size: 1.2rem;
  }
  .cjdd .van-cell__title {
      line-height: 2rem;
  }
  .custom-button {
    width: 2rem;
    display:block;
    color: #fff;
    font-size: 1.2rem;
    line-height: 2rem;
    text-align: center;
    background-color: #ee0a24;
    border-radius: 4rem;
    /* padding: 0.1rem 0.8rem 0.1rem 0.6rem; */
    box-shadow: #3f3637;
  }
</style>