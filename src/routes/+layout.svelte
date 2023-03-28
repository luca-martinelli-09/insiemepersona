<script>
  import Header from "$lib/components/Header.svelte";
  import "../app.css";
</script>

<svelte:head>
  <title>Insieme perSona & Viviamo Sona</title>
</svelte:head>

<Header />

<main class="max-w-screen-2xl mx-auto mb-20 px-3">
  <slot />
</main>

<footer>
  <div class="max-w-screen-2xl mx-auto">
    <a href="/privacy" class="underline text-sm">Privacy Policy</a>
  </div>
</footer>