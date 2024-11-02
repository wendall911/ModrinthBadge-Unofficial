<script lang="ts">
    import { page } from '$app/stores';
</script>

<main class="mx-4 my-32 flex max-w-5xl flex-col items-center gap-16 self-center">
    <article class="mb-8 flex flex-col gap-16">
        <div class="flex flex-col items-center gap-4 self-center">
            <h1 class="pb-1 text-5xl">Error {$page.status}</h1>
            <span class="text-lg">{$page.error?.message ?? 'Page Not Found'}</span>
        </div>

        <a href="/" variant="secondary"> Home </a>
    </article>
</main>
