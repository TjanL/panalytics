<script lang="ts">
	import Report, { type DataInterface } from '../components/report.svelte';

	export let data: Array<Array<DataInterface>>;
	let reports = Object.values(data)
</script>

<div class="container mx-auto">
	<div class="flex flex-col gap-10">
		<div class="text-5xl mt-10 md:text-7xl font-extrabold text-slate-800 uppercase text-center">
			<i class="text-5xl fa-solid fa-poop relative top-[-6px]" /> Analytics
		</div>
		{#each reports as report}
			<div><Report reportData={report} /></div>
		{/each}
	</div>
</div>
