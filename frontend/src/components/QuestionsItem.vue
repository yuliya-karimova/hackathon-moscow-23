<template>
  <div class="flex flex-col gap-3">
    <div class="font-bold text-xl">{{ question.title }}</div>
    <div class="text-gray-600">{{ question.answer }}</div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  question: {
    title: string;
    answer: string;
  }
}

defineProps<Props>()
</script>