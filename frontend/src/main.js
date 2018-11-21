import Vue from 'vue'
import App from './App.vue'
import router from './router'

import $risktypes from './risk-type_model'
import $fieldtypes from './field-type_model'
import $risks from './risk_model'
import $fields from './field_model'
import $fieldsbyrisks from './fields-by-risk_model'


Vue.prototype.$risktypes = $risktypes
Vue.prototype.$fieldtypes = $fieldtypes
Vue.prototype.$risks = $risks
Vue.prototype.$fields = $fields
Vue.prototype.$fieldsbyrisks = $fieldsbyrisks

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
