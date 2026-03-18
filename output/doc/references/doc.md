# Doc - Doc

**Pages:** 55

---

## API 模块 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/167.html

**Contents:**
- API 模块
- 流程介绍
- 基类解析
- 功能模块
  - 会员模块
  - 短信模块
  - 公共模块
  - 检测模块

这里的API指整个API接口模块，这里仅做部分API功能模块的使用介绍，如果需要查看前端开发和后端开发文档，请查看相对应的文档。

FastAdmin的API模块完全遵循ThinkPHP5的开发规范，在此基础上我们在API模块中提供了一个和前台相同的权限验证模块，我们可以方便快捷的控制我们的可访问权限。

FastAdmin的API模块采用默认的路由方式进行匹配，当然我们完全可以自定义我们的路由规则，达到个性化URL接口的目的。

API的所有功能模块的控制器都是继承于application/common/controller/Api.php这个基类控制器。

在基类控制器中我们有定义一些基础属性和通用方法，首先我们看看基础属性。

以上的属性和方法我们都可以通过在当前控制器定义来达到覆盖的目的。

我们在FastAdmin的API中集成了简单的会员接口，可以进行会员的注册、登录、找回密码、会员中心、修改个人资料、修改密码等操作。

会员模块可用于进行API会员功能开发时使用。此处的会员模块和前台中的会员模块账号是相通的，但他们登录时是不会互相影响的，可以同时登录。

FastAdmin的会员模块有注册几个事件，我们可以在事件中自定义我们的操作。你可以按照以下的方式监听相应的事件行为。

我们在FastAdmin的API中集成了简单的短信模块，可以根据相对应的事件进行短信的发送和检测是否正确等功能。

在使用短信模块时请确保已经正确在后台正确安装并启用了第三方短信插件。

公共模块一般用于客户端应用初始化时调用，例如APP的版本检测、APP的首屏轮换图等功能。

检测模块一般用于检测客户端提交数据的有效性验证，也常用于在前台进行数据录入时的实时有效性校验。

**Examples:**

Example 1 (php):
```php
/**
 * @var array 前置操作方法列表
 */
protected $beforeActionList = [];

/**
 * 无需登录的方法,同时也就不需要鉴权了
 * @var array
 */
protected $noNeedLogin = [];

/**
 * 无需鉴权的方法,但需要登录
 * @var array
 */
protected $noNeedRight = [];

/**
 * 权限Auth
 * @var Auth 
 */
protected $auth = null;
```

Example 2 (php):
```php
/**
 * 加载语言文件
 * @param string $name
 */
protected function loadlang($name)
{
}

/**
 * 操作成功返回的数据
 * @param string $msg   提示信息
 * @param mixed $data   要返回的数据
 * @param int   $code   错误码，默认为1
 * @param string $type  输出类型
 * @param array $header 发送的 Header 信息
 */
protected function success($msg = '', $data = null, $code = 1, $type = null, array $header = [])
{
}

/**
 * 操作失败返回的数据
 * @param string $msg   提示信息
 * @param mixed $data   要返回的数据
 * @param int   $code   错误码，默认为0
 * @param string $type  输出类型
 * @param array $header 发送的 Header 信息
 */
protected function error($msg = '', $data = null, $code = 0, $type = null, array $header = [])
{
}

/**
 * 返回封装后的 API 数据到客户端
 * @access protected
 * @param mixed  $msg    提示信息
 * @param mixed  $data   要返回的数据
 * @param int    $code   错误码，默认为0
 * @param string $type   输出类型，支持json/xml/jsonp
 * @param array  $header 发送的 Header 信息
 * @return void
 * @throws HttpResponseException
 */
protected function result($msg, $data = null, $code = 0, $type = null, array $header = [])
{
}

/**
 * 前置操作
 * @access protected
 * @param  string $method  前置操作方法名
 * @param  array  $options 调用参数 ['only'=>[...]] 或者 ['except'=>[...]]
 * @return void
 */
protected function beforeAction($method, $options = [])
{
}

/**
 * 验证数据
 * @access protected
 * @param  array        $data     数据
 * @param  string|array $validate 验证器名或者验证规则数组
 * @param  array        $message  提示信息
 * @param  bool         $batch    是否批量验证
 * @param  mixed        $callback 回调方法（闭包）
 * @return array|string|true
 * @throws ValidateException
 */
protected function validate($data, $validate, $message = [], $batch = false, $callback = null)
{
}
```

Example 3 (php):
```php
//登录成功后的事件
Hook::add('user_login_successed', function ($user) {
});
//注册成功后的事件
Hook::add('user_register_successed', function ($user) {
});
//会员删除后的事件
Hook::add('user_delete_successed', function ($user) {
});
//会员注销后的事件
Hook::add('user_logout_successed', function ($user) {
});
```

---

## Table对象 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/197.html

**Contents:**
- Table对象
  - Table.list
  - Table.defaults
  - Table.columnDefaults
  - Table.config
  - Table.button
  - Table.api
  - Table.api.formatter

我们引入表格依赖table后，就可以通过Table来进行相关表格的初始化和绑定相关事件。返回的Table对象包括以下几个对象：

其中Table.list存储的是表格实例化后的对象。比如我们实例化的表格有个id="mytable"的属性，则我们可以通过

来获取此表格的Bootstrap-table的对象。

Table.defaults是指Bootstrap-table表格参数默认值。修改单一的值，我们可以直接通过

Table.columnDefaults是指Bootstrap-table表格列参数默认值修改单一的值，我们可以直接通过

Table.config是指表格使用到的按钮和工具栏的DOM选择类，一般情况下不建议修改。

Table.button是指表格默认编辑、删除、挺拽按钮的配置信息，一般情况下不建议修改。

Table.api封装了表格常用的方法、单元格事件及渲染方法。在表格中会经常使用到。

Table.api.formatter封装了许多FastAdmin表格列表中常用的单元格数据渲染的方法，具体请参考格式化文章章节。

**Examples:**

Example 1 (json):
```json
{
    list:[], //实例化的表格对象列表
    defaults:{}, //默认表格参数
    columnDefaults:{}, //默认列参数
    config:{}, //相关按钮的DOM选择类
    button:{}, //默认编辑、删除、排序按钮配置
    api:{} //封装的API方法
}
```

Example 2 (unknown):
```unknown
Table.list['mytable']
```

Example 3 (unknown):
```unknown
Table.defaults.showExport = false;
```

Example 4 (unknown):
```unknown
Table.columnDefaults.align = 'left';
```

---

## 一键压缩打包 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/162.html

**Contents:**
- 一键压缩打包
  - 准备工作
  - 常用命令
  - 常见问题
  - 影响文件
  - 使用范例

在FastAdmin中如果修改了核心的JS或CSS文件，是需要重新压缩打包后在生产环境下才会生效。FastAdmin采用的是基于RequireJS的r.js进行JS和CSS文件的压缩打包。

首先确认你application/config.php中app_debug的值，当为true的时候是采用的无压缩的JS和CSS，当为false时采用的是压缩版的JS和CSS。

请确保php所在的目录已经加入到系统环境变量，否则会提示找不到该命令。

打开命令行控制台进入到你的站点根目录，也就是think文件所在的目录。

Windows系统需要手动配置node的路径,请参考在Windows下如何压缩打包JS和CSS。

如果无法进行打包，可以使用php think min -m all -r all -vvv尝试下，看下错误信息。

如果压缩打包后访问不生效，请检查是否是你的浏览器缓存的原因，请尝试清除浏览器缓存。

请不要直接修改以.min.js和.min.css结尾的文件，因为一键压缩打包后会进行覆盖。

安装或卸载插件后无需进行压缩打包JS和CSS

在调试模式和生产环境下所加载的JS和CSS是不一样的，压缩打包会重新生成生产环境下的JS和CSS文件，特别注意下。调试模式：

生产环境：(打包压缩后会重新生成以下文件)

JS和CSS文件压缩前和压缩后浏览器请求对比(请右键查看大图)：

更多一键生成JS和CSS的参数请使用php think min --help查看。

**Examples:**

Example 1 (php):
```php
//一键压缩打包前后台的JS和CSS
php think min -m all -r all
//一键压缩打包后台的JS和CSS
php think min -m backend -r all
//一键压缩打包前后台的JS
php think min -m all -r js
//一键压缩打包后台的CSS
php think min -m backend -r css
//使用uglify进行一键压缩打包后台的JS文件
php think min -m backend -r js -o uglify
```

Example 2 (unknown):
```unknown
public/assets/js/require-frontend.js
public/assets/js/require-backend.js
public/assets/css/frontend.css
public/assets/css/backend.css
```

Example 3 (unknown):
```unknown
public/assets/js/require-frontend.min.js
public/assets/js/require-backend.min.js
public/assets/css/frontend.min.css
public/assets/css/backend.min.css
```

---

## 一键生成API文档 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/163.html

**Contents:**
- 一键生成API文档
  - 准备工作
  - 常用命令
  - 参数介绍
  - 注释规则
  - 标准范例
  - 文档模板
  - 常见问题

FastAdmin中的一键生成API文档可以在命令行或后台一键生成我们API接口的接口测试文档，可以直接在线模拟接口请求，查看参数示例和返回示例。

请确保你的API模块下的控制器代码没有语法错误，控制器类注释、方法名注释完整，注释规则请参考下方注释规则。

请确保你的FastAdmin已经安装成功且能正常登录后台。

请确保php所在的目录已经加入到系统环境变量，否则会提示找不到该命令。

打开命令行控制台进入到你的站点根目录，也就是think文件所在的目录。

在我们的控制器中通常分为两部分注释，一是控制器头部的注释，二是控制器方法的注释。

如果需要修改生成API文档的模板，可以自行对模板文件：application/admin/command/Api/template/index.html 进行二次开发。

如果控制器的方法是private或protected的，则将不会生成相应的API文档。

**Examples:**

Example 1 (php):
```php
//一键生成API文档
php think api --force=true
//指定https://www.example.com为API接口请求域名,默认为空
php think api -u https://www.example.com --force=true
//输出自定义文件为myapi.html,默认为api.html
php think api -o myapi.html --force=true
//修改API模板为mytemplate.html，默认为index.html
php think api -e mytemplate.html --force=true
//生成指定控制器Demo的API文档
php think api -r Demo --force=true
//修改标题为Demo,作者为Lily
php think api -t Demo -a Lily --force=true
//生成插件标识为cms的API文档
php think api -a cms -o cmsapi.html --force=true
//查看API接口命令行帮助
php think api -h
```

Example 2 (sass):
```sass
-u, --url[=URL]            默认API请求URL地址 [default: ""]
-m, --module[=MODULE]      模块名(admin/index/api) [default: "api"]
-a, --addon[=ADDON]      插件标识(addons目录下的插件标识) [default: ""]
-o, --output[=OUTPUT]      输出文件 [default: "api.html"]
-e, --template[=TEMPLATE]  模板文件 [default: "index.html"]
-f, --force[=FORCE]        覆盖模式 [default: false]
-t, --title[=TITLE]        文档标题 [default: "FastAdmin"]
-c, --class[=CLASS]        扩展类 (支持多个值)
-l, --language[=LANGUAGE]  语言 [default: "zh-cn"]
-r,  --controller=CONTROLLER  控制器，默认为controller目录下的所有控制器(支持多个值),FastAdmin 1.3.0+支持
```

Example 3 (php):
```php
<?php

namespace app\api\controller;

/**
 * 测试API控制器
 */
class Test extends \app\common\controller\Api
{

    // 无需验证登录的方法
    protected $noNeedLogin = ['test'];
    // 无需要判断权限规则的方法
    protected $noNeedRight = ['*'];

    /**
     * 首页
     *
     * 可以通过@ApiInternal忽略请求的方法
     * @ApiInternal
     */
    public function index()
    {
        return 'index';
    }

    /**
     * 私有方法
     * 私有的方法将不会出现在文档列表
     */
    private function privatetest()
    {
        return 'private';
    }

    /**
     * 测试方法
     *
     * @ApiTitle    (测试名称)
     * @ApiSummary  (测试描述信息)
     * @ApiSector   (测试分组)
     * @ApiMethod   (POST)
     * @ApiRoute    (/api/test/test/id/{id}/name/{name})
     * @ApiHeaders  (name=token, type=string, required=true, description="请求的Token")
     * @ApiParams   (name="id", type="integer", required=true, description="会员ID")
     * @ApiParams   (name="name", type="string", required=true, description="用户名")
     * @ApiParams   (name="data", type="object", sample="{'user_id':'int','user_name':'string','profile':{'email':'string','age':'integer'}}", description="扩展数据")
     * @ApiReturnParams   (name="code", type="integer", required=true, sample="0")
     * @ApiReturnParams   (name="msg", type="string", required=true, sample="返回成功")
     * @ApiReturnParams   (name="data", type="object", sample="{'user_id':'int','user_name':'string','profile':{'email':'string','age':'integer'}}", description="扩展数据返回")
     * @ApiReturn   ({
        'code':'1',
        'mesg':'返回成功'
     * })
     */
    public function test($id = '', $name = '')
    {
        $this->success("返回成功", $this->request->request());
    }

}
```

---

## 一键生成CRUD - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/crud.html

**Contents:**
- 一键生成CRUD
  - 准备工作
  - 常用命令
  - 参数介绍
  - 常见问题

在FastAdmin中可以快速的一键生成CRUD，自动生成后台的控制器、模型、视图、JS、语言包、菜单、回收站等。

在数据库中默认有一个fa_test数据表可供参考，也可新建一个数据表，编辑好表字段结构，并且一定写上字段注释和表注释，相关数据表字段的设计要求可以参考数据库章节。FastAdmin在生成CRUD时会根据字段属性、字段注释、表注释自动生成语言包、组件和排版。

请确保你设计的表有且只有一个主键，不支持复合主键。请确保php所在的目录已经加入到系统环境变量，否则会提示找不到该命令。

下面以 fa_test 数据表为例，打开命令行控制台进入到你的站点根目录，也就是think文件所在的目录，进行执行命令。

更多CRUD一键生成可使用的参数请使用php think crud --help查看。

**Examples:**

Example 1 (php):
```php
//生成fa_test表的CRUD
php think crud -t test
//生成fa_test表的CRUD且一键生成菜单
php think crud -t test -u 1
//删除fa_test表生成的CRUD
php think crud -t test -d 1
//生成fa_test表的CRUD且控制器生成在二级目录下
php think crud -t test -c mydir/test
//删除fa_test表生成的二级目录的CRUD
php think crud -t test -c mydir/test -d 1
//生成fa_test_log表的CRUD且生成对应的控制器为testlog
php think crud -t test_log -c testlog
//生成fa_test表的CRUD且对应的模型名为testmodel
php think crud -t test -m testmodel
//生成fa_test表的CRUD且生成关联模型category，外链为category_id，关联表主键为id
php think crud -t test -r category -k category_id -p id
//生成fa_test表的CRUD且所有以list或data结尾的字段都生成复选框
php think crud -t test --setcheckboxsuffix=list --setcheckboxsuffix=data
//生成fa_test表的CRUD且所有以image和img结尾的字段都生成图片上传组件
php think crud -t test --imagefield=image --imagefield=img
//关联多个表,参数传递时请按顺序依次传递，支持以下几个参数relation/relationmodel/relationforeignkey/relationprimarykey/relationfields/relationmode
php think crud -t test --relation=category --relation=admin --relationforeignkey=category_id --relationforeignkey=admin_id
//生成v_phealth_db2数据库下的fa_test表的CRUD
php think crud -t test --db=v_phealth_db2
```

Example 2 (sass):
```sass
-t, --table=TABLE                              表名，带不带表前缀均可
-c, --controller[=CONTROLLER]                  生成的控制器名,可选,默认根据表名进行自动解析
-m, --model[=MODEL]                            生成的模型名,可选,默认根据表名进行自动解析
-i, --fields[=FIELDS]                          生成的数据列表中可见的字段，默认是全部
-f, --force[=FORCE]                            是否覆盖模式,如果目标位置已经有对应的控制器或模型会提示
-l, --local[=LOCAL]                            是否本地模型,默认1,置为0时,模型将生成在common模块下
-r, --relation[=RELATION]                      关联模型表名，带不带表前缀均可
-e, --relationmodel[=RELATIONMODEL]            生成的关联模型名,可选,默认根据表名进行自动解析
-k, --relationforeignkey[=RELATIONFOREIGNKEY]  表外键,可选,默认会识别为使用 模型_id 名称
-p, --relationprimarykey[=RELATIONPRIMARYKEY]  关联模型表主键,可选,默认会自动识别
-s, --relationfields[=RELATIONFIELDS]          关联模型表显示的字段，默认是全部
-o, --relationmode[=RELATIONMODE]              关联模型,hasone/belongsto/hasmany [default: "belongsto"]（v1.3+ 增加了 hasmany）
-d, --delete[=DELETE]                          删除模式,将删除之前使用CRUD命令生成的相关文件
-u, --menu[=MENU]                              菜单模式,生成CRUD后将继续一键生成菜单
--db[=key]                                     多数据库支持(参数为tp5中配置的数据库key 在application\config.php添加数据库配置信息)
--setcheckboxsuffix[=SETCHECKBOXSUFFIX]    自动生成复选框的字段后缀
--enumradiosuffix[=ENUMRADIOSUFFIX]        自动生成单选框的字段后缀
--imagefield[=IMAGEFIELD]                  自动生成图片上传组件的字段后缀
--filefield[=FILEFIELD]                    自动生成文件上传组件的字段后缀
--intdatesuffix[=INTDATESUFFIX]            自动生成日期组件的字段后缀
--switchsuffix[=SWITCHSUFFIX]              自动生成可选组件的字段后缀
--citysuffix[=CITYSUFFIX]                  自动生成城市选择组件的字段后缀
--selectpagesuffix[=SELECTPAGESUFFIX]      自动生成Selectpage组件的字段后缀
--ignorefields[=IGNOREFIELDS]                 排除的字段
--editorclass[=EDITORCLASS]                自动生成富文本组件的字段后缀
--headingfilterfield[=HEADINGFILTERFIELD]  自动生成筛选过滤选项卡的字段，默认是status字段
--sortfield[=SORTFIELD]                    排序字段
```

---

## 一键生成菜单 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/161.html

**Contents:**
- 一键生成菜单
  - 准备工作
  - 常用命令
  - 常见问题
  - 使用范例

FastAdmin可通过命令控制台快速的一键生成后台的权限节点菜单规则，同时后台的管理菜单也会同步改变，操作非常简单。

