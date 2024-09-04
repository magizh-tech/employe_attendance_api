import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getEmployeeById, getAttendanceByEmployeeId } from '../services/api';

const EmployeeDetail = () => {
    const { id } = useParams();
    const [employee, setEmployee] = useState(null);
    const [attendance, setAttendance] = useState([]);

    useEffect(() => {
        getEmployeeById(id).then(data => setEmployee(data));
        getAttendanceByEmployeeId(id).then(data => setAttendance(data));
    }, [id]);

    if (!employee) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>{employee.name}</h1>
            <p>Email: {employee.email}</p>
            <p>Department: {employee.department}</p>

            <h2>Attendance</h2>
            <ul>
                {attendance.map(record => (
                    <li key={record.id}>
                        Date: {new Date(record.date).toLocaleDateString()} - Status: {record.status}
                    </li>
                ))}
            </ul>

            <Link to="/">Back to Employee List</Link>
        </div>
    );
};

export default EmployeeDetail;
