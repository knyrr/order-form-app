<script>
export default {
  props: ['employees'],
  data() {
    return {
      selected: null,
      email: null,
      showEmployeeSelect: false
    }
  },
  methods: {
    submit() {
      this.saveStorage("user", this.selected)
      this.email = this.employees.find(x => x.id === parseInt(this.selected)).email
      this.toggleEmployeeSelect()

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
    },
    toggleEmployeeSelect() {
      this.showEmployeeSelect = !this.showEmployeeSelect
    }
  },
  mounted() {
    const userFromLocalStorage = this.getStorage("user")
    this.selected = userFromLocalStorage === undefined ? null : userFromLocalStorage
    if (this.selected != null) {
      this.email = this.employees.find(x => x.id === parseInt(this.selected)).email
    } else {
      this.showEmployeeSelect = true
    }
  },
}
</script>

<template>
  <div>
    <p>Praegune meil on: {{ email ? email : 'kohalikul kettal puudub' }} </p>
    <button v-if="!showEmployeeSelect" @click="toggleEmployeeSelect">Muudan</button>
    <form v-if="showEmployeeSelect">
      <label for="email-list">Muuda meiliaadressi:</label>
      <select name="email-list" id="email-list" v-model="selected">
        <option disabled :value="null" v-if="!selected">Vali töötaja</option>
        <option v-for="employee in employees" :value=employee.id>{{ employee.email }}</option>
      </select>
      <input type="submit" value="Valin" @click.prevent="submit">
    </form>
  </div>
</template>

<style></style>
