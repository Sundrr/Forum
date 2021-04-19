<template>
  <header>
    <h3>{{ currentSectionName }}</h3>
    <base-button link :to="newThreadRoute">Новая тема</base-button>
  </header>
  <main>
    <base-container>
      <div class="name-column"><h4>Темы</h4></div>
      <div><h4>Ответы</h4></div>
      <div><h4>Просмотры</h4></div>
      <div><h4>Последнее сообщение</h4></div>
    </base-container>
    <ul v-if="!loading">
      <thread-item
        v-for="thread in threads"
        :key="thread.id"
        :id="thread.id"
        :name="thread.name"
        :creator="thread.username"
        :created="thread.created_dt"
        :view-count="thread.views"
        :post-count="thread.post_count"
        :tag="sectionTag"
      ></thread-item>
    </ul>
  </main>
</template>


<script>
import ThreadItem from "../elements/ThreadItem.vue";
import BaseButton from "../ui/BaseButton.vue";

export default {
  components: { ThreadItem, BaseButton },
  created() {
    // this.$store.commit("setCurrentSectionId", this.$route.params.sectionId);
    this.$store.commit("setCurrentSectionId", this.sectionId);
    this.$store.commit("setCurrentThreadId", null);
    this.loadThreads();
  },
  props: {
    sectionId: { type: Number },
    sectionTag: { type: String },
  },
  data() {
    return {
      loading: false,
    };
  },
  methods: {
    async loadThreads() {
      this.loading = true;
      try {
        this.$store.dispatch("uploadThreads", this.currentSectionId);
      } catch (error) {
        console.log(error);
      }
      this.loading = false;
    },
  },
  computed: {
    currentSectionId() {
      return this.$store.getters.getCurrentSectionId;
    },
    currentSectionName() {
      return this.$store.getters.getCurrentSectionName;
    },
    threads() {
      return this.$store.getters.getCurrentSectionThreads;
    },
    newThreadRoute() {
      return {
        name: "new-thread",
        params: {
          sectionTag: this.sectionTag,
        },
      };
    },
  },
};
</script>


<style scoped>
.name-column {
  width: 40rem;
}
</style>