import { createRouter, createWebHistory } from 'vue-router'
import Games from '../components/Games.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Games',
      component: Games,
    },
  ]
})

export default router
