
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
      <div class="flex flex-col gap-16 w-full">
        <div class="space-y-6">
          <div class="text-2xl font-bold text-center">Прогноз по годам</div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-8 text-xl">
            <div class="space-y-2 bg-gray-200 p-6 rounded-xl">
              <div class="font-bold">Электричество</div>
              <div>
                <div><span class="font-bold">2022: </span>{{ result.result.result_el[2022].toFixed(0) }} руб.</div>
                <div><span class="font-bold">2023: </span>{{ result.result.result_el[2023].toFixed(0) }} руб.</div>
                <div><span class="font-bold">2024: </span>{{ result.result.result_el[2024].toFixed(0) }} руб.</div>
              </div>
            </div>
            <div class="space-y-2 bg-gray-200 p-6 rounded-xl">
              <div class="font-bold">Газ</div>
              <div>
                <div><span class="font-bold">2022: </span>{{ result.result.result_gaz[2022].toFixed(0) }} руб.</div>
                <div><span class="font-bold">2023: </span>{{ result.result.result_gaz[2023].toFixed(0) }} руб.</div>
                <div><span class="font-bold">2024: </span>{{ result.result.result_gaz[2024].toFixed(0) }} руб.</div>
              </div>
            </div>
            <div class="space-y-2 bg-gray-200 p-6 rounded-xl">
              <div class="font-bold">Тепло</div>
              <div>
                <div><span class="font-bold">2022: </span>{{ result.result.result_teplo[2022].toFixed(0) }} руб.</div>
                <div><span class="font-bold">2023: </span>{{ result.result.result_teplo[2023].toFixed(0) }} руб.</div>
                <div><span class="font-bold">2024: </span>{{ result.result.result_teplo[2024].toFixed(0) }} руб.</div>
              </div>
            </div>
            <div class="space-y-2 bg-gray-200 p-6 rounded-xl">
              <div class="font-bold">Вода</div>
              <div>
                <div><span class="font-bold">2022: </span>{{ result.result.result_voda[2022].toFixed(0) }} руб.</div>
                <div><span class="font-bold">2023: </span>{{ result.result.result_voda[2023].toFixed(0) }} руб.</div>
                <div><span class="font-bold">2024: </span>{{ result.result.result_voda[2024].toFixed(0) }} руб.</div>
              </div>
            </div>
          </div>
        </div>

        <div class="w-full flex flex-col gap-4 md:col-span-2">
          <div class="text-2xl font-bold text-center">Визуализация данных</div>
          <img class="w-full" :src="`data:image/png;base64,${result.images[0]}`" alt="home" />
        </div>
      </div>
    </div>
    <div class="w-full flex justify-center">
      <img class="w-full max-w-xl" src="/5.jpg" alt="home" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue';
import BaseInput from './base/BaseInput.vue';
import BaseSelect from './base/BaseSelect.vue';
import BaseNumberSlider from './base/BaseNumberSlider.vue';
import axios from 'axios';

interface YearData {
  2022: number,
  2023: number,
  2024: number,
}

interface ResultInterface {
  result: {
    result_el: YearData,
    result_gaz: YearData,
    result_teplo: YearData,
    result_voda: YearData,
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
    const response = await axios.post('http://84.201.139.219:5000/analyse', {
      city: form.city,
      area: form.area,
      temperature: form.temperature,
      inflation: form.inflation,
      taxes: form.taxes,
      expenses: form.expenses
    }) as { data: ResultInterface }

    result.value = response.data
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
  { value: 'Александровск-Сахалинский', label: 'Александровск-Сахалинский' },
  { value: 'Анадырь', label: 'Анадырь' },
  { value: 'Билибино', label: 'Билибино' },
  { value: 'Биробиджан', label: 'Биробиджан' },
  { value: 'Благовещенск', label: 'Благовещенск' },
  { value: 'Вилючинск', label: 'Вилючинск' },
  { value: 'Владивосток', label: 'Владивосток' },
  { value: 'Вольно-Надеждинское', label: 'Вольно-Надеждинское' },
  { value: 'Горные ключи', label: 'Горные ключи' },
  { value: 'Дальнереченск', label: 'Дальнереченск' },
  { value: 'Ключи', label: 'Ключи' },
  { value: 'Комсомольск-на-Амуре', label: 'Комсомольск-на-Амуре' },
  { value: 'Курильск', label: 'Курильск' },
  { value: 'Лаврентия', label: 'Лаврентия' },
  { value: 'Ленск', label: 'Ленск' },
  { value: 'Магадан', label: 'Магадан' },
  { value: 'Находка', label: 'Находка' },
  { value: 'Нерюнгри', label: 'Нерюнгри' },
  { value: 'Паратунка', label: 'Паратунка' },
  { value: 'Партизанск', label: 'Партизанск' },
  { value: 'Петропавловск-Камчатский', label: 'Петропавловск-Камчатский' },
  { value: 'Покровск', label: 'Покровск' },
  { value: 'Провидения', label: 'Провидения' },
  { value: 'Свободный', label: 'Свободный' },
  { value: 'Сковородино', label: 'Сковородино' },
  { value: 'Славянка', label: 'Славянка' },
  { value: 'Спасск-Дальний', label: 'Спасск-Дальний' },
  { value: 'Тиличики', label: 'Тиличики' },
  { value: 'Тында', label: 'Тында' },
  { value: 'Уссурийск', label: 'Уссурийск' },
  { value: 'Усть-Камчатск', label: 'Усть-Камчатск' },
  { value: 'Усть-Нера', label: 'Усть-Нера' },
  { value: 'Усть-Омчуг', label: 'Усть-Омчуг' },
  { value: 'Хабаровск', label: 'Хабаровск' },
  { value: 'Чурапча', label: 'Чурапча' },
  { value: 'Эгвекинот', label: 'Эгвекинот' },
  { value: 'Южно-Сахалинск', label: 'Южно-Сахалинск' },
  { value: 'Якутск', label: 'Якутск' }
]
</script>