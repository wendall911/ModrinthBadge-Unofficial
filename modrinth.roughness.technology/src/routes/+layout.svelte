<script>
    import '../app.css';
    import { ModeWatcher } from 'mode-watcher';
    import Head from '$comp/head.svelte';
    import Nav from '$comp/header/nav.svelte';
</script>

<Head />

<ModeWatcher />

<div class="flex min-h-screen flex-col">
    <Nav />
    <slot />
</div>
