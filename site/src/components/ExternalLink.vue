<template>
  <a-col :span="3" :offset="offset">
    <a v-if="href.endsWith('pdf')" :href="href" target="_blank" download class="external-link">
      <a-row>
        <svgicon :icon="icon" width="1.5cm" height="1.5cm" color="#ffffff"></svgicon>
      </a-row>
      <a-row>{{ text }}</a-row>
    </a>

    <a v-else-if="href.startsWith('mailto')" :href="href" class="external-link">
      <a-row>
        <svgicon :icon="icon" width="1.5cm" height="1.5cm" color="#ffffff"></svgicon>
      </a-row>
      <a-row>{{ text }}</a-row>
    </a>

    <a v-else :href="href" target="_blank" class="external-link">
      <a-row>
        <svgicon :icon="icon" width="1.5cm" height="1.5cm" color="#ffffff"></svgicon>
      </a-row>
      <a-row>{{ text }}</a-row>
    </a>
  </a-col>
</template>

<script>
export default {
  props: {
    offset: Number,
    href: String,
    icon: String,
    text: String
  }
};
</script>

<style>
.external-link {
  color: white;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}
</style>