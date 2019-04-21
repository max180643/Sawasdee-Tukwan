<template>
	<div class="home">
    <Navbar></Navbar>
    <div class="cointainer">
      <div class="row">
        <div class="col">
          <h1 v-if="date == 0">วันที่ 0</h1>
          <h1 v-else-if="date == 1">วันที่ 1</h1>
          <h1 v-else-if="date == 2">วันที่ 2</h1>
          <h1 v-else-if="date == 3">วันที่ 3</h1>
          <h1 v-else-if="date == 4">วันที่ 4</h1>
          <h1 v-else-if="date == 5">วันที่ 5</h1>
          <h1 v-else-if="date == 6">วันที่ 6</h1>
        </div>
      </div>
    </div>
	</div>
</template>

<script>
import Navbar from "@/components/navbar.vue";
import moment from 'moment';
export default {
  name: 'Home',
  data() {
    return {
      date: new Date().getDay()
    }
  },
  components: {
    Navbar,
  }
};
</script>
<style scoped>
  
</style>


