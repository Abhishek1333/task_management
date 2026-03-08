<template>
  <div>
    <h1 class="text-2xl font-bold mb-6">Dashboard</h1>

    <div class="grid grid-cols-3 gap-6">

      <div class="bg-white shadow rounded-lg p-6">
        <h3 class="text-gray-500 mb-2">Todo</h3>

        <p class="text-3xl font-bold text-blue-600">
          {{ stats.todo }}
        </p>
      </div>


      <div class="bg-white shadow rounded-lg p-6">
        <h3 class="text-gray-500 mb-2">In Progress</h3>

        <p class="text-3xl font-bold text-yellow-600">
          {{ stats.in_progress }}
        </p>
      </div>


      <div class="bg-white shadow rounded-lg p-6">
        <h3 class="text-gray-500 mb-2">Done</h3>

        <p class="text-3xl font-bold text-green-600">
          {{ stats.done }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../services/api";

const stats = ref({
  todo: 0,
  in_progress: 0,
  done: 0,
});

async function loadStats() {
  try {
    const res = await api.get("/dashboard/stats");

    stats.value = res.data;
  } catch (e) {
    alert("Failed loading dashboard");
  }
}

onMounted(loadStats);
</script>
