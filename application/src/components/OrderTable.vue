<script>
import { ref, toRef, watch, Teleport } from 'vue'
import { onClickOutside } from '@vueuse/core'
import { jsPDF } from 'jspdf'
import 'jspdf-autotable'
import axios from 'axios'
import EmailSelector from './EmailSelector.vue'


export default {
  props: {
    fields: Array,
    orderData: Array,
    employees: Array
  },
  components: {
    Teleport
  },
  data() {
    return {
      headers: this.fields,
      properties: this.orderData,
      sortDirection: -1,
      sortBy: 'orderNumber',
      showModal: false,
      modalData: null,
      modalHeaders: [
        {
          label: "productName",
          title: "Toote nimetus",
        },
        {
          label: "quantity",
          title: "Kogus",
        }
      ],
      selected: null,
      selectedError: null,
      selectedEmail: null,
    }
  },
  computed: {
    sortedProperties() {
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
      this.modalData = data
      this.showModal = true
    },
    createPDF() {
      const doc = new jsPDF();
      var x = 20
      var y = 20
      var ln = 5

      doc.setFontSize(16);
      doc.text("Tellimusvorm", x, y)
      y += ln + 5

      doc.setFontSize(10);
      doc.text("Tellimuse nr:", x, y)
      doc.text(this.modalData.orderNumber.toString(), x + 40, y)
      y += ln
      doc.text("Kliendi nimi:", x, y)
      doc.text(this.modalData.clientName, x + 40, y)
      y += ln
      doc.text("Kliendi kood:", x, y)
      doc.text(this.modalData.clientCode, x + 40, y)
      y += ln
      doc.text("Kuupäev:", x, y)
      doc.text(this.modalData.date.toString(), x + 40, y)
      y += ln

      const headers = this.modalHeaders.map(header => header.title);
      const data = this.modalData.lines.map(line => this.modalHeaders.map(header => line[header.label]));

      doc.autoTable({
        head: [headers],
        body: data,
        startY: y
      });
      return doc

    },
    downloadPDF() {
      const doc = this.createPDF()
      doc.save('a4.pdf');
    },
    sendPDF() {
      if (this.selected != null) {
        this.selectedError = null
        this.email = this.employees.find(x => x.id === parseInt(this.selected)).email
        var doc = this.createPDF()
        const pdfDataUrl = doc.output('datauristring')

        axios
          .post('http://127.0.0.1:8000/api/send-pdf/', { pdfDataUrl, email_to: this.selectedEmail })
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
      } else {
        this.selectedError = "Vali meiliaadress"
      }

    }
  },
  watch: {
    showModal(value) {
      if (value) {
        this.$nextTick(() => {
          this.modalRef = toRef(this.$refs, 'modal')
          onClickOutside(this.modalRef, () => {
            this.showModal = false
          })
        })
      }
    }
  }

}

</script>

<template>
  <Teleport to="#modal">
    <div class="modal-bg" v-if="showModal">
      <div class="modal" ref="modal">
        <button @click="this.showModal = false" class="close-btn">×</button>
        <div id="modal-content" ref="content">
          <h1>Tellimusvorm</h1>
          <div>Tellimuse nr: {{ modalData.orderNumber }}</div>
          <div>Kliendi nimi: {{ modalData.clientName }}</div>
          <div>Kliendi kood: {{ modalData.clientCode }}</div>
          <div>Kuupäev: {{ modalData.date }}</div>
          <div>Olek: {{ modalData.status }}</div>

          <table>
            <thead>
              <tr>
                <th v-for="head in modalHeaders">
                  {{ head.title }}
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(line, i) in  modalData.lines" :key="modalHeaders.id">
                <td v-for="(head, idx) in modalHeaders" :key="head.id">
                  {{ line[head.label] }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <form class="email-form">
          <label for="email-list">Saaja:</label>
          <select name="email-list" id="email-list" v-model="selected">
            <option disabled :value="null" v-if="!selected">Vali töötaja</option>
            <option v-for="employee in employees" :value=employee.id>{{ employee.email }}</option>
          </select>
          <input type="submit" value="Saadan" @click.prevent="sendPDF()">
          <p v-if="!selected && selectedError" class="error-message">{{ selectedError }}</p>
        </form>

        <button @click="downloadPDF()">Laadin alla</button>

        <button @click="showModal = false">Sulgen</button>


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
table {
  margin-bottom: 25px;
}

th {
  font-weight: bold;
}

th,
td {
  padding: 15px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

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
  min-width: 60vw;
  background: white;
  padding: 50px 100px;
  border-radius: 5px;
  box-shadow: 0px 10px 5px 2px, rgba(0, 0, 0, 0.1);
}

.close-btn {
  position: absolute;
  color: black;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  cursor: pointer
}

.email-form {
  margin-bottom: 20px;
}

.error-message {
  color: red;
  font-size: 12px;
}
</style>