<script>
import { ref, onMounted, toRef, getCurrentInstance } from 'vue'
import { onClickOutside } from '@vueuse/core'

const inner_modal = ref(null)

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
      sortBy: 'orderNumber',
      showModal: false,
      modalData: null,
    }
  },
  mounted() {
    console.log("tabeli moodul on laaditud")
    console.log('modal ref:', inner_modal)
  },
  computed: {
    sortedProperties() {
      console.log(this.orderData)
      const type = this.sortBy === 'orderNumber' ? 'Number' : 'String'
      const direction = this.sortDirection
      const head = this.sortBy
      return this.properties.sort(this.sortMethods(type, head, direction))
    }
  },
  methods: {
    sort(head) {
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
    },
    openOrderFrom(data) {
      console.log(data)
      this.modalData = data
      this.showModal = true
      const modalRef = toRef(this.$refs, 'inner_modal')
      console.log('modal ref:', modalRef)

      onClickOutside(modalRef, () => {
        this.showModal = false
        console.log("kinni")
        console.log(this.showModal)
      })
    },
  },

}

</script>

<template>
  <Teleport to="#modal">
    <div class="modal-bg" v-if="showModal">
      <div class="modal" ref="inner_modal">
        <p>hello world!</p>
        <button @click="this.showModal = false" class="close-btn">×</button>
      </div>
    </div>
  </Teleport>
  <div id="order-table">
    <table>
      <thead>
        <tr>
          <th v-for="head in headers" @click="sort(head)">
            {{ head.title }}
          </th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(data, i) in sortedProperties" :key="data.id">
          <td v-for="(head, idx) in headers" :key="head.id">
            <template v-if="head.label === 'buttons'">
              <button @click="openOrderFrom(data)">
                Ava
              </button>
            </template>
            <template v-else>
              {{ data[head.label] }}
            </template>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style>
.modal-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  position: relative;
  background: white;
  padding: 50px 100px;
  border-radius: 5px;
  box-shadow: 0px 10px 5px 2px, rgba(0, 0, 0, 0.1);
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  cursor: pointer
}
</style>