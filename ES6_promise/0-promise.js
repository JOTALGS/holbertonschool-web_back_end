export default function getResponseFromAPI() {
    return new Promise((resolve) => {
      setTimeout(() => {
        const response = 'I promise'
        resolve(response);
      }, 1000);
    });
  }