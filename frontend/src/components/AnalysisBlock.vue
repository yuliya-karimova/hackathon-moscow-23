
<template>
  <div class="flex flex-col gap-24">
    <div class="w-full flex flex-col items-center gap-12">
      <div class="text-4xl text-sky-950 text-center w-full font-bold">Провести анализ</div>
      <div class="space-y-8 w-full max-w-2xl">
        <BaseSelect label="Город" required placeholder="Город" :options="CitiesOptions" @update="onSelectCity" />
        <BaseInput v-model="form.area" label="Площадь здания" :min="0" unit="m²" required type="number" />
        <BaseNumberSlider v-model="form.temperature" :min="-50" :max="50" unit="°C" label="Температура" required />
        <BaseNumberSlider v-model="form.inflation" :min="0" :max="30" unit="%" label="Инфляция" required />
        <BaseInput v-model="form.taxes" label="Налог на имущество" :min="0" :max="50" unit="%" required type="number" />
        <BaseInput v-model="form.expenses" label="Oбъем затрат" :min="0" unit="руб." required type="number" />
      </div>
      <button
        class="text-xl uppercase bg-orange-500 hover:bg-orange-400 transition duration-150 text-white py-3 px-5 flex items-center justify-center gap-4 font-medium sm:w-64 rounded-lg"
        @click="submit">
        <div class="text-xl uppercase">
          Провести анализ
        </div>
      </button>
      <div v-if="errorText"
        class="fixed flex gap-4 items-center bottom-4 right-4 bg-white border-2 border-red-600 rounded-xl p-6 z-50">
        <div class="text-red-600 w-6">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"
            class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z" />
          </svg>
        </div>
        <div class="text-lg">
          {{ errorText }}
        </div>
      </div>
    </div>
    <div ref="resultBlock" v-if="result" class="w-full flex flex-col items-center gap-12">
      <div class="text-4xl text-sky-950 text-center w-full font-bold">Результаты анализа</div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-12 w-full">
        <div class="flex flex-col gap-4 text-xl">
          <div class="text-2xl font-bold">Прогноз по годам</div>
          <div><span class="font-bold">2022: </span>{{ result.result[2022].toFixed(0) }} руб.</div>
          <div><span class="font-bold">2023: </span>{{ result.result[2023].toFixed(0) }} руб.</div>
          <div><span class="font-bold">2024: </span>{{ result.result[2024].toFixed(0) }} руб.</div>
        </div>
        <div class="w-full flex flex-col gap-4 md:col-span-2">
          <div class="text-2xl font-bold">Визуализация данных</div>
          <div class="grid grid-cols-1 md:grid-cols-2 w-full gap-4">
            <img class="w-full" :src="`data:image/png;base64,${result.images[0]}`" alt="home" />
            <img class="w-full" :src="`data:image/png;base64,${result.images[1]}`" alt="home" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue';
import BaseInput from './base/BaseInput.vue';
import BaseSelect from './base/BaseSelect.vue';
import BaseNumberSlider from './base/BaseNumberSlider.vue';
import axios from 'axios';

interface ResultInterface {
  result: {
    2022: number,
    2023: number,
    2024: number,
  }
  images: string[]
}

const result = ref<undefined | ResultInterface>(undefined)
const errorText = ref('')
const resultBlock = ref<HTMLDivElement | undefined>(undefined)

const form = reactive({
  city: '',
  area: 0,
  temperature: 0,
  inflation: 0,
  taxes: 0,
  expenses: 0,
})

const onSelectCity = async (value?: string) => {
  form.city = value || '';
};

const submit = async () => {
  if (!form.city || form.area < 0 || form.temperature < -50 || form.temperature > 50 || form.inflation < 0 || form.inflation > 30 || form.taxes < 0 || form.taxes > 50 || form.expenses < 0) {
    errorText.value = 'Форма содержит невалидные значения'
    setTimeout(() => {
      errorText.value = ''
    }, 2000)
    return
  }


  try {
    const response = await axios.post('https://84.201.139.219:5000/analyse', {
      city: form.city,
      area: form.area,
      temperature: form.temperature,
      inflation: form.inflation,
      taxes: form.taxes,
      expenses: form.expenses
    }) as { data: ResultInterface }

    result.value = response.data
    scrollToResult()
  } catch (error: any) {
    console.error('Error making the request:', error);

    if (error.message === 'Network Error') {
      errorText.value = 'Пожалуйста, попробуйте выключить VPN'
    } else {
      errorText.value = 'Ошибка в запросе'
    }
    setTimeout(() => {
      errorText.value = ''
    }, 2000)
  }
}

const CitiesOptions = [
  { label: 'Анадырь', value: 'Анадырь' },
  { label: 'Билибино', value: 'Билибино' },
  { label: 'Биробиджан', value: 'Биробиджан' },
  { label: 'Благовещенск', value: 'Благовещенск' },
  { label: 'Владивосток', value: 'Владивосток' },
  { label: 'Вольно-Надеждинское', value: 'Вольно-Надеждинское' },
  { label: 'Горные ключи', value: 'Горные ключи' },
  { label: 'Ключи', value: 'Ключи' },
  { label: 'Комсомольск-на-Амуре', value: 'Комсомольск-на-Амуре' },
  { label: 'Ленск', value: 'Ленск' },
  { label: 'Магадан', value: 'Магадан' },
  { label: 'Находка', value: 'Находка' },
  { label: 'Паратунка', value: 'Паратунка' },
  { label: 'Петропавловск-Камчатский', value: 'Петропавловск-Камчатский' },
  { label: 'Покровск', value: 'Покровск' },
  { label: 'Тында', value: 'Тында' },
  { label: 'Уссурийск', value: 'Уссурийск' },
  { label: 'Усть-Камчатск', value: 'Усть-Камчатск' },
  { label: 'Усть-Нера', value: 'Усть-Нера' },
  { label: 'Усть-Омчуг', value: 'Усть-Омчуг' },
  { label: 'Хабаровск', value: 'Хабаровск' },
  { label: 'Чурапча', value: 'Чурапча' },
  { label: 'Южно-Сахалинск', value: 'Южно-Сахалинск' },
  { label: 'Якутск', value: 'Якутск' }
];

const scrollToResult = () => {
  const top = resultBlock.value?.offsetTop || 0
  window.scrollTo({ left: 0, top: top, behavior: "smooth" })
}
</script>