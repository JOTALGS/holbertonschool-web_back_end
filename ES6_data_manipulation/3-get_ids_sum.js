export default function getStudentIdsSum(arrayOfStudents) {
  return arrayOfStudents.reduce((sum, student) => sum + student.id, 0);
}
