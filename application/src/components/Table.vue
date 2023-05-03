<script setup>

import {computed} from "vue";

const whatever = computed({

    get() {
        console.log('check')
        return 'check?';
    }
})

defineProps({
    fields:{
        type: Array,
        // required: true
    },
    studentData: {
        type: Array,
        // required: true
    },
    sortDirection: 1,
    sortBy: 'name',

})

function sortedProperties() {
      const type = this.sortBy === 'name' ? 'String' : 'Number'
      const direction = this.sortDirection
      const head = this.sortBy
      // here is the magic
      return this.properties.sort(this.sortMethods(type, head, direction))
    }


function sort(head) {
      this.sortBy = head
      this.sortDirection *= -1
}

function sortMethods(type, head, direction) {
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

function sortTable(field) {
    console.log(field)
} 


// compatConfig: { MODE: 3 }
</script>

<template>

<table id="tableComponent" class="table table-bordered table-striped">
<thead>
  <tr>
    <!-- loop through each value of the fields to get the table header -->
    <th  v-for="field in fields" :key='field' @click="sort(field)" > 
      {{field}} <i class="bi bi-sort-alpha-down" aria-label='Sort Icon'></i>
     </th>
  </tr>
</thead>
<tbody>
    <!-- Loop through the list get the each student data -->
    <tr v-for="item in studentData" :key='item'>
    <td v-for="field in fields" :key='field'>{{item[field]}}</td>
  </tr>
</tbody>
</table> 

<p>{{ whatever }}</p>
</template>

