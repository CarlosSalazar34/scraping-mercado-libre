const objects = [];

document.querySelectorAll('.ui-search-layout__item').forEach(item => {
    
    const title = item.querySelector('.poly-component__title')?.textContent.trim();
    const price = item.querySelector('.andes-money-amount__fraction')?.textContent.trim();
    const image = item.querySelector('.poly-component__picture')?.src;
    const link = item.querySelector('.poly-component__link.poly-component__link--carousel')?.href;

    objects.push({
        title,
        price,
        image,
        link
    });
});

console.log(objects);

fetch(
    'http://172.20.10.3:5000/send-data',
    {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(objects)
    }
).then(response => response.json())
  .then(data => console.log('Success:', data))
  .catch((error) => console.error('Error:', error))