import { createRouter, createWebHistory } from 'vue-router'
import Index from '../views/Index.vue'
import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import CheckOut from '../views/CheckOut.vue'


const routes = [
    {
      path: '/',
      redirect: '/index',
    },
    {
      path:'/index',
      name: 'index',
      component: Index 
    },
    {
      path:'/:category_slug/:product_slug',
      name:'product',
      component: Product
    },
    {
      path:'/:category_slug',
      name:'category',
      component: Category
    },
    {
      path:'/search',
      name:'search',
      component: Search
    },
    {
      path:'/cart',
      name:'cart',
      component: Cart
    },
    {
      path:'/signup',
      name:'signup',
      component: SignUp
    },
    {
      path:'/login',
      name:'login',
      component: Login
    },
    {
      path:'/checkout',
      name:'checkout',
      component: CheckOut
    },

  ]
  
const router = createRouter({
    history: createWebHistory(),
    routes
})
  
  
export default router