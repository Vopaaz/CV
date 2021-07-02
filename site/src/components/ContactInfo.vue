<template>
  <a-row class="contact-info">
    <a-col
      :lg="{ span: 5, offset: 5}"
      :md="{ span: 9, offset: 1}"
      :sm="{ span: 11, offset: 1}"
      :xs="{ span: 20, offset: 2}"
      class="name en-name"
      v-if="this.lang == 'en'"
    >YiFan Li</a-col>
    <a-col
      :lg="{ span: 5, offset: 5}"
      :md="{ span: 9, offset: 1}"
      :sm="{ span: 11, offset: 1}"
      :xs="{ span: 20, offset: 2}"
      class="name zh-name"
      v-else
    >李逸凡</a-col>
    <a-col
      :lg="{span: 7}"
      :md="{span: 9}"
      :sm="{span: 12}"
      :xs="{span: 20, offset: 2}"
      class="contact"
    >
      <ul>
        <li>+86 188-1101-9056</li>
        <li>
          <a href="mailto:liyifan.steven616@gmail.com" style="color:white;">liyifan.steven616@gmail.com</a>
        </li>
      </ul>
    </a-col>
  </a-row>
</template>

<script>
export default {
  props: {
    state: Object
  },
  computed: {
    lang: function() {
      return this.state["lang"];
    }
  }
};
</script>

<style scoped>
.contact-info {
  background: rgb(66, 66, 66);
  background: linear-gradient(
    30deg,
    rgba(66, 66, 66, 1) 0%,
    rgba(97, 97, 97, 1) 100%
  );
  color: white;
  padding-top: 28pt;
  padding-bottom: 28pt;
  margin-bottom: 15pt;
}

.name {
  font-size: 45pt;
}

.en-name {
  font-family: Garamond, Helvetica, Arial, sans-serif;
}

.zh-name {
  font-family: NSimSun, "Microsoft Yahei";
}

.contact {
  font-family: Garamond;
  font-size: 20pt;
  text-align: left;
}

li {
  padding-left: 2pt;
}
</style>