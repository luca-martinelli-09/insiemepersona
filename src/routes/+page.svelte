<script lang="ts">
  import ArticleCard from "$lib/components/ArticleCard.svelte";
  import InsiemePerSonaLogo from "$lib/components/logos/InsiemePerSonaLogo.svelte";
  import Puzzle from "$lib/components/logos/Puzzle.svelte";
  import ViviamoSonaLogo from "$lib/components/logos/ViviamoSonaLogo.svelte";
  import gsap from "gsap";
  import { onMount } from "svelte";
  import type { PageData } from "./$types";

  export let data: PageData;

  const posts = data.posts;

  let title: HTMLElement;
  let logos: HTMLElement;
  let image: HTMLElement;
  let buttons: HTMLElement;

  let commonGsapOptions = {
    opacity: 0,
    ease: "Expo.easeOut",
    duration: 1,
    delay: 0.2,
  };

  onMount(() => {
    gsap.timeline().from(title, {
      ...commonGsapOptions,
      y: 100,
    });

    gsap
      .timeline()
      .from(logos, {
        ...commonGsapOptions,
        y: -100,
      })
      .from(buttons, {
        ...commonGsapOptions,
        delay: -0.2,
      })
      .from(image, {
        ...commonGsapOptions,
        delay: -0.4,
      });
  });
</script>

<section>
  <div class="flex gap-5 mb-44">
    <div class="flex flex-col gap-10 items-center md:items-start">
      <div bind:this={logos} class="flex gap-2 w-3/4 md:w-full">
        <ViviamoSonaLogo size={150} />
        <InsiemePerSonaLogo size={150} />
      </div>

      <h1 class="big text-center md:text-left" bind:this={title}>Ripartiamo dalle persone</h1>

      <div bind:this={buttons} class="flex flex-col sm:flex-row flex-1 items-start gap-2">
        <a class="button w-full sm:w-auto" href="/programma">Le nostre idee</a>
        <a class="button w-full sm:w-auto" href="/chi-siamo">Conosci i candidati</a>
      </div>
    </div>

    <div class="hidden md:block w-3/4" bind:this={image}>
      <Puzzle />
    </div>
  </div>
</section>

<section class="-mt-24">
  <h2>Ultime notizie</h2>

  <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
    {#each posts as post}
      <ArticleCard article={post} />
    {/each}
  </div>
</section>