<script lang="ts">
    import { navigating } from '$app/stores';
    import { slide } from 'svelte/transition';
    import { quadInOut } from 'svelte/easing';

    import MainNav from '$comp/header/main-nav.svelte';
</script>

<header class="border-border/40 bg-background/95 supports-[backdrop-filter]:bg-background/60 sticky top-0 z-50 w-full border-b backdrop-blur">
    <div class="container flex h-14 max-w-screen-2xl items-center justify-end md:justify-start">
        <MainNav />
    </div>
</header>

{#if $navigating}
    <div class="relative">
        <div
            class="absolute h-1 w-full bg-green-300"
            transition:slide={{ delay: 100, duration: 500, easing: quadInOut }}
        />
    </div>
{/if}
