<!-- <script setup>
defineProps({
  employees: {
    type: Array,
    required: true
  }
})
</script> -->

<script>
export default {
  props: {
    employees: Array
  },
  data() {
    return {
      employees: this.employees
    }
  }
}
</script>

<template>
  <div>
    <p>Praegune meil on: XXX </p>
    <form action="/action_page.php">
      <label for="email-list">Muuda meiliaadressi:</label>
      <select name="email-list" id="email-list">
        <option value="1">{{ employees }}</option>
        <option value="2">Saab</option>
        <option value="3">Mercedes</option>
        <option value="4">Audi</option>
      </select>
      <input type="submit" value="Muudan">
    </form>
  </div>
</template>

<style scoped>
/* h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.order-list h1,
.order-list h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .order-list h1,
  .order-list h3 {
    text-align: left;
  }
} */
</style>
