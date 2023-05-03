<template>
<div id="order-table">
  <table>
    <thead>
      <tr>
        <th v-for="head in headers" @click="sort(head)">
        {{ head.label }}
        </th>
      </tr>
    </thead>
    
    <tbody>
      <tr v-for="(data, i) in sortedProperties" :key="data.id">
          <td v-for="(head, idx) in headers" :key="head.id">
              {{ data[head.label] }}
          </td>
        </tr>
    </tbody>
  </table>
</div>

</template>

<script>

export default {
  props: {
    fields: Array,
    orderData: Array
  },
  data() {
    return {
      headers: this.fields,
      properties: this.orderData,
      sortDirection: 1,
      sortBy: 'orderNumber'
    }
  },
  computed: {
    sortedProperties() {
        //console.log(this.sortBy+ "x")
      const type = this.sortBy === 'orderNumber' ? 'Number' : 'String'
      const direction = this.sortDirection
      //const head = {label: this.sortBy}
      const head = this.sortBy
      console.log(type+" "+direction+" "+head)
      // here is the magic
      return this.properties.sort(this.sortMethods(type, head, direction))
    }
  },
  methods: {
    sort(head) {
      //this.sortBy = head.label
      this.sortBy = head.label
      this.sortDirection *= -1
      console.log(this.sortBy)
    },
    sortMethods(type, head, direction) {
       switch (type) {
          case 'String': {
            return direction === 1 ?
              (a, b) => b[head] > a[head] ? -1 : a[head] > b[head] ? 1 : 0 :
              (a, b) => a[head] > b[head] ? -1 : b[head] > a[head] ? 1 : 0 
          }
          case 'Number': {
            return direction === 1 ?
              (a, b) => Number(b[head]) - Number(a[head]) :
              (a, b) => Number(a[head]) - Number(b[head])
          } 
       }
    }
  }
  }
</script>