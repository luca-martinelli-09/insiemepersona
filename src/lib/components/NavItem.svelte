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
    @apply font-bold block text-gray-900;
  }

  a.active {
    @apply text-[#006896];
  }
</style>
