<template>
  <a-affix :offsetTop="this.top">
    <a-layout-header class="page-header">
      <a-row>
        <a-col :offset="15" :span="5">
          <span v-if="state['lang']=='zh'" class="label">只显示最近的条目</span>
          <span v-else class="label">Show recent items only</span>
          <a-switch defaultChecked @change="switch_verbose" />
        </a-col>

        <a-col :span="4">
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
    }
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