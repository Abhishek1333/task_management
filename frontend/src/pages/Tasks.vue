<template>

<div>

<h1 class="text-2xl font-bold mb-6">Tasks</h1>


<div class="bg-white shadow rounded p-4 mb-6 flex gap-3">

<input
v-model="title"
placeholder="Task title"
class="border p-2 flex-1"
/>

<textarea
v-model="description"
placeholder="Task description"
class="border p-2 flex-1"
/>

<select v-model="status" class="border p-2">

<option value="todo">Todo</option>
<option value="in_progress">In Progress</option>
<option value="done">Done</option>

</select>

<button
class="bg-indigo-600 text-white px-4 py-2 rounded"
@click="addTask"
>
Add
</button>

</div>



<div class="mb-6">

<select
v-model="filterStatus"
class="border p-2"
@change="loadTasks"
>

<option value="">All</option>
<option value="todo">Todo</option>
<option value="in_progress">In Progress</option>
<option value="done">Done</option>

</select>

</div>



<div
v-if="tasks.length === 0"
class="bg-white shadow rounded p-10 text-center"
>

<p class="text-gray-500 text-lg">
No tasks available
</p>

</div>



<div v-else class="grid grid-cols-3 gap-4">

<div
v-for="task in tasks"
:key="task.id"
class="bg-white shadow rounded p-4"
>

<input
v-model="task.title"
class="border p-2 w-full mb-2"
/>

<textarea
v-model="task.description"
class="border p-2 w-full mb-2"
/>

<select
v-model="task.status"
class="border p-2 w-full mb-3"
>

<option value="todo">Todo</option>
<option value="in_progress">In Progress</option>
<option value="done">Done</option>

</select>

<div class="flex justify-between">

<button
class="text-blue-600"
@click="updateTask(task)"
>
Update
</button>

<button
class="text-red-600"
@click="deleteTask(task.id)"
>
Delete
</button>

</div>

</div>

</div>



<div class="flex gap-4 mt-6">

<button
class="border px-4 py-1"
@click="prevPage"
>
Prev
</button>

<button
class="border px-4 py-1"
@click="nextPage"
>
Next
</button>

</div>

</div>

</template>


<script setup>

import { ref } from "vue"
import api from "../services/api"


const tasks = ref([])

const title = ref("")
const description = ref("")
const status = ref("todo")

const filterStatus = ref("")

const page = ref(1)


async function loadTasks(){

try{

const res = await api.get("/tasks",{

params:{
page:page.value,
status:filterStatus.value
}

})

tasks.value = res.data

}catch(e){

alert(e.response?.data?.detail || "Failed loading tasks")

}

}


async function addTask(){

try{

await api.post("/tasks",{
title:title.value,
description:description.value,
status:status.value
})

title.value=""
description.value=""

loadTasks()

}catch(e){

alert(e.response?.data?.detail || "Create failed")

}

}


async function updateTask(task){

try{

const payload = {}

if(task.title){
payload.title = task.title
}

if(task.description){
payload.description = task.description
}

if(task.status){
payload.status = task.status
}

await api.put(`/tasks/${task.id}`, payload)

alert("Task updated")

loadTasks()

}catch(e){

alert(e.response?.data?.detail || "Update failed")

}

}


async function deleteTask(id){

try{

await api.delete(`/tasks/${id}`)

loadTasks()

}catch(e){

alert(e.response?.data?.detail || "Delete failed")

}

}


function nextPage(){

page.value++

loadTasks()

}


function prevPage(){

if(page.value > 1){

page.value--

loadTasks()

}

}


loadTasks()

</script>