<template>
  <a-col :md="md" :sm="sm" :lg="lg" :xs="xs">
    <a v-if="href.endsWith('pdf')" :href="href" target="_blank" download class="external-link">
      <a-row>
        <svgicon :icon="icon" :width="size" :height="size" color="#ffffff"></svgicon>
      </a-row>
      <a-row>{{ text }}</a-row>
    </a>

    <a v-else-if="href.startsWith('mailto')" :href="href" class="external-link">
      <a-row>
        <svgicon :icon="icon" :width="size" :height="size" color="#ffffff"></svgicon>
      </a-row>
      <a-row>{{ text }}</a-row>
    </a>

    <a v-else :href="href" target="_blank" class="external-link">
      <a-row>
        <svgicon :icon="icon" :width="size" :height="size" color="#ffffff"></svgicon>
      </a-row>
      <a-row>{{ text }}</a-row>
    </a>
  </a-col>
</template>

<script>
export default {
  props: {
    href: String,
    icon: String,
    text: String,
    sm: Object,
    lg: Object,
    md: Object,
    xs: Object
  },
  data: function() {
    return {
      size: 0
    };
  },
  created() {
    window.addEventListener("resize", this.handleResize);
    this.handleResize()
  },
  methods: {
    handleResize() {
      if (window.innerWidth < 576) {
        this.size = "1cm";
      } else {
        this.size = "1.5cm";
      }
    }
  }
};
</script>

<style>
.external-link {
  color: white;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}
</style>