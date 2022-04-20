# git

> preference: https://zhuanlan.zhihu.com/p/94008510 [哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1XP4y147v1?from=search&seid=3299839228711840777&spm_id_from=333.337.0.0)
>
> `git log -5 --pretty=oneline` 显示5行简单查看日志

## 版本控制

git是分布式的版本控制系统

图：

{{< mermaid >}}
flowchart LR
subgraph computer1
    subgraph data1[version_database]
        v1[version1]-->v2[version2]
        v2--> v3[version3]
    end
end
subgraph computer2
    subgraph data2[version_database]
        v21[version1]-->v22[version2]
        v22--> v23[version3]
    end
end
subgraph computer3
    subgraph data3[version_database]
        v31[version1]-->v32[version2]
        v32--> v33[version3]
    end
end
computer1 --- computer2 --- computer3
{{< /mermaid >}}
所有clone远程库的本地库都拥有完整的version——databse

## 安装设置

设置用户名

```bash
git config --global user.name "your username"
```

设置用户邮箱

```bash
git config --global user.email "you useremail"
```

查看所有的配置

```bash
git config --list
```

## 三种状态
|状态|描述|
|---|---|
|已提交（committed）|已提交表明数据已经安全的保存在本地的数据库中|
|已修改（modified）|已修改表示修改了文件，但是还没有保存到数据库中|
|已暂存（staged）|表示对一个已修改的文件的当前版本做了标记，使之包含在下次提交的快照中(下次提交，将标记的文件从暂存区提交到本地库中)|


<center>三种状态的关系图</center>

[comment]: 三种状态的关系图
{{< mermaid >}}
sequenceDiagram
    participant w as working diectroy(工作区)
    participant s as staging area（暂存区）
    participant g as git diectory（本地仓库）
    g->>w: check the project
    w->>s: stage files(git add)
    s->>g: commit(git commit)
{{< /mermaid >}}

---------------------------------------------

<center>git工作流程图</center>

[comment]: git工作流程图
{{< mermaid >}}
graph LR;
    A[远程仓库] -->|fetch/clone| B[本地仓库]
    B --> |push|A
    B --> |checkout| D[工作区]
    D --> |add| C[缓存区]
    C --> |commit| B
    A -->|pull| D
{{< /mermaid >}}

## 创建版本库并提交文件例子

版本库及仓库，简单理解为一个目录，windows文件中的.git文件夹

1. 初始化本地仓库
   创建文件夹，进去后`git init` 创建一个空仓库
2. 在文件夹中放入一个a.txt文件，使用`git add`命令添加到暂存区，`git add <path>` path 可以是文件也可以是目录,例子：`git add a.txt`

   ```bash
        git status

        On branch master

        No commits yet

        Changes to be committed:
        (use "git rm --cached <file>..." to unstage)
                new file:   a.txt

        Untracked files:
        (use "git add <file>..." to include in what will be committed)
                b.txt

   ```

3. 提交到本地仓库 `git commit -m '本次提交的说明'`

    ```bash
    git log
    Author: mk310 <1594401797@qq.com>
    Date:   Sat Apr 16 18:26:05 2022 +0800
    
        git 测试提交了a.txt
    
    ```

## 版本回溯

修改工作区的a.txt，使用`git diff HEAD -- a.text`查看工作区的文件和版本库中的文件的区别

```bash
$  git diff HEAD -- a.txt
diff --git a/a.txt b/a.txt
index 75b9dc5..af32cb2 100644
--- a/a.txt
+++ b/a.txt
@@ -1,3 +1,3 @@
 this is a git test file

-git version plus test
\ No newline at end of file
+git version plus test - version
\ No newline at end of file
```

如果将b.txt 文件误提交到暂存区，使用`git reset HEAD` 撤回提交的文件



### 返回上一次的提交



```bash
git reset --hard HEAD^
```

```bash
Author: mk310 <1594401797@qq.com>
Date:   Mon Apr 18 15:35:05 2022 +0800

    添加全部

commit 4d13d943de4aa3bb183c01b9432cb693e3275fee
Author: mk310 <1594401797@qq.com>
Date:   Sat Apr 16 18:35:25 2022 +0800

    提交了a.txt的修改

commit b27872183beaa169349415830fe7261b9ba5f6d5
Author: mk310 <1594401797@qq.com>
Date:   Sat Apr 16 18:26:05 2022 +0800

    git 测试提交了a.txt

```

使用命令后

```bash
Author: mk310 <1594401797@qq.com>
Date:   Sat Apr 16 18:35:25 2022 +0800

    提交了a.txt的修改

commit b27872183beaa169349415830fe7261b9ba5f6d5
Author: mk310 <1594401797@qq.com>
Date:   Sat Apr 16 18:26:05 2022 +0800

    git 测试提交了a.txt

```

