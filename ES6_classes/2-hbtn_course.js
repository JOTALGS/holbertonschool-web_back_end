export default class HolbertonCourse {
  constructor(name, lenght, students) {
    if (typeof name != 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;
    if (typeof lenght != 'number') {
      throw new TypeError('Length must be a number');
    }
    this._lenght = lenght;
    if (typeof students != 'object') {
      throw new TypeError('Students must be a array');
    }
    this._students = students;
  };

  get name() {
    return this._name;
  };
  set name(name) {
    if (typeof name != 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;
  };

  get lenght() {
    return this._lenght;
  };
  set lenght(lenght) {
    if (typeof lenght != 'number') {
      throw new TypeError('Length must be a number');
    }
    this._lenght = lenght;
  };

  get students() {
    return this._students;
  };
  set students(students) {
    if (typeof students != 'object') {
      throw new TypeError('Students must be a array');
    }
    this._students = students;
  };
}
  