import { signUpUser } from './4-user-promise.js';
import { uploadPhoto } from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName).catch((error) => error),
  ]).then(([user, photo]) => {
    return [
      { status: "fulfilled", value: user },
      { status: "fulfilled", value: photo },
    ];
  }).catch((error) => {
    return [
      { status: "rejected", value: error },
    ];
  });
}
