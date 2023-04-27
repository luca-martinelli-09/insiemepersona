<script lang="ts">
  import ArticleCard from "$lib/components/ArticleCard.svelte";
  import type { PageData } from "./$types";

  export let data: PageData;
  const posts = data.posts;
</script>

<section>
  <main>
    <h1 class="title">Rassegna stampa</h1>

    <div class="mt-20 grid md:grid-cols-2 lg:grid-cols-3 gap-4">
      {#each posts as post}
        <ArticleCard article={post} />
      {/each}
    </div>
  </main>
</section>
