# 

# hugo

# #下载并安装hugo

[Releases · gohugoio/hugo (github.com)](https://github.com/gohugoio/hugo/releases)

下载amd64





git 删除仓库文件

> [如何删除GitHub仓库里的文件夹（配图详解）_行稳方能走远的博客-CSDN博客_github删除文件](https://blog.csdn.net/zhuguanlin121/article/details/118415768)

1复制仓库地址

https://github.com/mk310/mk310.github.io.git

2本地新建文件夹

3在文件中右键git bash

4 clone仓库

git clone  https://github.com/mk310/mk310.github.io.git

5 拉取远程仓库

cd mk310.github.io

6查看仓库文件

dir

7 git rm -r --cached 文件名

git commit -m ‘’ 删除的说明‘’

8更新远程库

git push -u origin master

问题：

```bash
$ git push -u origin master
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/mk310/mk310.github.io.git/'
```

解决：获取令牌

> [remote: Support for password authentication was removed on August 13, 2021_IT博客技术分享的博客-CSDN博客](https://blog.csdn.net/qq_41646249/article/details/119777084)

