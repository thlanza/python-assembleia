const axios = require("axios");
const json2csv = require('json2csv').parse;
const transform = require('camaro')

const template = {
  resu
}

axios.get("https://dadosabertos.almg.gov.br/ws/pronunciamentos/pesquisa/direcionada?ini=20190101&fim=20211231&tp=100")
  .then((res) => {
    const result = transform(xml, res.data);
    const csv = json2csv(result.data);
    fs.writeFile('parte1.csv', csv, 'utf8', function (err) {
      if (err) {
        console.log('Some error occured - file either not saved or corrupted file saved.');
      } else{
        console.log('It\'s saved!');
      }
    });
  })
  .catch((err) => console.log(err))

  for (i = 2; i < 47; i++) {
  axios.get(`https://dadosabertos.almg.gov.br/ws/pronunciamentos/pesquisa/direcionada?ini=20190101&fim=20211231&tp=100&p=${i}`)
  .then((res) => {
    const result = transform(xml, res.data);
    const csv = json2csv(result.data);
    fs.writeFile(`parte${i}.csv`, csv, 'utf8', function (err) {
      if (err) {
        console.log('Some error occured - file either not saved or corrupted file saved.');
      } else{
        console.log('It\'s saved!');
      }
    });
  })
  .catch((err) => console.log(err))
  }





  