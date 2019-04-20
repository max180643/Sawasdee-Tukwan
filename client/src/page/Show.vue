<template>
  <div class="container">
    <img :src="url">
    <h3>Size {{ this.size[0] + ' x ' + this.size[1] }}</h3>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      url: '',
      size: 0,
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/api/randomImage';
      axios.get(path)
        .then((res) => {
          console.log(res.data);
          this.url = res.data.img;
          this.size = res.data.size;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
