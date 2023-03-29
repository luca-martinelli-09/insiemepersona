<script lang="ts">
  import { page } from "$app/stores";

  export let href: string;
  export let name: string;
</script>

<li>
  <a {href} class:active={$page.url.pathname === href}>{name}</a>
</li>

<style lang="postcss">
  a {
    @apply font-bold block py-2 pl-3 pr-4 text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-600 md:p-0;
  }

  a.active {
    @apply bg-blue-600 md:bg-transparent text-white md:text-blue-600;
  }
</style>
