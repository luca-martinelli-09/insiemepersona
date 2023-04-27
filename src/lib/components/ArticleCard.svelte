<script lang="ts">
  import { formatDate } from "$lib/utils";
  import type { Post } from "$lib/utils/utils";

  export let article: Post;
</script>

<a href="/articoli/{article.id}" class="bg-white text-gray-900 shadow-md hover:shadow-lg transition-shadow duration-300 ease-in border border-gray-100 aspect-video w-full">
  <img src={article.image} alt={article.title} />
  <div class="p-4">
    <span class="text-sm block mb-3">{formatDate(article.date)}</span>
    <h3 class="text-2xl font-display font-bold">{article.title}</h3>
    <p class="font-serif text-sm mt-3 text-justify opacity-80">{article.abstract}</p>
  </div>
</a>
