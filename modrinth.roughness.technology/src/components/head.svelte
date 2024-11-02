<script lang="ts">
    import { METADATA as metadata } from '$content/info';
</script>

<svelte:head>
    <title>{metadata.title}</title>
    <meta name="description" content={metadata.description} />
    <meta name="robots" content="index, follow" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content={metadata['og:site_name']} />
    <meta property="og:title" content={metadata.title} />
    <meta property="og:description" content={metadata.descripton} />
</svelte:head>
