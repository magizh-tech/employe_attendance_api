const verifyRoles = (...allowedRoles) => {
    return (req, res, next) => {
        if (!req?.roles) return res.sendStatus(401);
        const rolesArray = [...allowedRoles];
        const result = req.roles.map(role => rolesArray.includes(role)).find(val => val === true);
        // the above line is used to check if the user has the role or not
        // find val => val === true is used to check if the user has the role or not
        if (!result) return res.sendStatus(401);
        next();
    }
}

module.exports = verifyRoles
// rolesarray=[admin]
// req.roles => [user,editor]

// 