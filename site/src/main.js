import Vue from 'vue'
import App from './App.vue'
import { Card, Row, Col, BackTop, Layout, Radio, Switch, Affix } from "ant-design-vue"

Vue.use(Card)
Vue.use(Row)
Vue.use(Col)
Vue.use(BackTop)
Vue.use(Layout)
Vue.use(Radio)
Vue.use(Switch)
Vue.use(Affix)

import VueSVGIcon from 'vue-svgicon'
Vue.use(VueSVGIcon)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

