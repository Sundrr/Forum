<template>
  <header>
    <h3>{{ currentSectionName }}</h3>
    <base-button link :to="newThreadRoute" mode="main">Новая тема</base-button>
  </header>
  <main>
    <base-wrapper>
      <base-container class="header-containter">
        <template #name-block>
          <div class="name-column"><h4>Темы</h4></div>
        </template>
        <template #stat-block>
          <div><h4>Ответы</h4></div>
        </template>
        <template #count-block>
          <div><h4>Просмотры</h4></div>
        </template>
        <template #user-block>
          <div><h4>Последнее сообщение</h4></div>
        </template>
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
    </base-wrapper>
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
ul {
  margin: 0;
  padding: 0;
}

h3 {
  color: #105289;
}

h4 {
  margin: 4px 0;
}
</style>