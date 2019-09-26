<template>
  <div id="app">
    <a-layout>
      <page-header :state="state" />
      <a-layout-content>
        <contact-info :state="state" />
        <general-section sec="education" :state="state" />
        <general-section sec="internship" :state="state" />
        <general-section sec="research" :state="state" />
        <general-section sec="others" :state="state" />
        <skill-section :state="state" />
      </a-layout-content>
      <page-footer :state="state" />
      <div>
        <a-back-top />
      </div>
    </a-layout>
  </div>
</template>

<script>
import GeneralSection from "./components/GeneralSection.vue";
import SkillSection from "./components/SkillSection.vue";
import PageFooter from "./components/PageFooter.vue";
import PageHeader from "./components/PageHeader.vue";
import ContactInfo from "./components/ContactInfo.vue";
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
    PageFooter,
    PageHeader,
    ContactInfo
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
}
</style>
