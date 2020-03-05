<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
	<div class="categorys">
		
		<van-cell v-for="(item,index) in categorys" :key="index" :title="item.name" is-link :to="'/categorys/'+item.id+'/'" />

	</div>
	
	
	
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
	<!-- <div>
		<button @click="requestCategoryList">发起请求分类列表</button>
	</div> -->
	
	<div>
		<!-- <label for="">分类名：</label> <input type="text" v-model="categoryName">
		<br> -->
		<van-field v-model="categoryName" placeholder="请输入分类名" />
		<van-button type="primary" @click="requestCreateCategory">发起创建分类请求</van-button>
	</div>
	
	<!-- <div>
		<label for="">需要修改的分类的id</label> <input type="text" v-model="newCategoryId">
		<br>
		<label for="">需要修改的分类的名字</label> <input type="text" v-model="newCategoryName">
		<br>
		<button @click="requestModifyCategory">修改分类</button>
	</div> -->
	
	

  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data(){
	return{
		categorys:[],
		// username:"admin",
		// password:"123456",
		categoryName:"",
		// newCategoryId:"",
		// newCategoryName:"",
	}  
  },
  components: {
    // HelloWorld
  },
  created(){
	  this.requestCategoryList();
  },
  methods:{
	  requestCategoryList(){
		  this.$api.getCategoryList().then(res=>{
			  console.log("得到分类列表",res);
			  if(res.status==200){
				  this.categorys=res.data;
			  }
			  
		  }).catch(err=>{
			  console.log("发生错误",err);
		  })
	  },

	  requestCreateCategory(){
		  if(this.categoryName != ""){
			  this.$api.createCategory({
				  name:this.categoryName
			  }).then(res=>{
				  console.log("创建结果",res);
				  this.categorys.push(res.data);
				  this.categoryName="";
			  }).catch(err=>{
				  console.log("发生错误",err);
			  })
		  }
		  else
		  {
			  this.$toast("必须输入分类名");
			  console.log("必须输入分类名");
		  }
	  },
	 //  requestModifyCategory(){
		//   if(this.newCategoryId=="" || this.newCategoryName=="")
		//   {
		// 	  console.log("需要选择分类并且重新给予名字")
		//   }
		//   else{
		// 	  this.$api.modifyCategory({
		// 		  id:this.newCategoryId,
		// 		  name:this.newCategoryName
		// 	  }).then(res=>{
		// 		  console.log("修改结果",res);
		// 	  }).catch(err=>{
		// 		  console.log("发生错误",err);
		// 	  })
		//   }
	 //  }
  }
}
</script>
