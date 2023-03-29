<script lang="ts">
  import { formatDate, LIST_TO_NAME } from "$lib/utils";
  import type { PageData } from "./$types";

  export let data: PageData;
  const candidato = data.info;
</script>

<section>
  <article class="prose font-serif mx-auto bg-white max-w-screen-lg shadow-lg">
    <img
      src={candidato.image}
      alt={candidato.name + " " + candidato.surname}
      class="aspect-video w-full mb-0 object-cover border-b-4 {candidato.gender == 'M' ? 'border-blue-600' : 'border-pink-300'}"
    />
    <div class="p-5 md:p-10 md:pt-5">
      <h1 class="mt-5 mb-2">{candidato.name} {candidato.surname}</h1>
      <span class="block font-sans font-bold">Candidato {candidato.type} per {candidato.list.map((e) => LIST_TO_NAME[e]).join(" e ")}</span>
      <span class="block mt-4">Nato il {formatDate(candidato.birthday)} a {candidato.birthplace}</span>
      <span class="block">Residente a {candidato.location}</span>
      <h2>Chi sono?</h2>
      <div class="text-justify">
        <svelte:component this={data.content} />
      </div>
      <div class="flex gap-3 mt-10 pt-10 border-t border-gray-200">
        <a class="button flex-1 text-sm" href={candidato.cv}>Scarica il curriculum</a>
        <a class="button flex-1 text-sm" href={candidato.casellario}>Scarica il casellario giudiziale</a>
      </div>
    </div>
  </article>
</section>
