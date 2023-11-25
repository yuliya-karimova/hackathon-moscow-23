<template>
  <div class="space-y-2">
    <div class="font-medium">{{ label }}<span v-if="unit"> ({{ unit }})</span>:<span v-if="required">*</span></div>
    <div class="flex gap-4">
      <div>{{ min }}</div>
      <div class="w-full">
        <input type="range" class="w-full" :min="min" :max="max" v-model="value">
        <p>Выбранное значение: {{ value }}<span v-if="unit">{{ unit }}</span></p>
      </div>
      <div>{{ max }}</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";

interface Props {
  label?: string;
  required?: boolean
  modelValue: number
  min?: number
  max?: number
  unit?: string
}

const props = withDefaults(defineProps<Props>(), {
  min: 0,
  max: 100,
  unit: ''
});

const emit = defineEmits(['update:modelValue'])

const value = computed({
  get: () => {
    return props.modelValue
  },
  set: (value: number) => {
    emit('update:modelValue', Number(value))
  },
})
</script>

