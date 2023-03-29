<script>
  import InsiemePerSonaLogo from "$lib/components/logos/InsiemePerSonaLogo.svelte";
  import ViviamoSonaLogo from "$lib/components/logos/ViviamoSonaLogo.svelte";
  import Icon from "@iconify/svelte";
  import NavItem from "./NavItem.svelte";

  let opened = false;
  let shadow = false;

  const onScroll = () => {
    if (window.scrollY > 10) {
      shadow = true;
    } else {
      shadow = false;
    }
  };
</script>

<svelte:window on:scroll={onScroll} />

<header class="p-3 {shadow ? 'bg-white' : ''} md:bg-opacity-80 md:backdrop-blur-md fixed inset-x-0 top-0 {shadow ? 'shadow-md' : ''} z-50 transition-shadow duration-200 ease-in">
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
      <ul class="flex flex-col mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium">
        <NavItem href="/" name="Home" />
        <NavItem href="/chi-siamo" name="Chi siamo" />
        <NavItem href="/programma" name="Le nostre idee" />
        <NavItem href="/articoli" name="Notizie" />
        <NavItem href="/contatti" name="Contatti" />
      </ul>
    </div>
  </nav>
</header>
