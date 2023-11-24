<template>
  <div class="flex flex-col gap-6">
    <div class="text-3xl text-center font-medium">
      Как мы проводим анализ?
    </div>
    <div class="text-gray-600 text-center">
      На основе ретроспективных данных создали модель зависимости и прогноза коммунальных расходов от объема вложений в
      хозяйственную деятельность и факторов внешней среды
    </div>
    <div class="grid grid-cols-2 gap-6">

      <!-- cart1 -->
      <div class="flex gap-4 bg-white p-6 rounded-lg">
        <div class="w-12 shrink-0 text-sky-600">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor"
            className="w-6 h-6">
            <path strokeLinecap="round" strokeLinejoin="round"
              d="M2.25 18.75a60.07 60.07 0 0115.797 2.101c.727.198 1.453-.342 1.453-1.096V18.75M3.75 4.5v.75A.75.75 0 013 6h-.75m0 0v-.375c0-.621.504-1.125 1.125-1.125H20.25M2.25 6v9m18-10.5v.75c0 .414.336.75.75.75h.75m-1.5-1.5h.375c.621 0 1.125.504 1.125 1.125v9.75c0 .621-.504 1.125-1.125 1.125h-.375m1.5-1.5H21a.75.75 0 00-.75.75v.75m0 0H3.75m0 0h-.375a1.125 1.125 0 01-1.125-1.125V15m1.5 1.5v-.75A.75.75 0 003 15h-.75M15 10.5a3 3 0 11-6 0 3 3 0 016 0zm3 0h.008v.008H18V10.5zm-12 0h.008v.008H6V10.5z" />
          </svg>
        </div>
        <div>
          <div class="font-medium text-xl">Анализ инвестиций</div>
          <div>Определяем зависимость изменения объема потребления коммунальных услуг от объемов
            вложений в ремонт и содержание зданий и сооружений.
          </div>
        </div>
      </div>

      <!-- cart2 -->
      <div class="flex gap-4 bg-white p-6 rounded-lg">
        <div class="w-12 shrink-0 text-sky-600">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor"
            className="w-6 h-6">
            <path strokeLinecap="round" strokeLinejoin="round"
              d="M12 3v2.25m6.364.386l-1.591 1.591M21 12h-2.25m-.386 6.364l-1.591-1.591M12 18.75V21m-4.773-4.227l-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z" />
          </svg>
        </div>
        <div>
          <div class="font-medium text-xl">Анализ внешней среды</div>
          <div>Определяем зависимость изменения объема потребления коммунальных услуг от факторов внешней среды (климат,
            инфляция, налоги).
          </div>
        </div>
      </div>

      <!-- cart3 -->
      <div class="flex gap-4 bg-white p-6 rounded-lg">
        <div class="w-12 shrink-0 text-sky-600">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor"
            className="w-6 h-6">
            <path strokeLinecap="round" strokeLinejoin="round"
              d="M2.25 18L9 11.25l4.306 4.307a11.95 11.95 0 015.814-5.519l2.74-1.22m0 0l-5.94-2.28m5.94 2.28l-2.28 5.941" />
          </svg>
        </div>
        <div>
          <div class="font-medium text-xl">Прогноз коммунальных расходов</div>
          <div>Прогноз показателей коммунальных расходов, с учетом внутренних и внешних факторов, с
            горизонтом 3 года.
          </div>
        </div>
      </div>

      <!-- cart4 -->
      <div class="flex gap-4 bg-white p-6 rounded-lg">
        <div class="w-12 shrink-0 text-sky-600">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor"
            className="w-6 h-6">
            <path strokeLinecap="round" strokeLinejoin="round"
              d="M8.25 3v1.5M4.5 8.25H3m18 0h-1.5M4.5 12H3m18 0h-1.5m-15 3.75H3m18 0h-1.5M8.25 19.5V21M12 3v1.5m0 15V21m3.75-18v1.5m0 15V21m-9-1.5h10.5a2.25 2.25 0 002.25-2.25V6.75a2.25 2.25 0 00-2.25-2.25H6.75A2.25 2.25 0 004.5 6.75v10.5a2.25 2.25 0 002.25 2.25zm.75-12h9v9h-9v-9z" />
          </svg>
        </div>
        <div>
          <div class="font-medium text-xl">Машинное обучение</div>
          <div>Используем технологии машинного обучения для получения максимально точного прогноза.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts"></script>