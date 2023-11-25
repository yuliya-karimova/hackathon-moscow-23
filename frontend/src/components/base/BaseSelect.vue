<template>
  <div class="flex flex-col gap-2 relative">
    <div class="font-medium">{{ label }}:<span v-if="required">*</span></div>
    <input ref="input" type="text" v-model="search" :placeholder="placeholder" class="border border-gray-400 rounded-md px-4 py-2"
      @input="filterCities" @click="isExpanded = !isExpanded" />
    <div ref="optionsList" v-if="isExpanded"
      class="border border-gray-400 rounded-md py-2 flex flex-col gap-1 max-h-44 overflow-y-auto absolute left-0 top-20 bg-white w-full z-10">
      <button v-for="option in filteredValues" :key="option.value" class="text-left px-4 py-1 hover:bg-gray-200"
        :class="selectedValueId === option.value && 'bg-gray-100'" @click="onSelect(option)">
        {{ option.label }}
      </button>
      <div v-if="!filteredValues.length" class="px-4 py-1 text-gray-500">
        Извините, ничего не нашлось
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from "vue";
import { onClickOutside } from "@vueuse/core";
import { Option } from "../../models/main";

interface Props {
  options?: Option[];
  placeholder?: string;
  isExpandedInitial?: boolean;
  label?: string
  required?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  options: () => [],
  placeholder: "Поиск...",
  isExpandedInitial: false,
  label: ''
});

const search = ref("");
const filteredValues = ref<Option[]>([]);
const selectedValueId = ref<number | string | null>(null);
const isExpanded = ref(false);
const optionsList = ref<HTMLDivElement | null>(null);
const searchInput = ref<HTMLInputElement | null>(null);

onMounted(() => {
  filteredValues.value = props.options;
  isExpanded.value = props.isExpandedInitial;
});

const emit = defineEmits(["update"]);

const onSelect = (option: Option) => {
  selectedValueId.value = option.value;
  isExpanded.value = false;
  search.value = option.label;
  emit("update", option.value);
};

const filterCities = () => {
  isExpanded.value = true;

  if (search.value) {
    filteredValues.value = props.options.filter((option) =>
      option.label.toLowerCase().includes(search.value.toLowerCase())
    );
  } else {
    filteredValues.value = props.options;
  }
};

onClickOutside(optionsList, () => (isExpanded.value = false), {
  ignore: [searchInput],
});

watch(
  () => props.options,
  (newValue) => {
    filteredValues.value = newValue;
  }
);

watch(
  () => props.isExpandedInitial,
  (newValue) => {
    isExpanded.value = newValue;
  }
);
</script>
