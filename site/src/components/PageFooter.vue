<template>
  <a-layout-footer class="page-footer">
    <a-row>
      <external-link :offset="6" :href="pdf_path" icon="file-pdf" text="PDF" />
      <external-link :offset="0" href="https://github.com/Vopaaz" icon="github" text="Github" />
      <external-link
        :offset="0"
        href="https://www.linkedin.com/in/yifan-li-vopaaz"
        icon="linkedin"
        text="LinkedIn"
      />
      <external-link :offset="0" href="mailto:liyifanv616@outlook.com" icon="email" text="E-mail" />
    </a-row>
    <a-row>
      <a-col>
        <div class="copyright-info">Created by YiFan Li &copy; {{ new Date().getFullYear() }}</div>
      </a-col>
    </a-row>
  </a-layout-footer>
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
  },
  computed: {
    pdf_path: function() {
      if (this.state["lang"] == "zh") {
        if (this.state["verbose"] == "false") {
          return "../pdf/CV-ZH.pdf";
        } else {
          return "../pdf/CV-ZH-verbose.pdf";
        }
      } else {
        if (this.state["verbose"] == "false") {
          return "../pdf/CV-EN.pdf";
        } else {
          return "../pdf/CV-EN-verbose.pdf";
        }
      }
      return;
    }
  }
};
</script>

<style scoped>
.page-footer {
  background-color: gray;
  margin-top: 1cm;
  padding-top: 1cm;
  padding-bottom: 2cm;
}

.copyright-info {
  margin-top: 1cm;
  color: whitesmoke;
  font-family: "Times New Roman";
}
</style>
