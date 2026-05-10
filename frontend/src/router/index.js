import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Dashboard from "../views/Dashboard.vue";
import Predict from "../views/Predict.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/dashboard", component: Dashboard },
  { path: "/predict", component: Predict },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;