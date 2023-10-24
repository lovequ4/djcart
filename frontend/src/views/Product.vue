<template>
    <div class="page-product" style="margin-top: 5%;">
      <div class="container">
        <div class="card">
          <div class="row g-0">
            <div class="col-md-8">
              <img :src="product.get_image" alt="Product Image" class="img-fluid" >
            </div>
            <div class="col-md-4">
              <div class="card-body d-flex flex-column justify-content-between h-100">
                <div>
                  <h1 class="card-title">{{ product.name }}</h1>
                  <p class="card-text">{{ product.description }}</p>
                  <p><strong>Price:</strong> ${{ product.price }}</p>
                  <div class="input-group mt-3 w-25">
                    <input type="number" class="form-control"  min="1"  >
                  </div>
                </div>
                <button class="btn btn-primary mt-3" @click="addToCart">Add to cart</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

        
</template>
  

<script>
import axios from 'axios'

export default{
    name: 'Product',
    data(){
        return{
            product:{},
            quantity:1,
        }
    },
    mounted(){
        this.getProduct()
    },
    methods:{
      async  getProduct(){
            this.$store.commit('setIsLoading',true)
            
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

          await  axios 
              .get(`/api/products/${category_slug}/${product_slug}`)
              .then(response =>{
                  this.product = response.data
              })
              .catch(error =>{
                  console.log(error)
              })
            this.$store.commit('setIsLoading',false)
        },
        addToCart(){
         
          if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
          }

          const item = {
                product: this.product,
                quantity: this.quantity
            }

          this.$store.commit('addToCart', item)
         
        }
    }
}
</script>