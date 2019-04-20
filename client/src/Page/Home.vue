<template>
	<div class="home">
  <Navbar></Navbar>
  <div class="container-fluid">
    <img src="../assets/flower_ex.jpg" height="50%" width="100%">
  </div>
  <div class="container card">
    <h3 style="font-size:3vw;">สวัสดี</h3>
    <span style="font-size:8vw;">{{ msg }}</span>
  </div>
	</div>
</template>

<script>
import Navbar from "@/components/navbar.vue";
export default {
  name: 'Home',
  data() {
    return {
      msg: 'วันจันทร์',
    };
  },
  components: {
    Navbar,
  }
};
</script>
<style scoped>
  body {
    background-image: url("../assets/bg_gold.gif");
  }

  .card{
    width: 30%;
    background-color: black;
    color: white;
    position: absolute;
    bottom: 30%;
    left: 60%;
    height: auto;
  }
</style>


