import request from '@/utils/request'

import qs from 'qs'
export function login(data) {
    return request({
      url: '/auth/login',
      method: 'post',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      data: qs.stringify(data)
    })
}

export function userInfo() {
    return request({
        url: '/auth/userinfo',
        method: 'get',
    })
}
export function personSubmit(data) {
    return request({
        url: '/person/submit',
        method: 'post',
        data
    })
}
export function personGet(params) {
    return request({
        url: '/person/get',
        method: 'get',
        params
    })
}

export function checkinSubmit(data) {
    return request({
        url: '/checkin/submit',
        method: 'post',
        data
    })
}

export function checkinList(params) {
    return request({
        url: '/checkin/list',
        method: 'get',
        params
    })
}

