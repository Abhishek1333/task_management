<template>
  <div class="flex justify-center items-center h-screen">
    <div class="bg-white p-8 shadow w-80">
      <h2 class="text-xl mb-4">Login</h2>

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

      <button class="bg-indigo-600 text-white w-full py-2" @click="login">
        Login
      </button>

      <p class="mt-4 text-center">
        <router-link to="/register">Register</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import api from "../services/api";

const email = ref("");
const password = ref("");
const router = useRouter();

async function login() {
  try {
    const res = await api.post("/login", {
      email: email.value,
      password: password.value,
    });

    localStorage.setItem("token", res.data.access_token);

    router.push("/dashboard");
  } catch (e) {
    alert("Login failed");
  }
}
</script>
