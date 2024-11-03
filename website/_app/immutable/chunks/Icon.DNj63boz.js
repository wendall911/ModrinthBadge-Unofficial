import{s as z,b as O,a as b,u as T,g as U,d as D,i as W,e as A}from"./scheduler.Bhe7-VEC.js";import{S as G,i as H,v as B,x as k,w as I,a as E,d as _,C as v,j as w,k as y,p as J,q as K,u as L}from"./index.BfFYL8sr.js";function M(n){return(n==null?void 0:n.length)!==void 0?n:Array.from(n)}function P(n,e){const i={},s={},o={$$scope:1};let u=n.length;for(;u--;){const d=n[u],r=e[u];if(r){for(const h in d)h in r||(s[h]=1);for(const h in r)o[h]||(i[h]=r[h],o[h]=1);n[u]=r}else for(const h in d)o[h]=1}for(const d in s)d in i||(i[d]=void 0);return i}function Y(n){return typeof n=="object"&&n!==null?n:{}}const Z={header_title:"Modrinth Badge",title:"Modrinth Badge - Unofficial",description:"A little badge/shield for mods on Modrinth","og:site_name":"modrinth.roughness.technology"},p={logo:"logo.png",overview:"API documentation for modrinth.roughness.technology. An unofficial badge API for Modrinth mods/modpacks/etc.",contact:{messaging:{p1:"wendallc",p2:"83864",p3:"com"},accounts:[{name:"CurseForge",url:"https://www.curseforge.com/members/wendall911/projects",curseforge:!0},{name:"Modrinth",url:"https://modrinth.com/user/wendall911",modrinth:!0},{name:"GitHub",url:"https://github.com/wendall911/ModrinthBadge-Unofficial",github:!0}]}};/**
 * @license lucide-svelte v0.441.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */const S={xmlns:"http://www.w3.org/2000/svg",width:24,height:24,viewBox:"0 0 24 24",fill:"none",stroke:"currentColor","stroke-width":2,"stroke-linecap":"round","stroke-linejoin":"round"};function j(n,e,i){const s=n.slice();return s[11]=e[i][0],s[12]=e[i][1],s}function N(n){let e,i=[n[12]],s={};for(let o=0;o<i.length;o+=1)s=b(s,i[o]);return{c(){e=B(n[11]),this.h()},l(o){e=I(o,n[11],{}),E(e).forEach(_),this.h()},h(){v(e,s)},m(o,u){w(o,e,u)},p(o,u){v(e,s=P(i,[u&32&&o[12]]))},d(o){o&&_(e)}}}function C(n){let e=n[11],i,s=n[11]&&N(n);return{c(){s&&s.c(),i=k()},l(o){s&&s.l(o),i=k()},m(o,u){s&&s.m(o,u),w(o,i,u)},p(o,u){o[11]?e?z(e,o[11])?(s.d(1),s=N(o),e=o[11],s.c(),s.m(i.parentNode,i)):s.p(o,u):(s=N(o),e=o[11],s.c(),s.m(i.parentNode,i)):e&&(s.d(1),s=null,e=o[11])},d(o){o&&_(i),s&&s.d(o)}}}function Q(n){let e,i,s,o,u,d=M(n[5]),r=[];for(let t=0;t<d.length;t+=1)r[t]=C(j(n,d,t));const h=n[10].default,f=O(h,n,n[9],null);let m=[S,n[7],{width:n[2]},{height:n[2]},{stroke:n[1]},{"stroke-width":s=n[4]?Number(n[3])*24/Number(n[2]):n[3]},{class:o=n[6]("lucide-icon","lucide",n[0]?`lucide-${n[0]}`:"",n[8].class)}],c={};for(let t=0;t<m.length;t+=1)c=b(c,m[t]);return{c(){e=B("svg");for(let t=0;t<r.length;t+=1)r[t].c();i=k(),f&&f.c(),this.h()},l(t){e=I(t,"svg",{width:!0,height:!0,stroke:!0,"stroke-width":!0,class:!0});var a=E(e);for(let l=0;l<r.length;l+=1)r[l].l(a);i=k(),f&&f.l(a),a.forEach(_),this.h()},h(){v(e,c)},m(t,a){w(t,e,a);for(let l=0;l<r.length;l+=1)r[l]&&r[l].m(e,null);y(e,i),f&&f.m(e,null),u=!0},p(t,[a]){if(a&32){d=M(t[5]);let l;for(l=0;l<d.length;l+=1){const g=j(t,d,l);r[l]?r[l].p(g,a):(r[l]=C(g),r[l].c(),r[l].m(e,i))}for(;l<r.length;l+=1)r[l].d(1);r.length=d.length}f&&f.p&&(!u||a&512)&&T(f,h,t,t[9],u?D(h,t[9],a,null):U(t[9]),null),v(e,c=P(m,[S,a&128&&t[7],(!u||a&4)&&{width:t[2]},(!u||a&4)&&{height:t[2]},(!u||a&2)&&{stroke:t[1]},(!u||a&28&&s!==(s=t[4]?Number(t[3])*24/Number(t[2]):t[3]))&&{"stroke-width":s},(!u||a&257&&o!==(o=t[6]("lucide-icon","lucide",t[0]?`lucide-${t[0]}`:"",t[8].class)))&&{class:o}]))},i(t){u||(J(f,t),u=!0)},o(t){K(f,t),u=!1},d(t){t&&_(e),L(r,t),f&&f.d(t)}}}function R(n,e,i){const s=["name","color","size","strokeWidth","absoluteStrokeWidth","iconNode"];let o=W(e,s),{$$slots:u={},$$scope:d}=e,{name:r=void 0}=e,{color:h="currentColor"}=e,{size:f=24}=e,{strokeWidth:m=2}=e,{absoluteStrokeWidth:c=!1}=e,{iconNode:t=[]}=e;const a=(...l)=>l.filter((g,q,F)=>!!g&&F.indexOf(g)===q).join(" ");return n.$$set=l=>{i(8,e=b(b({},e),A(l))),i(7,o=W(e,s)),"name"in l&&i(0,r=l.name),"color"in l&&i(1,h=l.color),"size"in l&&i(2,f=l.size),"strokeWidth"in l&&i(3,m=l.strokeWidth),"absoluteStrokeWidth"in l&&i(4,c=l.absoluteStrokeWidth),"iconNode"in l&&i(5,t=l.iconNode),"$$scope"in l&&i(9,d=l.$$scope)},e=A(e),[r,h,f,m,c,t,a,o,e,d,u]}class x extends G{constructor(e){super(),H(this,e,R,Q,z,{name:0,color:1,size:2,strokeWidth:3,absoluteStrokeWidth:4,iconNode:5})}}export{x as I,Z as M,Y as a,p as b,M as e,P as g};