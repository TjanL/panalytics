import type DataInterface from '../components/report.svelte';

export async function load() {
	const allFiles = import.meta.glob('../../data/*.csv');
	const iter = Object.entries(allFiles);

	const allData: Array<Array<DataInterface>> = [];
	for (const [_, resolver] of iter) {
        const csvFile: any = await resolver();
		const data = csvFile.default.map((item: any) => {
			return { label: item.Date, value: Number(item.Poops) };
		});

		allData.push(data);
	}

	return allData;
};
