<template>
  <div class="flex flex-col min-h-screen">
    <div class="flex-1">
      <router-view />
    </div>
    <Footer />
    <button
      class="z-50 bg-amber-500 text-cyan-950 font-bold rounded-full fixed bottom-10 right-10 h-14 w-14 text-4xl flex items-center justify-center pb-1 hover:pb-3 duration-150"
      @click="scrollToTop">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
        class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 19.5v-15m0 0l-6.75 6.75M12 4.5l6.75 6.75" />
      </svg>
    </button>
  </div>
</template>

<script setup lang="ts">
import Footer from "./components/Footer.vue";

const scrollToTop = () => {
  scroll({
    top: 0,
    behavior: "smooth",
  });
};
</script>
