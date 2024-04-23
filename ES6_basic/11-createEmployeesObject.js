export default function createEmployeesObject(departmentName, employees) {
  const employeesInfo = {
    [`${departmentName}`]: employees,
  };
  return employeesInfo;
}
