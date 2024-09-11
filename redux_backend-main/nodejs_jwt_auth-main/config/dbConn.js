const mongoose = require('mongoose');

const connectDB = async () => {
    try {
        await mongoose.connect(process.env.DATABASE_URI, {
            useUnifiedTopology: true,
            useNewUrlParser: true
        });
        // useUb=nifiedTopology: true to avoid deprecation warning
        // useNewUrlParser: true to avoid deprecation warning
    } catch (err) {
        console.error(err);
    }
}

module.exports = connectDB