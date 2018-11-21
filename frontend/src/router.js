import Vue from 'vue'
import Router from 'vue-router'
import vueResource from 'vue-resource'

Vue.use(Router)
Vue.use(vueResource)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('./views/Home.vue')
    },
    {
      path: '/risk-types',
      name: 'risktypes',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('./views/ManageRiskTypes.vue')
    },
    {
      path: '/risks',
      name: 'risks',
      component: () => import('./views/ManageRisks.vue')
    }
  ]
})
