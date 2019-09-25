import Vue from 'vue'
import App from './App.vue'
import { Card, Row, Col } from "ant-design-vue"
Vue.use(Card)
Vue.use(Row)
Vue.use(Col)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

