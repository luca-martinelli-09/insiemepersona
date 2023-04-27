<script lang="ts">
  import type { Candidato } from "$lib/utils/utils";

  export let candidato: Candidato;

  let clazz: string = "";
  export { clazz as class };

  export let mini = false;
</script>

<a href="/chi-siamo/{candidato.id}" class="flex flex-col items-center justify-center {mini ? '' : 'w-full max-w-sm'} {clazz}">
  <img
    src={candidato.image}
    alt={candidato.name + " " + candidato.surname}
    class="rounded-full aspect-square object-cover object-top w-full border-4 {candidato.gender == 'M' ? 'border-blue-600' : 'border-pink-300'}"
  />
  <h3 class="mt-4 font-display font-bold {mini ? 'text-xl' : 'text-3xl'} text-center">{candidato.name}<br />{candidato.surname}</h3>
</a>
