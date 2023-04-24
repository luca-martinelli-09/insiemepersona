<script>
  import Header from "$lib/components/Header.svelte";
  import "../app.css";
</script>

<svelte:head>
  <title>Viviamo Sona & Insieme per Sona</title>
</svelte:head>

<Header />

<main class="max-w-screen-2xl mx-auto mb-20 px-3">
  <slot />
</main>

<footer class="mt-10 bg-[#15457d] text-white">
  <div class="max-w-screen-2xl mx-auto py-5 text-sm flex flex-col gap-2">
    <p>Questo sito non utilizza cookie.</p>
    <a href="/privacy" class="underline">Privacy Policy</a>
  </div>
</footer>