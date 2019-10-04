<template>
  <a-row>
    <a-col
      :xs="{ span:24, offset: 0}"
      :sm="{ span:20, offset: 2}"
      :md="{ span:18, offset: 3}"
      class="section-col-container"
    >
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
          <a-card-grid
            style="width:100%;"
            class="info-card position-card"
          >{{ exp[lang]['position'] }}</a-card-grid>
          <a-card-grid
            :style="positionStyle"
            class="info-card position-card"
          >{{ exp[lang]['sub-position'] }} &nbsp;</a-card-grid>
          <a-card-grid :style="timeStyle" class="info-card">{{ process_time(exp['time']) }}</a-card-grid>
          <a-card-grid :style="locationStyle" class="info-card">{{ exp[lang]['location'] }}</a-card-grid>
        </span>
        <span v-else>
          <a-card-grid
            :style="positionStyle"
            class="info-card position-card"
          >{{ exp[lang]['position'] }}</a-card-grid>
          <a-card-grid :style="timeStyle" class="info-card">{{ process_time(exp['time']) }}</a-card-grid>
          <a-card-grid :style="locationStyle" class="info-card">{{ exp[lang]['location'] }}</a-card-grid>
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
  data: function() {
    return {
      positionStyle: "",
      timeStyle: "",
      locationStyle: ""
    };
  },
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
    },
    process_time: function(str) {
      function format_CN_date(d) {
        return `${d.getFullYear()}年${d.getMonth() + 1}月`;
      }

      var start = new Date(str.split("-")[0].trim());
      var end = str.split("-")[1].trim();
      if (this.lang == "en") {
        var options = {
          year: "numeric",
          month: "short"
        };
        start = start.toLocaleDateString("en-US", options);
        if (end == "now") {
          end = "Now";
        } else {
          end = new Date(end).toLocaleDateString("en-US", options);
        }
      } else {
        start = format_CN_date(start);
        if (end == "now") {
          end = "至今";
        } else {
          end = format_CN_date(new Date(end));
        }
      }
      return `${start} - ${end}`;
    },
    handleCardStyle: function() {
      if (window.innerWidth >= 1368) {
        this.positionStyle = "width:53%";
        this.timeStyle = "width:25%";
        this.locationStyle = "width:22%";
      } else if (window.innerWidth >= 576) {
        this.positionStyle = "width:100%";
        this.timeStyle = "width:50%; padding-left:30px";
        this.locationStyle = "width:50%; padding-left:30px";
      } else {
        this.positionStyle = "width:100%";
        this.timeStyle = "width:100%; padding-left:30px";
        this.locationStyle = "width:100%; padding-left:30px";
      }
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
  },
  created() {
    window.addEventListener("resize", this.handleCardStyle);
    this.handleCardStyle();
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
  padding-left: 14px;
  padding-right: 14px;
}

.position-card {
  padding-left: 30px;
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