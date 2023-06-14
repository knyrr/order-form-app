import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import './assets/main.css'
import Toast, { POSITION } from 'vue-toastification'
import 'vue-toastification/dist/index.css'

const app = createApp(App)
app.use(VueAxios, axios)

const options = {
  transition: 'Vue-Toastification__bounce',
  position: POSITION.BOTTOM_RIGHT,
  timeout: 2000
}

app.use(Toast, options)

app.provide('axios', app.config.globalProperties.axios)
app.mount('#app')
