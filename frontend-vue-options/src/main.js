import { createApp } from 'vue';
// import { createStore } from 'vuex';
import App from './App.vue';
import router from './router.js';
import store from './store/index.js';
import BaseButton from './components/ui/BaseButton.vue';
import BaseContainer from './components/ui/BaseContainer.vue';
import BaseWrapper from './components/ui/BaseWrapper.vue';

const app = createApp(App);
// const store = createStore(storeIndex);

app.use(router);
app.use(store);
app.component('base-button', BaseButton);
app.component('base-container', BaseContainer);
app.component('base-wrapper', BaseWrapper);
app.mount('#app');

