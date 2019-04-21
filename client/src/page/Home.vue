<template>
	<div class="home">
    <div class="container-fluid full-cover">
      <div class="row cover">
        <div class="col align-self-center">
        	<h1>
        		<span class="text">สวัสดี
		          <span v-if="date == 0">วันอาทิตย์</span>
		          <span v-else-if="date == 1">วันจันทร์</span>
		          <span v-else-if="date == 2">วันอังคาร</span>
		          <span v-else-if="date == 3">วันพุธ</span>
		          <span v-else-if="date == 4">วันพฤหัสบดี</span>
		          <span v-else-if="date == 5">วันศุกร์</span>
		          <span v-else-if="date == 6">วันเสาร์</span>
	        	</span>
	        </h1>
        </div>
      </div>
    </div>
	</div>
</template>

<script>
import moment from 'moment';
export default {
  name: 'Home',
  data() {
    return {
      date: new Date().getDay()
    }
  },
};
</script>
<style scoped>
	.text {
		background: white;
	}
	.cover {
		height: 100%;
	}
  .full-cover {
  	background: url("https://loremflickr.com/1024/512/flower");
  	background-size: cover;
  	background-repeat: no-repeat;
  	height: 48vh;
  }
</style>


