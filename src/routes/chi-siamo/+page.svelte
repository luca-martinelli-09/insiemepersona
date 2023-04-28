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
  <main class="justify-center">
    <h1 class="title text-center mb-20">Il candidato <span class="green font-medium">sindaco</span></h1>
    {#if sindaco}
      <div class="flex items-center justify-center">
        <AvatarCandidato candidato={sindaco} />
      </div>
    {/if}
    <div class="flex mt-10 justify-center">
      <a class="button primary" href="#consiglieri">Candidati consiglieri</a>
    </div>
  </main>
</section>

<section id="consiglieri">
  <main>
    <h2 class="title text-center mb-20">I candidati <span class="green">consiglieri</span></h2>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-5 text-gray-900">
      <div class="flex flex-col items-center gap-20 bg-white p-10 shadow-md">
        <ViviamoSonaLogo size={250} class="w-full" />
        <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 items-start gap-8">
          {#each viviamoSona as candidato}
            <AvatarCandidato {candidato} mini={true} />
          {/each}
        </div>
      </div>

      <div class="flex flex-col items-center gap-20 bg-white p-10 shadow-md">
        <InsiemePerSonaLogo size={250} class="w-full" />
        <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 items-start gap-8">
          {#each insiemePerSona as candidato}
            <AvatarCandidato {candidato} mini={true} />
          {/each}
        </div>
      </div>
    </div>
  </main>
</section>
