<template>
  <a-row>
    <div class="page-footer">
      <external-link :offset="8" href="../pdf/CV-ZH.pdf" icon="file-pdf" text="PDF" />
      <external-link :offset="0" href="https://github.com/Vopaaz" icon="github" text="Github" />
      <external-link
        :offset="0"
        href="https://www.linkedin.com/in/yifan-li-vopaaz"
        icon="linkedin"
        text="LinkedIn"
      />
      <external-link
        :offset="0"
        href="mailto:liyifanv616@outlook.com"
        icon="email"
        text="E-mail"
      />
    </div>
  </a-row>
</template>

<script>
import "../assets/compiled-icons/file-pdf";
import "../assets/compiled-icons/github";
import "../assets/compiled-icons/email";
import "../assets/compiled-icons/linkedin";
import ExternalLink from "./ExternalLink.vue";

export default {
  props: {
    state: Object
  },
  components: {
    ExternalLink
  }
};
</script>

<style scoped>
.page-footer {
  background-color: gray;
  margin-top: 1cm;
  padding-top: 1cm;
  padding-bottom: 5cm;
}
</style>
