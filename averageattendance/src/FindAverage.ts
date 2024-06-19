export class FindAverage {
    calculateAverage(lecture: number, lab: number, support: number, canvas: number): number {
        return (lecture + lab + support + canvas) / 4.0;
    }
}