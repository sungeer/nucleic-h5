<template>
    <div >
        <!-- <van-cell-group> -->
        <van-search
            style="position:fixed;left:0;top:2rem;width:100%;z-index:99"
            v-model="labelCode"
            round
            show-action
            placeholder="请输入标签号"
            @search="onSearch"
            @cancel="onCancel"
        >
        </van-search>
        <!-- </van-cell-group> -->
        <div style="overflow-y:hidden;margin-top:2.2rem;font-size:1rem">
        <van-cell-group v-for="(item, $idx) in list" :key="item.id" >
            <van-row style="padding:0.6rem 0.3rem; border-bottom:0.01rem solid #ebebeb">
                <van-col span="1">{{$idx + 1}} </van-col>
                <van-col span="4" style="border-right: 0.01rem solid #ebebeb">
                    {{item.xm}}
                </van-col>
                <van-col span="8" style="border-right: 0.01rem solid #ebebeb">
                    {{item.lxdh}}
                </van-col>
                <van-col span="11">
                    {{item.sfzh}}
                </van-col>
            </van-row>
        </van-cell-group>
        <div v-if="list.length == 0" style="overflow-y:hidden;margin-top:2.2rem;font-size:1rem">
            未找到记录
        </div>
        </div>
        
    </div>
</template>
<script>
import { checkinList } from '@/api'
export default {
    name: 'Query',
    data() {
        return {
            showPopover: false,
            
            labelCode: window.localStorage.getItem('labelCode'),
            list: []
        }
    },
    mounted() {
        this.$bus.$on('query', ()=>{
            this.labelCode = window.localStorage.getItem('labelCode')
            this.onSearch()
        })
       
    },
    methods: {
        onSearch() {
            checkinList({bqbh: this.labelCode, page:1, size: 10}).then(res=>{
                this.list=res.list
            })
        },
        onCancel() {},
    }
}
</script>