import { createRouter, createWebHistory } from 'vue-router';

import SectionList from './components/pages/SectionList.vue';
import ThreadList from './components/pages/ThreadList.vue';
import PostList from './components/pages/PostList.vue';
import NewPost from './components/pages/NewPost.vue';
import Login from './components/users/Login.vue';
import Register from './components/users/Register.vue';
import UserList from './components/users/UserList.vue';
import UserProfile from './components/users/UserProfile';
import NotFound from './components/elements/NotFound.vue';
import store from './store/index.js';
import { propsConverter } from './utils.js';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            redirect: '/index'
        },
        {
            path: '/index',
            component: SectionList
        },
        {
            path: '/login',
            component: Login,
            meta: { requiresUnauth: true }
        },
        {
            path: '/register',
            component: Register,
            meta: { requiresUnauth: true }
        },
        {
            path: '/users',
            component: UserList
        },
        {
            path: '/users/:userId',
            component: UserProfile,
            props(route) {
                return propsConverter(route, UserProfile);
            },
        },
        {
            path: '/sections/:sectionTag/new',
            name: 'new-thread',
            component: NewPost,
            props(route) {
                return propsConverter(route, NewPost);
            },
            meta: { requiresAuth: true }
        },
        {
            path: '/sections/:sectionTag',
            name: 'thread-list',
            component: ThreadList,
            props(route) {
                return propsConverter(route, ThreadList);
            },
        },
        {
            path: '/sections/:sectionTag/:threadId/new',
            name: 'new-post',
            component: NewPost,
            props(route) {
                return propsConverter(route, NewPost);
            },
            meta: { requiresAuth: true }
        },
        {
            path: '/sections/:sectionTag/:threadId',
            name: 'post-list',
            component: PostList,
            props(route) {
                return propsConverter(route, PostList);
            },
        },
        {
            path: '/:notFound(.*)',
            component: NotFound
        },
    ]
});

router.beforeEach(function (to, from, next) {
    if (to.meta.requiresAuth && !store.getters.isAuthenticated) {
        store.commit('setCurrentSectionId', null);
        store.commit('setCurrentThreadId', null);
        next('/login');
    } else if (to.meta.requiresNoauth && store.getters.isAuthenticated) {
        next('/index');
    } else {
        next();
    }
})

export default router;