<template>
  <div id="app">
    <Navbar></Navbar>
    <div id="content">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/navbar'
export default {
  name: 'App',
  components: {
    Navbar,
  }
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#content {
  margin-top: 20px;
}
</style>
