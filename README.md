# NpsBypass

> body="https://ehang.io/nps"

## 介绍

[mitmproxy](https://github.com/mitmproxy/mitmproxy) 插件，方便漏洞利用

## 用法

安装 `mitmproxy`

[mitmproxy安装方式](https://docs.mitmproxy.org/stable/addons-options/)

加载插件

> mitmproxy -s npsbypass.py

浏览器设置代理 `http://127.0.0.1:8080/` ，再访问存在漏洞的nps后台即可直接正常操作。

## Thanks

https://github.com/0xf4n9x/NPS-AUTH-BYPASS
