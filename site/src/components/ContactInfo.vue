<template>
  <a-row class="contact-info">
    <a-col :span="8" :offset="5" class="name en-name" v-if="this.lang == 'en'">YiFan Li</a-col>
    <a-col :span="8" :offset="5" class="name zh-name" v-else>李逸凡</a-col>
    <a-col :span="6" class="contact">
      <ul>
        <li>+86 188-1101-9056</li>
        <li>
          <a href="mailto:liyifanv616@outlook.com" style="color:white;">liyifanv616@outlook.com</a>
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
  background-color: grey;
  color: white;
  padding-top: 14pt;
  padding-bottom: 14pt;
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