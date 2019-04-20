<template>
	<div class="home">
		<div class="container">
			<h1>Home</h1>
			<h2>Welcome {{ this.msg }}!</h2>
			<input type="text" v-model="msg">
		</div>
		<div class="container bg-red">
			1234567890
		</div>
	</div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      msg: 'Icys',
    };
  }
};
</script>

<style scoped lang="scss">
	.bg-red {
		background: red;
	}
</style>