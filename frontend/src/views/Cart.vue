<template>
    <div class="container mt-5">
        <div class="row justify-content-center">
        
        <div class="">
            <h1 class="title" style="font-weight: bold;">Cart</h1>
        </div>
        
        <!-- table -->
        <div>
            <table class="table " v-if="cartTotalLength">
                <thead class="table-light">
                    <tr> 
                        <th>Product</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Total</th>
                        <th>action</th>
                    </tr>
                </thead>

                <tbody>
                    <CartItem
                        v-for="item in cart.items"
                        v-bind:key="item.product.id"
                        v-bind:initialItem="item"
                        v-on:removeFromCart="removeFromCart" />
                </tbody>
            </table>
            <p v-else>You don't have any products in your cart...</p>
        </div>
        
        <div class="">
            <h2 class="subtitle">Summary</h2>

            <strong>${{ cartTotalPrice}}</strong>, {{ cartTotalLength }} items

            <hr>

            <router-link to="/checkout" class="button is-dark">Proceed to checkout</router-link>
        </div>
        
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import CartItem from '../components/CartItem.vue'

export  default{
    name: 'Cart',
    components:{
        CartItem
    },
    data(){
        return{
            cart:{
                items:[]
            }
        }
    },
    mounted(){
        this.cart = this.$store.state.cart
    },
    methods:{
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        }
    },
    computed: {
        cartTotalLength() {    
            return this.cart.items.reduce((acc, curVal) => {   //reduce js內建函數
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
    }
}
</script>