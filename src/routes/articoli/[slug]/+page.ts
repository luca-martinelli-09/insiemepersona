import type { Post } from "$lib/utils/utils";
import type { PageLoad } from "./$types";

export const load = (async ({ params }) => {
  const post = await import(`../../../md/articoli/${params.slug}.md`);

  return {
    info: post.metadata as Post,
    content: post.default,
  };
}) satisfies PageLoad;
