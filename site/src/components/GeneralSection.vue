<template>
  <a-row>
    <a-col :span="16" :offset="4" class="section-col-container">
      <h2>{{ sec_title }}</h2>
      <a-card
        :title="exp[lang]['title']"
        class="exp-card"
        v-for="exp in ordered_exps"
        :key="exp[lang]['title']"
        headStyle="font-size:14pt;"
        bodyStyle="font-size:12pt; font-family:Helvetica;"
      >
        <ul>
          <li v-for="detail in exp[lang]['details']" :key="detail">
            <div v-html="preprocess(detail)"></div>
          </li>
        </ul>
      </a-card>
    </a-col>
  </a-row>
</template>

<script>
var _ = require("lodash");

export default {
  props: {
    sec: String,
    state: Object
  },
  methods: {
    preprocess: function(str) {
      var re = /\$HREF\{(.*?)\}\{(.*?)\}/;
      return str.replace(re, x => {
        return `<a href="${x.match(re)[2]}">${x.match(re)[1]}</a>`;
      });
    }
  },
  computed: {
    sec_title: function() {
      return this.state["data"][this.sec][this.lang];
    },
    ordered_exps: function() {
      var exps = this.state["data"][this.sec]["experiences"];
      if (this.sec == "education") {
        return exps;
      } else {
        return _.orderBy(exps, "time", "desc");
      }
    },
    lang: function() {
      return this.state["lang"];
    }
  }
};
</script>

<style scoped>
.exp-card {
  text-align: left;
  margin-bottom: 3pt;
}

h2 {
  margin-top: 10pt;
  font-size: 24pt;
}

li {
  margin-bottom: 3pt;
}
</style>