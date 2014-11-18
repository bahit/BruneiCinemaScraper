var request = require('request');
var cheerio = require('cheerio');

var url = 'http://timescineplex.com/schedule/';

request(url, function(err, resp, body){
  console.log('** Getting data from Times Cineplex.. **');
  
  if (err) {
    throw err;
  }
  $ = cheerio.load(body);
  console.log('** Getting data from Times Cineplex Schedule.. **');
  
  $('#time-quare').each(function() {
    $(this).find('.movie-show-panel').each(function() {
      $(this).find('h4').each(function() {
        console.log('Title: ' + $(this).text());   
      });
      $(this).find('img').each(function() {
        posterURL = $(this).attr('src');
        console.log('Poster: ' + posterURL);
      });
      $(this).find('.boxes').each(function() {
        date = $(this).find('.day').text();
        time = $(this).find('.time').text().trim();
        console.log('Date: ' + date);
        console.log('Time: ' + time);
      });
    });
    
  });

  console.log('** Getting data from Empire Schedule.. **');
  
  $('#empire-hotel').each(function() {
    $(this).find('.movie-show-panel').each(function() {
      $(this).find('h4').each(function() {
        console.log('Title: ' + $(this).text());   
      });
      $(this).find('img').each(function() {
        posterURL = $(this).attr('src');
        console.log('Poster: ' + posterURL);
      });
      $(this).find('.boxes').each(function() {
        date = $(this).find('.day').text();
        time = $(this).find('.time').text().trim();
        console.log('Date: ' + date);
        console.log('Time: ' + time);
      });
    });
    
  });

  console.log('** Getting data from Tutong Schedule.. **');
  
  $('#tutong').each(function() {
    $(this).find('.movie-show-panel').each(function() {
      $(this).find('h4').each(function() {
        console.log('Title: ' + $(this).text());   
      });
      $(this).find('img').each(function() {
        posterURL = $(this).attr('src');
        console.log('Poster: ' + posterURL);
      });
      $(this).find('.boxes').each(function() {
        date = $(this).find('.day').text();
        time = $(this).find('.time').text().trim();
        console.log('Date: ' + date);
        console.log('Time: ' + time);
      });
    });
    
  });
  console.log('** Finished processing Times Cineplex. **');
});

var url2 = 'http://www.mall-ticket.com/visShowtimes.aspx';

request(url2, function(err, resp, body){
  console.log('** Getting data from The Mall Cineplex.. **');
  
  if (err) {
    throw err;
  }
  $ = cheerio.load(body);
  $('.ShowtimesSummaryRow').each(function() {
    $(this).find('.ShowtimesMovieLink').each(function() {
      console.log('Title: ' + $(this).text());
    });
    // $(this).find('.movie-poster').each(function() {
    //   posterURL = $(this).find('a').attr('href');
    //   console.log('Poster: ' + posterURL);
    // });
    // $(this).find('.movie-poster').each(function() {
    //   miniPosterURL = $(this).find('img').attr('src');
    //   console.log('Poster: ' + miniPosterURL);
    // });
    $('.ShowtimesFilterDropDownList').each(function() {
      console.log('Date: ' + $(this).text().trim());
    });
    console.log('Time: ');
    $(this).find('.ShowtimesSessionLink').each(function() {
      console.log('Time: ' + $(this).text());
    });
  });
  $('.ShowtimesSummaryRowAlt').each(function() {
    $(this).find('.ShowtimesMovieLink').each(function() {
      console.log('Title: ' + $(this).text());
    });
    // $(this).find('.movie-poster').each(function() {
    //   posterURL = $(this).find('a').attr('href');
    //   console.log('Poster: ' + posterURL);
    // });
    // $(this).find('.movie-poster').each(function() {
    //   miniPosterURL = $(this).find('img').attr('src');
    //   console.log('Poster: ' + miniPosterURL);
    // });
    $('.ShowtimesFilterDropDownList').each(function() {
      console.log('Date: ' + $(this).text().trim());
    });
    console.log('Time: ');
    $(this).find('.ShowtimesSessionLink').each(function() {
      console.log($(this).text());
    });
  });

  console.log('** Finished processing The Mall Cineplex. **');

});