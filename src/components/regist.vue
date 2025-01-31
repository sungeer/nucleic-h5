<template>
    <div>
        <van-cell-group title="">
            <van-row style="padding: 0.5rem 0;text-align: center">
                <van-col style="font-size:1.1rem;" span="6">分组数量</van-col>
                <van-col span="6">
                    <span style="font-size:1.1rem; color: #059b00;">{{ counter.total}}</span> 
                </van-col>
                <van-col style="font-size:1.1rem;" span="6">已采集</van-col>
                <van-col span="6">
                    <span style="font-size:1.1rem">{{ counter.current}}</span>
                </van-col>
            </van-row>
        </van-cell-group>
        <van-field v-model="labelCode" type="number" label="标签内容" class="labelCode" readonly>
        </van-field>
        <van-cell-group title="">
            <van-field
                v-model="form.zjhm"
                required
                
                name="zjhm"
                label="身份证号"
                placeholder="身份证号"
                @input="handleInput"
            >
                <template #button>
                    <van-button size="small" type="primary" @click="readInfo" >扫二维码</van-button>
                </template>
            </van-field>
            <van-field
                v-model="form.xm"
                required
                name="name"
                label="姓名"
                placeholder="姓名"
            >
                
            </van-field>
            <van-cell title="性别" class="xb" style="text-align:left">
                <van-radio-group v-model="form.xb" direction="horizontal">
                    <van-radio name="1" shape="square">男</van-radio>
                    <van-radio name="2" shape="square">女</van-radio>
                </van-radio-group>
            </van-cell>
            <van-row>
                <van-col span="15">
                    <van-field
                        v-model="form.csrq"
                        readonly
                        type="text"
                        name="birth"
                        label="出生日期"
                        placeholder="出生日期"
                        clickable
                        right-icon="arrow-down" @click-input="onClickCsrq" @click-right-icon="onClickCsrq"
                    />
                </van-col>
                <van-col span="9" >
                    <van-field
                        v-model="form.nl"
                        class="nl"
                        name="nl"
                        required
                        type="tel"
                        label="年龄"
                        placeholder="年龄"
                    />
                </van-col>
            </van-row>
            <van-field
                    v-model="form.lxdh"
                    type="tel"
                    required
                    name="lxdh"
                    label="联系电话"
                    placeholder="联系电话"
                />
        </van-cell-group>
        <van-cell-group title="">
                <van-field
                v-model="form.hjdz"
                required
                name="hjdz"
                label="户籍地址"
                placeholder="户籍地址"
            />
            <van-field
                v-model="form.jzdz"
                required
                name="jzdz"
                label="居住地址"
                placeholder="居住地址"
            />
        </van-cell-group>
        <van-cell-group title="">
            <!-- <van-field
                v-model="form.tw"
                type="tel"
                name="tw"
                label="体温"
                placeholder="体温"
            /> -->
            <van-field
                v-model="form.bz"
                
                autosize
                
                name="bz"
                label="备注"
                placeholder="备注"
            />
        </van-cell-group>
        <van-cell-group :border="false">
            <div style="margin: 0.1rem 1rem 0.4rem 1rem;">
                <van-button round block type="info" @click="onSubmit">登记</van-button>
            </div>
        </van-cell-group>

        <van-cell-group :border="false">
            <div style="margin: 0.1rem 1rem 1rem 1rem;">
                <van-button round block plain type="danger" @click="onFinish">结束当前分组</van-button>
            </div>
        </van-cell-group>
        <van-popup v-model="popers.csrq.show" round position="bottom">
            <van-datetime-picker
            v-model="birthday"
            type="date"
            title="选择出生日期"
            :min-date="minDate"
            :max-date="maxDate"
            @confirm="confirmBirth"
            @cancel="popers.csrq.show = false"
            :formatter="formatter"
            />
        </van-popup>
        <van-overlay :show="isSaving" @click="isSaving = false">
        <div class="wrapper" @click.stop>
            <van-loading size="2rem">正在提交登记</van-loading>
        </div>
        </van-overlay>
    </div>
