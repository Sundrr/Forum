import { createStore } from 'vuex';

import mutations from './mutations.js';
import actions from './actions.js';
import getters from './getters.js';

const store = createStore({
    state() {
        return {
            token: null,
            user: null,
            sections: [],
            sectionThreads: [],
            threadPosts: [],
            users: [],
            currentSectionId: null,
            currentThreadId: null,
            currentPage: null,
            totalPages: null,
            totalPosts: null,
        }
    },
    getters,
    mutations,
    actions
});

export default store;