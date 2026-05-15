<script lang="ts">
    import { toggleMode, mode } from 'mode-watcher';
    import { MoonIcon, SunIcon } from '@lucide/svelte';
</script>

<button
    onclick={toggleMode}
    aria-label="Toggle dark mode"
    class="mr-5 opacity-80 hover:opacity-100"
>
    {#if mode.current === 'light'}
        <SunIcon aria-label="Sun" size={20} strokeWidth={1.5} />
    {:else}
        <MoonIcon aria-label="Moon" size={20} strokeWidth={1.5} />
    {/if}
</button>