首先确保已经将FastAdmin配置好，数据库连接正确，同时确保已经通过上一步的一键生成CRUD已经生成了test的CRUD。

请确保php所在的目录已经加入到系统环境变量，否则会提示找不到该命令。

打开命令行控制台进入到你的站点根目录，也就是think文件所在的目录。

更多CRUD一键生成可使用的参数请使用php think menu --help查看。

**Examples:**

Example 1 (php):
```php
//一键生成test控制器的权限菜单
php think menu -c test
//一键生成mydir/test控制器的权限菜单
php think menu -c mydir/test
//删除test控制器生成的菜单
php think menu -c test -d 1
//一键生成所有控制器的权限菜单，执行前请备份数据库。
php think menu -c all-controller
```

---

## 一键管理插件 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/164.html

**Contents:**
- 一键管理插件
  - 准备工作
  - 常用命令
  - 常见问题

FastAdmin中的插件可以通过命令行快速的进行安装、卸载、禁用和启用。

请确保你的FastAdmin已经能正常登录后台。

请确保php所在的目录已经加入到系统环境变量，否则会提示找不到该命令。

打开命令行控制台进入到你的站点根目录，也就是think文件所在的目录。

更多一键管理插件的参数请使用php think addon --help查看。

**Examples:**

Example 1 (php):
```php
//创建一个myaddon本地插件，常用于开发自己的插件时使用
php think addon -a myaddon -c create
//刷新插件缓存，如果禁用启用了插件，部分文件需要刷新才会生效
php think addon -a example -c refresh
//卸载本地的example插件
php think addon -a example -c uninstall
//启用本地的example插件
php think addon -a example -c enable
//禁用本地的example插件
php think addon -a example -c disable
//将本地的example插件打包成zip文件
php think addon -a example -c package
//将application和public目录下指定模块的CRUD相关文件复制到对应插件目录下
php think addon -a example -c move
```

---

## 介绍 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc

**Contents:**
- 介绍
- 介绍
- 主要特性
- 安装使用
- 在线演示
- 界面截图
- 问题反馈
- 特别鸣谢
- 版权信息

FastAdmin 是一款基于 PHP + Bootstrap 的开源、高效、极速后台管理框架。

我们的目标是努力为开发者节省时间，让你拥有更多时间投入到创造性工作和个人生活中。

https://doc.fastadmin.net

https://demo.fastadmin.net

提 示：演示站数据无法进行修改，请下载源码安装体验全部功能

在使用中有任何问题，请使用以下联系方式联系我们

问答社区: https://ask.fastadmin.net

Github: https://github.com/fastadminnet/fastadmin

Gitee: https://gitee.com/fastadminnet/fastadmin

ThinkPHP：http://www.thinkphp.cn

AdminLTE：https://adminlte.io

Bootstrap：http://getbootstrap.com

jQuery：http://jquery.com

Bootstrap-table：https://github.com/wenzhixin/bootstrap-table

Nice-validator: https://validator.niceue.com

Art-template: https://github.com/aui/art-template/tree/3.1.0

SelectPage: https://github.com/TerryZ/SelectPage

Autocomplete: https://github.com/devbridge/jQuery-Autocomplete

Tagsinput: https://github.com/bootstrap-tagsinput/bootstrap-tagsinput

FastAdmin遵循Apache2开源协议发布，并提供免费使用。

本项目包含的第三方源码和二进制文件之版权信息另行标注。

