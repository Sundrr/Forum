<template>
  <header>
    <h3>{{ currentThreadName }}</h3>
    <base-button link :to="newPostRoute">Ответить</base-button>
    <p>Сообщений: {{ postCount }}</p>
    <p>Страница {{ page }} из {{ pageCount }}</p>
    <thread-paginator
      :answers="postCount"
      :id="currentThreadId"
      :tag="currentSectionTag"
      :current-page="page"
    ></thread-paginator>
  </header>
  <main>
    <ul>
      <post-item
        v-for="post in posts"
        :key="post.id"
        :id="post.id"
        :text="post.text"
        :username="post.username"
        :created="post.created"
      ></post-item>
    </ul>
  </main>
</template>


<script>
import PostItem from "../elements/PostItem.vue";
import ThreadPaginator from "../elements/ThreadPaginator.vue";

export default {
  components: { PostItem, ThreadPaginator },
  created() {
    this.$store.commit("setCurrentThreadId", this.threadId);
    this.loadPosts();
  },
  props: {
    sectionTag: { type: String },
    threadId: { type: Number },
    page: { type: Number },
  },
  data() {
    return {};
  },
  methods: {
    async loadPosts() {
      try {
        this.$store.dispatch("uploadPosts", {
          threadId: this.currentThreadId,
          page: this.page,
        });
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    currentThreadName() {
      return this.$store.getters.getCurrentThreadName;
    },
    currentThreadId() {
      return this.$store.getters.getCurrentThreadId;
    },
    currentSectionTag() {
      return this.$store.getters.getCurrentSectionTag;
    },
    posts() {
      return this.$store.getters.getCurrentThreadPosts;
    },
    postCount() {
      return this.$store.getters.getTotalThreadPostsCount;
    },
    pageCount() {
      return this.$store.getters.getTotalThreadPagesCount;
    },
    newPostRoute() {
      return {
        name: "new-post",
        params: {
          sectionTag: this.sectionTag,
          threadId: this.currentThreadId,
        },
      };
    },
  },
  watch: {
    page() {
      this.loadPosts();
    },
  },
};
</script>


<style scoped>
</style>