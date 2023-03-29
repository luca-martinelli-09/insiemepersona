<script lang="ts">
  import AvatarCandidato from "$lib/components/AvatarCandidato.svelte";
  import InsiemePerSonaLogo from "$lib/components/logos/InsiemePerSonaLogo.svelte";
  import ViviamoSonaLogo from "$lib/components/logos/ViviamoSonaLogo.svelte";
  import type { PageData } from "./$types";

  export let data: PageData;

  const people = data.people;

  const sindaco = people.filter((c) => c.type == "sindaco")?.at(0);
  const consiglieri = people.filter((c) => c.type == "consigliere");

  const viviamoSona = consiglieri.filter((c) => c.list.includes("viviamosona"));
  const insiemePerSona = consiglieri.filter((c) => c.list.includes("insiemepersona"));
</script>

<section>
  <h1 class="text-center mt-10">Il candidato sindaco</h1>
  {#if sindaco}
    <div class="flex items-center justify-center">
      <AvatarCandidato candidato={sindaco} />
    </div>
  {/if}

  <h2 class="text-center mt-10">I candidati consiglieri</h2>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
    <div class="flex flex-col items-center gap-20 bg-white p-10 shadow-md">
      <ViviamoSonaLogo size={200} />
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 items-center gap-8">
        {#each viviamoSona as candidato}
          <AvatarCandidato {candidato} mini={true} />
        {/each}
      </div>
    </div>

    <div class="flex flex-col items-center gap-20 bg-white p-10 shadow-md">
      <InsiemePerSonaLogo size={200} />
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 items-center gap-8">
        {#each insiemePerSona as candidato}
          <AvatarCandidato {candidato} mini={true} />
        {/each}
      </div>
    </div>
  </div>
</section>
