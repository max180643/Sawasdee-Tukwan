<template>
  <b-container class="full-width">
    <b-navbar toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="#"><img src="../assets/myLogo.png" alt="SAWASDEE TUKWAN">SAWASDEE TUKWAN</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/">Home</b-nav-item>
          <b-nav-item to="/random">Today</b-nav-item>
          <b-nav-item to="/custom">Customize</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </b-container>
</template>

<script>
    export default {
    data() {
      return 0;
    }
  }
</script>

<style scoped>
    .full-width {
    width: 100%;
    min-width: 100%;
    padding: 0;
  }

    img {
        width: 30px;
        height: 30px;
        margin-right: 10px;
    }
</style>
