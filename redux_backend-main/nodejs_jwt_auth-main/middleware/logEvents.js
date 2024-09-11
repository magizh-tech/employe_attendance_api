const { format } = require('date-fns');
// date-fns is used to format the date
const { v4: uuid } = require('uuid');
// uuid is used to generate unique ids
const fs = require('fs');
// fs is used to access the file system
const fsPromises = require('fs').promises;
// fsPromises is used to access the file system in promises, instead of callbacks, 
const path = require('path');
// path is used to access the path of the file system


const logEvents = async (message, logName) => {
    const dateTime = `${format(new Date(), 'yyyyMMdd\tHH:mm:ss')}`;
    // format is used to format the date
    const logItem = `${dateTime}\t${uuid()}\t${message}\n`;

    try {
        if (!fs.existsSync(path.join(__dirname, '..', 'logs'))) {
            await fsPromises.mkdir(path.join(__dirname, '..', 'logs'));
        }

        await fsPromises.appendFile(path.join(__dirname, '..', 'logs', logName), logItem);
    } catch (err) {
        console.log(err);
    }
}

const logger = (req, res, next) => {
    logEvents(`${req.method}\t${req.headers.origin}\t${req.url}`, 'reqLog.txt');
    console.log(`${req.method} ${req.path}`);
    next();
}

module.exports = { logger, logEvents };
