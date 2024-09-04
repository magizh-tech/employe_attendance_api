import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

export const getEmployees = async () => {
    const response = await axios.get(`${API_BASE_URL}/employees/`);
    return response.data;
};

export const getEmployeeById = async (id) => {
    const response = await axios.get(`${API_BASE_URL}/employees/${id}`);
    return response.data;
};

export const createEmployee = async (employeeData) => {
    const response = await axios.post(`${API_BASE_URL}/employees/`, employeeData);
    return response.data;
};

export const getAttendanceByEmployeeId = async (id) => {
    const response = await axios.get(`${API_BASE_URL}/employees/${id}/attendance/`);
    return response.data;
};

export const createAttendance = async (id, attendanceData) => {
    const response = await axios.post(`${API_BASE_URL}/employees/${id}/attendance/`, attendanceData);
    return response.data;
};
