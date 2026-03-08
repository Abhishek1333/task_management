import { createRouter, createWebHistory } from "vue-router";

import Login from "../pages/Login.vue";
import Register from "../pages/Register.vue";
import Dashboard from "../pages/Dashboard.vue";
import Tasks from "../pages/Tasks.vue";
import Users from "../pages/Users.vue";
import Layout from "../layouts/Layout.vue";

const routes = [
  { path: "/", component: Login },
  { path: "/register", component: Register },

  {
    path: "/",
    component: Layout,
    meta: { requiresAuth: true },
    children: [
      { path: "dashboard", component: Dashboard },
      { path: "tasks", component: Tasks },
      { path: "users", component: Users },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token");

  if (to.meta.requiresAuth && !token) {
    next("/");
  } else {
    next();
  }
});

export default router;
