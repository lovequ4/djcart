<template>

<div class="container mt-5">
      <div class="row justify-content-center">

            <div class="column is-12">
                <h4 class="is-size-5 has-text-grey">Search term: "{{ query }}"</h4>
            </div>

            <div class="col-4" v-for="product in Products" :key="product.id">
                <div class="card p-3 bg-white">
                    <i v-if="product.description.toLowerCase().includes('apple')" class="fab fa-apple" style="color: #000000;"></i>
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

export default{
    name:'Search',
    data(){
        return {
            Products: [],
            query: ''
        }
    },
    mounted(){
        let uri = window.location.search.substring('1')
        let params = new URLSearchParams(uri)

        if(params.get('query')){
            this.query = params.get('query')
            this.performSearch()
        }
    },
    methods:{
        async performSearch(){
            this.$store.commit('setIsLoading',true)
        
            await axios
                .post('/api/products/search',{'query':this.query})
                .then(response => {
                console.log(response.data)    
                this.Products = response.data
            })
            .catch(error => {
                console.log(error)
            })
            this.$store.commit('setIsLoading',false)
        }
    }
}
</script>