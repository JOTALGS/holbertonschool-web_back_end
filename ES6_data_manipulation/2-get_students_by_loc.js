export default function getStudentsByLocation(arrayOfStudents, city) {
  return arrayOfStudents.filter((student) => student.location === city);
}
