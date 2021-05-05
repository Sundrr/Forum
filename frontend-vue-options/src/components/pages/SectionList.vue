<template>
  <base-wrapper>
    <base-container class="header-containter">
      <template #name-block>
        <div class="name-column"><h4>Разделы</h4></div>
      </template>
      <template #stat-block>
        <div><h4>Темы</h4></div>
      </template>
      <template #count-block>
        <div><h4>Сообщения</h4></div>
      </template>
      <template #user-block>
        <div><h4>Последнее сообщение</h4></div>
      </template>
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
  </base-wrapper>
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
ul {
  margin: 0;
  padding: 0;
}

h4 {
  margin: 4px 0;
}
</style>

