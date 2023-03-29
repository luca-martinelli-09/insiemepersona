import type { Candidato } from "$lib/utils/utils";
import type { PageLoad } from "./$types";

export const load = (async ({ params }) => {
  const candidato = await import(`../../../md/candidati/${params.slug}.md`);

  return {
    info: candidato.metadata as Candidato,
    content: candidato.default,
  };
}) satisfies PageLoad;
