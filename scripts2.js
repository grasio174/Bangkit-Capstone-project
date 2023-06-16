fetch('https://api-gtgktzpmaq-et.a.run.app/fashion/catalog')
  .then(response => response.json())
  .then(data => {
    if (Array.isArray(data)) {
      data.forEach(item => {
        createCard(item);
      });
    } else if (typeof data === 'object') {
      const dataArray = Object.values(data);
      dataArray.forEach(item => {
        createCard(item);
      });
    } else {
      console.error('Invalid data format:', data);
    }
    adjustCardLayout(); // Call the function to adjust the card layout
  })
  .catch(error => {
    console.error('Error:', error);
  });

function createCard(item) {
  const card = document.createElement('div');
  card.classList.add('card');

  const image = document.createElement('img');
  image.src = item.picture;
  image.alt = item.name;

  const name = document.createElement('h3');
  name.textContent = item.name;

  card.appendChild(image);
  card.appendChild(name);

  const cardContainer = document.getElementById('cardContainer');
  if (cardContainer) {
    cardContainer.appendChild(card);
  } else {
    console.error('Card container element not found.');
  }

  // Add click event listener to the card
  card.addEventListener('click', () => {
    // Navigate to the details page passing the item ID as a query parameter
    window.location.href = `details.html?name=${item.name}`;
  });
}

function adjustCardLayout() {
  const cardContainer = document.getElementById('cardContainer');
  if (cardContainer) {
    const cardItems = cardContainer.getElementsByClassName('card');
    const cardWidth = cardItems[0].offsetWidth;
    const containerWidth = cardContainer.offsetWidth;
    const columns = Math.floor(containerWidth / cardWidth);
    cardContainer.style.gridTemplateColumns = `repeat(${columns}, minmax(${cardWidth}px, 1fr))`;
  }
}




// Get the item name from the query parameter in the URL
const urlParams = new URLSearchParams(window.location.search);
const itemName = urlParams.get('name');

// Fetch item details from the API based on the name
fetch(`https://api-gtgktzpmaq-et.a.run.app/fashion/catalog?name=${itemName}`)
  .then(response => response.json())
  .then(data => {
    displayItemDetails(data);
  })
  .catch(error => {
    console.error('Error:', error);
  });

function displayItemDetails(item) {
  const itemDetailsContainer = document.getElementById('itemDetails');
  itemDetailsContainer.classList.add('details-container');

  // Left column for image
  const leftColumn = document.createElement('div');
  leftColumn.classList.add('left-column');

  const image = document.createElement('img');
  image.src = item.picture;
  image.alt = item.name;

  const name = document.createElement('h2');
  name.textContent = item.name;

  leftColumn.appendChild(image);
  leftColumn.appendChild(name);

  // Right column for details
  const rightColumn = document.createElement('div');
  rightColumn.classList.add('right-column');

  const description = document.createElement('p');
  description.textContent = item.description;

  const category = document.createElement('p');
  category.textContent = `Category: ${item.category || 'N/A'}`;

  const buyLink = document.createElement('a');
  buyLink.textContent = 'Buy Now';
  buyLink.href = item.buy_link || '#'; // Provide a fallback link if not available

  rightColumn.appendChild(description);
  rightColumn.appendChild(category);
  rightColumn.appendChild(buyLink);

  itemDetailsContainer.appendChild(leftColumn);
  itemDetailsContainer.appendChild(rightColumn);
}
