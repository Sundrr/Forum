import { createApp } from 'vue';
// import { createStore } from 'vuex';
import App from './App.vue';
import router from './router.js';
import store from './store/index.js';
import BaseButton from './components/ui/BaseButton';
import BaseContainer from './components/ui/BaseContainer';

const app = createApp(App);
// const store = createStore(storeIndex);

app.use(router);
app.use(store);
app.component('base-button', BaseButton);
app.component('base-container', BaseContainer);
app.mount('#app');

