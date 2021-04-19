<template>
  <base-container>
    <form @submit.prevent="submitForm">
      <div class="form-control">
        <label for="username">Имя пользователя</label>
        <input type="text" id="username" v-model.trim="username" />
      </div>
      <div class="form-control">
        <label for="password">Пароль</label>
        <input type="password" id="password" v-model.trim="password" />
      </div>
      <p v-if="!formIsValid">Некорректные авторизационные данные</p>
      <base-button>Войти</base-button>
    </form>
  </base-container>
</template>


<script>
import BaseButton from "../ui/BaseButton.vue";
import BaseContainer from "../ui/BaseContainer.vue";

export default {
  components: { BaseContainer, BaseButton },
  data() {
    return {
      formIsValid: true,
      username: null,
      password: null,
    };
  },
  methods: {
    async submitForm() {
      this.formIsValid = true;
      if (!this.username || !this.password || this.password.length < 6) {
        this.formIsValid = false;
        return;
      }

      const payload = {
        username: this.username,
        password: this.password,
      };

      try {
        await this.$store.dispatch("loginUser", payload);
        this.$router.replace("/index");
      } catch (e) {
        this.error = e.message || "Ошибка авторизации";
      }
    },
  },
};
</script>


<style scoped>
</style>