const { uploadPhoto, createUser } = require('./utils.js');

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((resp) => {
      const body = resp[0];
      const firstName = resp[1];
      const lastName = resp[1];
      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch(() => console.error('Signup system offline'));
}
