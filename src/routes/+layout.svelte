<script>
  import Header from "$lib/components/Header.svelte";
  import "../app.css";
</script>

<svelte:head>
  <title>Viviamo Sona & Insieme per Sona</title>
</svelte:head>

<Header />

<slot />

<footer>
  <div class="max-w-screen-2xl mx-auto py-10 text-sm flex flex-col gap-2 px-5">
    <div class="flex flex-col sm:flex-row gap-3">
      <a href="/" class="underline">Home</a>
      <a href="/chi-siamo/tabella" class="underline">Candidati in formato tabellare</a>
      <a href="/articoli" class="underline">Rassegna stampa</a>
    </div>
    <p class="mt-3">
      Questo sito non utilizza cookie di profilazione, ma si avvale di cookie tecnici necessari al suo funzionamento. <a href="/privacy" class="underline">Informativa sulla privacy</a>
    </p>
    <p>
      <a href="mailto:viviamosona@gmail.com">viviamosona@gmail.com</a>
    </p>
  </div>
</footer>
