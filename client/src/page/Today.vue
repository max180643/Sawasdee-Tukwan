<template>
  <div class="today container">
    <h1 v-if="!url">Loading...</h1>
    <div v-else class="container">
      <img :src="url">
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Random',
  data() {
    return {
    	url: '',
      size: [0, 0],
    };
  },
  methods: {
    getRandomImage() {
      const path = 'http://localhost:5000/api/randomImage?size=512&encode=png';
      axios.get(path)
        .then((res) => {
          console.log(res.data);
          this.size = res.data.size;
          this.renderImage(res.data.base64, res.data.type);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    renderImage(base64, type) {
    	this.url = `data:image/${type};base64,${base64}`
    },
  },
  created() {
    this.getRandomImage();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.today {
  padding-top: 10px;
}
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
