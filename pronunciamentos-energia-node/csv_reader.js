const fs = require('fs'); 

const csv = require('fast-csv');


var stream = fs.createReadStream('pronunciamentos.csv', {
  encoding: 'utf8'
});

stream.once('readable', function () {
  // Read through the stream until we encounter a new line
  var chunk;
  while (null !== (chunk = stream.read(1))) {
    if (chunk === '\n')
      break;
  }

  // Then do the CSV parsing
  const csvStream = csv
    .fromStream(stream,
      {
        headers: true,
        delimiter: ',',
        rowDelimiter: '\n',
        quoteHeaders: false,
        quoteColumns: false
      })
    .on("data", data => {
      // i do something with datas
      console.log('data', data);
    })
    .on("data-invalid", data => {
      console.log('invalid data', data);
    })
    .on("error", error => {
      console.log("Le fichier CSV est invalide !", error);
    })
    .on("end", data => {
      console.log("End of parsing");
      console.log(data);
    });
});