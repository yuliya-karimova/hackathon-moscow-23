<template>
  <div class="flex flex-col gap-2">
    <div class="font-medium">{{ label }}<span v-if="unit"> ({{ unit }})</span>:<span v-if="required">*</span></div>
    <input v-model="value" :type="type" class="border border-gray-400 rounded-md py-2 px-4" :class="error && 'border-red-600'" @blur="validate">
    <div v-if="error" class="text-red-600 text-xs">{{ error }}</div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";

interface Props {
  label?: string;
  placeholder?: string;
  required?: boolean
  modelValue: string | number
  type?: string
  min?: number
  max?: number
  unit?: string
}

const props = withDefaults(defineProps<Props>(), {
  placeholder: "Введите",
  required: false,
  type: 'text',
  min: 0,
  unit: ''
});

const error = ref('')

const emit = defineEmits(['update:modelValue'])

const validate = () => {
  const currentValue = value.value

  if (!currentValue.toString()) {
      error.value = 'Обязательное поле'
    } else if (typeof currentValue === 'number') {
      if (currentValue < props.min) {
        error.value = `Минимальное значение: ${props.min}`
      } else if (props.max && currentValue > props.max) {
        error.value = `Максимальное значение: ${props.max}`
      } else {
        error.value = ''
      }
    } else {
      error.value = ''
    }
}

const value = computed({
  get: () => {
    return props.modelValue
  },
  set: (value: string | number) => {
    validate()
    emit('update:modelValue', value)
  },
})
</script>
