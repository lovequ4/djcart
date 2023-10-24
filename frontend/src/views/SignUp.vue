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
              <label for="email" class="form-label">Email</label>
              <input type="email" class="form-control" id="email" v-model="email">
            </div>
  
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input type="password" class="form-control" id="password" v-model="password">
            </div>
  
            <div class="mb-3">
              <label for="password2" class="form-label">Repeat password</label>
              <input type="password" class="form-control" id="password2" v-model="password2">
            </div>
  
            <div class="alert alert-danger" role="alert" v-if="errors.length">
              <ul>
                <li v-for="error in errors" :key="error">{{ error }}</li>
              </ul>
            </div>
  
            <div class="mb-3">
              <button type="submit" class="btn btn-dark">Sign up</button>
            </div>
  
            <hr>
  
            <p>Or <router-link to="/login">click here</router-link> to log in!</p>
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
            email:'',
            password:'',
            password2:'',
            errors:[]
        }
        
    },
    methods:{
      async submitForm() {

            const formData = {
                username: this.username,
                email:this.email,
                password: this.password,
                password2: this.password2,
            }

            await axios
                .post("/api/user/register", formData)
                  .then(response => {
                    
                      this.$router.push('login')
                  })
                  .catch(error =>{
                      console.log(error)
                  })

        }
    }
}
</script>