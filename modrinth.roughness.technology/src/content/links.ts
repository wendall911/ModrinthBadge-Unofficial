import { INFO } from './info';

export const NAVIGATION = [
    {
        name: 'Contact',
        url: '#contact',
        sub: [
            {
                name: 'Email',
                url: `mailto:${INFO.contact.messaging.p1}@${INFO.contact.messaging.p2}.${INFO.contact.messaging.p3}`,
            },
            ...INFO.contact.accounts,
        ],
    },
    {
        name: 'API',
        url: '#api',
    },
];
