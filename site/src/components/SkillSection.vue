<template>
  <a-row>
    <a-col :span="16" :offset="4" class="section-col-container">
      <h2>{{ sec_title }}</h2>
      <a-card
        class="exp-card"
        headStyle="font-size:16pt; font-family:Calibri, Helvetica, Arial, sans-serif"
        bodyStyle="font-size:14pt; font-family:Calibri, Helvetica, Arial, sans-serif"
      >
        <ul>
          <li v-for="detail in details" :key="detail">
            <div v-html="preprocess(detail)"></div>
          </li>
        </ul>
      </a-card>
    </a-col>
  </a-row>
</template>

<script>
export default {
  props: {
    state: Object
  },
  methods: {
    preprocess: function(str) {
      var re = /\$HREF\{(.*?)\}\{(.*?)\}/;
      return str.replace(re, x => {
        return `<a target="_blank" href="${x.match(re)[2]}">${
          x.match(re)[1]
        }</a>`;
      });
    }
  },
  computed: {
    sec_title: function() {
      return this.state["data"]["skills"][this.lang];
    },
    lang: function() {
      return this.state["lang"];
    },
    details: function() {
      return this.state["data"]["skills"]["details"][this.lang];
    }
  }
};
</script>
