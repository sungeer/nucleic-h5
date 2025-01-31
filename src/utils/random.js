// 生成指定长度的随机字符串
export function randomString(length) {
    var str = '0123456789';
    var result = '';
    for (var i = length; i > 0; --i) 
        result += str[Math.floor(Math.random() * str.length)];
    return result;
}

// 生成随机的身份证号，长度18位，其中7-14位是年月日
export function randomIdCard() {
    return randomString(6) + '20020601' + randomString(4)
}
