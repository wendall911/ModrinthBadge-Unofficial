import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    // Consult https://kit.svelte.dev/docs/integrations#preprocessors
    // for more information about preprocessors
    preprocess: vitePreprocess(),

    kit: {
        // adapter-auto only supports some environments, see https://kit.svelte.dev/docs/adapter-auto for a list.
        // If your environment is not supported, or you settled on a specific environment, switch out the adapter.
        // See https://kit.svelte.dev/docs/adapters for more information about adapters.
        adapter: adapter({
            pages: '../website',
            assets: '../website',
            fallback: 'index.html',
        }),
        csp: {
            mode: 'hash',
        },
        csrf: {
            // Only disable if in development mode
            checkOrigin: process.env.NODE_ENV !== 'development',
        },
        alias: {
            $comp: './src/components',
            $ui: './src/components/ui',
            $lib: './src/lib',
            $content: './src/content',
        },
    },
};

export default config;
