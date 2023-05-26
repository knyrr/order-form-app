<script setup>
import { inject, onMounted, onUpdated, ref } from 'vue'
import EmailSelector from './components/EmailSelector.vue'
import OrderTable from './components/OrderTable.vue'

const axios = inject('axios')
/* const employeeData = ref([])
const orderData = ref([])
const orderLineData = ref([])
const clientData = ref([])
const productData = ref([])
const consolidatedData = ref([]) */

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
      console.log(employeeData)
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
      //clientData.value = response.data
      clientData = response.data
      //console.log(clientData)
    })
    .catch(error => {
      console.log(error)
    })



  //toodete andmed
  await axios
    .get('http://127.0.0.1:8000/api/products/')
    .then(response => {
      //productData.value = response.data
      productData = response.data
      //console.log(JSON.parse(JSON.stringify(productData.value)))
    })
    .catch(error => {
      console.log(error)
    })

  //tellimuste ridade andmed
  await axios
    .get('http://127.0.0.1:8000/api/order-form-lines/')
    .then(response => {
      //orderLineData.value = response.data
      orderLineData = response.data
      //console.log(orderLineData)
    })
    .catch(error => {
      console.log(error)
    })

  //tellimuste andmed
  await axios
    .get('http://127.0.0.1:8000/api/order-forms/')
    .then(response => {
      //orderData.value = response.data
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
      clientName: client.name,
      clientCode: client.code,
      date: element.date,
      status: element.status,
      lines: [...orderLineData.filter(x => x.order === element.order_form).map(item => {
        let line = {
          productName: productData.find(x => x.id === item.product).name,
          quantity: item.quantity
        }
        return line
      })]
    }
    consolidatedOrderData.push(item)
  })

  console.log(consolidatedOrderData)
  showOrderTable.value = true
  orderTableKey.value++
})

onUpdated(() => {
  console.log("andmeid on uuendatud")
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

<template>
  <header>
    <div v-if="showEmailSelector" :key="emailSelectorKey">
      <EmailSelector :employees="employeeData" />
    </div>
  </header>

  <main>
    <OrderTable v-if="showOrderTable" :key="orderTableKey" :fields="fields" :orderData="consolidatedOrderData" />
  </main>
</template>

<style></style>
