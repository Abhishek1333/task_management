<template>
  <div>
    <nav class="bg-white shadow p-4 flex justify-between">
      <h1 class="font-bold text-indigo-600">Task Manager</h1>

      <div class="flex gap-6">
        <router-link to="/dashboard">Dashboard</router-link>

        <router-link to="/tasks">Tasks</router-link>

        <router-link v-if="isAdmin" to="/users">Users</router-link>

        <button @click="logout" class="text-red-500">Logout</button>
      </div>
    </nav>

    <div class="p-8">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import api from "../services/api";

const router = useRouter();
const isAdmin = ref(false);

function logout() {
  localStorage.removeItem("token");

  router.push("/");
}

onMounted(async () => {
  try {
    const res = await api.get("/info");

    if (res.data.role === "admin") {
      isAdmin.value = true;
    }
  } catch (e) {}
});
</script>
