<template>
  <base-container>
    <div class="name-column"><h4>Разделы</h4></div>
    <div><h4>Темы</h4></div>
    <div><h4>Сообщения</h4></div>
    <div><h4>Последнее сообщение</h4></div>
  </base-container>
  <ul>
    <section-item
      v-for="section in sections"
      :key="section.id"
      :id="section.id"
      :name="section.name"
      :description="section.description"
      :tag="section.tag"
      :thread-count="section.thread_count"
      :post-count="section.post_count"
      :last-username="section.username"
      :last-date="section.created_dt"
    ></section-item>
  </ul>
</template>


<script>
import SectionItem from "../elements/SectionItem.vue";

export default {
  components: { SectionItem },
  created() {
    this.$store.commit("setCurrentSectionId", null);
    this.$store.commit("setCurrentThreadId", null);
    this.loadSections();
  },
  methods: {
    async loadSections() {
      try {
        this.$store.dispatch("uploadSections");
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    sections() {
      return this.$store.getters.getSections;
    },
  },
};
</script>


<style scoped>
.name-column {
  width: 40rem;
}
</style>

