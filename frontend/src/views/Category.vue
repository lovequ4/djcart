<template>
<div class="container mt-5">
      <div class="row justify-content-center">
        
    


            <div class="column is-12">
                <h2 class="text-center">{{ category.name }}</h2>
            </div>
        
            <div class="col-4" v-for="product in category.products" :key="product.id">
            <div class="card p-3 bg-white">
              
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
    name: 'Category',
    components: {
       
    },
    data() {
        return {
            category: {
                products: []
            }
        }
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory() {
            const categorySlug = this.$route.params.category_slug
           
            this.$store.commit('setIsLoading', true)

            axios
                .get(`/api/products/${categorySlug}`)
                .then(response => {
                    this.category = response.data
                    console.log(response.data)
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}

</script>