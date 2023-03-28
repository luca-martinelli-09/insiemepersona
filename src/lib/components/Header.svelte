<script>
  import InsiemePerSonaLogo from "$lib/components/logos/InsiemePerSonaLogo.svelte";
  import ViviamoSonaLogo from "$lib/components/logos/ViviamoSonaLogo.svelte";
  import Icon from "@iconify/svelte";

  let opened = false;
</script>

<header class="p-3 bg-white md:bg-opacity-80 md:backdrop-blur-md fixed inset-x-0 top-0 shadow-md z-50">
  <nav class="container flex flex-wrap items-center justify-between mx-auto">
    <a href="/" class="flex items-center gap-2">
      <ViviamoSonaLogo />
      <InsiemePerSonaLogo />
    </a>
    <button on:click={() => (opened = !opened)} type="button" class="inline-flex items-center p-2 ml-3 text-3xl text-gray-500 md:hidden">
      <span class="sr-only">Apri il menù</span>
      <Icon icon="ci:menu-duo-md" />
    </button>
    <div class="{opened ? 'block' : 'hidden'} w-full md:block md:w-auto">
      <ul class="flex flex-col mt-4 bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-transparent">
        <li>
          <a href="/" class="font-bold block py-2 pl-3 pr-4 text-white bg-blue-600 md:bg-transparent md:text-blue-600 md:p-0">Home</a>
        </li>
        <li>
          <a href="/chi-siamo" class="font-bold block py-2 pl-3 pr-4 text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-600 md:p-0">Chi siamo</a>
        </li>
        <li>
          <a href="/programma" class="font-bold block py-2 pl-3 pr-4 text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-600 md:p-0">Le nostre idee</a>
        </li>
        <li>
          <a href="/articoli" class="font-bold block py-2 pl-3 pr-4 text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-600 md:p-0">Notizie</a>
        </li>
        <li>
          <a href="/contatti" class="font-bold block py-2 pl-3 pr-4 text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-600 md:p-0">Contatti</a>
        </li>
      </ul>
    </div>
  </nav>
</header>
