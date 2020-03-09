<template>
	<div class="usercenter">
		用户中心
		<div v-if="userinfo">
			用户名：{{userinfo.username}}
			<br>
			注册日期：{{userinfo.date_joined|dataFormat}}
			
			<h2>修改信息</h2>
			<!-- 输入手机号，调起手机号键盘 -->
			<van-field v-model="userinfo.telephone" type="tel" label="手机号" />
			<van-field v-model="userinfo.password" type="password" label="密码" />
			<van-field v-model="userinfo.email" type="email" label="邮箱" />
			
			<van-button @click="modify" round block type="info" native-type="submit">
			  提交
			</van-button>
		</div>
	</div>
	
</template>

<script>
	export default{
		methods:{
			modify(){
				this.$api.modifyUserInfo({
					userinfo:this.userinfo
				}).then(res=>{
					console.log("更改成功",res);
				}).catch(err=>{
					console.log("更改出错",err);
				})
			}
		},
		data(){
			return{
				userinfo:null
			}
		},
		created() {
			this.$api.getUserinfo().then(res=>{
				console.log("个人信息",res);
				this.userinfo=res.data;
				this.$jsCookie.set("userinfo",res.data)
			}).catch(err=>{
				console.log("出错了",err);
			})
		},
		filters:{
			dataFormat(date){
				date = new Date(date)
				console.log(date,typeof(date));
				return `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`
			}
		}
		
	}
	
	
</script>

<style>
</style>
