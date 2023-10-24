<template>
  <div class="app">
    <Navbar/>
    <router-view/>

    <!-- loading bar -->
    <div class="d-flex justify-content-center " v-if="$store.state.isLoading">
      <div class="spinner-border text-warning"  >
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    
  </div>
  
</template>


<script setup>
import { RouterView } from 'vue-router';
import Navbar from './components/Navbar.vue';
</script>


<style scoped>

</style>
