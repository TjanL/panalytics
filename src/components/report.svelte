<script lang="ts" context="module">
	export type DataInterface = {
		label: string;
		value: number;
	};
</script>

<script lang="ts">
	import '../app.css';
	import { onMount } from 'svelte';
	import Card from './card.svelte';
	import SmallCard from './smallCard.svelte';
	import { LineChart } from 'chartist';

	function LSR(data: Array<number>) {
		let n = data.length;
		let x = (n * (n + 1)) / 2; // Sum of x
		let y = data.reduce((sum, item) => sum + item, 0); // Sum of y
		let xy = data.reduce((sum, item, index) => sum + item * index, 0); // x * y
		let x2 = (n * (n + 1) * (2 * n + 1)) / 6; // Sum of x suares

		return (n * xy - x * y) / (n * x2 - x2); // Least Squares Regression
	}

	function trendLine(data: Array<number>) {
		let n = data.length;
		let x = (n * (n + 1)) / 2; // Sum of x
		let y = data.reduce((sum, item) => sum + item, 0); // Sum of y

		let m = LSR(data);
		let b = (y - m * x) / n; // b intercep

		return Array.from({ length: n }, (_, x) => m * x + b);
	}

	function slope(data: Array<number>) {
		let n = data.length;
		let max = maxPerDay(data);
		let slope = (max - 1) / n;

		return slope
	}

	function linear(data: Array<number>) {
		let n = data.length;
		let a = slope(data);

		return Array.from({ length: n }, (_, x) => a * x + 1);
	}

	function isMonthPositive(data: Array<number>) {
		return avgPerDay(data) >= 1;
	}

	function maxPerMonth(data: Array<number>) {
		return data.reduce((sum, item) => sum + item, 0);
	}

	function maxPerDay(data: Array<number>) {
		return Math.max(...data);
	}

	function avgPerDay(data: Array<number>) {
		return data.reduce((sum, item) => sum + item, 0) / data.length;
	}

	export let reportData: Array<DataInterface> = [];

	let monthData: Array<number> = [];
	let labels: Array<string> = [];
	reportData.forEach((item) => {
		monthData.push(item.value);
		labels.push(item.label);
	});

	let re = /[a-z]+/i;
	let monthSearch = re.exec(reportData[0].label);
	let month = monthSearch ? monthSearch[0] : '';

	let data = {
		labels: labels,
		series: [linear(monthData), monthData]
	};

	let options = {
		showPoint: false,
		axisX: {
			showGrid: false
		},
		stretch: true,
		onlyInteger: true
	};

	let chart: Element;
	onMount(() => {
		new LineChart(chart, data, options);
	});
</script>

<div class="flex flex-col gap-8 mb-10">
	<div class="text-6xl font-bold text-slate-800 ml-11 capitalize">{month}</div>
	<div class="flex flex-col md:flex-row gap-6">
		<div class="grow" bind:this={chart} />
		<div class="grid grid-cols-2 gap-2 md:gap-4 m-2">
			<Card icon="fa-solid fa-poop" main={String(maxPerMonth(monthData))} sub="total per month" />
			<Card
				icon="fa-solid fa-gauge-high"
				main={String(maxPerDay(monthData))}
				sub="maximum in a day"
				color="green"
			/>
			<Card
				icon="fa-solid fa-gauge-simple"
				main={String(avgPerDay(monthData).toFixed(2))}
				sub="average per day"
				color="slate"
			/>
			<SmallCard
				main={isMonthPositive(monthData) ? 'good' : 'bad'}
				sub={isMonthPositive(monthData) ? 'month is positive' : 'month is negative'}
				color={isMonthPositive(monthData) ? 'green' : 'red'}
			/>
		</div>
	</div>
</div>
<!-- <div class="bg-red-100 text-red-800 bg-green-100 text-green-800 bg-slate-100 text-slate-800" /> -->
