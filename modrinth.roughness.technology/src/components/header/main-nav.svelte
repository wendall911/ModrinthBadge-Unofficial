<script lang="ts">
    import { page } from '$app/state';
    import cn from 'classnames';
    import ModeToggle from '$comp/header/mode-toggle.svelte';
    import { NAVIGATION } from '$content/links';
    import { INFO } from '$content/info';
    import { METADATA } from '$content/info';
</script>

<div class="flex w-full flex-row justify-between">
    <!-- eslint-disable-next-line svelte/no-navigation-without-resolve -->
    <a href="/">
        <img
            id="logo"
            src={INFO.logo}
            class="logo-img mr-3 mb-2 ml-2 inline max-h-9 sm:h-9"
            alt={METADATA.title}
        />
        <h3 class="mt-2 hidden self-center sm:inline">
            {METADATA.header_title}
        </h3>
    </a>
    <nav class="items-right mt-2 text-sm">
        {#each NAVIGATION as link (link.name)}
            <!-- eslint-disable svelte/no-navigation-without-resolve -->
            <a
                href={link.url}
                class={cn(
                    'hover:text-foreground mb-2 inline-block pr-4 align-middle transition-colors',
                    page.url.pathname.includes(link.url) ? 'text-foreground' : 'text-foreground/80'
                )}
            >
                {link.name}
            </a>
        {/each}
        <ModeToggle />
    </nav>
</div>