版权所有Copyright © 2017-2026 by FastAdmin ( https://www.fastadmin.net )

---

## 介绍 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/index.html

**Contents:**
- 介绍
- 介绍
- 主要特性
- 安装使用
- 在线演示
- 界面截图
- 问题反馈
- 特别鸣谢
- 版权信息

FastAdmin 是一款基于 PHP + Bootstrap 的开源、高效、极速后台管理框架。

我们的目标是努力为开发者节省时间，让你拥有更多时间投入到创造性工作和个人生活中。

https://doc.fastadmin.net

https://demo.fastadmin.net

提 示：演示站数据无法进行修改，请下载源码安装体验全部功能

在使用中有任何问题，请使用以下联系方式联系我们

问答社区: https://ask.fastadmin.net

Github: https://github.com/fastadminnet/fastadmin

Gitee: https://gitee.com/fastadminnet/fastadmin

ThinkPHP：http://www.thinkphp.cn

AdminLTE：https://adminlte.io

Bootstrap：http://getbootstrap.com

jQuery：http://jquery.com

Bootstrap-table：https://github.com/wenzhixin/bootstrap-table

Nice-validator: https://validator.niceue.com

Art-template: https://github.com/aui/art-template/tree/3.1.0

SelectPage: https://github.com/TerryZ/SelectPage

Autocomplete: https://github.com/devbridge/jQuery-Autocomplete

Tagsinput: https://github.com/bootstrap-tagsinput/bootstrap-tagsinput

FastAdmin遵循Apache2开源协议发布，并提供免费使用。

本项目包含的第三方源码和二进制文件之版权信息另行标注。

版权所有Copyright © 2017-2026 by FastAdmin ( https://www.fastadmin.net )

---

## 代码安全 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/170.html

**Contents:**
- 代码安全
  - SQL注入
  - XSS跨站注入
  - CSRF跨站请求

开发安全是我们在开发过程中很容易忽略的一个环节，由于程序的不严谨很容易数据泄漏、数据丢失、服务器被提权，因此我们在开发过程中就要尽量做到开发规范严谨，接下来主要讲解下在开发过程中要注意避免产生BUG的几种情形

这种问题常常出现在读写操作数据库时产生，很多时候我们需要查询数据库的数据做逻辑操作，由于未对请求的参数做过滤或处理，很容易产生数据丢失和数据泄漏的问题。

例如，我们需要根据用户名查询指定用户的信息，我们常用的SQL语句如下：

一般情况下我们username参数传普通参数都不会有问题，但是如果遇到别有用心之人传一些特殊参数，例如传递username的参数为

此时我们接收到的username为' OR '1'='1，生成的SQL语句为

此时将导致筛选所有数据或筛选我们任意想要的数据。

那如何避免这种情况发生呢？我们有以下几种解决方法

在ThinkPHP5中提供了许多数据输入过滤方法，例如

FastAdmin从1.2.0版本开始已经内置了xss_clean函数用于清除过滤请求中可能的危险字段，可以搭配其它过滤方式一同使用，如

XSS跨站点脚本注入常常出现在浏览器客户端输出时由于未对输出的数据进行过滤和转换，导致浏览器响应执行了Javascript代码，这个代码代具有管理员权限的用户做一些隐藏的操作，比如提权、恶意修改删除数据，甚至将用户当前浏览器端的Cookie等数据传到攻击者的服务器，攻击者通过伪造Cookie请求，很容易造成用户信息漏洞和数据丢失的情况。这种问题常出现在会员昵称、会员头像输出、会员评论数据等情况下。

解决防范XSS跨站注入的首先是按照上方的SQL注入做好请求数据过滤，其次是做好数据输出时的编码，我们在视图模板中编写代码时，可以通过添加htmlentities对HTML代码做实体编码，例如

千万不要直接使用以下的代码，以下代码都是非常不安全的

CSRF全称为cross site request forgery，中文意思为：跨站点伪装请求。

跨站点请求的原理就是用户A在站点1发布上传粘贴了一个站点2的URL，用户B不明就里的点击了站点2的URL，而这个URL因为是伪装请求站点1修改密码(其它危险请求)的操作。此时用户A就已经获取了用户B的账户信息。

例如我们常常在编写表单提交的时候都是如下的写法

以上的写法很容易产生CSRF跨站点伪装请求。

在ThinkPHP5可以很方便的使用token的方式来防范这种威胁，比如我们将上面的代码改写为

我们添加了一个{:token()}，由于这个token是我们服务端动态输出的，伪装者的服务器没法获取该值，此时我们再做好服务端验证这个token是否有效即可，常用的方法如下

更多Token表单令牌的使用方法可以参考ThinkPHP5官方文档：https://www.kancloud.cn/manual/thinkphp5/193918

**Examples:**

Example 1 (php):
```php
// 错误写法
$username = $this->request->request("username");
\think\Db::query("SELECT * FROM fa_user WHERE username='{$username}'");
```

Example 2 (yaml):
```yaml
http://www.yoursite.com/test/index?username=' OR '1'='1
```

Example 3 (sql):
```sql
SELECT * FROM fa_user WHERE username='' OR '1'='1'
```

Example 4 (sql):
```sql
// 推荐写法
$username = $this->request->request("username", "");
$username = htmlspecialchars($username, ENT_QUOTES);
\think\Db::query("SELECT * FROM fa_user WHERE username=:username", ['username'=>$username]);
```

---

## 依赖 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/196.html

**Contents:**
- 依赖
  - 载入依赖
  - 引入CSS

在FastAdmin中如果需要使用Bootstrap-table，需要使用require引入table模块。table模块对应的是assets/js/require-table.js文件，FastAdmin做了许多通用方法和默认值操作。

由于表格列表常用于后台管理列表，后台已经默认引入了表格相关的CSS文件，在前台未引入相关的CSS文件，如果你需要在前台使用到Bootstrap-table，则需要手动载入表格相关的CSS文件。如下：

**Examples:**

Example 1 (javascript):
```javascript
require(['table'], function(Table){
    //编写实例化代码
    //使用Table对象
});
```

Example 2 (html):
```html
<link rel="stylesheet" type="text/css" href="__CDN__/assets/libs/bootstrap-table/dist/bootstrap-table.min.css"/>
```

---

## 公共模块 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/169.html

**Contents:**
- 公共模块
- Token验证
  - 功能介绍
  - 使用示例
      - 获取Token信息
      - 设置会员的Token信息
      - 判断会员Token是否可用
      - 删除单个会员Token
      - 删除指定会员的所有Token
- 邮件发送

Token验证主要用于会员登录状态信息的维护和验证，通常情况下不需要我们调用此类的方法，在一些特殊情况下我们可以手动调用。

获取Token的详情、关联的会员ID、过期时间、有效期等信息。

新增会员Token并更新，且有效期为3600秒

通过Token和会员ID来判断Token是否可以使用。

FastAdmin中的邮件发送采用phpmailer进行邮件发送，在使用邮件发送功能前请先在后台常规管理->系统配置中配置好邮件的相关信息。

首先我们需要采用单例或实例化一个Email对象

其次我们可以设置邮件主题正文、接收者、标题等信息，比如

如果我们邮件发送失败，想获取错误的详情，可使用。

在我们开发过程中经常会用到短信发送和短信推广的功能，FastAdmin提供了一个简单实用的短信接口供开发者调用。

在使用短信发送之前，务必在后台安装好我们短信服务商的插件，如果我们要使用的服务商未提供有FastAdmin的插件，我们则需要自己开发一个，或注册一个sms_send和sms_check的事件用于我们的发送和检测操作。

首先常用的是发送短信，比如我们发送一个注册验证码。

发送以后我们有时需要检测验证码是否正确，则可以使用。

当然有些时候我们还需要发送营销短信或通知，则可以使用。

如果我们需要清空指定手机号的验证码，则可以使用。

在FastAdmin中我们有提供几个常用的辅助函数。

**Examples:**

Example 1 (php):
```php
\app\common\library\Token::get('c2259a37-5fee-4c4b-93b0-1d7313e1d1ac');
```

Example 2 (php):
```php
\app\common\library\Token::set('c2259a37-5fee-4c4b-93b0-1d7313e1d1ac', 1, 3600);
```

Example 3 (julia):
```julia
\app\common\library\Token::check('c2259a37-5fee-4c4b-93b0-1d7313e1d1ac', 1);
```

Example 4 (php):
```php
\app\common\library\Token::delete('c2259a37-5fee-4c4b-93b0-1d7313e1d1ac');
```

---

## 其他命令 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/165.html

**Contents:**
- 其他命令
  - 一键安装 FastAdmin
  - 准备工作
  - 常用命令
  - 登录后台
  - 常见问题

FastAdmin 不仅提供了 Web 在线安装方式，也可以在命令行使用命令快速的一键安装或重新安装。

请确保你的数据库存储引擎支持innodb引擎，如果不支持将无法正常安装FastAdmin。

请确保php所在的目录已经加入到系统环境变量，否则会提示找不到该命令。

打开命令行控制台进入到你的站点根目录，也就是think文件所在的目录。

为了安全，执行安装命令后会在public目录生成随机后台入口，请通过随机后台入口登录管理后台。

更多一键安装FastAdmin的参数请使用php think install --help查看。

**Examples:**

Example 1 (php):
```php
//一键安装FastAdmin
php think install
//配置数据库连接地址为127.0.0.1
php think install -a 127.0.0.1
//配置数据库用户名密码
php think install -u root -p 123456
//配置数据库表名为dbname
php think install -d dbname
//配置数据库表前缀为ff_
php think install -r ff_
//强制重新安装FastAdmin
php think install -f 1
```

---

## 函数 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/1263.html

**Contents:**
- 函数
- 函数位置
- 常用函数
  - 生成URL地址 url
  - 补全资源地址 cdnurl
  - 附加关联列表数据 addtion
  - 生成首字母图像 letter_avatar
  - 跨域请求检测 check_cors_request
  - 清理XSS xss_clean
  - 检测IP是否允许 check_ip_allowed

在FastAdmin中除了自带ThinkPHP5中常用的函数以外，还额外扩展了许多非常实用的函数，可以将这些函数快速的应用于我们的开发中。

以下是ThinkPHP5和FastAdmin中定义的函数所在位置，如果你需要添加自定义函数，请参考ThinkPHP5的文档：https://www.kancloud.cn/manual/thinkphp5/182270 。请勿修改FastAdmin和ThinkPHP5定义的函数文件。

返回值返回经过补全后的URL地址或完整URL地址

返回值返回经过补全后的上传资源的URL地址

cdnurl函数无法判断资源是云存储资源还是本地资源，如果安装启用了云存储插件，cdnurl补全的是云存储的cdn地址，如果需要补全本地资源的全路径，需要手动传递第二个$domain参数为本地域名或request()->domain()即可

返回值无，如果检测到不允许跨域，将会输出403响应

温馨提示此跨域仅用于处理PHP端跨域检测和判断，无法处理到请求图片、JS、字体文件的跨域问题，静态资源跨域处理，需要自行修改Nginx或Apache配置

检测IP是否允许访问，如果检测到IP在常规管理->系统配置中配置的禁止IP中，将会输出403响应

返回值无，如果检测到IP不允许，将会输出403响应

**Examples:**

Example 1 (unknown):
```unknown
//ThinkPHP5中定义的函数所在文件
站点目录/thinkphp/helper.php
//FastAdmin中定义的函数所在文件
站点目录/application/common.php
```

Example 2 (php):
```php
//前台模块(index/api/插件模块)
$url = url('/index/user/login'); 
//返回：/index/user/login

$url = url('/index/user/login', ['a'=>1], false, true); 
//返回：http://www.example.com/index/user/login?a=1

$url = url('/index/user/login', [], false, true); 
//返回：http://www.example.com/index/user/login

$url = url('/index/user/login', [], false, 'www.baidu.com'); 
//返回：http://www.baidu.com/index/user/login
```

Example 3 (php):
```php
//后台模块(admin)
$url = url('/index/user/login'); 
//返回：/x02lsfdsSf02Sap.php/index/user/login

$url = url('/index/user/login',[],false,true); 
//返回：http://www.example.com/x02lsfdsSf02Sap.php/index/user/login
```

Example 4 (json):
```json
//模板视图中使用
{:url('/index/user/login')}
```

---

## 列参数 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/191.html

**Contents:**
- 列参数
  - searchList格式说明

列参数定义在 jQuery.fn.bootstrapTable.columnDefaults，我们在实例化章节中配置columns的参数中可以使用以下参数。

searchList仅支持Object和二维数组

searchList返回的值只能是关联数组或二维数组，如：

如果返回["正常","隐藏"]，搜索时会将值作为参数值进行传递。

如果在服务端一定要使用数值键名返回，建议参考使用json_encode的JSON_FORCE_OBJECT来实现

**Examples:**

Example 1 (json):
```json
{"normal":"正常", "hidden":"隐藏"}
```

Example 2 (json):
```json
[
    {"id":"normal", "name":"正常"},
    {"id":"hidden", "name":"隐藏"}
]
```

Example 3 (unknown):
```unknown
return json_encode(["正常","隐藏"], JSON_FORCE_OBJECT);
```

---

## 前台模块 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/166.html

**Contents:**
- 前台模块
- 前台功能模块
  - 首页模块
  - 会员模块
- 流程介绍
- 基类解析
  - 基类控制器

FastAdmin 主要专注于后台框架，前台模块相对比较简单，前台可以根据自己项目的需求自由发挥。

FastAdmin 前台模块包含了前台首页和前台会员中心，前台首页只是一个单页面，前台会员中心有简单的注册、登录、找回密码和个人中心等。

这里的前台指整个前台 index 模块，这里仅做部分前台功能使用介绍，如果需要查看前端开发文档，请查看前端章节的文档。

首页模块比较简单，只是一个单页。完全遵循ThinkPHP5的开发结构。你可以按需修改或移除此功能模块。

FastAdmin的前台自带一个简单的会员功能模块，可以进行会员的注册、登录、找回密码、会员中心、修改个人资料、修改密码等操作。

会员模块可用于进行前台会员功能开发时使用。此处的会员模块和API中的会员模块账号是相通的，但他们登录时是不会互相影响的，可以同时登录。

FastAdmin的会员模块有注册几个事件，我们可以在事件中自定义我们的操作。你可以按照以下的方式监听相应的事件行为。

FastAdmin的前台模块完全遵循ThinkPHP5的开发规范，在此基础上我们在前台提供了一个类似后台的权限验证模块，我们可以方便快捷的控制我们的可访问权限。

前台的所有功能模块的控制器都是继承于application/common/controller/Frontend.php这个基类控制器。

在基类控制器中我们有定义一些基础属性和通用方法，首先我们看看基础属性。

以上的属性和方法我们都可以通过在当前控制器定义来达到覆盖的目的。

**Examples:**

Example 1 (php):
```php
//登录成功后的事件
Hook::add('user_login_successed', function ($user) {
});
//注册成功后的事件
Hook::add('user_register_successed', function ($user) {
});
//会员删除后的事件
Hook::add('user_delete_successed', function ($user) {
});
//会员注销后的事件
Hook::add('user_logout_successed', function ($user) {
});
```

Example 2 (php):
```php
/**
 * 布局模板
 * @var string
 */
protected $layout = '';

/**
 * 无需登录的方法,同时也就不需要鉴权了
 * @var array
 */
protected $noNeedLogin = [];

/**
 * 无需鉴权的方法,但需要登录
 * @var array
 */
protected $noNeedRight = [];

/**
 * 权限Auth
 * @var Auth 
 */
protected $auth = null;
```

Example 3 (php):
```php
/**
 * 加载语言文件
 * @param string $name
 */
protected function loadlang($name)
{
}

/**
 * 渲染配置信息
 * @param mixed $name 键名或数组
 * @param mixed $value 值 
 */
protected function assignconfig($name, $value = '')
{
}
```

---

## 前端 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/frontend.html

**Contents:**
- 前端
- 基础介绍
- 目录结构
- 标准模块
- 工具模块
  - 表单(Form)
    - 引入方式
    - 内部方法
    - 使用示例
  - 上传(Upload)

FastAdmin的前端部分使用或涉及到的是RequireJS,jQuery,AdminLTE,Bower,Less,CSS。其中：

RequireJS主要是用于JS的模块化加载。

Less主要是用于我们编写LESS和编译成CSS代码。

在阅读接下来的文档之前建议先简单的了解下RequireJS和Bower，而jQuery是我们必须要掌握的工具库

FastAdmin中前端的常用的第三方插件有Layer,Toastr，Layer用于弹窗，Toastr用于提示。

assets主要存在我们框架所需要使用到的静态资源。

assets/js/backend主要存在后台控制器所对应的JS模块。

assets/libs主要存在第三方的插件。

assets/less主要存在Less文件。

assets/img主要存在图片相关文件。

assets/css主要存在CSS样式相关文件。

assets/addons主要存放插件的相关静态资源。

在控制器章节我们有提到每个控制器都对应一个JS模块，控制器名称和JS中模块名称是一一对应的。

比如我们的控制器是application/admin/controller/Article.php，则我们JS中对应的JS模块是public/assets/js/backend/article.js。

如果我们的控制器是application/admin/controller/Member/Teacher.php，则我们JS中对应的JS模块是public/assets/js/backend/member/teacher.js。

每一个控制器请求的方法对应JS模块中一个方法。

比如控制器Article.php中的index方法，对应的是JS的article模块中的Controller.index方法，如果我们添加了自己的方法detail方法，则对应Controller.detail方法。

我们可以看到该模块第一行为RequireJS标准语法，意思是此模块依赖'jquery', 'bootstrap', 'backend', 'table', 'form'几个模块，同时将它们加载为$, undefined, Backend, Table, Form这几个对应，我们就可以放心大胆在其中使用这几个对象了。

其中有定义一个Controller 对象，它有index/add/edit/api四个方法，这四个方法分别与我们控制器中的方法一一对应。

在FastAdmin中我们封装了非常多实用的模块类便于我们使用。以下做详细介绍。

表单模块主要用于框架表单组件元素的渲染和事件绑定，当我们自定义了一个表单后，必须使用表单模块中Form.api.bindevent进行绑定表单，否则不会有任何作用。

以上代码表格当表单提交处理成功后提示成功，处理失败提示失败。

上传模块主要用于框架JS端的上传逻辑，默认采用upload进行上传，也可以采用Ajax的方法进行上传，upload的方法上传支持上传进度展示。

以上代码表格当表单提交处理成功后提示成功，处理失败提示失败。

表格模块主要用于渲染数据列表，对数据列表进行排序、过滤、筛选、绑定事件、增删改查等等操作。我们在CRUD一键生成后看到的列表就是使用表格模块进行完成的。

表格的详细介绍可以查看一张图解表格：https://ask.fastadmin.net/article/323.html

**Examples:**

Example 1 (unknown):
```unknown
public
├── assets
│   ├── addons
│   ├── css
│   ├── fonts
│   ├── img
│   ├── js
│   │   ├── backend
│   │   ├── frontend
│   ├── less
│   └── libs
```

Example 2 (sass):
```sass
define(['jquery', 'bootstrap', 'backend', 'table', 'form'], function ($, undefined, Backend, Table, Form) {

    var Controller = {
        index: function () {
            // 初始化表格参数配置
            Table.api.init({
                extend: {
                    index_url: 'category/index',
                    add_url: 'category/add',
                    edit_url: 'category/edit',
                    del_url: 'category/del',
                    multi_url: 'category/multi',
                    dragsort_url: '',
                    table: 'category',
                }
            });

            var table = $("#table");

            // 初始化表格
            table.bootstrapTable({
                url: $.fn.bootstrapTable.defaults.extend.index_url,
                escape: false,
                pk: 'id',
                sortName: 'weigh',
                pagination: false,
                commonSearch: false,
                columns: [
                    [
                        {checkbox: true},
                        {field: 'id', title: __('Id')},
                        {field: 'type', title: __('Type')},
                        {field: 'name', title: __('Name'), align: 'left'},
                        {field: 'nickname', title: __('Nickname')},
                        {field: 'flag', title: __('Flag'), operate: false, formatter: Table.api.formatter.flag},
                        {field: 'image', title: __('Image'), operate: false, formatter: Table.api.formatter.image},
                        {field: 'weigh', title: __('Weigh')},
                        {field: 'status', title: __('Status'), operate: false, formatter: Table.api.formatter.status},
                        {field: 'operate', title: __('Operate'), table: table, events: Table.api.events.operate, formatter: Table.api.formatter.operate}
                    ]
                ]
            });

            // 为表格绑定事件
            Table.api.bindevent(table);
        },
        add: function () {
            Controller.api.bindevent();
        },
        edit: function () {
            Controller.api.bindevent();
        },
        api: {
            bindevent: function () {
                Form.api.bindevent($("form[role=form]"));
            }
        }
    };
    return Controller;
});
```

Example 3 (javascript):
```javascript
require(['form'], function(Form){});
```

Example 4 (swift):
```swift
//为表单绑定事件，将自动绑定上传/富文本/下拉框/selectpage/表单验证等功能，FastAdmin中最常用的方法，
Form.api.bindevent(form, success, error, submit);

//表单自定义事件存储对象
Form.api.custom

//提交表单的方法，在表单完成验证后进行提交
Form.api.submit(form, success, error, submit);

//以下事件为具体第三方插件实现的方法，可以在调用`Form.api.bindevent`之前修改对应的方法来修改相应功能
Form.events.bindevent(form)
Form.events.citypicker(form)
Form.events.cxselect(form)
Form.events.datetimepicker(form)
Form.events.faselect(form)
Form.events.fieldlist(form)
Form.events.faupload(form)
Form.events.selectpage(form)
Form.events.selectpicker(form)
Form.events.slider(form)
Form.events.autocomplete(form)
Form.events.tagsinput(form)
Form.events.validator(form, success, error, submit)
```

---

## 参与开源生态贡献 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/contributing.html

**Contents:**
- 参与开源生态贡献

FastAdmin 致力于服务开发者，努力为开发者节省更多的时间。

参与开源社区的方式有很多种，比如：使用开源、推荐开源、写书写教程、贡献代码、回答社区问题、总结经验、打赏赞助等等，这些都可以让开源可持续的发展下去，开源更像是一群志同道合的小伙伴们同时开发一个有趣的项目，并吸引更多有趣的小伙伴们加入。

欢迎广大开发者朋友们贡献自己的智慧，让 FastAdmin 变得更强大，让 FastAdmin 变得更完美，最终为你节省更多的时间，让大家有更多的时间读书、健身、开源、投资、帮朋友和陪家人。

感谢支持 FastAdmin，感谢支持国内的开源社区。

以下介绍如何以贡献代码的方式参与开源社区。

---

## 参考文档列表 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/1452.html

**Contents:**
- 参考文档列表
- FastAdmin
- 后端
- 前端
- 工具
- 规范
- 精选文章
- 视频教程

FastAdmin 站在巨人的肩膀上，只为更好的服务开发者，努力为开发者节省更多的时间，FastAdmin 开源后台框架整合了很多优秀的第三方开源软件，本文将列出部分 FastAdmin 参考文档，供大家查阅。

FastAdmin 参考文档会不定期更新，如有补充欢迎私信 QQ 群中的 F4nniu 进行完善，感谢支持 FastAdmin。

规范的制定并非为了束缚，而是为了达到以下目标：

特别提出语义化版本规范的重要性，《语义化版本规范》对于业务相关性越强的场景越发关键。

---

## 后台模块 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/168.html

**Contents:**
- 后台模块
  - 介绍
- 后台界面概览
- 后台功能模块
  - 控制台
  - 常规管理
    - 系统配置
      - 附件管理
    - 个人资料
  - 权限管理

后台模块是 FastAdmin 开源后台框架的核心模块，提供了大量高效和实用的功能，方便开发者快速搭建项目的后台。

在此仅做后台的流程介绍、核心类解析及相关功能模块功能使用介绍，如果需要查看前端开发文档，请前往相应章节查看文档。

FastAdmin 的后台界面布局直观，主要由以下三个区域组成：

后台模块默认包含了控制台、常规管理、权限管理、插件管理、会员管理、分类管理（默认隐藏）、测试管理（用户自行生成）。

在后台管理中一些基础配置，例如系统配置、附件管理、个人配置等功能都归属到该级栏目下面。

用于管理系统的配置信息，包括站点标题、站点底部信息、邮件配置、字典配置等。

在开发中经常会遇到一些配置信息可以在后台进行修改的功能，此时我们在系统配置中进行增改操作。系统配置中的配置项不支持删除功能，如果需要删除配置项，需要删除数据库中fa_config表中相对应的行。

在系统配置中的添加一栏，我们可以自定义添加系统配置。以下是添加项的详细解释。

系统配置支持多种数据类型，下面依次做简单介绍。

附件管理可以管理前后台上传的文件资源，也可以在此上传资源到服务器或云存储。

附件管理中的删除只会删除数据库的记录，并不会删除对应的文件（云存储文件根据插件管理中配置的附件删除时是否同步删除文件判断是否删除对应的文件）。

当我们配置了第三方云储存插件时，附件管理中的添加将出现上传到第三方的按钮，此时我们的上传就是上传到第三方云存储。

用于管理后台管理员，包括添加、编辑、删除、禁用、启用等操作。

用于管理角色组，包括添加、编辑、删除、启用、禁用等操作。

插件管理是FastAdmin的插件的控制面板，在插件管理中可以在线免费或付费购买安装 FastAdmin插件市场中的应用插件，也可以在插件管理中配置、禁用、启用、卸载、升级插件。

如果我们安装完插件是需要启用、刷新插件缓存、清除后台缓存才会生效。部分插件是没有后台管理菜单或前台访问页面。

默认隐藏，无实际功能，仅供开发者参考，可在菜单规则中显示。

默认未生成，可通过快速开始章节由用户自行一键 CRUD 生成，主要用于开发者用户参考，开发者可以复制一份 fa_test 根据 FastAdmin 数据库规范自由修改数据表，然后通过一键生成 CRUD 重新生成。

首先需要知道FastAdmin的后台模块是禁用了路由功能，因此后台的操作都是根据URL进行分段解析，例如我们请求的是以下链接，其中example.php为你后台入口文件

则调用的是默认控制器application/admin/controller/Index.php中的默认方法index。

则调用的是application/admin/controller/Dashboard.php中的index方法

框架在调用到Dashboard.php这个控制器的index方法后会自动渲染application/admin/view/dashboard/index.html这个视图文件。

如果需要修改显示的内容，则修改这个这个视图文件即可。

但我们会发现有些控制器并没有index,add,edit,del等方法，但其实这些方法都在控制器的父类中采用了traits进行引入，我们转到父类application/common/controller/Backend.php就可以看到有一行

这一行就相当于把文件application/admin/library/traits/Backend.php中的所有方法引入到当前控制器。如果我们需要覆盖基类定义的方法，则直接在当前控制器中定义即可。

后台的所有功能模块的控制器都是继承于application/common/controller/Backend.php这个基类控制器。

在基类控制器中我们有定义一些基础属性和通用方法，首先我们看看基础属性。

以上的属性和方法我们都可以通过在当前控制器定义来达到覆盖的目的。

**Examples:**

Example 1 (yaml):
```yaml
https://demo.fastadmin.net/奇怪的文件名.php
```

Example 2 (yaml):
```yaml
https://www.example.com/example.php
```

Example 3 (yaml):
```yaml
https://www.example.com/example.php/dashboard/index
```

Example 4 (markdown):
```markdown
/**
 * 引入后台控制器的traits
 */
use \app\admin\library\traits\Backend;
```

---

## 城市选择 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/180.html

**Contents:**
- 城市选择
  - 常规示例
  - 常用属性
  - 事件捕获
  - 数据源

FastAdmin中集成了强大的city-picker城市选择插件，可以很方便的选择省份和城市。

我们只需要简单的为input元素添加一个data-toggle="city-picker"属性即可自动渲染相应的城市选择组件，如下：

我们还可以通过添加以下属性来扩展城市选择组件的功能

city-picker组件默认选择后渲染的是中文城市信息，我们可以通过在JS中监听city-picker更新后的事件来获取省份城市地区对应的code值。代码如下：

如果我们数据库中存放的是地区的code值，在显示时我们则需要把对应的code通过读取数据库转换成我们的地区中文，然后再设定input的value值即可。

该组件数据源使用本地数据源，数据源位于public/assets/libs/fastadmin-citypicker/dist/js/city-picker.data.js

**Examples:**

Example 1 (html):
```html
<div class='control-relative'>
    <input id="c-city" class="form-control" data-toggle="city-picker" name="row[city]" type="text" value="" />
</div>
```

Example 2 (gdscript):
```gdscript
$("#city-picker").on("cp:updated", function() {
  var citypicker = $(this).data("citypicker");
  var code = citypicker.getCode("district") || citypicker.getCode("city") || citypicker.getCode("province");
  $("#code").val(code);
});
```

---

## 多语言 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/language.html

**Contents:**
- 多语言
- 使用方法
- 加载方式
- 常见问题

在FastAdmin中可以在任何位置(控制器、视图、JS)使用__('语言标识');调用语言包，如果语言标识不存在，则直接输出该语言标识。

FastAdmin中的__函数和ThinkPHP中的lang函数在传参上有些许区别

而如果采用ThinkPHP中的lang中的写法则是

可以看到ThinkPHP中的第二个参数必须传入数组，而FastAdmin中的__则没有这个要求，其实在多个参数时FastAdmin会忽略掉第三个参数$lang比如

因此如果要使第三个参数$lang生效，则只能将第二个参数传为数组或采用ThinkPHP中的lang函数

如果需要在HTML视图文件中使用多语言，则需要使用{:__('Home')}的方式调用，而在PHP和JS中均可以使用__('Home')的方式发起调用。

如果我们调用的多语言不存在，则会原样输出字符。例如我们调用__('Undefined')，则会原样输出Undefined字符。

在FastAdmin当中，框架会自动按照当前请求的控制器进行加载对应的语言包。例如当前我们是中文环境，如果我们请求的是

可以看到FastAdmin会默认加载zh-cn.php这个全局语言包。

如果我们需要跨模块引入其它模块的语言包，则可以在 控制器中使用loadlang方法来引入，如

如果需要在JS中跨模块引入语言包，则需要修改Ajax.php中的lang这个方法。

**Examples:**

Example 1 (php):
```php
__('My name is %s', "FastAdmin");
```

Example 2 (unknown):
```unknown
My name is FastAdmin
```

Example 3 (php):
```php
lang('My name is %s', ["FastAdmin"]);
```

Example 4 (php):
```php
__('This is %s,base on %s', 'FastAdmin', 'ThinkPHP5');
```

---

## 安全建议 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/security.html

**Contents:**
- 安全建议
  - 安全建议

FastAdmin 致力于服务开发者，一直在不断的迭代更新中。

FastAdmin 团队非常关注安全问题，安全不仅仅代码安全，同时还涉及到服务器安全等多方面，建议你配置好服务器相关安全配置，做好目录权限控制。

请技术工程师、安全运维工程师关注以下几点：

感谢支持 FastAdmin，感谢支持开源社区。我们会更加努力的做好开源社区，为开发者节省更多的时间。

---

## 安装 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/install.html

**Contents:**
- 安装
- 环境要求
  - 服务器环境要求
  - 客户端浏览器推荐
- 安装教程
  - 第一步：新建站点
  - 第二步：上传框架
  - 第三步：配置并安装
- 视频教程
- 开发环境可选项

为了确保 FastAdmin 框架能够正常运行，请确保你的服务器满足以下环境要求：

推荐使用 Google Chrome v100+、Firefox v100+、Microsoft EDGE v100+ 或 Apple Safari v13+。

FastAdmin 开源框架的安装非常简单，只需简单三步即可安装完成。（推荐使用云服务器）

下面以 Linux 宝塔面板 （Linux + Nginx + PHP7.4 + MySQL5.7）为例。

注意事项：如果你重复执行install.php，数据库中的 FastAdmin 框架基础表和用户表将被重置，请提前做好全站备份。

我们还提供了更加详细的 FastAdmin 安装教程，欢迎观看。

为了节省你的时间，FastAdmin 开源框架推荐的 php 环境如下。

---

## 富文本编辑器 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/187.html

**Contents:**
- 富文本编辑器

FastAdmin的富文本编辑器只需要给对应的textarea增加一个class为editor即可，FastAdmin在使用Form.api.bindevent绑定事件时即会将textarea渲染为富文本编辑器，目前支持summernote、nkeditor和ueditor等富文本编辑器，需安装对应的插件即可正常使用。

如果是自定义表单,例如在index页面，需使用Form.api.bindevent绑定事件才会生效，否则单独添加个editor是不会生效的如果是动态生成的元素，需使用Form.api.bindevent绑定事件才会生效在安装完对应的富文本插件后我务必启用、刷新插件缓存并清除浏览器缓存后才生效。建议只启用一个富文本编辑器，如果需要不同的页面展示不同的编辑器，需要修改编辑器插件代码，修改对应的选择器，将editor改成自定义的class(目前最新版本1.3.0+已经支持在插件管理中配置富文本渲染的class，无需修改插件代码)

---

## 常见问题 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/faq.html

**Contents:**
- 常见问题
  - 在FastAdmin中如何开启调试模式？
  - 为什么在调试模式下功能正常，但在生产环境下功能失效
  - 为什么在外网访问后台速度非常慢
  - 如何启用后台管理多级菜单功能
  - 插件管理配置了错误的伪静态前台无法访问时如何操作
  - 如何在生成CRUD时生成回收站功能
  - 如何在控制器或模型中获取当前登录的管理员或登录用户信息
  - 安装后提示控制器不存在:E或控制器不存在:N
  - FastAdmin的数据库SQL文件在哪里

如果你在使用FastAdmin开发框架的过程中遇到问题,请到问答社区提问: https://ask.fastadmin.net

如果你有修改了框架核心的JS文件或者修改了核心样式文件，需要使用命令重新压缩打包JS和CSS后才会在生产环境下生效，具体请参考：https://doc.fastadmin.net/doc/162.html

如果你在外网开启了调试模式，因为在调试模式下加载的文件非常多，访问速度会非常慢，请在外网或生产环境下关闭调试模式。如果有更高的响应要求，建议采用CDN部署静态资源。部署方式请参考：#如何将静态资源采用CDN方式部署到第三方云存储

FastAdmin从1.0.0.20180513_beta版本开始新增了多级菜单功能，开发者可以很方便的在配置文件中修改是否开启多级菜单功能，找到application/config.php文件最下方有个multiplenav配置，默认是false，如果需要启用，请将multiplenav置为true即可。

如果启用了多级菜单后，菜单规则中的第一级将作为一级菜单显示在顶部。我们可以在权限管理->菜单规则中额外添加一级菜单，然后再重新规划我们的菜单。

FastAdmin从1.3.0版本开始已经支持后台个性化布局，后台管理员登录后直接在后台管理右上角修改对应的布局后即可实时生效，无需修改配置文件。

如果在后台配置某一插件的伪静态错误时，导致前台完全无法打开时，你可以尝试使用http://www.example.com/随机字符.php 进行登录后台，登录后再重新配置伪静态即可。如果连后台登录也报错，可以尝试修改application/extra/addons.php，移除键名为route对应的值，修改为[]，然后登录后台修改正确的伪静态，再清除缓存即可。

FastAdmin从1.0.0.20190301_beta版本开始已经支持自动生成回收站功能，如果需要生成回收站功能，请确保你的FastAdmin版本，其次确保你的数据表中存在deletetime这个字段，默认值必须为null,不能为0，只需保证存在此字段，CRUD在生成时会自动生成回收站相关的前后端代码和文件。

在FastAdmin所提供的基类Frontend、Backend、Api中都有提供获取当前管理员或登录用户的信息方法

在后台管理的控制器中可以通过$this->auth->id来获取管理员ID，$this->auth->字段名获取管理员的其它信息，如果需要在后台的Model中获取当前登录的管理员ID，可以通过两种方式获取：

在前台或API的控制器中可以通过$this->auth->id来获取当前登录会员ID，$this->auth->字段名获取登录会员的其它信息，如果需要在前台的Model中获取当前登录的用户信息，可以通过以下的方式获取：

出现这种情况一般是由于Web服务器的PATH_INFO未配置正确，导致服务器接收到了错误的PATH_INFO值，请检查你的PATH_INFO并修复后再重试

FastAdmin在安装时会自动创建数据库和数据表,免除了你手动创建数据库和导入数据库的烦恼。FastAdmin的数据库安装文件保存在 application/admin/command/Install/fastadmin.sql

为了进一步提升加载速度，后台默认启用了绿色主题的皮肤，如何修改其它皮肤呢？从1.3.0版本开始，已经支持在后台配置自定义皮肤(仅对当前浏览器生效)，无需要修改配置文件。从1.2.0版本开始，已经支持通过配置文件修改后台默认皮肤，可以直接修改application/config.php中的adminskin值来实现快速换肤功能，adminskin支持的值有

这是由于控制器的基类你肯定继承的是Frontend，Frontend基类有鉴权判断，有以下两种办法可以尝试

如果是你自己添加的控制器，可以使用一键生成菜单命令(php think menu -c 控制器名)来生成菜单，如果你是手动添加的规则菜单，权限规则必须细化到控制器的方法才可以。

这是由于php.exe文件所在目录未加入到PATH环境变量导致的

找到php.exe文件所在的目录，将该目录加入到系统PATH环境变量中后，重启CMD即可解决

如果你找不到php.exe，可以参考FastAdmin开发环境配置系列教程

这是由于在Linux环境下未找到php的脚本程序

有两种解决办法，首先尝试使用which php找到php所在的位置。

这是由于你的服务器伪静态没有生效或错误导致的。

如果你使用宝塔面板，请直接在宝塔面板后台->网站->伪静态 中选择ThinkPHP5的伪静态规则即可。如果你使用的是 lnmp.org 的一键安装LNMP环境，请查阅 https://lnmp.org/faq/lnmp-vhost-add-howto.html#rewrite 的伪静态配置。如果你使用的是phpStudy，建议参考视频安装教程中的伪静态配置：https://www.fastadmin.net/video/install.html

如果你是自行安装的Nginx，建议将虚拟主机的root绑定运行目录至public目录

这是由于你的服务器伪静态没有生效或错误导致的，如果你使用宝塔面板，请直接在宝塔面板后台->网站->伪静态 中选择ThinkPHP5的伪静态规则即可。

这种情况一般在Apache下伪静态不工作的情况下出现，首先确保已经启用Apache的伪静态，确保目录已经配置好权限，如下面的Directory配置

其次伪静态规则在Apache fastcgi模式下会导致No input file specified.，未指定输入文件。请修改public目录下的.htaccess文件

这是由于composer默认配置是境外的源，如遇网络故障则会导致无法下载

FastAdmin后台左侧菜单栏有彩色的小角标，这一般用于通知和提醒操作，在后台开发时是非常方便的一个小功能，如何修改和禁用它呢？找到/application/admin/controller/Index.php中的index方法，其中有一段

数组的键名是对应的左侧菜单栏的相对链接数组的键值是需要显示的文字或数字，可以传字符串或数组

如果是字符串，则角标的颜色是按照'red', 'green', 'yellow', 'blue', 'teal', 'orange', 'purple'的方式进行循环的。如果是数组，这三个值分别表示：[显示的文字, 颜色，展现方式(badge或label)]

如果需要删除这个小角标，则可以直接到数组置为空即可

在JS端同样可以进行相应的操作，在JS中对应需要刷新角标的地方使用以下方法即可添加或删除

首先可以尝试下清空浏览器缓存后再刷新重试其次可以使用谷歌浏览器的开发者工具，按F12，切换到Network，看具体的上传文件时的错误信息。

在FastAdmin中压缩打包JS和CSS文件需要NodeJS的支持在Windows下需要手动配置Node的可执行文件,请修改application/admin/command/Min.php中$nodeExec的值如你的Node可执行文件是C:/Program Files/nodejs/node.exe，则请配置$nodeExec = '"C:/Program Files/nodejs/node.exe"';

如果我们在FastAdmin开发过程中遇到此错误，说明我们application/config.php中的app_debug是关闭的，必须开启app_debug为true才可以显示出详细的错误信息。如果开启app_debug仍然显示不出详细错误，请确保php.ini中的display_error为开启状态。

很多时候都有可能遇到提示未知的数据格式或网络错误这个提示，产生这个错误的原因一般来说都是服务端报错，导致返回的数据不是JSON格式或直接未返回，如下图

准备工作：首先确保你的FastAdmin开启了调试模式application/config.php中的app_debug置为true两种定位错误的方法：

FastAdmin建议运行在PHP7.4及以上版本，因此如果提示网络错误请检查你的PHP是否低于该版本

如果你只需要将上传的文件上传至又拍云、七牛云或阿里OSS，请在插件管理中下载对应第三方云存储的插件并配置好即可，无需下方的步骤。

FastAdmin可以将框架静态的资源部署到云存储或CDN，可大大的加快网站的访问，默认FastAdmin框架的静态资源是不采用CDN部署的，如果需要启用，需要修改以下两个文件的配置

然后请将你的静态资源public/assets文件夹同步至你的CDN。

如果采用了静态资源CDN部署，在后台插件管理中对插件执行安装、禁用、启用、卸载后都需要将public/assets/addons/目录和public/assets/js/addons.js文件刷新缓存或同步更新到CDN。

为了后台安全，新版本默认开启了后台IP变动检测，如果你需要关闭此功能，可以修改application/config.php，将loginip_check置为false即可。

如果你使用了CDN、分布式部署或负载均衡，也有可能导致获取IP地址不正确，从而导致一登录就自动退出，请参考https://doc.fastadmin.net/doc/faq.html#toc-50

一般出现这种情况都是由于你使用了Windows自带编辑器编辑了某个配置文件或模板，导致文件本身的编码变成了utf8-bom格式，这时你需要排查你的项目的所有文件。如果你使用PHPStorm进行开发，可以在项目目录根路径上点击右键，点击Remove BOM来移除bom头，将文件编码变为utf8(新版本PHPStorm请选中文件夹后，点击菜单中的文件->文件属性->移除BOM进行移除)。

后台管理后台默认是控制台首页，如需修改，请在后台->常规管理->系统配置中，将后台固定页修改为你的控制器方法的链接即可，这里注意使用相对链接即可，注意链接无需包含?ref=addtabs。

这是由于系统在检测到POST提交时会记录提交的参数信息，如果提交的POST数据过大，会导致日志表的content字段溢出，此时我们需要修改fa_admin_log表的content字段，将字段类型修改为longtext类型即可。

这是由于上传配置中的cdnurl为空，导致导出的图片没有截图域名前缀，需要手动修改application/extra/upload.php中的cdnurl值，将cdnurl的值修改为你的站点地址即可，例如：https://www.example.com，注意不能以/结尾。

有些时候我们在前台提交的富文本内容被过滤了，比如富文本首行的缩进丢失，这是由于FastAdmin的基类是有开启全局过滤。

修改方法一：修改application/common/controller/Frontend.php移除trim过滤限制修改application/common/controller/Backend.php移除trim过滤限制修改application/common/controller/Api.php移除trim过滤限制

特别注意strip_tags,htmlspecialchars不建议移除，移除后会导致跨站安全问题。

修改方法二：不修改框架核心文件，仅在控制器中接收数据时单独处理，如：

这种情况常出现在安装后又卸载插件，而卸载插件时由于插件目录中有文件被打开或被其它软件占用，导致卸载插件时目录无法清除干净，此时再次安装插件时就会出现该情况，请尝试做好备份，手动清除addons/插件标识文件夹后重试，插件标识可以从插件URL中查询到，如知识付费问答社区：https://www.fastadmin.net/store/ask.html 它的插件标识则是ask。

在FastAdmin中插件中配置的伪静态优先级默认是按照字母来排序的，如果我们需要修改插件伪静态的优先级，可以手动配置application/extra/addons.php，修改其中的priority，添加应用插件标识，放在前面则优先匹配，如

这里表示优先配置third，然后才是cms和ask。最后在后台插件管理右上角清除插件缓存即可。

后台常规管理->系统配置的cdn地址仅限用于静态资源采用CDN部署时才需要配置，如果静态资源未部署CDN，而此时在后台系统配置中配置了cdn地址会导致后台样式丢失，且后台无法登录，此时我们需要手动修改application/extra/site.php中的cdnurl，将它的值修改为空即可。

FastAdmin 从1.3.x版本开始已经在后台移除该配置。

这是由于你的Mysql配置中设置了only_full_group_by导致的错误，需要你修改你的Mysql配置，首先需要找到你的Mysql的my.cnf，找到其中的mysqld，修改sql_mode，移除ONLY_FULL_GROUP_BY，如

从1.3.0+版本开始，后台系统配置中添加配置项的功能只在开发环境才可使用，如需添加配置，需要开启调试模式后，再刷新页面即可。

如果启用固定列，此时不支持拖拽排序，所以会为灰色，如需启用拖拽排序，只能禁用固定列，找到页面对应的JS，移除代码中的fixedColumns：true即可。

目前多文件(多图片)中的文件地址暂不支持存在,，会导致图片错误，请参考：https://doc.fastadmin.net/doc/177.html#toc-5 温馨提示中的说明。

打开 application/extra/upload.php，修改mimetype，加入需要上传类型的文件后缀。

首先请检查：application/config.php是否设置login_captcha，为true时才会启用验证码功能。其次请参考：https://ask.fastadmin.net/question/985.html 排查下图片是否有报错信息，如果状态码为500或404，请开启调试后查看具体错误原因。如果接口状态码为200，说明图片接口正常，请检查下是否在Windows下使用自带记事本编辑了代码文件(或修改配置文件)，导致编辑的文件存在utf8 bom头，请移除utf8 bom头，使用utf8编码后重试。请检查PHP环境GD库是否正确安装。如果以上方法试了都不行，建议开启调试模式后调试下vendor/topthink/think-captcha/src/Captcha.php中的entry方法排查具体错误原因。

这是由于FastAdmin框架默认开启了登录失败重试次数限制，当失败次数超过10次时，需要1天后才可以重新登录，你可以手动登录数据库修改数据库表fa_admin中对应管理员的loginfailure为0，然后重试登录即可。

这种情况一般出现在本地上传时出现，通常情况下是由于上传的文件超出了服务器配置的限制，导致服务端无法正常获取到数据，请参考问题进行修改服务器配置：https://ask.fastadmin.net/question/27680.html

打开 application/config.php，找到底部fastadmin配置，修改usercenter值为false即可。

首先在插件市场安装一款短信插件并配置相关的参数，然后打开 application/config.php，找到底部fastadmin配置，修改user_register_captcha值为mobile即可。

打开 application/config.php，找到底部fastadmin配置，修改user_register_captcha值为email即可。

这是由于你在页面中使用了session，或视图模板中有调用{:token()}输出token(此时也会使用到session)，因使用了session的页面，会自动添加响应头Cache-Control: no-store, no-cache, must-revalidate。

首先请检查runtime/log中的日志信息，检查是否有错误信息产生，如果有错误信息请根据错误信息进行处理，如果没有错误，请检查是否使用了宝塔面板，请检查是否宝塔面板中的防火墙进行了拦截。

这是因为数据表的字符集不一致导致的，请将数据表统一一下，比如都使用 utf8mb4_general_ci

这是由于FastAdmin框架中引入了新版本Bootstrap-Select组件导致冲突，目前建议你做好备份后，下载https://cdn.fastadmin.net/uploads/2023/03/24/d9988d44627f5407ab4d3027b9b19b87.zip

解压后将其中的public文件夹覆盖到站点目录进行合并，然后清浏览器缓存即可。

首先如果有安装使用云存储插件，请检查云存储插件中配置的CDN地址和上传接口地址是否使用了http其次如果我们使用了CDN，也有可能导致该问题发生，此时建议你检查你使用的CDN的配置在回源时是否支持HTTP_X_FORWARDED_PROTO，如果支持请检查该值是否为https，如果不支持HTTP_X_FORWARDED_PROTO，请检查你的CDN是否支持自定义回源参数，如果支持自定义回源参数，请自定义一个回源参数，然后修改application/config.php，添加一项https_agent_name配置，https_agent_name的值为你自定义回源参数即可。如果无法自定义回源参数，请参考下方的问题2：生成的URL链接不正确(协议不正确)")的解决办法修改配置。

如果服务器使用了负载均衡或CDN后造成获取客户端IP为内网IP以及生成URL链接不正确时可按以下方式修改配置。

因为在ThinkPHP5框架中获取客户端IP是通过REMOTE_ADDR参数来获取的，如果此时我们使用了负载均衡或CDN后会造成客户端IP为负载均衡或CDN服务器的IP地址，此时我们可以咨询我们使用的云服务商或参考云服务商提供的相关文档，获取负载均衡或CDN传递真实IP的参数名，然后修改application/config.php中的http_agent_ip值即可。

因为ThinkPHP5框架中使用url函数生成URL路径时，优先使用HTTPS/REQUEST_SCHEME/SERVER_PORT/HTTP_X_FORWARDED_PROTO来判断是否是SSL请求，从而生成URL地址。如果服务器使用了负载均衡或CDN后，由于服务器无法获取到这几个参数判断，从而导致生成URL地址错误，主要表现在生成的URL地址本应该是https://开头，但却生成了http://开头。

解决办法分两种：一种是需要修改application/config.php，添加一个is_https的参数，值设定为true即可，这种解决方案会导致不管是否是SSL请求，都会强制生成https://开头的URL。另一种就是添加转发参数，通常情况下负载均衡或CDN都会有转发或回源参数的配置，添加以下转发(回源)参数，让服务器识别到SSL请求即可。

因为ThinkPHP5框架中使用url函数生成URL路径时，优先使用HTTP_X_REAL_HOST/HTTP_HOST来生成URL地址。如果服务器使用了负载均衡或CDN后，由于服务器无法获取到这几个参数判断，从而导致生成URL地址错误

解决办法：添加转发参数，通常情况下负载均衡或CDN都会有转发或回源参数的配置，添加以下转发(回源)参数，让服务器识别到正确请求即可。

在FastAdmin框架中如果使用了throw new \think\exception\HttpException(404, '页面不存在');或abort(404,'页面不存在');抛出了404错误，默认情况下会提示你所浏览的页面暂时无法访问，如果我们希望自定义404的错误页面，可以修改application/config.php配置文件，找到http_exception_template 的配置文件，如果不存在，需要手动添加配置项，配置如下：

然后在对应的application/common/view/tpl/目录下创建404.tpl模板即可。

1、该配置仅在生产环境下生效，如果开启了调试模式仍然会提示详细的错误信息。2、默认修改application/config.php会对application目录下的所有模块起作用，如index、admin、api，如果希望仅对index模块起作用，可以在application/index目录下创建一个config.php配置并做以上的配置。

默认情况下插件管理配置的菜单都是需要通过插件管理->配置进行管理，如果需要在左侧菜单中添加相应的快捷链接，可以通过权限管理->菜单规则->添加，添加中规则使用addon/config/name/插件标识的菜单即可。

默认前后台使用同一个域名时前台插件系统不会报错，如果后台单独绑定了域名，导致插件前台URL地址拼接错误，此时框架无法得知你前台插件域名主站的域名，此时需要手动修改application/admin/config.php，添加上如下配置：

其中https://www.example.com为你主站的站点地址。

通常情况下我们请求的页面都是不带/index.php，如果希望只保留不带/index.php的页面，可以通过修改application/common/behavior/Common.php中的moduleInit方法，在该方法内开头处添加如下代码即可

如果在微信PC端内打开调试模式后报Undefined offset: 1 in /www/wwwroot/www.example.com/application/common/view/tpl/think_exception.tpl或Undefined offset: 1 in /www/wwwroot/www.example.com/thinkphp/library/think/Lang.php，可参考以下方法进行修复：application/common/view/tpl/think_exception.tpl大概第22行

thinkphp/library/think/Lang.php大概第204行

使用旧版本FastAdmin的如果不需要多语言的可以关闭多语言application/config.php修改为'lang_switch_on' => false

这是由于新版本微信电脑端HTTP_ACCEPT_LANGUAGE获取为*而导致该错误。参考：https://gitee.com/fastadminnet/fastadmin/blob/1.x/application/common/view/tpl/think_exception.tpl

这是由于FastAdmin应用插件系统菜单升级功能导致，如果不希望菜单升级覆盖原有的菜单，可通过修改application/common/library/Menu.php中的menuUpdate方法，将大概第196行的

温馨提示：这种修改将导致无法和最新版本应用插件的菜单标题同步。

这是由于FastAdmin框架后台设定了referer为never，也就是不发送携带referer参数，你可以自行修改application/admin/view/common/meta.html，找到大概第5行的

移除该行即可，但通常不建议移除，这样会导致我们的列表中的图片携带有referer信息，如果一定要移除，建议配合浏览器安全策略插件：https://www.fastadmin.net/store/csp.html 来限制只加载指定域名下图片的加载。

如果我们在插件管理修改配置或右上角清缓存时提示file_put_contents(/www/wwwroot/www.example.com/xxx/xxx): failed to open stream: Permission denied，请检查对应的文件是否有写权限，修改配置或清缓存需要更新该文件，开发或配置阶段建议给对应文件添加相应的写权限，正式上线后建议移除写权限。

请确保对应文件所属的用户是否为www(通常情况下)，如果所属用户为root，也会导致该错误，请修改对应文件的归属权，请参考使用chown www:www /www/wwwroot/www.example.com/xxx/xxx，其中/www/wwwroot/www.example.com/xxx/xxx为报错的文件。

请参考以下几点进行排查：1、停留在登录页时间过长2、开启了新的登录页，原登录页token会失效3、当前登录页有其它请求导致刷新了token(如图片地址为空或使用了当前页URL)，建议使用网页开发者工具进行排查当前页面是否被请求了两次或多次4、检查服务器磁盘是否有剩余空间，磁盘空间满也会导致该错误5、检查是否使用了分布式部署，在分布式部署时务必保证将Session存储至数据库或Redis6、使用浏览器无痕模式测试，排除浏览器扩展影响。7、使用手机蜂窝网络测试，排除受网络影响。

这是由于第三方组件PHP-ZIP在解压文件时获取文件最后修改时间时，在Win32位系统下整型数据溢出导致，修复方法是做好备份后手动修改以下两处：vendor/nelexa/zip/src/Util/DateTimeConverter.php第59行，将public static function msDosToUnix(int $dosTime): int修改为public static function msDosToUnix(int $dosTime)

vendor/nelexa/zip/src/Model/ZipEntry.php第636行，将public function getTime(): int修改为public function getTime()

也就是移除对应位置两个方法结尾的: int

这是由于/public/assets/js/addons.js缓存导致，请按以下方法进行排查修复：1、点击后台右上角清除缓存->一键清除缓存2、在插件管理，找到对应报错的插件，禁用然后重新启用，然后再点击后台右上角清除缓存->一键清除缓存3、如果1和2步骤均尝试了均不行，请检查下/public/assets/js/addons.js文件中是否存在报错插件的相关代码，如果没有相关代码，可能没有报错插件的相关代码，请检查/public/assets/js/addons.js文件是否有读写权限，插件在禁用或启用时需要更新该文件，如果没有相应的权限，也会导致部分JS报错404。

首先需要根据上传模式找到需要修改的文件控制器：

在相应控制器中找到_initialize()方法，在调用父类的_initialize()之前追加以下代码：

这里修改了savekey的值，也就相当于修改了上传的目录，这样适用于所有的第三方存储插件临时修改配置。如果是中转模式，修改addons/插件标识/controller/Index.php时，你需要自行添加条件判断来源页面来动态修改，不然会影响所有中转模式下的文件上传。

云存储插件标识目前FastAdmin框架有以下几个标识：

默认不导出第一列(checkbox)与操作(operate)列，如果你在开发时移除了第一列默认的checkbox或最后一列，则会在导出时丢失相应列。解决办法：在控制器对应的JS的表格初始化时传入需要忽略的列或设置ignoreColumn为空，如：

后台管理列表页的导入功能默认禁用，如需调用导入功能，请参考文档：https://ask.fastadmin.net/article/540.html

application/common/library/Auth.php中$keeptime的值。

由于目前插件市场绝大多数应用插件均无法适配1.0.0版本，FastAdmin插件市场已于2022年停止了对FastAdmin框架1.0.0版本的支持，请升级FastAdmin框架。

由于应用插件存在频繁更新，为了接口加载响应及体验，接口在响应时只会返回最近的5个版本。

**Examples:**

Example 1 (php):
```php
\think\Session::get('admin');
```

Example 2 (php):
```php
$auth = \app\admin\library\Auth::instance();
```

Example 3 (php):
```php
//获取Auth对象
$auth = \app\common\library\Auth::instance();
//获取会员模型
$user = $auth->getUser();
```

Example 4 (unknown):
```unknown
skin-blue/skin-black/skin-purple/skin-green/skin-red/skin-yellow
skin-blue-light/skin-black-light/skin-purple-light/skin-green-light/skin-red-light/skin-yellow-light
skin-black-blue/skin-black-purple/skin-black-green/skin-black-red/skin-black-yellow
```

---

## 开关组件 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/185.html

**Contents:**
- 开关组件
  - 常用示例
  - 自定义值
  - 开关提示
  - 开关事件
  - 开关禁用

开关组件常用于状态值的变更或只有两个值的切换。

使用开关组件只需要给我们的操作按钮添加data-toggle="switcher"即可，如下：

如果你的开关的值不是1和0，则可以通过data-yes和data-no属性来指定开关的值，如下：

从1.2.0版本开始，开关组件支持切换前提示，请尝试给a标签添加一个data-confirm属性即可，如下：

如果你需要监听开关切换后的事件，可以在JS中给隐藏的input文本框添加一个change事件，如下：

如果需要禁用开关组件，只需要给a添加一个disabled的class即可，如下：

**Examples:**

Example 1 (html):
```html
<!-- 根据变量值判断 -->
<input  id="c-switch" name="row[switch]" type="hidden" value="{$row.switch}">
<a href="javascript:;" data-toggle="switcher" class="btn-switcher" data-input-id="c-switch" data-yes="1" data-no="0" >
<i class="fa fa-toggle-on text-success {eq name="$row.switch" value="0"}fa-flip-horizontal text-gray{/eq} fa-2x"></i>
</a>

<!-- 默认开 -->
<input  id="c-switch" name="row[switch]" type="hidden" value="1">
<a href="javascript:;" data-toggle="switcher" class="btn-switcher" data-input-id="c-switch" data-yes="1" data-no="0" >
<i class="fa fa-toggle-on text-success fa-2x"></i>
</a>

<!-- 默认关 -->
<input  id="c-switch" name="row[switch]" type="hidden" value="0">
<a href="javascript:;" data-toggle="switcher" class="btn-switcher" data-input-id="c-switch" data-yes="1" data-no="0" >
<i class="fa fa-toggle-on text-success fa-flip-horizontal text-gray fa-2x"></i>
</a>
```

Example 2 (html):
```html
<input  id="c-switch" name="row[switch]" type="hidden" value="open">
<a href="javascript:;" data-toggle="switcher" class="btn-switcher" data-input-id="c-switch" data-yes="open" data-no="closed" >
<i class="fa fa-toggle-on text-success {eq name="$row.switch" value="closed"}fa-flip-horizontal text-gray{/eq} fa-2x"></i>
</a>
```

Example 3 (html):
```html
<input  id="c-switch" name="row[switch]" type="hidden" value="0">
<a href="javascript:;" data-toggle="switcher" class="btn-switcher" data-confirm="确认切换开关？" data-input-id="c-switch" data-yes="1" data-no="0" >
<i class="fa fa-toggle-on text-success {eq name="$row.switch" value="0"}fa-flip-horizontal text-gray{/eq} fa-2x"></i>
</a>
```

Example 4 (r):
```r
$(document).on("change", "#c-switch", function(){
    //开关切换后的回调事件
});
```

---

## 快速开始 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/1589.html

**Contents:**
- 快速开始
- 第一步：安装 FastAdmin 开源框架
- 第二步：一键生成 CRUD
- 第三步：根据项目需求二次开发
- 其他事项
- 文档日志

FastAdmin 开源后台框架提供了强大的一键生成功能，可根据数据表一键 CRUD 生成，自动生成控制器、模型、视图、JS、语言包、菜单、回收站等，下面介绍如何快速开始。

FastAdmin 后台框架只需简单三步即可快速开始，以下为详细步骤。

参考 安装 章节，可以快速完成 FastAdmin 开源框架的安装。

FastAdmin 默认内置一个 test 表，可根据表字段名、字段类型和字段注释通过一键 CRUD 自动生成。

刷新一下 FastAdmin 后台页面，可以看到多了 测试管理 的菜单，打开 测试管理 可对数据库 test 表中的数据进行增删改查操作。

一键 CRUD 后的演示：https://demo.fastadmin.net/admin.php/test?ref=addtabs

如果有大量的字段需要修改可以使用命令重新生成，字段规则可参考数据库章节进行修改。

命令执行成功后会生成以下文件，接下来就可以修改对应的文件以符合自己的项目需求。

**Examples:**

Example 1 (unknown):
```unknown
cd fastadmin
```

Example 2 (unknown):
```unknown
php think crud -t test -u 1
```

Example 3 (unknown):
```unknown
├── application
│   └── admin
│       ├── controller
│       │   └── Test.php                //控制器类
│       ├── lang
│       │   └─ zh-cn
│       │       └── test.php            //功能语言包，按需加载
│       ├── model
│       │   └── Test.php                //模型类
│       ├── validate
│       │   └── Test.php                //验证器类
│       └── view
│           └── test
│               ├── index.html          //列表视图
│               ├── add.html            //添加视图
│               ├── edit.html           //编辑视图
│               └── recyclebin.html     //回收站视图
└── public
    └── assets
        └── js
            └── backend
                └── test.js             //功能模块JS文件
```

---

## 控制器 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/controller.html

**Contents:**
- 控制器
- 基类控制器
- 基础结构
- 属性和方法
- 数据限制
- 关联查询
- 数据校验
- 权限控制
- 视图渲染
- 模板布局

FastAdmin中定义了三个基类控制器，分别位于

这里我们主要对Backend.php这个控制器基类做详细解读，因为我们后台管理的所有控制器都继承于它，而Frontend.php功能和Backend.php功能类似，而Api.php控制器主要用于API接口开发，这里就不再进行过多介绍。

在后台中我们的控制器都必须继承自\app\common\controller\Backend这个基类，其中控制器的index/add/edit/del/multi/recyclebin/destroy/restore/import/selectpage全都是可选的方法，基类的这些方法使用traits进行引入，具体位置在application/admin/library/traits/Backend.php中，CRUD生成的标准控制器如下：

基类中所定义的方法如下，以下方法都是通过application/admin/library/traits/Backend.php引入的

我们在开发过程中建议注释好每一个控制器和控制器的方法，因为我们后期可以使用php think menu -c all-controller一键生成后台管理的菜单，注释支持@icon/@remark/@internal这三个属性，分别表示图标/备注/忽略，如果是protected或private的方法在后期一键生成时会自动忽略。

控制器支持目录层级，如果在使用目录层级的时候，请注意当前控制器的命名空间，比如当前控制器文件位置是application/admin/controller/member/Teacher.php，当Teacher.php的命名空间请务必是namespace app\admin\controller\member;，如果命名空间不对会报找不到控制器的错误。

当我们的控制器继承自app\common\controller\Backend以后，我们就可以使用以下属性

我们可以直接在当前控制器使用$this->属性名来调用所支持的属性，也支持直接在当前控制器定义相关属性来覆盖父类的属性，同时TP5中\think\Controller所支持的属性也全部支持。

基类app\common\controller\Backend中所支持的方法如下

我们可以直接在当前控制器使用$this->方法名()来调用所支持的方法，同时TP5中\think\Controller所支持的方法也全部支持。

在后台开发的过程中经常会有这样的一个需求，每个管理员单独管理自己添加的数据或单独管理自己下级管理员添加的数据，管理员之间的数据是不相通的，每个管理员看到的数据是不同的。在FastAdmin中可以很方便的实现此功能。

$dataLimitField字段默认为admin_id，请注意添加该字段类型为int(10)。

通过以上配置后，在列表加载数据的时候将默认添加条件过滤不属于自己权限的数据，同时在添加时会自动维护admin_id的数据，在编辑、删除的时候会自动控制权限避免越权操作。

如果需要将原有的数据加入到FastAdmin后台管理权限控制当中，比如已有的数据已经有标识归属，但这个归属体系并非是FastAdmin的后台管理员体系。在这个时候我们就需要重写基类的getDataLimitAdminIds方法，将此方法返回数据标识的归属ID数组集合，这样即可使用FastAdmin的后台管理权限进行管理。

目前FastAdmin后台index方法支持一对一关联查询，比如我们一篇文章有归属分类，我们在列出数据时需要同时列表文章分类名称。

然后我们修改控制器的index方法，代码如下：

然后在控制器对应的model(非关联model)中添加以下代码：

更多的关联用户可以参考TP5关联模型的章节：关联模型

我们在控制器对应的JS中可以直接使用category.id、category.name等关联表的字段

在FastAdmin中默认的add/edit方法可以使用模型验证，验证器位于application/admin/validate/模型名.php中，模型验证默认是关闭的状态，如果需要启用，我们需要在当前控制器定义以下属性

当开启模型验证后，我们的添加和修改操作都会首先进行模型验证，验证不通过将会抛出错误信息，具体的模型验证规则可以参考TP5官方文档的模型验证规则：https://www.kancloud.cn/manual/thinkphp5/129355

场景验证可以参考TP5场景验证章节：https://www.kancloud.cn/manual/thinkphp5/129322

比如我们有定义一个方法mywork，而这个方法是不需要登录即可访问的，则我们需要在当前的控制器定义

比如我们有定义一个方法mytest，而这个方法是需要登录后任何管理员都可以访问，则我们需要在当前的控制器定义

如果我们需要动态定义，请务必放在调用父类的_initialize方法之前，否则是不会生效的。

基类app\common\controller\Backend会默认渲染以下几个对象到视图中

我们可以在视图中使用{$site.name}、{$config.modulename}、{$auth.id}、{$admin.username}来获取我们所需要的数据

如果我们需要自己在控制器中透传数据到JS中去，则可以使用控制器的assignconfig方法来透传，使用如下

控制器默认全部采用模板布局，因此我们的页面都会自动加上头部和尾部，如果我们有特殊的页面不需要采用模板布局，我们可以使用$this->view->engine->layout(false); 来关闭当前方法的模板布局。

如果我们需要使用自己的模板布局，在当前控制器定义protected $layout = '布局模板';即可。

请注意如果采用了自己的模板布局或禁用了模板布局，将无法使用FastAdmin的JS按需加载和Config变量访问。

FastAdmin的\app\common\controller\Api和\app\common\controller\Frontend基类控制器有启用全局过滤，过滤方法为trim,strip_tags,htmlspecialchars，当使用ThinkPHP5的方法获取请求的参数值时，会被过滤HTML和特殊字符，如有特殊情况下需要不过滤(如获取小程序请求的encryptedData)，可以使用$this->request->post("参数名", "默认值", null);将第三个参数设置为null即可获取原生请求的数据，特别注意当使用原生请求的数据时务必注意服务端的安全处理和安全输出。

**Examples:**

Example 1 (unknown):
```unknown
application/common/controller/Api.php //API接口基类控制器
application/common/controller/Backend.php //后台基类控制器
application/common/controller/Frontend.php //前台基类控制器
```

Example 2 (php):
```php
<?php

namespace app\admin\controller;

/**
 * 文章管理
 *
 * @icon fa fa-list
 * @remark 用于统一管理网站的所有文章
 */
class Article extends Backend
{

    protected $model = null;
    protected $noNeedLogin = [];
    protected $noNeedRight = ['selectpage'];

    public function _initialize()
    {
        parent::_initialize();
    }
    
    /**
     * 默认生成的控制器所继承的父类中有index/add/edit/del/multi/destroy/restore/recyclebin八个方法
     * 因此在当前控制器中可不用编写增删改查的代码,如果需要自己控制这部分逻辑
     * 需要将application/admin/library/traits/Backend.php中对应的方法复制到当前控制器,然后进行修改
     */

}
```

Example 3 (php):
```php
class Backend extends Controller{
    /**
     * 查看
     */
    public function index(){}
  
    /**
     * 添加
     */
    public function add($ids = ""){}
  
    /**
     * 编辑
     */
    public function edit($ids = ""){}
  
    /**
     * 删除
     */
    public function del($ids = ""){}
  
    /**
     * 批量更新
     */
    public function multi($ids = ""){}
  
    /**
     * 回收站
     */
    public function recyclebin(){}
  
    /**
     * 真实删除
     */
    public function destroy($ids = ""){}
  
    /**
     * 还原
     */
    public function restore($ids = ""){}
  
      /**
     * 导入
     */
    protected function import(){}
  
    /**
     * 下拉筛选
     */
    public function selectpage()
    {
        return parent::selectpage();
    }
}
```

Example 4 (php):
```php
/**
 * 无需登录的方法,同时也就不需要鉴权了
 * @var array
 */
protected $noNeedLogin = [];

/**
 * 无需鉴权的方法,但需要登录
 * @var array
 */
protected $noNeedRight = [];

/**
 * 布局模板
 * @var string
 */
protected $layout = 'default';

/**
 * 权限控制类
 * @var Auth
 */
protected $auth = null;

/**
 * 快速搜索时执行查找的字段
 */
protected $searchFields = 'id';

/**
 * 是否是关联查询
 */
protected $relationSearch = false;

/**
 * 是否开启数据限制
 * 支持auth/personal
 * 表示按权限判断/仅限个人 
 * 默认为禁用,若启用请务必保证表中存在admin_id字段
 */
protected $dataLimit = false;

/**
 * 数据限制字段
 */
protected $dataLimitField = 'admin_id';

/**
 * 是否开启Validate验证
 */
protected $modelValidate = false;

/**
 * 是否开启模型场景验证
 */
protected $modelSceneValidate = false;

/**
 * Multi方法可批量修改的字段
 */
protected $multiFields = 'status';
```

---

## 插件 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/addon.html

**Contents:**
- 插件
- FastAdmin 插件市场
  - 插件开发者
  - 常见问题

插件是 FastAdmin 生态中重要的一环，在 FastAdmin 中完整应用和普通插件统一称为插件，开发者可以在后台管理 插件管理 中对插件进行安装、禁用、卸载等操作。

插件市场 目录结构 行为事件 插件安装 插件配置

如果你是 FastAdmin 插件开发者，请直接阅读FastAdmin开发者文档，有更详细的插件开发文档

---

## 插件安装 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/176.html

**Contents:**
- 插件安装
  - 安装插件
  - 升级插件
- 温馨提示

FastAdmin 框架的插件管理可以安装、配置、升级、卸载插件。

FastAdmin 所有插件都需要先安装 FastAdmin 框架，插件的安装需要以下三个步骤：

对于插件的安装或使用问题可以提交工单，或者将问题发到问答区。

升级插件前务必做好全站（代码+数据库）备份！备份！备份！如果需要对插件进行在线升级，请做好备份后在插件管理->本地插件，找到对应的插件进行升级即可，升级前务必做好全站备份。如果插件新版本依赖的FastAdmin版本不符合条件，请先升级FastAdmin框架，如何升级FastAdmin框架。

---

## 插件市场 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/175.html

**Contents:**
- 插件市场
- 插件开发文档
- 插件示例

FastAdmin 致力于服务开发者，努力为开发者节省时间，让大家有更多的时间读书、健身、开源、投资、旅行，以及帮朋友和陪家人。

为了 FastAdmin 开源社区长期可持续的发展下去，FastAdmin 团队听取了社区开发者用户的建议，邀请了社区开发者一起组建了插件市场。

欢迎大家一起参与 FastAdmin 生态建设，让 FastAdmin 开源生态更加繁荣，生态成员之间合作共赢，最终为你节省更多的时间。

目前 FastAdmin 官方已经上线插件市场：https://www.fastadmin.net/store.html

如果你开发了一款插件需要上架到 FastAdmin 的插件市场，请点击开发者文档了解合作方式。地址：https://doc.fastadmin.net/developer

我们准备了一篇插件开发简明教程，请点击这里查看

---

## 插件配置 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/1864.html

**Contents:**
- 插件配置
  - 配置信息
  - 伪静态
  - 温馨提示

请参考开发者文档配置章节：https://doc.fastadmin.net/developer/80.html

请参考开发者文档伪静态章节：https://doc.fastadmin.net/developer/98.html

1、因默认插件系统是按照应用插件标识字母升序排序伪静态优先级，如果存在多个应用插件伪静态时，如需要调整伪静态的优先级，需要手动修改application/extra/addons.php中的priority值，如：

则表示cms的伪静态规则优先于ask的伪静态规则，应用插件标识字母可以在应用插件介绍页应用信息或插件信息查看。2、application/extra/addons.php中的domain配置值用于配置当某应用或插件未绑定二级域名时所默认使用的默认二级域名，该值只有当启用url_domain_deploy为true时才生效。3、请在修改应用插件的绑定域名或伪静态配置后，务必在后台右上角清除缓存，否则可能导致伪静态不生效。

**Examples:**

Example 1 (scala):
```scala
'priority' => ['cms', 'ask'],
```

---

## 数据库 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/docs/database.html

**Contents:**
- 数据库
- 根据字段类型
- 特殊字段
- 以特殊字符结尾的规则
- 注释说明
- 常见问题

这里提供的是数据库表字段规则在你创建表时使用，当按如下的规则进行字段命名、类型设置和备注时使用php think crud -t 表名生成CRUD时会自动生成对应的控制器、模型、视图、JS等。

---

## 文件上传 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/177.html

**Contents:**
- 文件上传
- 上传配置
  - 文件名规则
  - 上传示例
  - 按钮属性
  - 上传按钮事件回调
- 直接上传
- 分片上传
- 上传成功后归类
- 自定义上传预览

FastAdmin开发框架支持将文件、图片、视频、压缩包等文件快速的上传至本地服务器或云存储，同时支持云存储直传模式和服务器进行中转模式。你可以直接在后台插件管理安装第三方云存储的插件后使用，目前支持以下云存储平台：

从FastAdmin 1.2.0版本开始，所有云存储均已适配分片上传功能FastAdmin只支持启用一个云存储插件，请勿同时启用多个云存储插件

FastAdmin开发框架的上传功能非常强大，我们只需要简单的配置即可支持单图或多图上传。

如果我们未启用云存储插件，此时上传读取的是application/extra/upload.php这个配置文件。

如果安装了云存储插件并启用，则相关配置请在后台插件管理，对应的云存储配置中进行设置。如果安装了云存储插件并启用，则所有的文件都将上传至云存储，如果需要上传到本地服务器，请给按钮添加data-url="ajax/upload"属性不支持同时启用多个云存储插件，只允许启用一个云存储插件mimetype如配置允许 pdf,ppt,docx,svg 等可能含有脚本的文件时，请先从服务器配置此类文件直接下载而不是预览

文件保存文件名savekey支持替换的变量如下：

如在savekey中使用了{filemd5}，上传超大文件时可能导致前端MD5计算耗时过长

我们可以看到这里配置了一个文本框、一个上传按钮、一个选择按钮和一个预览的DIV

如果我们想直接通过JS上传一个文件到我们的服务器(支持云存储插件)，我们可以在JS中使用

来上传文件，注意仅适用于在FastAdmin框架前端标准模块对应的JS中调用。

从FastAdmin 1.2.0版本开始已经支持分片上传，如果需要启用分片上传，必须客户端和服务端同时开启。首先找到application/extra/upload.php，修改其中的chunking值为true。其次给按钮添加data-chunking=true属性即可，如果提示文件过大，可以再添加data-maxsize="1024M"来控制允许上传的文件大小。

1、因为FastAdmin 框架不支持断点续传，如果采用分片上传大文件时，如果受网络波动影响，有其中一片上传错误，会导致整个文件上传失败，建议使用第三方工具进行上传超大文件。2、分片上传不支持富文本编辑器内的上传。

从FastAdmin 1.2.1版本开始已经支持上传成功后归类功能，我们可以通过给上传按钮添加data-params='{"category":"category2"}'来实现，这个即是上传归类到category2，这个category2可以在常规管理->系统配置->字典配置中添加修改

FastAdmin中的上传组件，默认只支持预览图片预览，当判断到不是图片时会使用对应的文件后缀进行预览，如果需要使用自定义上传预览，可以参考以下方法进行实现。首先请参考上方的上传示例代码，我们给预览区域<ul class="row list-inline faupload-preview" id="p-avatar"></ul>添加一个data-template的属性

然后在页面底部添加一个avatartpl的自定义模板，如：

这其中的data-template的值对应我们自定义模板ID的值，自定义模板中支持的变量如下：

当我们在大文件上传时(文件大小超过2M)，除了可以采用上方的分片上传以外，还可以通过修改服务器的配置来实现大文件上传。大文件上传时通常涉及到插件配置/本地配置/PHP配置/Nginx配置四处地方需要修改。1、如果有安装云存储插件，首先请在后台插件管理修改云存储插件->配置中的最大可上传配置值。2、然后修改 application/extra/upload.php 里的 maxsize的值。3、接着修改PHP上传限制，修改你服务器运行环境的 php.ini 里的 max_execution_time=300、upload_max_filesize=100M、post_max_size=100M三个配置值。4、如果使用Nginx 还需要修改Nginx的配置client_max_body_size 100M;5、修改配置后务必重启Web服务和清浏览器缓存。6、如果有使用CDN分布式部署或负载均衡，还需检查你的云服务提供商是否有上传大小限制。

如果我们希望在不同页面使用不同的上传配置，可以参考以下方法。在当前控制器添加_initialize方法，如已有则按需要修改添加\think\Config::set('upload.mimetype', 'zip,rar');

1、动态配置仅适用于本地上传，如果有安装插件市场云存储插件则不适用2、upload.mimetype的配置仅用于前端限制文件的选择，服务端验证时仍然会以application/extra.php中限制的文件后缀为准。3、如果前端上传按钮使用了data-mimetype，则动态配置无效

1、动态配置仅适用于本地上传，如果有安装插件市场云存储插件则不适用2、upload.mimetype的配置仅用于前端限制文件的选择，服务端验证时仍然会以application/extra.php中限制的文件后缀为准。3、如果前端上传按钮使用了data-mimetype，则动态配置无效

请参考文档：https://doc.fastadmin.net/doc/frontend.html#toc-6

1、如果是动态生成的上传按钮，需要使用Form.events.faupload(表单);绑定事件2、即使设置了分片上传，也只有当上传的文件超过设置的单一分片文件大小时才会启用分片上传。3、从FastAdmin 1.2.0开始，前端上传默认超时为600000毫秒，也就是10分钟，如上传超大文件，请给上传按钮添加data-upload-options='{"timeout":1800000}'设定为30分钟超时。4、如果安装了云存储插件，上传没有生效，请尝试清空浏览器缓存。5、如果遇到上传大文件失败，请参考https://ask.fastadmin.net/question/26919.html 进行修改服务器的限制。6、如果安装了云存储插件并启用，则所有的文件都将上传至云存储，如果仍需要上传文件到本地服务器，请给按钮添加data-url="ajax/upload"属性7、由于FastAdmin中多图(多文件)使用,作为分隔符处理，因此不支持单个文件(图片)URL中使用,，这种情况常见于云存储图片自定义处理，建议云存储图片处理时采用自定义样式来避免使用到,的情况。

**Examples:**

Example 1 (html):
```html
<div class="form-group">
    <label for="c-avatar" class="control-label col-xs-12 col-sm-2">头像:</label>
    <div class="col-xs-12 col-sm-8">
        <div class="input-group">
            <input id="c-avatar" data-rule="" class="form-control" size="50" name="row[avatar]" type="text" value="{$row.avatar}">
            <div class="input-group-addon no-border no-padding">
                <span><button type="button" id="faupload-avatar" class="btn btn-danger faupload" data-input-id="c-avatar" data-mimetype="image/gif,image/jpeg,image/png,image/jpg,image/bmp" data-multiple="false" data-preview-id="p-avatar"><i class="fa fa-upload"></i> 上传</button></span>
                <span><button type="button" id="fachoose-avatar" class="btn btn-primary fachoose" data-input-id="c-avatar" data-mimetype="image/*" data-multiple="false"><i class="fa fa-list"></i> 选择</button></span>
            </div>
            <span class="msg-box n-right" for="c-avatar"></span>
        </div>
        <ul class="row list-inline faupload-preview" id="p-avatar"></ul>
    </div>
</div>
```

Example 2 (javascript):
```javascript
require(['upload'], function(Upload){
    //fileInput为你的文件选择框，file为文件流，file也可以在fileInput的change事件中通过e.originalEvent.target.files[0];获取
    var fileInput = $('#fileInput')[0];
    var file = fileInput.files[0];
    Upload.api.send(file, function(data, ret, up, file){
        // 上传成功的回调
        // 其中data.url为文件URL的链接、data.fullurl为完整URL链接
    }, function(data, ret, up, file){
        // 上传失败的回调
    });
});
```

Example 3 (jsx):
```jsx
<ul class="row list-inline faupload-preview" id="p-avatar" data-template="avatartpl"></ul>
```

Example 4 (sass):
```sass
<script type="text/html" id="avatartpl">
    <li class="col-xs-3">
        <a href="<%=fullurl%>" data-url="<%=url%>" target="_blank" class="thumbnail">
            <img src="<%=fullurl%>" class="img-responsive">
        </a>
        <a href="javascript:;" class="btn btn-danger btn-xs btn-trash"><i class="fa fa-trash"></i></a>
    </li>
</script>
```

---

## 方法 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/192.html

**Contents:**
- 方法

使用方法的语法：$('#table').bootstrapTable('method', parameter);。

---

## 日期时间 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/181.html

**Contents:**
- 日期时间
  - 常用属性
  - 事件捕获
  - 手动渲染

在FastAdmin中的日期时间组件采用的是Bootstrap-datetimepicker插件

我们在使用时可以为文本框添加一个class为datetimepicker的值即可自动添加日期时间选择框。

同时我们还可以通过配置以下属性来自定义我们日期选择器的功能

如果你需要捕获元素值变更后的事件，可以通过以下方式来实现，如：

如果你的HTML是异步渲染，可能导致日期时间组件无法正常渲染，此时我们需要进行手动渲染，如下：

**Examples:**

Example 1 (r):
```r
$("#c-createtime").on("dp.change", function(){
    //回调事件
});
```

Example 2 (javascript):
```javascript
require(['bootstrap-datetimepicker'], function () {
    var options = {
        format: 'YYYY-MM-DD HH:mm:ss',
        icons: {
            time: 'fa fa-clock-o',
            date: 'fa fa-calendar',
            up: 'fa fa-chevron-up',
            down: 'fa fa-chevron-down',
            previous: 'fa fa-chevron-left',
            next: 'fa fa-chevron-right',
            today: 'fa fa-history',
            clear: 'fa fa-trash',
            close: 'fa fa-remove'
        },
        showTodayButton: true,
        showClose: true
    };

    var form = $("日期时间组件所在的父元素选择器");
    $('.datetimepicker', form).parent().css('position', 'relative');
    $('.datetimepicker', form).datetimepicker(options).on('dp.change', function (e) {
        $(this, document).trigger("changed");
    });
});
```

---

## 日期时间区间 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/736.html

**Contents:**
- 日期时间区间
  - 使用示例
  - 常用属性
  - 事件捕获

在FastAdmin中的日期时间区间组件采用的是Bootstrap-daterangepicker插件

我们在使用只可以为文本框添加一个class为datetimerange的值即可自动添加日期时间区间选择框。

同时我们还可以通过配置以下属性来自定义我们日期选择器的功能

如果你需要捕获元素值变更后的事件，可以通过以下方式来实现，如：

**Examples:**

Example 1 (json):
```json
<input type="text" class="form-control datetimerange" placeholder="指定日期时间" />

<input type="text" class="form-control datetimerange" placeholder="指定日期时间" value="2021-03-30 00:00:00 - 2021-03-30 23:59:59" />

<input type="text" class="form-control datetimerange" data-locale='{"format":"YYYY-MM-DD"}' placeholder="指定日期" value="2021-03-30 - 2021-03-30" />
```

Example 2 (r):
```r
$("#c-createtime").on("blur", function(){
    //回调事件
});
```

---

## 服务器安全 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/171.html

**Contents:**
- 服务器安全
  - 操作系统安全
  - 目录安全
  - WEB配置
  - 下载配置
  - 运行配置

服务器安全涉及操作系统安全、目录安全、站点配置和运行配置等多个方面。

生产用的操作系统强烈推荐使用 LTS 版本，留意操作系统的更新，并定期更新操作系统。

在实际生产中，目录安全是比较容易被忽略的配置，因此我们更应该加倍注意防范，以免造成不必要的损失。

首先我们建议在生产环境只开放uploads和runtime目录的读写权限，其次还需要关闭uploads目录执行PHP脚本的权限，假设时服务端uploads目录有读写权限且有PHP的脚本执行权限，那么当有恶意脚本被上传到这个目录并被执行时，会导致服务器数据泄漏或恶意修改，从而造成损失。

为避免不必要的损失，在生产环境下建议使用以下命令进行目录权限设置

通过以上的目录权限配置还不够，我们还需要继续对服务器做WEB配置，以限制PHP脚本的运行

Nginx可以通过以下配置禁止PHP脚本执行

Apache可以通过在.htaccess中配置来禁用PHP脚本执行

其次在新增网站配置时务必绑定public目录为运行目录，同时启用open_basedir限制只允许FastAdmin的根目录，例如：fastcgi_param PHP_VALUE "open_basedir=/var/www/fastadmin/:/tmp/:/proc/";

通常也建议修改php.ini，禁用不安全的函数，配置如disable_functions = passthru,exec,system,chroot,chgrp,chown,shell_exec,proc_open,proc_get_status,popen,ini_alter,ini_restore,dl,openlog,syslog,readlink,symlink,popepassthru

默认我们在请求txt/doc/pdf/ppt等类型的文件时会在浏览器进行渲染，为了安全，强烈建议当请求此类文件时进行下载而不是预览，我们可以按以下方法进行修改服务器配置来实现。

Nginx可以修改配置文件(宝塔面板可直接在面板伪静态中添加)

Apache可以通过修改public/.htaccess配置来实现

首先打开application/config.php，做以下几项配置

其次前台开启全局过滤，早期FastAdmin版本并未开启全局过滤。你也可以检查下你的代码。请手动修改以下代码：

注意修改其中的$this->request->filter过滤代码，可以修改成：

同时也可以参考https://ask.fastadmin.net/article/7534.html 设置全局 HtmlPurifier 安全过滤

最后务必修改后台管理入口，新版 FastAdmin 会随机生成后台入口，可以自定义修改后台入口文件，但请勿将入口改为容易被猜测到的入口文件，以后可以安全的从我们自定义的后台入口进行登录。

**Examples:**

Example 1 (sass):
```sass
chown www:www /var/www/yoursite -R
chmod 555 /var/www/yoursite -R
chmod u+w /var/www/yoursite/runtime -R
chmod u+w /var/www/yoursite/public/uploads -R
```

Example 2 (unknown):
```unknown
location ~ ^/(uploads|assets)/.*\.(php|php5|jsp)$ {
    deny all;
}
```

Example 3 (unknown):
```unknown
RewriteEngine on RewriteCond % !^$
RewriteRule uploads/(.*).(php)$ – [F]
```

Example 4 (jsx):
```jsx
<Directory "/www/yoursite/public/uploads">
  <Files ~ ".php">
      Order allow,deny
      Deny from all
  </Files>
</Directory>
```

---

## 架构 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/construct.html

**Contents:**
- 架构
- 架构总览
- 目录结构
- 应用模块
- 功能模块

FastAdmin基于MVC的设计模式，将我们的应用分为三层（模型M、视图V、控制器C）。

FastAdmin目录结构遵循ThinkPHP5官方建议的模块设计：

在FastAdmin中默认有四个应用模块：common、admin、index、api，你也可以扩展开发自己的应用模块。

后台模块(admin)是FastAdmin中的核心模块，后台模块又分为系统配置、附件管理、插件管理等多个功能模块，更多的功能模块可以在插件管理中自由的安装和卸载。

后台的前端是基于AdminLTE和Bootstrap进行了大量二次开发，采用RequireJS进行JS模块化管理和加载。

前台模块(index)的结构和后台功能类似，具体请参考后台模块的章节。

公共模块(common)是一个特殊的模块，默认是禁止直接访问的，一般用于放置一些公共的类或其它模块的继承基类等。

Api 模块(api)通常用于对接APP或小程序，用于向APP或小程序提供接口，具体 api 代码编写可以直接参考ThinkPHP5官方的文档，api 文档可以通过命令行生成，详细请参看 一键生成API文档 章节。

功能模块指后台管理中的功能模块，比如我们的系统配置、附件管理、分类管理（分类管理在新版中默认隐藏，可自行在权限管理中打开）。

后台开发的每一个功能模块都是基于MVC的设计模式进行开发 。在FastAdmin中，我们提供了一键生成CRUD的功能，这个一键生成CRUD生成的文件也就是我们标准的MVC文件。

在FastAdmin中每一个功能模块至少对应一个功能模块JS文件，也就是说每一个控制器都对应一个同名的JS文件，其次每一个控制器的方法对应JS文件中同名的方法。

具体控制器详细介绍可参考控制器章节，JS的部分可以参考前端章节。

**Examples:**

Example 1 (unknown):
```unknown
FastAdmin项目目录
├── addons                  //插件存放目录
├── application             //应用目录
│   ├── admin               //后台管理应用模块
│   ├── api                 //API应用模块
│   ├── common              //通用应用模块
│   ├── extra               //扩展配置目录
│   ├── index               //前台应用模块
│   ├── build.php
│   ├── command.php         //命令行配置
│   ├── common.php          //通用辅助函数
│   ├── config.php          //基础配置
│   ├── database.php        //数据库配置
│   ├── route.php           //路由配置
│   ├── tags.php            //行为配置
├── extend
│   └── fast                //FastAdmin扩展辅助类目录
├── public                  //框架入口目录
│   ├── assets
│   │   ├── addons         //插件前端资源目录
│   │   ├── build           //打包JS、CSS的资源目录
│   │   ├── css             //CSS样式目录
│   │   ├── fonts           //字体目录
│   │   ├── img             //图片资源目录
│   │   ├── js
│   │   │   ├── backend     //后台功能模块JS文件存放目录
│   │   │   └── frontend    //前台功能模块JS文件存放目录
│   │   ├── libs            //Bower资源包位置（只读，通过 bower 更新）
│   │   └── less            //Less资源目录
│   └── uploads             //上传文件目录
│   ├── index.php           //应用入口主文件
│   ├── install.php         //FastAdmin安装引导（安装完成后会自动删除）
│   ├── admin.php           //后台入口文件(自动安装后会被修改为随机文件名）
│   ├── robots.txt
│   └── router.php
├── runtime                 //缓存目录
├── thinkphp                //ThinkPHP框架核心目录（只读，通过 composer 更新）
├── vendor                  //Compposer资源包位置（只读，通过 composer 更新）
├── .bowerrc                //Bower目录配置文件
├── .env.sample             //环境配置模板（可复制一份为 .env 生效）
├── LICENSE
├── README.md               //项目介绍
├── bower.json              //Bower前端包配置
├── build.php
├── composer.json           //Composer包配置
└── think                   //命令行控制台入口（使用 php think 命令进入）
```

Example 2 (unknown):
```unknown
├── application
│   └── admin
│       ├── controller
│       │   └── Test.php                //控制器类
│       ├── lang
│       │   └─ zh-cn
│       │       └── test.php            //功能语言包，按需加载
│       ├── model
│       │   └── Test.php                //模型类
│       ├── validate
│       │   └── Test.php                //验证器类
│       └── view
│           └── test
│               ├── index.html           //列表视图
│               ├── add.html              //添加视图
│               ├── edit.html              //编辑视图
│               └── recyclebin.html     //回收站视图
└── public
    └── assets
        └── js
            └── backend
                └── test.js             //功能模块JS文件
```

---

## 标签输入 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/1207.html

**Contents:**
- 标签输入
  - 使用示例
  - 常用属性
  - 方法和事件
  - 动态下拉提示
  - 特别感谢

标签输入组件可用于快速的为文本框添加标签输入功能，目前在FastAdmin1.3.0+版本支持该功能。

该组件基于Bootstrap-tagsinput进行二次开发，除了动态获取typeahead配置不同外，其余属性均相同，因此可直接查询Bootstrap-tagsinput的文档：http://bootstrap-tagsinput.github.io/bootstrap-tagsinput/examples/

以上为常用属性，更多属性请参考Bootstrap-tagsinput文档

请直接参考Bootstrap-tagsinput的文档：http://bootstrap-tagsinput.github.io/bootstrap-tagsinput/examples/

原生的Bootstrap-tagsinput是需要配合typeahead来实现，但是在FastAdmin中是需要配合自动完成(Autocomplete)组件来实现。

我们只需要传递autocomplete属性即可，其中url为数据源地址。

数据源的格式我们可以参考左侧自动完成(Autocomplete)组件章节的文档。

Bootstrap-tagsinput：https://github.com/bootstrap-tagsinput/bootstrap-tagsinput

**Examples:**

Example 1 (html):
```html
<!--常规渲染-->
<input type="text" class="form-control" data-role='tagsinput' />
<!--设定默认值-->
<input type="text" class="form-control" data-role='tagsinput' value="你好,世界" />
<!--自定义属性-->
<input type="text" class="form-control" data-role='tagsinput' value="你好,世界" data-tagsinput-options='{"maxTags":4, "trimValue":true}' />
```

Example 2 (json):
```json
$("#test1").data("tagsinput-options", {
    "maxTags":4, 
    "trimValue":true,
    "onTagExists":function(){
        //处理回调事件
    }
});
```

Example 3 (json):
```json
<input type="text" class="form-control" data-role='tagsinput' data-tagsinput-options='{"autocomplete":{"url":"/index/ajax/autocomplete"}}' />
```

---

## 格式化 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/195.html

**Contents:**
- 格式化
  - 格式化方法
- 自定义格式化方法
- 按钮组配置

在表格初始化的字段列配置中我们通常可以看到以下的代码

其中formatter有以下可配置的方法，用好以下的渲染方法可以让你的开发更加便捷。

如果框架自带的格式化不满足的使用，可以使用自定义的格式化方法，格式如下：

buttons按钮组配置支持使用数组，格式如下：

**Examples:**

Example 1 (json):
```json
table.bootstrapTable({
    url: $.fn.bootstrapTable.defaults.extend.index_url,
    columns: [
        [
            {checkbox: true},
            {field: 'id', title: __('Id')},
            {field: 'type', title: __('Type'), operate: false, searchList: Config.searchList, formatter: Table.api.formatter.normal},
            {field: 'name', title: __('Name'), align: 'left'},
            {field: 'nickname', title: __('Nickname')},
            {field: 'intro', title: __('Intro'), formatter: Table.api.formatter.content, class: 'autocontent', hover:true},
            {field: 'flag', title: __('Flag'), formatter: Table.api.formatter.flag},
            {field: 'image', title: __('Image'), operate: false, events: Table.api.events.image, formatter: Table.api.formatter.image},
            {field: 'weigh', title: __('Weigh')},
            {field: 'status', title: __('Status'), operate: false, formatter: Table.api.formatter.status},
            {field: 'operate', title: __('Operate'), table: table, events: Table.api.events.operate, formatter: Table.api.formatter.operate}
        ]
    ]
});
```

Example 2 (json):
```json
table.bootstrapTable({
    url: $.fn.bootstrapTable.defaults.extend.index_url,
    columns: [
        [
            {checkbox: true},
            {field: 'id', title: __('Id')},
            {field: 'intro', title: __('Intro'), formatter: function(value, row, index) {
                //value：intro字段的值，在开启escape时，value值已经自动做转义处理
                //row：当前行所有原始字段的数据，注意row下的所有数据均未做转义处理，需自行做好转义处理
                //index：当前行索引
                //示例：
                return value + " - " + parseInt(row.id);
            }
        ]
    ]
});
```

Example 3 (sass):
```sass
buttons: [
    {
        name: 'add', //唯一标识、权限标识
        dropdown: '', //按钮下拉分组，默认为不分组
        text: '同意', //按钮显示的文字，支持function
        title: '我是标题', //按钮显示的文字，支持function
        classname: 'btn btn-info btn-xs btn-dialog', //按钮的class，支持btn-dialog/btn-ajax/btn-addtabs
        icon: 'fa fa-plus', //按钮的图标
        url: 'department/index/add/parent_id/{ids}', //按钮的链接，支持使用{字段名}来占位替换，支持function
        confirm: '是否同意该请求？', //点击按钮后的确认框，支持function
        refresh: true, //操作完成后是否刷新列表
        disable: function(row){}, //判断按钮是否禁用，支持function
        visible: function(row){}, //判断按钮是否可见，支持function
        hidden: function(row){}, //判断按钮是否隐藏，支持function
        extend: '', //扩展的扩展属性，FastAdmin1.4.0+支持function
    },
    {
        ...
    }
]
```

---

## 框架 env 变量配置 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/2483.html

**Contents:**
- 框架 env 变量配置
- 使用 env 的好处
- 启用 env
- 默认支持 的 env 键

FastAdmin 框架提供了对 .env 环境变量配置的支持，并附带一个默认示例文件 .env.sample。在安装后，框架并不会自动启用 env 环境变量，需要手动将 .env.sample 复制为 .env 并进行配置。

在 Linux 环境下，可通过以下命令快速完成复制并生效：

然后使用文本编辑器打开 .env 文件进行配置。

启用了 .env 后，.env 文件中的配置将覆盖框架中其他地方的相应配置，确保了配置的一致性。这种方式为项目提供了更大的灵活性和可维护性。

**Examples:**

Example 1 (bash):
```bash
cp .env.sample .env
```

Example 2 (json):
```json
[app]
;是否开启Debug调试
debug = false
;是否开启Trace调试
trace = false

[database]
hostname = 数据库连接地址
database = 数据库名
username = 数据库连接用户名
password = 数据库连接密码
hostport = 数据库连接端口
charset = 数据库连接编码
prefix = 数据库表前缀
;是否开启数据库调试
debug = false
```

---

## 框架默认配置 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/2484.html

**Contents:**
- 框架默认配置

框架默认的配置在 application/config.php 内。

以下为 FastAdmin v1.x 的默认配置。

https://gitee.com/karson/fastadmin/blob/1.x/application/config.php

---

## 模块 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/module.html

**Contents:**
- 模块

FastAdmin中模块总共由四大部分组成，分别是前台、API、后台、公共模块组成。

后台模块 前台模块 API 模块 公共模块

---

## 目录结构 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/173.html

**Contents:**
- 目录结构

FastAdmin中每一个应用插件都是一个独立的插件目录，所有的应用插件都是存放在项目目录中的addons目录下。

其中的application和public文件夹会覆盖到根目录，这两个文件夹主要用于我们后台管理功能的开发，我们可以先在后台开发好对应的管理功能后，再将对应的功能打包进插件即可，FastAdmin在插件安装和卸载时会自动进行文件冲突检测，如果遇到冲突的文件会提醒用户是否进行覆盖或删除。

assets这个文件夹很关键，FastAdmin会将assets中的所有文件夹和文件复制到/public/assets/addons/blog/文件夹中去，这个blog即是我们的插件目录名称，assets文件夹中的所有文件不会进行文件冲突检测，/public/assets/addons/blog/这个目录下的文件，我们在视图文件中可以直接通过__ADDON__指向这个路径。因此在开发视图时我们可以先使用相对路径设计，完成后我们再统一加上这个__ADDON__的前缀

controller、lang、model和view这四个文件夹是我们插件前台功能的MVC部分，这部分文件夹不会复制或移动到其它位置。

Blog.php这个文件是插件的核心文件，我们可以在这个文件中编写插件安装或卸载时执行的脚本，或者在此插件中编写菜单的生成或删除，同时插件的行为方法也是编写在此文件中的，插件所支持的行为事件会在后面讲到。此文件规则为插件目录名称首字母大写。

bootstrap.js这个文件是插件的启动文件，插件在安装完启用后，FastAdmin会将此文件中的内容合并到/public/assets/js/addons.js中去，你可以在此编写插件核心JS或注册事件，在此JS中可以使用require依赖其它模块。同时在此插件中可以使用Fast、Backend、Lang等全局对象，因为在此之前此类对象已经加载且注册。

config.html这个文件是插件配置的模板文件，我们在后台插件管理中点配置按钮时会调用该模板文件进行渲染，如果不存在该模板文件，将调用框架自带的配置模板进行渲染。

config.php这个文件是插件的配置文件，我们在后台插件管理中点配置按钮时会保存在此文件，此文件的内容格式为：

config.php中的值在FastAdmin任何地方均可使用get_addon_config('blog')来获取配置值

info.ini这个文件仅用于保存插件基础信息和开启状态，此文件的内容格式为

注意这个name是插件的唯一标识，不能和现在的插件冲突，其次注意下这个name值，如果我们有涉及到数据库，那个表的前缀也必须是__PREFIX__标识名开头。比如我们下面的__PREFIX__blog_category。

install.sql 这个文件中只能是SQL语句，同时在此文件中可以使用__PREFIX__表示数据库表前缀，FastAdmin在安装导入SQL时自动进行替换。此文件的内容格式为

**Examples:**

Example 1 (unknown):
```unknown
blog
├── application    //此文件夹中所有文件会覆盖到根目录的/application文件夹
├── assets        //此文件夹中所有文件会复制到/public/assets/addons/blog文件夹
├── controller    //此文件夹为插件控制器目录
├── lang            //此文件夹为插件语言包目录
├── model            //此文件夹为插件模型目录
├── public        //此文件夹中所有文件会覆盖到根目录的/public文件夹
├── view            //此文件夹为插件视图目录
├── Blog.php        //此文件为插件核心安装卸载控制器,必需存在
├── bootstrap.js    //此文件为插件JS启动文件
├── LICENSE        //版权文件
├── config.php    //插件配置文件,我们在后台插件管理中点配置按钮时配置的文件,必需存在
├── config.html    //插件配置模板文件,我们在后台插件管理中点配置按钮时会调用此模板文件，可选
├── info.ini        //插件信息文件,用于保存插件基本信息，插件开启状态等,必需存在
└── install.sql    //插件数据库安装文件,此文件仅在插件安装时会进行导入
```

Example 2 (php):
```php
<?php

return [
    [
        //配置名称,该值在当前数组配置中确保唯一
        'name'    => 'yourname',
        //配置标题
        'title'   => '配置标题',
        //配置类型,支持string/text/number/datetime/array/select/selects/image/images/file/files/checkbox/radio/bool
        'group'    => '分组一', //配置分组，只支持FastAdmin1.3.3+
        'visible'    => '配置名=验证值', //可视条件，只有满足条件该配置才会显示，只支持FastAdmin1.3.3+
        'type'    => 'string',
        //配置select/selects/checkbox/radio/bool时显示的列表项
        'content' => [
            '1' => '显示',
            '0' => '不显示'
        ],
        //配置值
        'value'   => '1',
        //配置验证规则,更多规则可参考nice-validator文件
        'rule'    => 'required',
        'msg'     => '验证失败提示文字',
        'tip'     => '字段填写帮助',
        'ok'      => '验证成功提示文字'
    ],
    [
        'name'    => 'yourname2',
        'title'   => '配置标题2',
        'group'    => '分组二', //配置分组，只支持FastAdmin1.3.3+
        'type'    => 'radio',
        'options' => [
            '1' => '显示',
            '0' => '不显示'
        ],
        'value'   => '1',
        'rule'    => 'required',
        'msg'     => '验证失败提示文字',
        'tip'     => '字段填写帮助',
        'ok'      => '验证成功提示文字'
    ],
    [
        'name'    => '__tips__',
        'title'   => '温馨提示',
        'type'    => 'string',
        'content' =>
            array(),
        'value'   => '该提示将出现的插件配置头部，通常用于提示和说明',
        'rule'    => '',
        'msg'     => '',
        'tip'     => '',
        'ok'      => '',
        'extend'  => '',
    ],
];
```

Example 3 (unknown):
```unknown
name = blog
title = 博客插件
intro = 响应式博客插件，包含日志、评论、分类、归档等
author = FastAdmin
website = https://www.fastadmin.net
version = 1.0.0
state = 1
```

Example 4 (sql):
```sql
#我们在创建数据库时建议加上IF NOT EXISTS
CREATE TABLE IF NOT EXISTS `__PREFIX__blog_category` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `pid` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '父分类ID',
  `name` varchar(30) NOT NULL DEFAULT '' COMMENT '分类名称',
  `nickname` varchar(50) NOT NULL DEFAULT '' COMMENT '分类昵称',
  `flag` set('hot','index','recommend') NOT NULL DEFAULT '' COMMENT '分类标志',
  `image` varchar(100) NOT NULL DEFAULT '' COMMENT '图片',
  `keywords` varchar(255) NOT NULL DEFAULT '' COMMENT '关键字',
  `description` varchar(255) NOT NULL DEFAULT '' COMMENT '描述',
  `diyname` varchar(30) NOT NULL DEFAULT '' COMMENT '自定义名称',
  `createtime` bigint(16) unsigned DEFAULT NULL COMMENT '创建时间',
  `updatetime` bigint(16) unsigned DEFAULT NULL COMMENT '更新时间',
  `weigh` int(10) NOT NULL DEFAULT '0' COMMENT '权重',
  `status` varchar(30) NOT NULL DEFAULT '' COMMENT '状态',
  PRIMARY KEY (`id`),
  KEY `weigh` (`weigh`,`id`),
  KEY `pid` (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4_general_ci COMMENT='博客分类表';

INSERT INTO `__PREFIX__blog_category` VALUES ('1', '0', '默认分类', 'default', '', '/assets/img/qrcode.png', '', '', '', '1502112587', '1502112587', '0', 'normal');
```

---

## 自动完成(Autocomplete) - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/1206.html

**Contents:**
- 自动完成(Autocomplete)
  - 使用示例
  - 常用属性
  - Ajax返回值
  - 整合标签输入
  - 特别感谢

自动完成组件可用于快速的为文本框添加Autocomplete功能，目前在FastAdmin1.3.0+版本支持该功能。

同时我们还可以通过配置data-autocomplete-options属性来自定义Autocomplete的功能data-autocomplete-options支持以下属性配置：

Ajax返回值必须是JSON类型，格式如下：

Autocomplete组件还可以与标签输入无缝整合，实现标签输入的自动提示，具体请参考标签输入章节文档

Autocomplete组件使用开源组件：https://github.com/devbridge/jQuery-Autocomplete

**Examples:**

Example 1 (json):
```json
<input type="text" class="form-control" data-role="autocomplete" data-autocomplete-options='{"url":"ajax/get_user_list"}' />

<input type="text" class="form-control" data-role="autocomplete" data-autocomplete-options='{"url":"ajax/get_user_list", "minChars":2}' />
```

Example 2 (json):
```json
$("#test1").data("autocomplete-options", {
    "url":"ajax/get_user_list", 
    "minChars":2,
    "onSelect":function(){
        //处理回调事件
    },
    "params": function(){
        //动态传递参数
        return {"a":1,"b":2};
    }
});
```

Example 3 (json):
```json
{
    "query": "iPhone",
    "suggestions": [
        { "value": "iPhone 11", "data": "iphone11" },
        { "value": "iPhone 12",       "data": "iphone12" },
        { "value": "iPhone XR",        "data": "iphonexr" }
    ]
}
```

Example 4 (json):
```json
{
    "query": "iPhone",
    "suggestions": ["iphone11", "iphone12", "iphone13"]
}
```

---

## 行为事件 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/174.html

**Contents:**
- 行为事件

FastAdmin中的行为支持ThinkPHP5的所有行为，同时FastAdmin自定义部分专属的行为事件，以下是所有所支持的行为事件。

使用行为时在Blog.php中添加上对应的方法，FastAdmin在安装时、禁用、启用即可自动注册行为。但一定请注意在Blog.php中编写行为方法是使用的是驼峰式规则，例如upload_after，方法名则为uploadAfter，如果方法名使用upload_after则不会注册成功。

至此，FastAdmin插件开发所涉及到的文件和文件夹已经介绍完了，如果有疑问，请及时在问答社区反馈。

---

## 表单验证 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/179.html

**Contents:**
- 表单验证
  - 常规示例
  - 常用规则
  - 自定义规则
  - 忽略验证
  - 温馨提示

FastAdmin的表单验证采用的是Nice-validator验证插件，Nice-validator是一款非常强大的表单验证插件，通过简单在元素上配置规则，即可达到验证的效果。

在FastAdmin当中我们只需要给元素添加data-rule="规则"即可开启Nice-validator的验证，如下：

如果常用规则不满足我们的需求，我们可以采用自定义规则来实现，如下：

然后我们在JS中定义规则的实现方法，如下：

然后我们需要在服务端控制器的check方法返回

因为引入了Nice-validator后会对所有表单的所有元素进行验证，如果你的表单不希望使用Nice-validator组件进行验证，可以给form添加一个novalidate属性即可，如

同时如果JS中有使用Form.api.bindevent($("form[role=form]"));，也需要将该行移除。

**Examples:**

Example 1 (html):
```html
<input id="c-title" class="form-control" data-rule="required;username" name="row[title]" type="text" value="" />
```

Example 2 (html):
```html
<input id="c-title" class="form-control" data-rule="required;diyname" name="row[title]" type="text" value="" />
```

Example 3 (css):
```css
$.validator.config({
    rules: {
        diyname: function (element) {
            //如果直接返回文本，则表示失败的提示文字
            //如果返回true表示成功
            //如果返回Ajax对象则表示远程验证
            if (element.value.toString().match(/^\d+$/)) {
                return '不能为纯数字';
            }
            if (!element.value.toString().match(/^[a-zA-Z0-9\-_]+$/)) {
                return '请输入字母或数字组合';
            }
            return $.ajax({
                url: 'ajax/check',
                type: 'POST',
                data: {id: $("#c-title").val(), name: element.name, value: element.value},
                dataType: 'json'
            });
        }
    }
});
```

Example 4 (php):
```php
$result = "验证结果";
if ($result) {
    //失败
    $this->error("用户名已经存在");
} else {
    //成功
    $this->success();
}
```

---

## 表格 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/table.html

**Contents:**
- 表格
- 一张图解析FastAdmin中表格列表的功能

FastAdmin中的表格列表使用的是早期Bootstrap-table版本，版本号为1.11.1，FastAdmin官方对其进行了二次开发，新增了page-jumpto跳转插件，以及修改了在多维数组下events传参错误的BUG。

实例化 表格参数 列参数 方法 多语言 事件 格式化 依赖 Table对象

因为Bootstrap-table官方已经是1.18.1+版本了，因此Bootstrap-table官方的文档已经不再适用于FastAdmin中使用的Bootstrap-table，如需要查看Bootstrap-table文档，请直接查看旧版本文档：https://gitee.com/F4NNIU/bootstrap-table-home 。

因为Bootstrap-Table功能较多，FastAdmin特地制作了一张图来解析表格列表中的功能，建议对照截图来寻找匹配的功能。链接：https://ask.fastadmin.net/article/323.html 。

---

## 表格参数 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/190.html

**Contents:**
- 表格参数

表格的参数定义在 jQuery.fn.bootstrapTable.defaults，我们在上一章节实例化表格时可以配置以下参数。

---

## 贡献代码 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/2482.html

**Contents:**
- 贡献代码
- 开源仓库
- 开始之前
- 安装工具
- 首次配置
- 操作流程
- FastAdmin 开源贡献者名单
- 报告BUG
- 文档日志

FastAdmin 致力于服务开发者，努力为开发者节省更多的时间。

参与开源社区的方式有很多种，比如：使用开源、推荐开源、写书写教程、贡献代码、回答社区问题、总结经验、打赏赞助等等，这些都可以让开源可持续的发展下去，开源更像是一群志同道合的小伙伴们同时开发一个有趣的项目，并吸引更多有趣的小伙伴们加入。

欢迎广大开发者朋友们贡献自己的智慧，让 FastAdmin 变得更强大，让 FastAdmin 变得更完美，最终为你节省更多的时间，让大家有更多的时间读书、健身、开源、投资、帮朋友和陪家人。

FastAdmin 从 v1.6.0 开始使用了 npm 作为前端组件的管理，废弃了原来的 bower ，以下是关于 FastAdmin 的贡献说明，请查看。

FastAdmin 开源框架仓库地址如下：

以下为 FastAdmin 开发环境必备工具：

以 FastAdmin 的 Gitee 仓库为例：

进入 fastadmin 目录，并切换到 1.x-dev 分支。

为节省你的宝贵时间，请详细的描述一下合并请求，比如新功能描述详细的使用方法，修复 Bug 时写出详细的复现过程和环境，这样可以节省你的时间并更快的得到回应或合并，感谢支持 FastAdmin，感谢支持国内的开源社区。

FastAdmin 开源后还有更大的惊喜，我们结识了一群有趣的小伙伴，有小伙伴为 FastAdmin 赞助服务器的，有为 FastAdmin 打赏支持的，还有参与到 FastAdmin 生态建设中的，截至 2025-05-18 已经有 100 位小伙伴为 FastAdmin 贡献了代码，以下为 FastAdmin 开源贡献者名单，感谢支持 FastAdmin，感谢支持国内的开源社区。开源贡献者名单（实时更新） https://gitee.com/karson/fastadmin/contributors?ref=1.x

在使用 composer 或 npm 命令时需保障网络流畅，可以自行使用国内的镜像地址，可能需要连接到 Github，需要保证网络畅通。

FastAdmin 开源后台框架的 Bug 或建议请帮忙提交到 Gitee Issues 中，谢谢。

**Examples:**

Example 1 (bash):
```bash
git clone https://gitee.com/<yourname>/fastadmin.git
```

Example 2 (bash):
```bash
cd fastadmin
 git checkout 1.x-dev
```

Example 3 (bash):
```bash
composer update -vvv
 npm install --ddd
 npm run build
```

---

## 辅助类 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/1264.html

**Contents:**
- 辅助类
- 常用类
  - 日期时间处理类
  - Http请求处理类
  - 随机字符处理类
  - 中文转拼音处理类
  - 表单元素生成类

FastAdmin中有自带常用的辅助类可以在我们开发中便捷使用，如果你需要扩展自己的类，可以参考ThinkPHP5的文档：https://www.kancloud.cn/manual/thinkphp5/177200

FastAdmin中的辅助类位于站点目录/extend/fast目录中。

表单前台使用示例可以参考：https://ask.fastadmin.net/article/5567.html

**Examples:**

Example 1 (sass):
```sass
//获取两个时区间相差的秒数
$seconds = \fast\Date::offset('America/Chicago', 'GMT');

//计算两个数值之间相差的时间
$span = \fast\Date::span(60, 182, 'minutes,seconds'); // array('minutes' => 2, 'seconds' => 2)
$span = \fast\Date::span(60, 182, 'minutes'); // 2，如果第三个参数只需返回一个数据时，此时直接返回值，不返回数组。
//第三个参数支持years,months,weeks,days,hours,minutes,seconds

//格式化时间戳为易读的字符串
$text = \fast\Date::human(time()-10); //10 seconds ago
$text = \fast\Date::human(time()+10); //10 seconds after
$text = \fast\Date::human(time()-70); //1 minute ago
$text = \fast\Date::human(time()+70); //1 minute ago

//获取一个基于时间偏移的Unix时间戳，常用于统计功能筛选日期时间的计算
$timestamp = \fast\Date::unixtime('day'); // 返回今天0点0分0秒的时间戳
$timestamp = \fast\Date::unixtime('day', -1); //返回昨天0点0分0秒的时间戳
$timestamp = \fast\Date::unixtime('day', -1, 'end'); //返回昨天23点59分59秒的时间戳
$timestamp = \fast\Date::unixtime('week'); // 返回本周一0点0分0秒的时间戳
$timestamp = \fast\Date::unixtime('week', -1); //返回上周一0点0分0秒的时间戳
$timestamp = \fast\Date::unixtime('week', -1, 'end'); //返回上周日23点59分59秒的时间戳
//\fast\Date::unixtime($type = 'day', $offset = 0, $type = 'begin');
//$type：默认为day，支持minute,hour,day,week,month,quarter,year
//$offset：默认为0，正数表示当前$type之后，负数表示当前$type之前
//$type：默认为begin，时间的开始或结束，可选前(begin,start,first,front)，end
```

Example 2 (php):
```php
//发送一个POST请求并获取返回结果
$result = \fast\Http::post("http://www.example.com", ['name'=>'张三', 'age'=>20]);
//发送一个POST请求并设置Content-Type并获取返回结果
$result = \fast\Http::post("http://www.example.com", ['name'=>'张三', 'age'=>20], [CURLOPT_TIMEOUT => 30, CURLOPT_HTTPHEADER => ['Content-Type: text/plain', 'Authorization: abcdefg']]);

//发送一个GET请求并获取返回结果，此时返回$result=['ret'=>true, 'msg'=>'返回结果'];
$result = \fast\Http::sendRequest("http://www.example.com", ['name'=>'张三', 'age'=>20], [CURLOPT_HTTPHEADER => ['Content-Type: text/plain']]);

//发送一个无需获取返回结果的请求
\fast\Http::sendAsyncRequest("http://www.example.com", ['name'=>'张三', 'age'=>20]);

//发送输出一个临时文件到浏览器端下载，并删除该文件
\fast\Http::sendToBrowser("你的临时文件绝对路径");
```

Example 3 (php):
```php
//生成一个包含数字和字母的6位随机字符串，默认为6位
$result = \fast\Random::alnum();
//生成一个包含数字和字母的15位随机字符串
$result = \fast\Random::alnum(15);

//生成一个仅包含字母的15位随机字符串
$result = \fast\Random::alpha(15);

//生成一个仅包含数字的15位随机数字
$result = \fast\Random::numeric(15);
//生成一个仅包含数字且不包含0的15位随机数字
$result = \fast\Random::nozero(15);

//生成全球唯一标识
$result = \fast\Random::uuid();
```

Example 4 (php):
```php
//中文转拼音全拼
$result = \fast\Pinyin::get("中文"); //返回zhongwen
//中文转拼音首字母
$result = \fast\Pinyin::get("中文", true); //返回zw
//中文转拼音使用-进行连接
$result = \fast\Pinyin::get("中文", false, '-'); //zhong-wen
//中文转拼音使用-进行连接并首字母大写
$result = \fast\Pinyin::get("中文", false, '-', true); //Zhong-Wen
//\fast\Pinyin::get($chinese, $onlyfirst = false, $delimiter = '', $ucfirst = false);
//$chinese：中文字符，必选
//$onlyfirst：是否只返回拼音首字母，默认为false
//$delimiter：拼音间分隔符，默认为空
//$ucfirst：是否拼音首字母大小，默认为false
```

---

## 键值组件(Fieldlist) - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/184.html

**Contents:**
- 键值组件(Fieldlist)
  - 组件特点
  - 数据源
  - 常规示例
  - 自定义模板
  - 表格布局
  - 事件绑定
  - 重新渲染
  - 追加数据
  - 相关链接

键值组件是FastAdmin开发的一项简洁实用的基础组件，在FastAdmin中很多模块都有使用到该组件，例如常规管理->系统配置->字典配置均使用此组件开发，我们在插件管理配置中也经常可以看到键值组件的身影。

1、支持一维数组和二维数组数据源2、支持添加、删除、排序3、支持自定义列表模板

fieldlist组件支持一维数组和二维数组数据源，默认为一维数组数据源，如果需要使用二维数组数据源，请务必同时使用自定义模板功能才支持。

以下是键值组件常用的一维数组数据源使用方法：

通过将以上代码放置在我们的表单中，然后使用Form.api.bindevent("form")或Form.events.fieldlist("form")进行初始化即可。

以上是最简洁的使用方法，fieldlist还有更强大的自定义功能来实现自定义模板和二维数组数据源，如下：

在自定义模板中有固定的变量，如<%=name%>、<%=index%>、<%=row['列名']%>，说明如下：

温馨提示：使用自定义模板时，二维数据请勿仅使用key和value这个键名，会导致被识别为键值数组。

fieldlist默认使用的是dl dd布局，此外还支持使用table来进行布局，达到更好的展示效果，如下：

可以看到我们我们给table添加了一个额外的属性data-tag="tr"通过以上定义，可以任意自定义我们展示项的数据。使用表格布局时必须使用自定义模板，且自定义模板中的第一个DOM元素必须是<tr>

如果我们需要在点击追加按钮以后再对新增的展示项绑定事件，我们可以在JS中通过监听事件来给新增的元素绑定事件，这种情况常用于我们自定义列表中有表单组件，如日期选择、上传按钮、动态下拉等情况下使用。

如果我们在JS中外部对fieldlist中的组件做了修改，此时我们需要手动触发下组件的change事件，如：

通过以上代码来触发input的change事件，此时我们隐藏的textarea值才会刷新，否则textarea仍然是旧的数据

如果我们通过JS手动修改了隐藏的textarea的值，此时需要重新渲染我们的fieldlist组件，我们可以通过

如果我们希望在外部追加数据，可以通用调用追加按钮的点击事件并透传数据来实现

Art-Template模板语法文档：https://github.com/aui/art-template/tree/3.1.0

**Examples:**

Example 1 (html):
```html
<textarea name="row[configgroup]" class="form-control hide" cols="30" rows="5">
    {
        "basic":"基础配置",
        "email":"邮件配置",
        "dictionary":"字典配置",
        "user":"会员配置",
        "example":"示例分组"
    }
</textarea>
```

Example 2 (html):
```html
<textarea name="row[test]" class="form-control hide" cols="30" rows="5">
    [
        {"name":"张三","gender":"男","age":"23","score":"80"},
        {"name":"李四","gender":"男","age":"26","score":"90"}
    ]
</textarea>
```

Example 3 (html):
```html
<dl class="fieldlist" data-name="row[configgroup]">
    <dd>
        <ins>键名</ins>
        <ins>键值</ins>
    </dd>
    <dd>
        <a href="javascript:;" class="btn btn-sm btn-success btn-append"><i class="fa fa-plus"></i> 追加</a>
    </dd>
    <textarea name="row[configgroup]" class="form-control hide" cols="30" rows="5">{"basic":"基础配置","email":"邮件配置","dictionary":"字典配置","user":"会员配置","example":"示例分组"}</textarea>
</dl>
```

Example 4 (html):
```html
<dl class="fieldlist" data-name="row[test]" data-template="testtpl">
    <dd>
        <ins>姓名</ins>
        <ins>性别</ins>
        <ins>年龄</ins>
        <ins>成绩</ins>
    </dd>
    <dd>
        <a href="javascript:;" class="btn btn-sm btn-success btn-append"><i class="fa fa-plus"></i> 追加</a>
    </dd>
    <textarea name="row[test]" class="form-control hide" cols="30" rows="5">[{"name":"张三","gender":"男","age":"23","score":"80"},{"name":"李四","gender":"男","age":"26","score":"90"}]</textarea>
</dl>
<!--定义模板，模板语法使用Art-Template模板语法-->
<script type="text/html" id="testtpl">
    <dd class="form-inline">
        <input type="text" name="<%=name%>[<%=index%>][name]" class="form-control" value="<%=row['name']%>" size="10"> 
        <input type="text" name="<%=name%>[<%=index%>][gender]" class="form-control" value="<%=row['gender']%>" size="30"> 
        <input type="text" name="<%=name%>[<%=index%>][age]" class="form-control" value="<%=row['age']%>" size="30"> 
        <input type="text" name="<%=name%>[<%=index%>][score]" class="form-control" value="<%=row['score']%>" size="30"> 
        <span class="btn btn-sm btn-danger btn-remove"><i class="fa fa-times"></i></span> <span class="btn btn-sm btn-primary btn-dragsort"><i class="fa fa-arrows"></i></span>
    </dd>
</script>
```

---

## 附件选择 - FastAdmin框架文档 - FastAdmin开发文档

**URL:** https://doc.fastadmin.net/doc/183.html

**Contents:**
- 附件选择
  - 常规示例
  - 常用属性
  - 事件绑定

FastAdmin中拥有强大的附件选择功能，可以很方便的给文本框添加一个按钮或链接来快速使用附件选择功能。

通常情况下我们只需要给按钮或链接添加一个faselect的class即可实现附件选择的功能，如下：

首先需要给你的元素添加一个faselect的class样式名，其次可以添加以下的属性

如果你的附件选择按钮是动态生成的，你需要使用Form.events.faselect("按钮父元素");进行绑定相关的事件。

**Examples:**

Example 1 (html):
```html
<input type="text" id="c-file" class="form-control" />
<a href="javascript:" class="btn btn-info faselect" data-input-id="c-file" data-mimetype="image/*" data-multiple="false">选择附件</a>
```

---
