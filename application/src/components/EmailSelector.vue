<script>
export default {
  props: ['employees'],
  mounted() {
    console.log("meilivaliku leht on laaditud")
  }
}
</script>

<template>
  <div>
    <p>Praegune meil on: XXX kohalikult kettalt </p>
    <form>
      <label for="email-list">Muuda meiliaadressi:</label>
      <select name="email-list" id="email-list">
        <option v-for="employee in employees" :value=employee.id>{{ employee.email }}</option>
      </select>
      <input type="submit" value="Muudan">
    </form>
  </div>
</template>

<style></style>
