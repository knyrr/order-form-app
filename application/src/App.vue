<script setup>
import EmailSelector from './components/EmailSelector.vue'
import OrderList from './components/OrderList.vue'
</script>

<template>
  <header>
    <div class="wrapper">
      <EmailSelector/>
    </div>
  </header>

  <main>
    <OrderList msg="You did it!" />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
