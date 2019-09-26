<template>
  <div id="app">
    <general-section sec="education" :state="state" />
    <general-section sec="internship" :state="state" />
    <general-section sec="research" :state="state" />
    <general-section sec="others" :state="state" />
    <skill-section :state="state" />
    <page-footer :state="state" />
    <div>
      <a-back-top />
    </div>
  </div>
</template>

<script>
import GeneralSection from "./components/GeneralSection.vue";
import SkillSection from "./components/SkillSection.vue";
import PageFooter from "./components/PageFooter.vue"
import state from "./assets/Global.js";

export default {
  name: "app",
  data: function() {
    return {
      state: state
    };
  },
  components: {
    GeneralSection,
    SkillSection,
    PageFooter
  }
};
</script>

<style scoped>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
