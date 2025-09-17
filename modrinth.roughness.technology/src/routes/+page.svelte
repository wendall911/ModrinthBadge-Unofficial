<script lang="ts">
    import Contacts from '$comp/contacts.svelte';
    import { INFO } from '$content/info';
    import { METADATA } from '$content/info';
</script>

<main class="mx-4 my-12 flex max-fit flex-col items-center gap-6 self-center">
    <article class="mb-8 flex flex-col gap-8">
        <div class="flex flex-col items-center self-center">
            <h1>{METADATA.title}</h1>
            <span class="text-lg">{METADATA.description}</span>
        </div>

        <p class="max-w-2xl">{INFO.overview}</p>
    </article>

    <article class="mb-8 flex flex-col gap-8">
        <div class="flex flex-col" id="api">
            <h2>Modrinth Badge API Usage</h2>
            <p>The base url is <a href="https://modrinth.roughness.technology">https://modrinth.roughness.technology</a>. HTTPS Only.</p>
        </div>
        <div class="flex flex-col">
            <h3>/&#123;project&#125;.svg</h3>
            <p>&#123;project&#125; can either be the id or slug</p>
            <ul>
                <li>
                    <a href="https://modrinth.com/mod/actually-harvest"><img src="/actually-harvest.svg" alt="actually-harvest.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/actually-harvest.svg</code>
                </li>
                <li>
                    <a href="https://modrinth.com/mod/actually-harvest"><img src="/sUbuUC7R.svg" alt="sUbuUC7R.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/sUbuUC7R.svg</code>
                </li>
            </ul>
        </div>
        <div class="flex flex-col">
            <h3>/&#123;style&#125;_&#123;project&#125;_&#123;extra&#125;.svg</h3>
            <p>&#123;style&#125; can either be 'short' or 'full', extra is optional text to be appended.
            <ul>
                <li>
                    <a href="https://modrinth.com/mod/actually-harvest"><img src="/short_actually-harvest.svg" alt="short_actually-harvest.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/short_actually-harvest.svg</code>
                </li>
                <li>
                    <a href="https://modrinth.com/mod/actually-harvest"><img src="/full_actually-harvest_downloads.svg" alt="full_actually-harvest_downloads.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/full_actually-harvest_downloads.svg</code>
                </li>
            </ul>
        </div>
        <div class="flex flex-col">
            <h3>/versions/&#123;project&#125;.svg</h3>
            <p>&#123;project&#125; can either be the id or slug</p>
            <p>Only returns one of: 1.6.4, 1.7.10, 1.8.9, 1.9.4, 1.10.2, 1.11.2, 1.12.2, 1.16.5, 1.18.2, 1.19.2, 1.20.1, 1.21.1, 1.21.8</p>
            <p>Versions will be updated in the future as they are released/stabilized</p>
            <ul>
                <li>
                    <a href="https://modrinth.com/mod/actually-harvest"><img src="/versions/actually-harvest.svg" alt="Versions actually-harvest.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/versions/actually-harvest.svg</code>
                </li>
                <li>
                    <a href="https://modrinth.com/mod/actually-harvest"><img src="/versions/sUbuUC7R.svg" alt="Versions sUbuUC7R.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/versions/sUbuUC7R.svg</code>
                </li>
            </ul>
        </div>
        <div class="flex flex-col">
            <h3>/versions/&#123;text&#125;_&#123;project&#125;_&#123;style&#125;.svg</h3>
            <p>&#123;text&#125; is optional and replaces the default 'Available for' text. &#123;style&#125; can either be 'all' or 'latest'.</p>
            <p>Only returns one of: 1.6.4, 1.7.10, 1.8.9, 1.9.4, 1.10.2, 1.11.2, 1.12.2, 1.16.5, 1.18.2, 1.19.2, 1.20.1, 1.21.1, 1.21.8</p>
            <p>Versions will be updated in the future as they are released/stabilized</p>
            <ul>
                <li>
                    <a href="https://modrinth.com/mod/actually-harvest"><img src="/versions/actually-harvest_latest.svg" alt="actually-harvest_latest.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/actually-harvest_latest.svg</code>
                </li>
                <li>
                    <a href="https://modrinth.com/mod/actually-harvest"><img src="/versions/For%20MC_actually-harvest_all.svg" alt="For MC actually-harvest_all.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/versions/For%20MC_actually-harvest_all.svg</code>
                </li>
            </ul>
        </div>
        <div class="flex flex-col">
            <h3>/author/&#123;name&#125;.svg</h3>
            <p>&#123;name&#125; can either be the id or username</p>
            <ul>
                <li>
                    <a href="https://modrinth.com/user/wendall911"><img src="/author/wendall911.svg" alt="wendall911.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/author/wendall911.svg</code>
                </li>
                <li>
                    <a href="https://modrinth.com/mod/modmuss50"><img src="/author/modmuss50.svg" alt="modmuss50.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/author/modmuss50.svg</code>
                </li>
            </ul>
        </div>
        <div class="flex flex-col">
            <h3>/author/&#123;style&#125;_&#123;project&#125;_&#123;extra&#125;.svg</h3>
            <p>&#123;style&#125; can either be 'short' or 'full', extra is optional text to be appended.</p>
            <ul>
                <li>
                    <a href="https://modrinth.com/user/wendall911"><img src="/author/short_wendall911.svg" alt="short_wendall911.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/author/short_wendall911.svg</code>
                </li>
                <li>
                    <a href="https://modrinth.com/user/modmuss50"><img src="/author/full_modmuss50_downloads.svg" alt="full_modmuss50_downloads.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/author/full_modmuss50_downloads.svg</code>
                </li>
            </ul>
        </div>
        <div class="flex flex-col">
            <h3>Alternate Badge Styles</h3>
            <p>Using the get param badge_style allows for changing the style. Currently only option is flat</p>
            <ul>
                <li>
                    <a href="https://modrinth.com/user/wendall911"><img src="/author/wendall911.svg" alt="wendall911.svg" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/author/wendall911.svg</code>
                </li>
                <li>
                    <a href="https://modrinth.com/user/wendall911"><img src="/author/wendall911.svg?badge_style=flat" alt="wendall911.svg flat" class="inline-block" /></a> -&gt; <code>https://modrinth.roughness.technology/author/wendall911.svg?badge_style=flat</code>
                </li>
            </ul>
        </div>
        <p class="max-w-6xl self-center font-bold">Not an official API.</p>
    </article>

    <article class="mb-8 flex flex-col gap-8">
        <Contacts />

        <div class="flex flex-col items-center self-center">
            <p class="my-2 max-w-3xl">
                Roughness Technology, LLC hosts this API as a courtesy for mod developers using Modrinth.
            </p>
            <p class="font-semibold">
                Roughness Technology, LLC and this site are not affiliated with Modrinth.
            </p>
        </div>
    </article>
</main>
