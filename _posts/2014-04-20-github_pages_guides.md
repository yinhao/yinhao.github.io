#Github Pages + jekyll 搭建个人主页

## 环境搭建

### github 账户申请

Mac用户可用github for Mac

### github pages账户申请

申请username.github.io，并且clone到本地

### jekyll 安装tips

安装jekyll:

	gem install jekyll

修改gem源，否则老掉线：

	sudo gem sources --remove http://rubygems.org/ 
	sudo gem sources -a http://ruby.taobao.org/ 

如遇报错，则更新ruby至最新版本，可以用rvm安装：
	
	curl -L https://get.rvm.io | bash -s stable --ruby
	rvm install ruby-2.1.0

### 用jekyll生成站点

	jekyll new myblog
	cd myblog
	jekyll serve
	