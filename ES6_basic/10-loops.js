export default function appendToEachArrayValue(array, appendString) {
    let newArray = array
    for (let idx in array) {
      let value = array[idx];
      newArray[idx] = appendString + value;
    }
  
    return newArray;
  }
