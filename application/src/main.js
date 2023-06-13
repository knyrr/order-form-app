import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
/* import dotenv from 'dotenv'
dotenv.config() */
/* import { env } from '@next/env'

env({
  // Specify the path to your .env file
  path: '.env'
}) */

import './assets/main.css'

const app = createApp(App)
app.use(VueAxios, axios)
app.provide('axios', app.config.globalProperties.axios)
app.mount('#app')
