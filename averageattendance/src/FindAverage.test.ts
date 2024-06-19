import {FindAverage} from "./FindAverage";
import {describe, expect, it} from "vitest";

const findAv = new FindAverage();

describe("#FindAverage", () => {
    it("returns 2", () => {
        expect(findAv.calculateAverage(2,4,6,8)).toBe(5)
    })
})

describe('#Endpoint', () => {
    it('returns status code 200', async () => {
        const response = await fetch('http://averageattendance.40112152.qpc.hal.davecutting.uk/?lecture=90&lab=85&support_sessions=78&canvas_activities=92');
        expect(response.status).toBe(200);
    });
});