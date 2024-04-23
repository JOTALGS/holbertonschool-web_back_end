export default function createReportObject(employeesList) {
    const newReport = {
      allEmployees: { ...employeesList },
      getNumberOfDepartments(employeesList) {
        return Object.keys(employeesList).length;
      },
    };
    return newReport;
  }