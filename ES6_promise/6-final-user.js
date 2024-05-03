const signUpUser = require('./4-user-promise.js').default;
const uploadPhoto = require('./5-photo-reject.js').default;

export default function handleProfileSignup(firstName, lastName, fileName) {
  const userResponse = signUpUser(firstName, lastName)
    .then((value) => ({
        status: 'fulfilled',
        value,
    }))
    .catch((error) => ({
      status: 'rejected',
      value: error,    
    }));
  const fileResponse = uploadPhoto(fileName)
    .then((value) => ({
        status: 'fulfilled',
        value,
    }))
    .catch((error) => ({
      status: 'rejected',
      value: error,    
    }));
  const response = [userResponse, fileResponse];
  return Promise.allSettled(response);
}