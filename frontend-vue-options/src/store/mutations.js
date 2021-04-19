export default {
    setToken(state, token) {
        state.token = token;
    },

    setUser(state, user) {
        state.user = user;
    },

    setCurrentSectionId(state, sectionId) {
        state.currentSectionId = parseInt(sectionId);
    },

    setCurrentThreadId(state, threadId) {
        state.currentThreadId = parseInt(threadId);
    },

    setCurrentPage(state, currentPage) {
        state.currentPage = parseInt(currentPage);
    },

    setTotalPages(state, totalPages) {
        state.totalPages = parseInt(totalPages);
    },

    setTotalPosts(state, totalPosts) {
        state.totalPosts = parseInt(totalPosts);
    },
   
    uploadSections(state, payload) {
        state.sections = payload;
    },

    uploadSectionThreads(state, payload) {
        state.sectionThreads = payload;
    },

    uploadThreadPosts(state, payload) {
        state.threadPosts = payload;
    },

    uploadUsers(state, payload) {
        state.users = payload;
    }
};