var request = require('request');
var cheerio = require('cheerio');

var url = 'http://timescineplex.com/schedule/';

request(url, function(err, resp, body){
  if (err) {
    throw err;
  }
  $ = cheerio.load(body);
  $('.movie-sched-outer').each(function() {
    $(this).find('.movie-title').each(function() {
      console.log('Title: ' + $(this).text());
    });
    $(this).find('.movie-poster').each(function() {
      posterURL = $(this).find('a').attr('href');
      console.log('Poster: ' + posterURL);
    });
    $(this).find('.movie-poster').each(function() {
      miniPosterURL = $(this).find('img').attr('src');
      console.log('Poster: ' + miniPosterURL);
    });
    $(this).find('.table-col-1').each(function() {
      date = $(this).find('.textwidget').text();
      movTime = $(this).find('.table-contents').text().trim();
      console.log('Date: ' + date);
      console.log('Time: ' + movTime);
    });
    $(this).find('.table-col-2').each(function() {
      date = $(this).find('.textwidget').text();
      movTime = $(this).find('.table-contents').text().trim();
      console.log('Date: ' + date);
      console.log('Time: ' + movTime);
    });
    $(this).find('.table-col-3').each(function() {
      date = $(this).find('.textwidget').text();
      movTime = $(this).find('.table-contents').text().trim();
      console.log('Date: ' + date);
      console.log('Time: ' + movTime);
    });
    $(this).find('.table-col-4').each(function() {
      date = $(this).find('.textwidget').text();
      movTime = $(this).find('.table-contents').text().trim();
      console.log('Date: ' + date);
      console.log('Time: ' + movTime);
    });
    $(this).find('.table-col-5').each(function() {
      date = $(this).find('.textwidget').text();
      movTime = $(this).find('.table-contents').text().trim();
      console.log('Date: ' + date);
      console.log('Time: ' + movTime);
    });
    $(this).find('.table-col-6').each(function() {
      date = $(this).find('.textwidget').text();
      movTime = $(this).find('.table-contents').text().trim();
      console.log('Date: ' + date);
      console.log('Time: ' + movTime);
    });
    $(this).find('.table-col-7').each(function() {
      date = $(this).find('.textwidget').text();
      movTime = $(this).find('.table-contents').text().trim();
      console.log('Date: ' + date);
      console.log('Time: ' + movTime);
    });
  });
});