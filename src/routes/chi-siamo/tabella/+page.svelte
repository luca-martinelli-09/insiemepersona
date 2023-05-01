<script lang="ts">
  import { formatDate, LIST_TO_NAME } from "$lib/utils";
  import type { PageData } from "./$types";
  import InsiemePerSonaLogo from "$lib/components/logos/InsiemePerSonaLogo.svelte";
  import ViviamoSonaLogo from "$lib/components/logos/ViviamoSonaLogo.svelte";

  export let data: PageData;

  const people = data.people;

  const consiglieri = people.filter((c) => c.type == "consigliere");

  const viviamoSona = consiglieri.filter((c) => c.list.includes("viviamosona"));
  const insiemePerSona = consiglieri.filter((c) => c.list.includes("insiemepersona"));
</script>

<section>
  <main>
    <h2 class="title">Candidati consiglieri in formato <span class="green">tabellare</span></h2>

    <div class="max-w-screen-2xl mt-20 mx-auto">
      <article class="bg-white prose max-w-none w-full mx-auto shadow-lg p-5 md:p-10 md:pt-5">
        <div class="flex gap-3 items-center">
          <ViviamoSonaLogo size={75} />
          <h1 class="my-0">Viviamo Sona</h1>
        </div>

        <div class="overflow-x-auto mt-5">
          <table class="w-full">
            <thead>
              <tr>
                <th class="uppercase whitespace-nowrap">#</th>
                <th class="uppercase whitespace-nowrap">Cognome e nome</th>
                <th class="uppercase whitespace-nowrap">Data di nascita</th>
                <th class="uppercase whitespace-nowrap">Luogo di nascita</th>
                <th class="uppercase whitespace-nowrap">Curriculum Vitae</th>
                <th class="uppercase whitespace-nowrap">Casellario giudiziale</th>
              </tr>
            </thead>
            <tbody>
              {#each viviamoSona as candidato}
                <tr>
                  <td class="whitespace-nowrap">{candidato.order}</td>
                  <th class="whitespace-nowrap">{candidato.surname} {candidato.name}</th>
                  <td class="whitespace-nowrap">{formatDate(candidato.birthday)}</td>
                  <td class="whitespace-nowrap">{candidato.birthplace}</td>
                  <td class="whitespace-nowrap"><a href={candidato.cv}>Scarica</a></td>
                  <td class="whitespace-nowrap"><a href={candidato.casellario}>Scarica</a></td>
                </tr>
              {/each}
            </tbody>
          </table>
        </div>
      </article>
    </div>

    <div class="max-w-screen-2xl mt-20 mx-auto">
      <article class="bg-white prose max-w-none w-full mx-auto shadow-lg p-5 md:p-10 md:pt-5">
        <div class="flex gap-3 items-center">
          <InsiemePerSonaLogo size={75} />
          <h1 class="my-0">Insieme per Sona</h1>
        </div>

        <div class="overflow-x-auto mt-5">
          <table class="w-full">
            <thead>
              <tr>
                <th class="uppercase whitespace-nowrap">#</th>
                <th class="uppercase whitespace-nowrap">Cognome e nome</th>
                <th class="uppercase whitespace-nowrap">Data di nascita</th>
                <th class="uppercase whitespace-nowrap">Luogo di nascita</th>
                <th class="uppercase whitespace-nowrap">Curriculum Vitae</th>
                <th class="uppercase whitespace-nowrap">Casellario giudiziale</th>
              </tr>
            </thead>
            <tbody>
              {#each insiemePerSona as candidato}
                <tr>
                  <td class="whitespace-nowrap">{candidato.order}</td>
                  <th class="whitespace-nowrap">{candidato.surname} {candidato.name}</th>
                  <td class="whitespace-nowrap">{formatDate(candidato.birthday)}</td>
                  <td class="whitespace-nowrap">{candidato.birthplace}</td>
                  <td class="whitespace-nowrap"><a href={candidato.cv}>Scarica</a></td>
                  <td class="whitespace-nowrap"><a href={candidato.casellario}>Scarica</a></td>
                </tr>
              {/each}
            </tbody>
          </table>
        </div>
      </article>
    </div>
  </main>
</section>
