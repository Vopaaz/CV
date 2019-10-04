<template>
  <a-affix offsetTop="0">
    <a-layout-header class="page-header">
      <a-row>
        <a-col
          :xl="{ offset: 15, span: 5}"
          :lg="{ offset: 12, span: 7}"
          :sm="{ offset: 4, span: 12}"
          style="text-align:right;"
          v-if="showImportantSwitch"
        >
          <span v-if="state['lang']=='zh'" class="label">只显示重要的条目</span>
          <span v-else class="label">Show important items only</span>
          <a-switch defaultChecked @change="switch_verbose" />
        </a-col>
        <a-col
          :xl="{span: 4, offset: 0}"
          :lg="{span: 5, offset: 0}"
          :sm="{span: 8, offset: 0}"
          :xs="{span: 12, offset: 12}"
        >
          <a-radio-group @change="change_lang" :value="state['lang']">
            <a-radio-button value="zh">中文</a-radio-button>
            <a-radio-button value="en">English</a-radio-button>
          </a-radio-group>
        </a-col>
      </a-row>
    </a-layout-header>
  </a-affix>
</template>

<script>
export default {
  data: function() {
    return {
      showImportantSwitch: true
    };
  },
  props: {
    state: Object
  },
  methods: {
    change_lang(e) {
      this.state["lang"] = e.target.value;
    },
    switch_verbose(checked) {
      if (checked) {
        this.state["verbose"] = "false";
      } else {
        this.state["verbose"] = "true";
      }
    },
    handleShowImportant() {
      if (window.innerWidth >= 576) {
        this.showImportantSwitch = true;
      } else {
        this.showImportantSwitch = false;
      }
    }
  },
  created() {
    window.addEventListener("resize", this.handleShowImportant);
    this.handleShowImportant();
  }
};
</script>

<style>
.page-header {
  margin: 0;
}
.label {
  color: white;
  margin-right: 8pt;
}
</style>