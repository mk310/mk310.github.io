# 配置


{% markmap 300px %}
- hexo
  - markdown语法
  
  - 功能
    - 插入图片
    
    - 思维导图
    
    - 文章加密
    
      {%endmarkmap%}


## markdow 语法

> reference: [Markdown 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/markdown/md-tutorial.html)

## 功能

### typora配合hexo 上传图片

> 参考 https://blog.csdn.net/ayuayue/article/details/109198493

安装插件：

```bash
//markd 渲染
cnpm install hexo-renderer-marked 
```

hexo new postname 时创建相同文件名的文件夹存放img **注意**:postname 应为英文，中文生成静态文件后不能识别

```bash
cnpm install https://github.com/CodeFalling/hexo-asset-image
```

引用的格式为：

```bash
![文字](图片的名字)
```

同时还可以使用typroa将网页链接粘贴时保存到对应的文件夹中 详情见引用

### 思维导图

> reference: [ 如何在Hexo中较为优雅的插入思维导图？_张﻿‌‍﻿‍﻿﻿‌‍麦麦的博客-CSDN博客_hexo 思维导图](https://blog.csdn.net/u011316675/article/details/114482375)

 安装：`npm install hexo-markmap`

使用实例

```bash
{% markmap 300px %}
- Testa
  - test1
  - test2
- Testb
  - test1
  - test2
{%endmarkmap%}
```



### 文章加密 

> pefrence:[ Hexo（sakura）设置文章置顶+私密文章_cungudafa的博客-CSDN博客_hexo隐藏文章](https://blog.csdn.net/cungudafa/article/details/104346521)

**bug**：使用文章加密后思维导图功能不可用

----------------------------------------
