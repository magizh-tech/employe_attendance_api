const allowedOrigins = require('../config/allowedOrigins');

const credentials = (req, res, next) => {
    const origin = req.headers.origin;
    if (allowedOrigins.includes(origin)) {
        res.header('Access-Control-Allow-Credentials', true);
       
        // the above line is added to enable credentials to be sent with the request, 
        // crendentials in this case are cookies.

    }
    next();
}

module.exports = credentials