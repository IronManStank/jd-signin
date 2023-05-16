# Description
Auto Sign in JD and daily check in.

它提供了三种获取JD_COOKIE的方式:
1. 环境变量:会首先尝试从JD_COOKIE环境变量获取,如果存在则返回。我们非常推荐使用该种方式添加COOKIE。
2. 本地文件:如果环境变量不存在,则尝试从当前目录下的cookies.txt文件获取。
3. 手动输入:如果前两种方式都失败,则提示用户手动输入JD_COOKIE。

## Usage

### 1. Fork this repo
