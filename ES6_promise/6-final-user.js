import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName).catch((error) => error),
  ])
    .then(([userResp, fileResp]) => {
      return [
        {
          status: "fulfilled",
          value: userResp
        },
        {
          status: "fulfilled",
          value: fileResp
        },
      ];
      }).catch((error) => {
        return [
          {
            status: "rejected",
            value: error
          },
        ];
      });
}