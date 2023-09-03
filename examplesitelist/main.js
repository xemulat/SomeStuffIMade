// Cache frequently used DOM elements
const tableBody = document.querySelector('#data-table tbody');
const outputElement = document.createElement('pre');
document.body.appendChild(outputElement);

// Cache size regex and multiplier
const sizeRegex = /^(\d*\.?\d+)\s*(KB|MB|GB|TB)$/;
const sizeMultiplier = {
  'KB': 1024,
  'MB': 1024 * 1024,
  'GB': 1024 * 1024 * 1024,
  'TB': 1024 * 1024 * 1024 * 1024
};

// Parse data, calculate archive size, and display table
function processDataAndDisplayTable(data) {
  const fragment = document.createDocumentFragment();

  data.forEach(item => {
    const row = document.createElement('tr');
    const cells = Array.from({ length: 7 }, () => document.createElement('td'));

    cells[0].textContent = item.source;
    cells[1].textContent = item.name;
    cells[2].textContent = item.size;
    cells[3].textContent = item.items[0];
    cells[4].textContent = item.items[1];

    const linkCell = cells[5];
    const link = document.createElement('a');
    link.href = item.link;
    link.target = '_blank';
    link.textContent = truncateLink(item.link);
    linkCell.appendChild(link);

    cells.forEach(cell => row.appendChild(cell));
    fragment.appendChild(row);
  });

  tableBody.appendChild(fragment);

  calculateArchiveSize(data);
}

// Calculate and display archive size, pictures, and videos
function calculateArchiveSize(data) {
  let totalSizeBytes = 0;
  let totalPictures = 0;
  let totalVideos = 0;

  data.forEach(item => {
    const matches = item.size.match(sizeRegex);
    if (matches) {
      const size = parseFloat(matches[1]);
      const unit = matches[2];
      const sizeInBytes = size * (sizeMultiplier[unit] || 1);
      totalSizeBytes += sizeInBytes;

      if (item.items && item.items.length === 2) {
        const [pictures, videos] = item.items;
        totalPictures += pictures;
        totalVideos += videos;
      }
    }
  });

  const totalSizeGB = (totalSizeBytes / (1024 * 1024 * 1024)).toFixed(2);
  const totalSizeTB = (totalSizeBytes / (1024 * 1024 * 1024 * 1024)).toFixed(2);

  const output = `PPA Stats:
  Archive size:
    ${totalSizeGB}GB
    ${totalSizeTB}TB
  
  Content:
    ${totalVideos} Pictures
    ${totalPictures} Videos`;

  outputElement.textContent = output;
}

async function fetchData() {
  try {
    const response = await fetch('index.json');
    const data = await response.json();
    processDataAndDisplayTable(data);
  } catch (error) {
    displayError(`Error reading the index: ${error}`);
  }
}

// Table sorter
async function sortTable(tableId, column) {
  try {
    const table = document.querySelector(`#${tableId}`);
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    const sortOrder = table.dataset.sortOrder || 'asc';
    table.dataset.sortOrder = sortOrder === 'asc' ? 'desc' : 'asc';
    const sortFunction = getSortFunction(column);
    rows.sort((a, b) => sortFunction(a, b) * (sortOrder === 'asc' ? 1 : -1));
    while (tbody.firstChild) {
      tbody.removeChild(tbody.firstChild);
    }

    const fragment = document.createDocumentFragment();
    for (const row of rows) {
      fragment.appendChild(row);
    }
    tbody.appendChild(fragment);
  } catch (error) {
    displayError(`Error sorting table: ${error}`);
  }
}

function getSortFunction(column) {
  const sortFunctions = [
    (a, b) => compareCells(a.cells[0], b.cells[0]),
    (a, b) => compareCells(a.cells[1], b.cells[1]),
    (a, b) => compareCellsBySize(a.cells[2], b.cells[2]),
    (a, b) => compareCellsByNumber(a.cells[3], b.cells[3]),
    (a, b) => compareCellsByNumber(a.cells[4], b.cells[4])
  ];
  return sortFunctions[column] || null;
}

function compareCells(cellA, cellB) {
  return cellA.textContent.localeCompare(cellB.textContent);
}

function compareCellsBySize(cellA, cellB) {
  return convertSizeToBytes(cellA.textContent) - convertSizeToBytes(cellB.textContent);
}

function compareCellsByNumber(cellA, cellB) {
  return parseInt(cellA.textContent) - parseInt(cellB.textContent);
}

function convertSizeToBytes(size) {
  const matches = size.match(sizeRegex);
  if (matches) {
    const sizeValue = parseFloat(matches[1]);
    const unit = matches[2];
    return sizeValue * (sizeMultiplier[unit] || 1);
  }
  return 0;
}

function truncateLink(link) {
  const truncatedText = link.substring(0, 17);
  return truncatedText.length === link.length ? link : `${truncatedText}...`;
}

function getColumnId(column) {
  const columnIds = ['', 'source', 'name', 'size', 'videos', 'pictures'];
  return columnIds[column] || '';
}

// Call the main function asynchronously
async function main() {
  try {
    await fetchData();
    const table = document.querySelector('#data-table');
    table.addEventListener('click', async (event) => {
      if (event.target.tagName === 'TH') {
        const columnIndex = Array.from(event.target.parentNode.children).indexOf(event.target);
        const columnId = getColumnId(columnIndex);
        await sortTable('data-table', columnIndex);
      }
    });
  } catch (error) {
    displayError(`An error occurred: ${error}`);
  }
}

main();
