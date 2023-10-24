<template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        
         <!-- Category Checkboxes -->
        <div class="col-12 mb-3">
          <form>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="radio"
                id="phone"
                value="phone"
                v-model="selectedCategory"
                
              >
              <label class="form-check-label" for="category1">Phone</label>
            </div>
            <div class="form-check form-check-inline">
              <input
                class="form-check-input"
                type="radio"
                id="notebook"
                value="notebook"
                v-model="selectedCategory"
              
              >
              <label class="form-check-label" for="category2">Notebook</label>
            </div>
          </form>
        </div>

        <!--  Card -->
        <div class="col-4" v-for="product in latestProducts" :key="product.id">
          <div class="card p-3 bg-white" >
            <!-- <i v-if="product.description.toLowerCase().includes('apple')" class="fab fa-apple" style="color: #000000;"></i> -->
            <div class="about-product text-center mt-2">
              <img :src="product.get_thumbnail" width="300" height="200" href="" style="text-decoration: none;">
              <div>
                <h4>{{ product.name }}</h4>
                <h6 class="mt-0 text-black-50">{{product.description}}</h6>
              </div>
            </div>
            <div class="d-flex justify-content-between total font-weight-bold mt-4">
              <span>Total</span>
              <span>{{'$'+product.price}}</span>
            </div>
            <router-link v-bind:to="product.get_absolute_url" style="text-decoration: none; padding-left: 35%;">View details</router-link>
          </div>
        </div>
  
        

      </div>
    </div>
</template>
  

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: [],
      selectedCategory: {},
    }
  },
  components: {

  },
  mounted() {
    this.getLatestProducts()
    
  },
  watch: {
    selectedCategory(newVal) {
      if (newVal === 'phone') {
        this.navigateToPhoneCategory();
      } else if (newVal === 'notebook') {
        this.navigateToNotebookCategory();
      }
    }
  },
  methods: {
    async getLatestProducts() {
        this.$store.commit('setIsLoading',true)
        
        await axios
            .get('/api/products/latest')
            .then(response => {
            console.log(response.data)    
            this.latestProducts = response.data
        })
        .catch(error => {
            console.log(error)
        })
        this.$store.commit('setIsLoading',false)
    },
    navigateToPhoneCategory() {
      this.$router.push('/phone'); 
    },
    navigateToNotebookCategory() {
      this.$router.push('/notebook'); 
    }
  }
}
</script>


<style>
</style>