<template>
  <h2>{{ inputHeader }}</h2>
  <h4>{{ inputDescription }}</h4>
  <form @submit.prevent="createNewPost">
    <div class="form-control">
      <label for="name">Заголовок</label>
      <input type="text" id="name" v-model.trim="threadName" />
    </div>
    <div class="form-control">
      <textarea id="text" rows="5" v-model.trim="text"></textarea>
    </div>
    <base-button>Создать</base-button>
    <p v-if="!formIsValid">Введены некорректные данные</p>
  </form>
</template>


<script>
export default {
  created() {
    this.sectionId = this.$store.getters.getCurrentSectionId;
    this.threadName = this.$store.getters.getCurrentThreadName;
  },
  // props: ['sectionTag', 'threadId'],
  props: {
    sectionTag: {
      type: String,
      required: true,
    },
    threadId: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      sectionId: null,
      threadName: null,
      text: null,
      formIsValid: true,
    };
  },
  methods: {
    validateForm() {
      this.formIsValid = true;
      if (this.text.length === 0 || this.threadName.length === 0) {
        this.formIsValid = false;
      }
    },
    async createNewPost() {
      this.validateForm();
      if (!this.formIsValid) {
        return;
      }

      const payload = {
        sectionId: this.sectionId,
        threadId: this.threadId,
        threadName: this.threadName,
        text: this.text,
      };

      try {
        await this.$store.dispatch("createNewPost", payload);
      } catch (e) {
        this.error = e.message || "Не удалось создать пост";
      }
      const newThreadId = this.$store.getters.getCurrentThreadId;
      const currentSectionTag = this.$store.getters.getCurrentSectionTag;
      this.$router.replace({
        name: "post-list",
        params: { 
          threadId: newThreadId,
          sectionTag: currentSectionTag,
          },
      });
    },
  },
  computed: {
    inputHeader() {
      return this.threadId ? this.threadName : this.$store.getters.getCurrentSectionName;
    },
    inputDescription() {
      return this.threadId ? 'Ответить' : 'Новая тема'
    }
  }
};
</script>


<style scoped>
</style>