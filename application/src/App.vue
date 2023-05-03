<script setup>
import { inject, onMounted, ref } from 'vue'
import EmailSelector from './components/EmailSelector.vue'
import OrderList from './components/OrderList.vue'
import Table from './components/Table.vue'
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

let showEmailSelector = false


onMounted(async () => {
  //töötajate andmed
  await axios
    .get('http://127.0.0.1:8000/api/employees/')
    .then(response => {
      //employeeData.value = response.data
      employeeData = response.data
      console.log(employeeData)
      showEmailSelector = true
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
      //console.log(orderData)
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
})

const studentData = [
  { ID: "01", Name: "Abiola Esther", Course: "Computer Science", Gender: "Female", Age: "17" },
  { ID: "02", Name: "Robert V. Kratz", Course: "Philosophy", Gender: "Male", Age: '19' },
  { ID: "03", Name: "Kristen Anderson", Course: "Economics", Gender: "Female", Age: '20' },
  { ID: "04", Name: "Adam Simon", Course: "Food science", Gender: "Male", Age: '21' },
  { ID: "05", Name: "Daisy Katherine", Course: "Business studies", Gender: "Female", Age: '22' },
]
//const fields = ['ID','Name','Course','Gender','Age']

//const fields = ['Tellimuse nr','Klient','Kliendikood','Kuupäev','Olek','Nupud']

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
    <EmailSelector :employees="employeeData" />
    <div v-if="showEmailSelector" class="wrapper">
      <EmailSelector :employees="employeeData" />
    </div>
  </header>

  <main>
    <!-- <OrderList msg="You did it!" :data="studentData"/> -->

    <OrderTable :fields="fields" :orderData="consolidatedOrderData" />
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
