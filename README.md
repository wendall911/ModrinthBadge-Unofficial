# ModrinthBadge (Unofficial)

A little badge/shield for mods on Modrinth. This service is not affiliated with
Modrinth, it is a personal project by wendall911 for people to display stats in
a simple way on their project pages.

## API

Full Documentation can be found at [Modrinth Badge - Unofficial](https://modrinth.roughness.technology)

### API Examples

The base url is
[https://modrinth.roughness.technology](https://modrinth.roughness.technology). HTTPS Only.

  * /{project}.svg: project either id or slug
    * [![](https://modrinth.roughness.technology/actually-harvest.svg)](https://modrinth.com/mod/actually-harvest) -> `https://modrinth.roughness.technology/actually-harvest.svg`
    * [![](https://modrinth.roughness.technology/sUbuUC7R.svg)](https://modrinth.com/mod/actually-harvest) -> `https://modrinth.roughness.technology/sUbuUC7R.svg`
  * /{style}\_{project}\_{extra}.svg: {style} can either be 'short' or 'full', extra is optional text to be appended.
    * [![](https://modrinth.roughness.technology/short_actually-harvest.svg)](https://modrinth.com/mod/actually-harvest) -> `https://modrinth.roughness.technology/short_actually-harvest.svg`
    * [![](https://modrinth.roughness.technology/full_actually-harvest_downloads.svg)](https://modrinth.com/mod/actually-harvest) -> `https://modrinth.roughness.technology/full_actually-harvest_downloads.svg`
  * /author/{name}.svg: {name} can either be the id or username
    * [![](https://modrinth.roughness.technology/author/wendall911.svg)](https://modrinth.com/user/wendall911) -> `https://modrinth.roughness.technology/author/wendall911.svg`

## Credits

Derived from [CurseForgeBadge Unofficial](https://github.com/way2muchnoise/CurseForgeBadge-Unofficial) No permissions were granted. This is not for profit, but only to support the modding community.
