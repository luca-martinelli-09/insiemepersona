import type { Post } from "$lib/utils/utils";
import type { PageLoad } from "./$types";

export const load = (async () => {
  const postsFiles = import.meta.glob("../../md/articoli/*.md");
  const iterablePosts = Object.entries(postsFiles);

  let posts = await Promise.all(
    iterablePosts.map(async ([_, resolver]) => {
      const post = <Post>(<any>await resolver()).metadata;
      return post;
    })
  );

  posts = posts.sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));

  return {
    posts,
  };
}) satisfies PageLoad;
