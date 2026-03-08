<template>
  <div>
    <h1 class="text-2xl font-bold mb-6">All Users</h1>

    <div
      v-for="u in users"
      :key="u.id"
      class="bg-white p-4 shadow mb-2 rounded"
    >
      {{ u.email }}
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../services/api";

const users = ref([]);

async function load() {
  const res = await api.get("/users");

  users.value = res.data;
}

onMounted(load);
</script>
