import { signUpUser } from './4-user-promise.js';
import { uploadPhoto } from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const userResponse = signUpUser(firstName, lastName)
    .then((value) => ({
        status: 'fulfilled',
        value: value,
    }))
    .catch((error) => ({
      status: 'rejected',
      value: error,    
    }));
  const fileResponse = uploadPhoto(fileName)
    .then((value) => ({
        status: 'fulfilled',
        value: value,
    }))
    .catch((error) => ({
      status: 'rejected',
      value: error,    
    }));
  const response = [userResponse, fileResponse];
  return Promise.allSettled(response);
}