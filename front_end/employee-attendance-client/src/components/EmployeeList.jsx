import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { getEmployees } from '../services/api';

const EmployeeList = () => {
    const [employees, setEmployees] = useState([]);

    useEffect(() => {
        getEmployees().then(data => setEmployees(data));
    }, []);

    return (
        <div>
            <h1>Employee List</h1>
            <ul>
                {employees.map(employee => (
                    <li key={employee.id}>
                        <Link to={`/employees/${employee.id}`}>{employee.name}</Link>
                    </li>
                ))}
            </ul>
            <Link to="/create-employee">Create New Employee</Link>
        </div>
    );
};

export default EmployeeList;
