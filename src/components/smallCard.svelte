<script lang="ts">
	export let main: string;
	export let sub: string;
	export let color = 'slate';
</script>

<div>
	<div class="flex flex-col rounded-3xl bg-{color}-100 text-{color}-800 p-8">
		<div>
			<div class="text-2xl font-bold text-ellipsis overflow-hidden capitalize">{main}</div>
		</div>
		<div>
			<div class="text-base lowercase">{sub}</div>
		</div>
	</div>
</div>
