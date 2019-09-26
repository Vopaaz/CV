<template>
  <a-row>
    <a-col :span="18" :offset="3" class="section-col-container">
      <h2>{{ sec_title }}</h2>
      <a-card
        :title="exp[lang]['title']"
        class="exp-card"
        v-for="exp in ordered_exps"
        :key="exp[lang]['title']"
        headStyle="font-size:16.5pt; font-family:Calibri, Helvetica, Arial, sans-serif;padding-top:5pt;padding-bottom:5pt;"
        bodyStyle="font-size:14pt; font-family:Calibri, Helvetica, Arial, sans-serif;"
      >
        <span v-if="exp[lang]['sub-position']">
          <a-card-grid style="width:100%;" class="info-card">{{ exp[lang]['position'] }}</a-card-grid>
          <a-card-grid style="width:56%;" class="info-card">{{ exp[lang]['sub-position'] }} &nbsp;</a-card-grid>
          <a-card-grid style="width:22%" class="info-card">{{ exp['time'] }}</a-card-grid>
          <a-card-grid style="width:22%;" class="info-card">{{ exp[lang]['location'] }}</a-card-grid>
        </span>
        <span v-else>
          <a-card-grid style="width:56%;" class="info-card">{{ exp[lang]['position'] }}</a-card-grid>
          <a-card-grid style="width:22%" class="info-card">{{ exp['time'] }}</a-card-grid>
          <a-card-grid style="width:22%;" class="info-card">{{ exp[lang]['location'] }}</a-card-grid>
        </span>
        <a-card-grid style="width:100%;">
          <ul>
            <li v-for="detail in exp[lang]['details']" :key="detail">
              <div v-html="preprocess(detail)"></div>
            </li>
          </ul>
        </a-card-grid>
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
        return `<a target="_blank" href="${x.match(re)[2]}">${
          x.match(re)[1]
        }</a>`;
      });
    }
  },
  computed: {
    sec_title: function() {
      return this.state["data"][this.sec][this.lang];
    },
    ordered_exps: function() {
      var exps = this.state["data"][this.sec]["experiences"];
      if (this.state["verbose"] == "false") {
        exps = exps.filter(exp => {
          return exp[this.state["lang"] + "-on"] == "true";
        });
      }
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

<style>
.exp-card {
  text-align: left;
  margin-bottom: 3pt;
}

.info-card {
  vertical-align: middle;
  padding: 12px;
  padding-left: 24px;
  padding-right: 24px;
}

h2 {
  margin-top: 10pt;
  font-size: 26pt;
  font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif;
}

li {
  margin-bottom: 3pt;
}

ul {
  margin-bottom: 0pt;
}

a {
  color: #3976c6;
}
</style>