</template>
<script>
import { personGet, checkinSubmit } from '@/api'
function validateIdCard(code) {
    if (code.length != 18) {
        return false;
    }
    return true;
}
export default {
    name: 'Regist',
    data() {
        return {
            isSaving:false,
            birthday: new Date(),
            minDate: new Date(1900, 0, 1),
            maxDate: new Date(),
            labelCode: '',
            counter: {
                current: 1,
                total: 5,
            },
            form: {
                rylb: '',
                zjhm: '',
                xm: '',
                xb: '',
                nl: '',
                csrq: '',
                dz: '', 
                hjdz: '',
                jzdz: '',
                lxdh: '',
                cjry: window.sessionStorage.getItem('userid'),
                person_id: '',
            },
            popers: {
                userType: {
                    show: false,
                    options: [
                        
                    ]
                },
                csrq: {
                    show: false,
                }
            },
            readerIsReady: false,
        }
    },
    mounted() {
        this.counter.total =  window.localStorage.getItem('labelCount')
        this.labelCode = window.localStorage.getItem('labelCode')
        if (this.labelCode == '') {
            this.$bus.$emit('labelCodeClear', '')
            this.$emit('close', 0)
        }
        var total = window.localStorage.getItem('labelCount') || 5
        var current = window.localStorage.getItem('labelCounter') || 0
        this.counter.total = Number(total)
        this.counter.current = Number(current)
        this.$bus.$on('lableCodeChange', (v)=>{
            this.labelCode = v;
            this.counter.current = 0;
            window.localStorage.setItem('labelCounter', this.counter.current)
        })
        this.$bus.$on('labelCountChange', (v)=>{
            this.counter.total = v;
            this.counter.current = 0;
            window.localStorage.setItem('labelCounter', this.counter.current)
        })
    },
    watch:{
        '$store.state.bqsl' (val) {
            this.counter.total = Number(val)
            this.counter.current = 0
        }
    },
    methods: {
        formatter(type, val) {
            if (type === 'year') {
                return `${val}年`;
            } else if (type === 'month') {
                return `${val}月`;
            }
            return val;
        },
        readInfo(){
            this.$dialog.alert({
                message: '原系统中，调起摄像头拍摄预约人员的二维码，获取预约人员信息，根据人员信息中的证件号码获取后台数据，填入页面，本系统中使用模拟数据',
            }).then(() => {
                this.form.zjhm = window.localStorage.getItem('v-card-id')
                if (this.form.zjhm !== '') {
                    this.getPersonInfo(this.form)
                } else {
                    this.$toast('请输入预约人员的身份证号码')
                }
            });
            
        },
         decode(base64){
            // 对base64转编码
            var decode = atob(base64);
            // 编码转字符串
            var str = decodeURI(decode);
            return str;
        },
        handleInput(value) {
            if (value.length == 18) {
                var csrq = value.substr(6,8).replace(/(\d{4})(\d{2})(\d{2})/, '$1-$2-$3')
                var xb = value.substr(16,1)
                this.form.xb = xb 
                this.form.csrq = csrq
            }
        },
        confirmBirth(v) {
            console.log(v)
            this.popers.csrq.show = false;
            this.form.csrq = this.$dayjs(this.birthday).format('YYYY-MM-DD')
        },
        onClickCsrq() {
            if (this.form.csrq) {
                this.birthday = this.$dayjs(this.form.csrq).toDate()
            } 
            this.popers.csrq.show = true;
        },
        getPersonInfo(result) {
            personGet({zjhm: result.zjhm}).then(res=>{
                if (res) {
                    res.csrq = this.$dayjs(res.csrq).format('YYYY-MM-DD')
                    Object.assign(this.form, res)
                    // 预约人员ID字段
                    this.form.person_id = res.id
                } else {
                    console.log('未找到人员信息')
                }
            })
        },
        onSubmit() {
            if (this.labelCode == '') {
                this.$toast('请先选择标签')
                this.$bus.$emit('labelCodeClear', '')
                this.$emit('close', 0)
                return;
            }
            if (this.form.zjhm == '') {
                this.$toast('身份证号不能为空')
                return
            }
            var valid = validateIdCard(this.form.zjhm)
            if (!valid) {
                this.$toast('身份证号无效')
                return
            }
            if (this.form.xm == '') {
                this.$toast('姓名不能为空')
                return
            }
            if (this.form.nl == '') {
                this.$toast('年龄不能为空')
                return
            }
            if (this.form.hjdz == '') {
                this.$toast('户籍地址不能为空')
                return
            }
            if (this.form.jzdz == '') {
                this.$toast('居住地址不能为空')
                return
            }
            if (this.form.lxdh == '') {
                this.$toast('联系电话不能为空')
                return
            }
            let data = Object.assign({}, this.form)
            let sbid = window.localStorage.getItem('device-uuid')
            data = Object.assign(data, {
                bqbh: this.labelCode,
                bqxh: this.counter.current,
                csrq: this.$dayjs(this.form.csrq).format('YYYY-MM-DD 00:00:00'),
                sbid: sbid,
                cjdd: window.localStorage.getItem('cjdd') || '',
                
            })
            this.isSaving = true;
            checkinSubmit(data).then(res=>{
                this.isSaving = false;
                if (res) {
                    this.form = {
                        rylb: '',
                        zjhm: '',
                        xm: '',
                        xb: '',
                        nl: '',
                        csrq: '',
                        hjdz: '', 
                        jzdz: '',
                        lxdh: '',
                        person_id: '',
                    },
                    this.$toast('登记成功')
                    if (this.counter.current == (this.counter.total - 1)) {
                        this.$bus.$emit('finishGather')
                        this.$bus.$emit('labelCodeClear', '')
                        this.labelCode = ''
                        this.$emit('close', 0)
                    } else {
                        //上传当前人员和标签号到服务器
                        this.counter.current++;
                        window.localStorage.setItem('labelCounter', this.counter.current)
                    }
                    
                } else {
                    console.log('error')
                    this.$dialog.alert({title: '错误', message: res.msg || '登记失败'})
                }
            }).catch(e=>{
                this.isSaving = false;
                this.$toast(e)
            })
        },
        onFinish() {
            if (this.labelCode == '') {
                this.$toast('请先选择标签')
                this.$bus.$emit('labelCodeClear', '')
                this.$emit('close', 0)
                return;
            }
            this.$dialog.confirm({
            title: '提示',
            message: '是否结束当前分组',
            })
            .then(() => {
                window.localStorage.setItem('isGathering',0)
                this.form = {
                    rylb: '',
                    zjhm: '',
                    xm: '',
                    xb: '',
                    nl: '',
                    csrq: '',
                    dz: '', 
                    jzdz: '',
                    lxdh: '',
                    hjdz: '',
                    person_id: ''
                }
                this.$dialog.alert({
                    title: '提示',
                    message: '当前标签采集完毕'})
                .then(()=>{
                    this.$bus.$emit('finishGather')
                    this.$bus.$emit('labelCodeClear', '')
                    this.labelCode = ''
                    this.$emit('close', 0)
                })
            })
            .catch(() => {
                // on cancel
            });
            
        },
    }
}
</script>
<style lang="less" scoped>
</style>