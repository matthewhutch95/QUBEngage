import express, { Application, Request, Response } from 'express';
import cors from 'cors';
import {FindAverage} from "./FindAverage";
const app: Application = express();

const findAv = new FindAverage();

app.use(cors());

app.get('/', (req: Request, res: Response) => {
    res.set('Access-Control-Allow-Origin', '*')
    const { lecture, lab, support_sessions, canvas_activities } = req.query;

    if (checkForInt(lecture as string) && checkForInt(lab as string) && checkForInt(support_sessions as string) && checkForInt(canvas_activities as string)) {
        const average = findAv.calculateAverage(
            Number(lecture),
            Number(lab),
            Number(support_sessions),
            Number(canvas_activities)
        );

        res.json({ average });
    } else {
        res.status(400).json({ error: 'Invalid parameters, please use integers 0-9 and do not leave blank spaces' });
    }
});
app.listen(3000,() => {
    console.log("Server listening on port 3000");
});

function checkForInt(value: string): boolean {
    return typeof value !== 'undefined' && /^[0-9]+$/.test(value);
}

// It should be noted here that whenever we update our code inside src directory.
// We should run npm run build to transpile .ts files into .js files.
// Afterwards, npm run start will execute our code from build directory.