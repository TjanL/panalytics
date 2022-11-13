import { sveltekit } from '@sveltejs/kit/vite';
import type { UserConfig } from 'vite';
import dsv from '@rollup/plugin-dsv';

const config: UserConfig = {
	plugins: [sveltekit(), dsv()]
};

export default config;
