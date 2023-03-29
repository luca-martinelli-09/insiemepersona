<script lang="ts">
  import ArticleCard from "$lib/components/ArticleCard.svelte";
  import type { PageData } from "./$types";

  export let data: PageData;
  const posts = data.posts;
</script>

<section>
  <h1>Ultime notizie</h1>

  <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
    {#each posts as post}
      <ArticleCard article={post} />
    {/each}
  </div>
</section>