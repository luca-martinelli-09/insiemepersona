import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/kit/vite';
import { mdsvex } from 'mdsvex'
import rehypeExternalLinks from 'rehype-external-links';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';
import accessibleEmojis from 'rehype-accessible-emojis';

const extensions = ['.svelte', '.svx', '.md'];

/** @type {import('@sveltejs/kit').Config} */
const config = {
	extensions: extensions,
	preprocess: [
		vitePreprocess(),
		mdsvex({
			extensions: extensions,
			rehypePlugins: [
				rehypeExternalLinks,
				rehypeSlug,
				accessibleEmojis,
				[rehypeAutolinkHeadings, {
					behavior: 'append'
				}]
			]
		})
	],

	kit: {
		adapter: adapter()
	}
};

export default config;
