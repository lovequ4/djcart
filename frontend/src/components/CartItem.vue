<template>
  <tr>
        <td><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
        <td>${{ item.product.price }}</td>
        <td>
            <button class="btn btn-info btn-sm"  @click="decrementQuantity(item)" >
                <i class="fa-solid fa-minus fa-xs"></i>
            </button>
            
                {{ item.quantity }}
            
            <button class="btn btn-info btn-sm" @click="incrementQuantity(item)">
                <i class="fa-solid fa-plus fa-xs"></i>
            </button>    
            
        </td>
        <td>${{ getItemTotal(item)}}</td>
        <td><button class="btn btn-danger"  @click="removeFromCart(item)"><i class="fa-solid fa-trash-can"></i></button></td>
    </tr>
</template>


<script>
export default{
    name:'CartItem',
    props:{
        initialItem: Object
    },
    data(){
        return{
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        decrementQuantity(item) {
            item.quantity -= 1

            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }
           
            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1
           
            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)

            this.updateCart()
        },
    }
}

</script>


<style>

</style>