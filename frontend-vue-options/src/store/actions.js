import axios from 'axios';

import userData from "../data/users.js";

export default {
    async loginUser(context, payload) {
        const response = await axios.post(`http://127.0.0.1:5000/auth/login`, payload);

        if (response.status !== 200) {
            console.log('error', response);
            const error = new Error(
                response.message || 'Ошибка авторизации'
            );
            throw error;
        }
        const token = response.data;
        const user = payload.username;
        context.commit('setToken', token);
        context.commit('setUser', user);
    },

    async registerUser(context, payload) {
        const response = await axios.post('http://127.0.0.1:5000/auth/register', payload);

        if (response.status !== 201) {
            console.log('error', response);
            const error = new Error(
                response.message || 'Ошибка авторизации'
            );
            throw error;
        }
        const token = response.data;
        const user = payload.username;
        context.commit('setToken', token);
        context.commit('setUser', user);
    },

    async uploadSections(context) {
        const response = await axios.get('http://127.0.0.1:5000/sections/full_list');
        const sections = response.data;
        context.commit('uploadSections', sections);
    },

    async uploadThreads(context, payload) {
        const response = await axios.get(`http://127.0.0.1:5000/threads/${payload}`);
        const threads = response.data;
        context.commit('uploadSectionThreads', threads);
    },

    async uploadPosts(context, payload) {
        const response = await axios.get(`http://127.0.0.1:5000/posts/${payload.threadId}?page=${payload.page}`);
        const threadPosts = response.data.data;
        const currentPage = response.data.page;
        const totalPages = response.data.pages_total;
        const totalPosts = response.data.total;
        context.commit('uploadThreadPosts', threadPosts);
        context.commit('setCurrentPage', currentPage);
        context.commit('setTotalPages', totalPages);
        context.commit('setTotalPosts', totalPosts);
    },

    async createNewPost(context, payload) {
        const config = {
            headers: {
                Authorization: context.getters.getToken
            }
        };
        const data = {
            section_id: payload.sectionId,
            thread_id: payload.threadId,
            thread_name: payload.threadName,
            text: payload.text,
        };
        const response = await axios.post('http://127.0.0.1:5000/threads/create', data, config);
        
        if (response.status !== 201) {
            console.log('error', response);
            const error = new Error(
                response.message || 'Ошибка авторизации'
            );
            throw error;
        }
        const currentSectionId = context.getters.getCurrentSectionId;
        await context.dispatch('uploadThreads', currentSectionId);
        context.commit('setCurrentThreadId', response.data);
        // context.commit('setCurrentThreadName', response.data);
    },

    uploadUsers(context) {
        const users = userData;
        context.commit('uploadUsers', users);
    }
};
