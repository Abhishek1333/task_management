<template>
  <div class="flex justify-center items-center h-screen">
    <div class="bg-white p-8 shadow w-80">
      <h2 class="text-xl mb-4">Register</h2>

      <input
        v-model="email"
        placeholder="Email"
        class="border p-2 w-full mb-2"
      />

      <input
        v-model="password"
        type="password"
        placeholder="Password"
        class="border p-2 w-full mb-4"
      />

      <button class="bg-indigo-600 text-white w-full py-2" @click="register">
        Register
      </button>

      <p class="mt-4 text-center">
        <router-link to="/">Back to Login</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import api from "../services/api";
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const router = useRouter();

async function register() {
  try {
    await api.post("/register", {
      email: email.value,
      password: password.value,
    });

    router.push("/");
  } catch (e) {
    alert("Registration failed");
  }
}
</script>