### 特定版本的回退

`git reset --hard HEAD^` 这个`^`最多三个，表示退回三个版本

更多的回退则使用

```bash
git reset --hard HEAD~34
```

回到特定的版本

```bash
git reset --hard <版本标识符>
```



## 文件删除

在git中只关注文件的修改，文件的删除也是修改

如果在工作区误删除文件(前提是文件在删除前已经提交到本地仓库)

```bash
git checkout -- <filename>
```

删除文件/目录

```bash
git rm <filename>
```

> `git ls-files`查看本地库的文件



## 远程仓库

**https** 是简单的方式

**ssh** 加密的方式，而且更加的高效

```bash
#新建工作目录并进入
git init 
#若已经有本地仓库直接进行下列操作
git remote add <要上传的仓库地址>
git add .
git commit -m ""
git push -u origin master
```



## git分支操作

### 本地分支

常见分支操作命令

| 命令                                   | 描述                                                         | 注意                                                         |
| -------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| git checkout branch                    | 切换到指定的分支                                             | 切换分支的时候，工作区的文件会随分支变化                     |
| git checkout -b new_branch             | 新建分支并切换到新建分支                                     |                                                              |
| git branch -d branch                   | 删除指定的分支                                               |                                                              |
| git branch                             | 查看所有的分支，并且标记当前所在的分支`*`                    |                                                              |
| git merge branch                       | 合并分支                                                     | 合并分支时要切换到**master**,操作后将分支的修改覆盖到master中；只能在master中合并分支 |
| git branch -m \|-M oldbranch newbranch | 重命名分支，若newbranch已经存在，则使用-M强制重命名，否则使用-m重命名 |                                                              |

### 分支push pull操作

| 命令                                             | 描述                               |
| ------------------------------------------------ | ---------------------------------- |
| git branch -a                                    | 查看本地与远程分支                 |
| git push origin branch_name                      | 推送本地分支到远程                 |
| git push origin :remote_branch                   | 删除远程分支（本地分支还在保存）   |
| git checkout -b local_brach origin/remote_branch | 提取远程指定的分支并在本地创建分支 |

> `git fetch`查看远程仓库的最新状态

### 分支操作冲突和解决办法

#### 本地分支冲突

master 和分支同时进行不同的操作

未进行操作前master 和 leaf01

```bash
52e331fcc94db2b49c5efa47e101ab584ffd3fb3 b
fc5e024e572348dec05c7f4f57cd4e67eea30d30 (origin/master, origin/leaf02) 删除readme
ccb26cdce7fc848baa33b857c874cb873472373a 提交readme
```

进行操作  

master

```bash
2b0e87f699833770cac0f49543be8436310fbc15 (HEAD -> master) master 添加 master.txt
fc5e024e572348dec05c7f4f57cd4e67eea30d30 (origin/master, origin/leaf02) 删除readme
52e331fcc94db2b49c5efa47e101ab584ffd3fb3 b
ccb26cdce7fc848baa33b857c874cb873472373a 提交readme
```

leaf01

```bash
57998bcf8cfa6a81b424c505b8d2686dff7f585e (HEAD -> leaf01) leaf01 添加 leaf01.txt
fc5e024e572348dec05c7f4f57cd4e67eea30d30 (origin/master, origin/leaf02) 删除readme
52e331fcc94db2b49c5efa47e101ab584ffd3fb3 b
ccb26cdce7fc848baa33b857c874cb873472373a 提交readme
```

切换到master，使用`git merge leaf01`填写commit解释

```bash
$ git log --graph --pretty=oneline
*   1d9c9a7319ef31eaff0b92d10afea718105a84a8 (HEAD -> master, origin/master) ---
|\
| * 57998bcf8cfa6a81b424c505b8d2686dff7f585e (leaf01) leaf01 添加 leaf01.txt
* | 2b0e87f699833770cac0f49543be8436310fbc15 master 添加 master.txt
|/
* fc5e024e572348dec05c7f4f57cd4e67eea30d30 (origin/leaf02) 删除readme
* 52e331fcc94db2b49c5efa47e101ab584ffd3fb3 b
* ccb26cdce7fc848baa33b857c874cb873472373a 提交readme
```

# git 使用

## git远程仓库切换到gitee

删除本地远程仓库

```bash
git remote rm origin
```

添加gitee远程仓库

```bash
git remote add 仓库名
```

设置用户名，用户邮箱

```bash
git config --global user.name ""
git config --global user.email " "
```



## git删除远程仓库的所有文件

> prefence:[git删除所有文件夹（清空远程仓库）](https://blog.csdn.net/qq_43498002/article/details/120357263)

首先确定与远程仓库连接，然后命令：

```bash
git rm * -f -r #删除所有的文件
git add . #提交修改到暂存区
git commit -m"" #提交修改到本地仓库
git push
```


