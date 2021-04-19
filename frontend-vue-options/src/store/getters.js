export default {
    getToken(state) {
        return state.token;
    },

    isAuthenticated(state) {
        return !!state.token;
    },

    activeUser(state) {
        return state.user;
    },

    getUsers(state) {
        return state.users;
    },

    getSections(state) {
        return state.sections;
    },

    getCurrentSectionId(state) {
        return state.currentSectionId;
    },

    getCurrentSectionTag(state) {
        if (state.currentSectionId) {
            const currentSection = state.sections.find(section => section.id === state.currentSectionId);
            return currentSection.tag;
        }
    },

    getCurrentSectionName(state) {
        if (state.currentSectionId) {
            const currentSection = state.sections.find(section => section.id === state.currentSectionId);
            return currentSection.name;
        }
        return
    },

    getCurrentThreadId(state) {
        return state.currentThreadId;
    },

    getCurrentThreadName(state) {
        if (state.currentThreadId) {
            const currentThread = state.sectionThreads.find(thread => thread.id === state.currentThreadId);
            return currentThread.name;
        }
        return
    },

    getCurrentSectionThreads(state) {
        return state.sectionThreads;
    },

    getCurrentThreadPosts(state) {
        return state.threadPosts;
    },

    getTotalThreadPostsCount(state) {
        return state.totalPosts;
    },

    getTotalThreadPagesCount(state) {
        return state.totalPages;
    },
};