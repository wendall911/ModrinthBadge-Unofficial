<script lang="ts">
    import { page } from '$app/stores';
    import cn from 'classnames';
    import ModeToggle from '$comp/header/mode-toggle.svelte';
    import { NAVIGATION } from '$content/links';
    import { INFO } from '$content/info';
    import { METADATA } from '$content/info';
    import { mode } from 'mode-watcher';

    $: invert = $mode === 'light' ? 'dark:invert' : '';
</script>

<div class="justify-between flex flex-row w-full">
    <a href="/">
        <img id="logo" src={INFO.logo} class="ml-2 mr-3 mb-2 sm:h-9 max-h-9 {invert} inline" alt={METADATA.title} />
        <h3 class="hidden self-center sm:inline mt-2" >
            {METADATA.header_title}
        </h3>
    </a>
    <nav class="items-right text-sm mt-2">
        {#each NAVIGATION as link}
            <a
                href={link.url}
                class={cn(
                    'hover:text-foreground transition-colors pr-4 mb-2 align-middle inline-block',
                    $page.url.pathname.includes(link.url) ? 'text-foreground' : 'text-foreground/80'
                )}
            >
                {link.name}
            </a>
        {/each}
        <ModeToggle />
    </nav>
</div>
