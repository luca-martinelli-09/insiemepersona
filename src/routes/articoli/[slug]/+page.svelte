<script lang="ts">
  import { formatDate } from "$lib/utils";
  import type { PageData } from "./$types";

  export let data: PageData;
</script>

<section class="mt-32">
  <article class="prose font-serif mx-auto bg-white max-w-screen-lg shadow-lg">
    <img src={data.info.image} alt={data.info.title} class="aspect-video w-full mb-0" />
    <div class="p-5 md:p-10 md:pt-5">
      <span class="block mb-5">{formatDate(data.info?.date)}</span>
      <h1 class="mt-0">{data.info.title}</h1>
      <div class="text-justify">
        <svelte:component this={data.content} />
      </div>
    </div>
  </article>
</section>
