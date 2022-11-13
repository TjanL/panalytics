<script lang="ts">
	export let main: string;
	export let sub: string;
	export let color = 'slate';
	export let icon = '';
</script>

<div>
	<div class="flex flex-col rounded-3xl bg-{color}-100 text-{color}-800 p-8">
		<div>
			<div class="text-xl md:text-3xl"><i class={icon} /></div>
		</div>
		<div class="md:mt-4">
			<div class="text-3xl md:text-5xl font-extrabold text-ellipsis overflow-hidden capitalize">
				{main}
			</div>
		</div>
		<div>
			<div class="text-base lowercase">{sub}</div>
		</div>
	</div>
</div>
