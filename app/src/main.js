import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import axios from 'axios';

console.log('starting vue application.');
axios.defaults.baseURL = 'http://localhost:5000/api';

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
