<script setup>
import { inject, onMounted, onUpdated, ref } from 'vue'
import OrderTable from './components/OrderTable.vue'

const axios = inject('axios')

let employeeData = []
let orderData = []
let orderLineData = []
let clientData = []
let productData = []
let consolidatedOrderData = []

const showEmailSelector = ref(false)
const emailSelectorKey = ref(0)

const showOrderTable = ref(false)
const orderTableKey = ref(0)

onMounted(async () => {
  //töötajate andmed
  await axios
    .get('http://127.0.0.1:8000/api/employees/')
    .then(response => {
      employeeData = response.data
      showEmailSelector.value = true
      emailSelectorKey.value++

    })
    .catch(error => {
      console.log(error)
    })

  //klientide andmed
  await axios
    .get('http://127.0.0.1:8000/api/clients/')
    .then(response => {
      clientData = response.data
    })
    .catch(error => {
      console.log(error)
    })

  //toodete andmed
  await axios
    .get('http://127.0.0.1:8000/api/products/')
    .then(response => {
      productData = response.data
    })
    .catch(error => {
      console.log(error)
    })

  //tellimuste ridade andmed
  await axios
    .get('http://127.0.0.1:8000/api/order-form-lines/')
    .then(response => {
      orderLineData = response.data
    })
    .catch(error => {
      console.log(error)
    })

  //tellimuste andmed
  await axios
    .get('http://127.0.0.1:8000/api/order-forms/')
    .then(response => {
      orderData = response.data
      console.log(orderData)
    })
    .catch(error => {
      console.log(error)
    })

  orderData.forEach(element => {
    let client = clientData[clientData.findIndex(x => x.id === element.client)]
    let item = {
      id: element.id,
      orderNumber: element.number,
      clientId: element.client,
      clientName: client.name,
      clientCode: client.code,
      date: element.date,
      status: element.status,
      lines: [...orderLineData.filter(x => x.order_form === element.id).map(item => {
        let line = {
          productName: productData.find(x => x.id === item.product).name,
          quantity: item.quantity
        }
        return line
      })]
    }
    consolidatedOrderData.push(item)
  })
  showOrderTable.value = true
  orderTableKey.value++
  console.log(consolidatedOrderData)
})


const fields = [
  {
    label: "orderNumber",
    title: "Tellimuse nr",
  },
  {
    label: "clientName",
    title: "Klient",
  },
  {
    label: "clientCode",
    title: "Kliendikood",
  },
  {
    label: "date",
    title: "Kuupäev",
  },
  {
    label: "status",
    title: "Olek",
  },
  {
    label: "buttons",
    title: "Nupud",
  }
]

</script>

<template >
  <div class="app">
    <main>
      <h1>Tellimusvormide saatmine</h1>
      <OrderTable v-if="showOrderTable" :key="orderTableKey" :fields="fields" :orderData="consolidatedOrderData"
        :employees="employeeData" />
      <div id="modal"></div>
    </main>
  </div>
</template>

<style>
button,
input {
  background-color: #4CAF50;
  margin: 0px 10px;
  border: none;
  color: white;
  padding: 5px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
}

.app {
  margin: 25px;
}
</style>
