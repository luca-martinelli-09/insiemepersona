<script lang="ts">
  import InsiemePerSonaLogo from "$lib/components/logos/InsiemePerSonaLogo.svelte";
  import ViviamoSonaLogo from "$lib/components/logos/ViviamoSonaLogo.svelte";
  import Icon from "@iconify/svelte";
  import type { PageData } from "./$types";

  export let data: PageData;

  const posts = data.posts;
</script>

<section>
  <main class="flex flex-col gap-20">
    <div class="flex justify-center gap-2 md:gap-5 w-full">
      <ViviamoSonaLogo size={300} class="h-auto w-full lg:w-auto" />
      <InsiemePerSonaLogo size={300} class="h-auto w-full lg:w-auto" />
    </div>
    <div class="flex flex-col gap-16 items-center">
      <h1 class="title text-center">Ripartiamo dalle<br /><span class="green font-medium">persone</span></h1>
      <div class="flex gap-2">
        <a class="button primary" href="/chi-siamo">Conosci i candidati</a>
        <a class="button gap-3" href="/programma-amministrativo.pdf"><span class="text-3xl"><Icon icon="ic:round-arrow-downward" /></span>Le nostre idee</a>
      </div>
      <div class="flex gap-2 text-3xl">
        <a href="https://www.facebook.com/viviamosona" target="_blank" rel="noopener noreferrer"><Icon icon="mdi:facebook" /></a>
        <a href="http://instagram.com/viviamosona" target="_blank" rel="noopener noreferrer"><Icon icon="mdi:instagram" /></a>
      </div>
    </div>
  </main>
</section>
<!--
<section class="items-stretch">
  <main class="pills">
    <h2 class="title">5 passi per ripartire a <span class="green">Lugagnano</span></h2>

    <ol class="pills">
      <li><p><strong>Riqualificare</strong> il centro anche attraverso la realizzazione di nuovi parcheggi</p></li>
      <li><p><strong>Creare una rete di ciclabili</strong> che colleghino tutto il paese</p></li>
      <li><p><strong>Credere</strong> nelle potenzialità delle associazioni, <strong>e progettare</strong> una <strong>sede per le associazioni socio-assistenziali</strong> (Sos e Dono)</p></li>
      <li><p><strong>Creare</strong> un <strong>polo sportivo</strong> per tutti gli sport e per tutte le persone</p></li>
      <li><p><strong>Difendere l'ambiente</strong> (no ad alcun ampliamento della discarica Cà di Capri)</p></li>
    </ol>
  </main>
  <img src="/bg/lugagnano.webp" alt="5 passi per ripartire a Lugagnano" class="side" />
</section>

<section class="items-stretch flex-col-reverse lg:flex-row">
  <img src="/bg/sona.webp" alt="5 passi per ripartire a Sona" class="side" />
  <main class="pills">
    <h2 class="title">5 passi per ripartire a <span class="green">Sona</span></h2>

    <ol class="pills">
      <li><p><strong>Riqualificare</strong> il centro anche attraverso la realizzazione di nuovi parcheggi</p></li>
      <li><p><strong>Creare una rete di ciclabili</strong> che colleghino tutto il paese</p></li>
      <li><p><strong>Credere</strong> nelle potenzialità delle associazioni, <strong>e progettare</strong> una <strong>sede per le associazioni socio-assistenziali</strong> (Sos e Dono)</p></li>
      <li><p><strong>Creare</strong> un <strong>polo sportivo</strong> per tutti gli sport e per tutte le persone</p></li>
      <li><p><strong>Difendere l'ambiente</strong> (no ad alcun ampliamento della discarica Cà di Capri)</p></li>
    </ol>
  </main>
</section>

<section class="items-stretch">
  <main class="pills">
    <h2 class="title">5 passi per ripartire a <span class="green">San Giorgio</span></h2>

    <ol class="pills">
      <li><p><strong>Riqualificare</strong> il centro anche attraverso la realizzazione di nuovi parcheggi</p></li>
      <li><p><strong>Creare una rete di ciclabili</strong> che colleghino tutto il paese</p></li>
      <li><p><strong>Credere</strong> nelle potenzialità delle associazioni, <strong>e progettare</strong> una <strong>sede per le associazioni socio-assistenziali</strong> (Sos e Dono)</p></li>
      <li><p><strong>Creare</strong> un <strong>polo sportivo</strong> per tutti gli sport e per tutte le persone</p></li>
      <li><p><strong>Difendere l'ambiente</strong> (no ad alcun ampliamento della discarica Cà di Capri)</p></li>
    </ol>
  </main>
  <img src="/bg/san-giorgio.webp" alt="5 passi per ripartire a San Giorgio" class="side" />
</section>

<section class="items-stretch flex-col-reverse lg:flex-row">
  <img src="/bg/palazzolo.webp" alt="5 passi per ripartire a Palazzolo" class="side object-left" />
  <main class="pills">
    <h2 class="title">5 passi per ripartire a <span class="green">Palazzolo</span></h2>

    <ol class="pills">
      <li><p><strong>Riqualificare</strong> il centro anche attraverso la realizzazione di nuovi parcheggi</p></li>
      <li><p><strong>Creare una rete di ciclabili</strong> che colleghino tutto il paese</p></li>
      <li><p><strong>Credere</strong> nelle potenzialità delle associazioni, <strong>e progettare</strong> una <strong>sede per le associazioni socio-assistenziali</strong> (Sos e Dono)</p></li>
      <li><p><strong>Creare</strong> un <strong>polo sportivo</strong> per tutti gli sport e per tutte le persone</p></li>
      <li><p><strong>Difendere l'ambiente</strong> (no ad alcun ampliamento della discarica Cà di Capri)</p></li>
    </ol>
  </main>
</section>
-->