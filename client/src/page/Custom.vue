<template>
  <div class="container custom">
    <div class="form-group">
      <input type="text" class="form-control" v-model:value="msg">
      <div class="row">
        <div class="col">
          <input type="range" class="form-control form-control-sm" v-model:value="size" step="2" min="64" max="1024">
        </div>
        <div class="col">
          <h4>Size: <span>{{ this.size }}</span></h4>
        </div>
      </div>
      <button type="button" class="btn btn-success" @click="getCustomImage(msg, size)">Render</button>
    </div>
    <div class="container" v-if="url">
      <img :src="url" download="sawandee.jpg"></div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Custom',
  data() {
    return {
      url: '',
      size: 512,
      msg: '',
    };
  },
  methods: {
    getCustomImage(msg, size) {
      const path = `http://localhost:5000/api/customImage?size=${size}&encode=jpeg&msg=${msg}`;
      axios.get(path)
        .then((res) => {
          console.log(res.data);
          this.renderImage(res.data.base64, res.data.type)
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
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.custom {
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
