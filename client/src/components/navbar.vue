<template>
  <div class="container-fluid fixed-top">
    <div class="navbar navbar-expand-lg navbar-light bg-gold">
        <a class="navbar-brand" href="#">
            <img src="../assets/goldFlower-removebg.png" width="30" height="30" class="d-inline-block align-top" alt="">
            SawandeeTukwan
        </a>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="#">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Random</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Custom</a>
                </li>
            </ul>
        </div>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return 0;
    }
}
</script>

<style scoped>
    .bg-gold{
    background-image: linear-gradient(to right, #f9e782, #fbe86d, #fde856, #fee93a, #ffe900);
  }
</style>

