<script lang="ts">
    import { toggleMode, mode } from 'mode-watcher';
    import { MoonIcon, SunIcon } from 'lucide-svelte';
</script>

<button on:click={toggleMode} aria-label="Toggle dark mode" class="opacity-80 hover:opacity-100 mr-5">
    {#if $mode === 'light'}
        <SunIcon aria-label="Sun" size={20} strokeWidth={1.5} />
    {:else}
        <MoonIcon aria-label="Moon" size={20} strokeWidth={1.5} />
    {/if}
</button>
