<script>
export default {
  props: ['employees'],
  data() {
    return {
      selected: null,
      email: null,
    }
  },
  methods: {
    submit() {
      this.saveStorage("user", this.selected)
      this.email = this.employees.find(x => x.id === parseInt(this.selected)).email

      //saada põhikomponendile
      //this.$emit('submit', this.selected)
    },
    saveStorage(key, data) {
      localStorage.setItem(key, JSON.stringify(data))
    },
    getStorage(key) {
      if (localStorage.getItem(key)) {
        return localStorage.getItem(key)
      }
    }
  },
  mounted() {
    const userFromLocalStorage = this.getStorage("user")
    this.selected = userFromLocalStorage === undefined ? null : userFromLocalStorage
    if (this.selected != null) {
      this.email = this.employees.find(x => x.id === parseInt(this.selected)).email
    }
  },
}
</script>

<template>
  <div>
    <p>Praegune meil on: {{ email ? email : 'kohalikul kettal puudub' }}
    </p>
    <form>
      <label for="email-list">Muuda meiliaadressi:</label>
      <select name="email-list" id="email-list" v-model="selected">
        <option disabled :value="null" v-if="!selected">Vali töötaja</option>
        <option v-for="employee in employees" :value=employee.id>{{ employee.email }}</option>
      </select>
      <input type="submit" value="Muudan" @click.prevent="submit">
    </form>
  </div>
</template>

<style></style>
