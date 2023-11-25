<template>
  <div class="text-gray-800">
    <!-- header -->
    <div class="sticky top-0 bg-white z-30 px-8 py-4" :class="scrollHeight > 10 && 'shadow-md'">
      <div class="mx-auto max-w-screen-xl flex flex-col sm:flex-row gap-x-4 gap-y-2 sm:gap-10 text-lg sm:text-xl items-center uppercase font-medium text-sky-950 justify-between">
        <button class="w-10 shrink-0 sm:w-16 hover:opacity-80" @click="scrollTo('top')">
          <img class="w-full" src="/logo.svg" alt="home" />
        </button>
        <button class="hover:opacity-80 transition duration-150" @click="scrollTo('about')">Как мы работаем</button>
        <button class="hover:opacity-80 transition duration-150" @click="scrollTo('analysis')">Анализ</button>
        <button class="hover:opacity-80 transition duration-150" @click="scrollTo('questions')">FAQ</button>
        <button class="hover:opacity-80 transition duration-150" @click="scrollTo('contacts')">Контакты</button>
      </div>
    </div>

    <!-- main block -->
    <div class="px-8 pb-16 md:py-16">
      <div class="grid grid-cols-1 sm:grid-cols-2 mx-auto max-w-screen-xl">
        <div class="uppercase z-10 space-y-10 py-10 md:py-20 flex-col justify-center">
          <div class="text-center sm:text-left text-2xl sm:text-5xl font-bold text-sky-950">
            Оценка эффективности вложений в содержание недвижимости
          </div>
          <div class="flex gap-3 md:gap-6 flex-col md:flex-row">
            <button
              class="flex bg-orange-500 hover:bg-orange-400 transition duration-150 text-white py-3 px-5 items-center justify-center gap-4 font-medium sm:w-64 rounded-lg"
              @click="scrollTo('analysis')">
              <div class="text-xl uppercase">
                Провести анализ
              </div>
              <div class="w-8">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                  stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round"
                    d="M15.59 14.37a6 6 0 01-5.84 7.38v-4.8m5.84-2.58a14.98 14.98 0 006.16-12.12A14.98 14.98 0 009.631 8.41m5.96 5.96a14.926 14.926 0 01-5.841 2.58m-.119-8.54a6 6 0 00-7.381 5.84h4.8m2.581-5.84a14.927 14.927 0 00-2.58 5.84m2.699 2.7c-.103.021-.207.041-.311.06a15.09 15.09 0 01-2.448-2.448 14.9 14.9 0 01.06-.312m-2.24 2.39a4.493 4.493 0 00-1.757 4.306 4.493 4.493 0 004.306-1.758M16.5 9a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z" />
                </svg>
              </div>
            </button>
          </div>
        </div>
        <div class="flex items-center">
          <img class="w-full" src="/7.jpg" alt="home" />
        </div>
      </div>
    </div>

    <!-- about block -->
    <div ref="aboutBlock" class="bg-gray-200 px-8 py-16">
      <div class="mx-auto max-w-screen-xl">
        <AboutBlock />
      </div>
    </div>

    <!-- analysis block -->
    <div ref="analysisBlock" class="px-8 py-16">
      <div class="mx-auto max-w-screen-xl">
        <AnalysisBlock />
      </div>
    </div>

    <!-- questions block -->
    <div ref="questionsBlock" class="bg-gray-200 px-8 py-16">
      <div class="mx-auto max-w-screen-xl">
        <QuestionsBlock />
      </div>
    </div>

    <div class="w-full flex justify-center pt-16">
      <img class="w-full" src="/1.jpg" alt="home" />
    </div>

    <button
      class="transition-all z-40 bg-orange-500 hover:bg-orange-400 text-white font-bold rounded-full fixed bottom-10 right-10 h-14 w-14 text-4xl flex items-center justify-center pb-1 hover:pb-2 duration-150"
      :class="scrollHeight > 10 ? 'opacity-100' : 'opacity-0'" @click="scrollTo('top')">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"
        class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 19.5v-15m0 0l-6.75 6.75M12 4.5l6.75 6.75" />
      </svg>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import AboutBlock from "../components/AboutBlock.vue";
import QuestionsBlock from "../components/QuestionsBlock.vue";
import AnalysisBlock from "../components/AnalysisBlock.vue";

const analysisBlock = ref<HTMLDivElement | undefined>(undefined)
const aboutBlock = ref<HTMLDivElement | undefined>(undefined)
const questionsBlock = ref<HTMLDivElement | undefined>(undefined)
const scrollHeight = ref(0)

const scrollTo = (id: string) => {
  let top = 0
  let offset = 100
  const screenWidth = window.innerWidth

  if (screenWidth < 640) {
    offset = 218
  }

  switch (id) {
    case 'analysis':
      top = (analysisBlock.value?.offsetTop || 0) - offset
      break;
    case 'about':
      top = (aboutBlock.value?.offsetTop || 0) - offset
      break;
    case 'questions':
      top = (questionsBlock.value?.offsetTop || 0) - offset
      break;
    case 'top':
      break;
    case 'contacts':
      top = document.body.scrollHeight
      break;
    default:
      break;
  }

  window.scrollTo({ left: 0, top: top, behavior: "smooth" })
}

const updateScroll = () => {
  scrollHeight.value = window.scrollY || document.documentElement.scrollTop
}

onMounted(() => {
  window.addEventListener('scroll', updateScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', updateScroll)
})
</script>
