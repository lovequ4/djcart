<template>
     <nav class="navbar navbar-expand-lg bg-dark sticky-top navbar-dark p-3 shadow-sm">
      <div class="container">
        <a class="navbar-brand" href="/index"><i class="fa-solid fa-shop me-2"></i> <strong>Demo</strong></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
    
        
        <div class=" collapse navbar-collapse" id="navbarNavDropdown">
        
        <form method="get" action="/search">  
          <div class="ms-auto d-none d-lg-block">
            <div class="input-group">
              <span class="border-warning input-group-text bg-warning text-white"><i class="fa-solid fa-magnifying-glass"></i></span>
              <input type="text" class="form-control border-warning" style="color:#7a7a7a" name="query">
              <button class="btn btn-warning text-white">Search</button>
            </div>
          </div>
        </form>

          <ul class="navbar-nav ms-auto ">
            
            <!-- <li class="nav-item">
              <a class="nav-link mx-2 text-uppercase" href="#">Products</a>
            </li> -->
            
          
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link to="/cart" class="nav-link mx-2 text-uppercase"><i class="fa-solid fa-cart-shopping me-1"></i>Cart ({{ cartTotalLength }})</router-link>
            </li>

            <template v-if="$store.state.isAuthenticated">
              <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                      <i class="fa-solid fa-circle-user me-1"></i>User
                  </a>
                  <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <li><a class="dropdown-item" href='' @click="logout">Logout</a></li>
                  </ul>
              </li>
            </template>

            <template v-else>
              <li class="nav-item">
                  <a class="nav-link " href="" @click="login"  aria-expanded="false">
                      <i class="fa-solid fa-circle-user me-1" ></i>Login
                  </a>
              </li>
            </template>

          </ul>
        </div>
      </div>
    </nav>
</template>

<script>
import axios from 'axios'

export default{
  data(){
    return{
      cart:{
        items:[]
      },
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token 

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }

  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
      cartTotalLength() {
          let totalLength = 0

          for (let i = 0; i < this.cart.items.length; i++) {
              totalLength += this.cart.items[i].quantity
          }

          return totalLength
      }
  },
  methods:{
    logout() {
      console.log("logout")
        axios.defaults.headers.common["Authorization"] = ""

        localStorage.removeItem("token")
        localStorage.removeItem("username")
        localStorage.removeItem("userid")

        this.$store.commit('removeToken')

        this.$router.push('/')
    },
    login(){
      this.$router.push('/login')
    }
  }
}
</script>

