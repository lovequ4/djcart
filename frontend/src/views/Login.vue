<template>
    <div class="container mt-5">
      <div class="d-flex justify-content-center align-items-center">
        <form @submit.prevent="submitForm" class="border p-4 rounded shadow col-md-6">
          <div>
            <div class="mb-3">
              <label for="username" class="form-label">Username</label>
              <input type="text" class="form-control" id="username" v-model="username">
            </div>
  
  
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input type="password" class="form-control" id="password" v-model="password">
            </div>
  
  
            <div class="alert alert-danger" role="alert" v-if="errors.length">
              <ul>
                <li v-for="error in errors" :key="error">{{ error }}</li>
              </ul>
            </div>
  
            <div class="mb-3">
              <button type="submit" class="btn btn-dark">Log in</button>
            </div>
  
            <hr>
  
            <p>Or <router-link to="/signup">click here</router-link> to Sign Up!</p>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  
  
  

<script>
import axios from 'axios';

export default{
    data(){
        return{
            username:'',
            password:'',
            errors:[]
        }
    },
    methods:{
      async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post("/api/user/login", formData)
                  .then(response => {
                      const token = response.data.token
                      
                      this.$store.commit('setToken', token)
                      
                      axios.defaults.headers.common["Authorization"] = "Token " + token

                      localStorage.setItem("token", token)

                      this.$router.push('index')
                  })
                  .catch(error =>{
                      console.log(error)
                  })

        }
    }
}
</script>