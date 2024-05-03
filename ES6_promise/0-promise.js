export default function getResponseFromAPI() {
return new Promise((resolve) => {
  setTimeout(() => {
    const response = 'ok'
    resolve(response);
  }, 1000);
  });
}
