class performance {
  constructor(name, place, showtime) {
    this.name = name;
    this.place = place;
    this.showtime = showtime;
    this.date = showtime.split(" ")[0].split('/');
    this.year = parseInt(this.date[2]);
    this.month = parseInt(this.date[1])-1;
    if (this.month == 0) 
      this.month = 12;
    this.day = parseInt(this.date[0]);
  }
}

const performance1 = new performance("이무진", "신촌역 2번 출구", "30/05/2022 17:25");
const performance2 = new performance("이무진", "신촌 명품거리 김가네 앞", "20/05/2022 22:25");
const performance3 = new performance("잔나비", "홍대입구역 2번 출구", "30/05/2022 20:25");

var events = [
  {'Date': new Date(performance1.year, performance1.month, performance1.day), 'Title': performance1.name + " " + performance1.place, 'Link': 'https://garfield.com'},
  {'Date': new Date(performance2.year, performance2.month, performance2.day), 'Title': performance2.name + " " + performance2.place, 'Link': 'https://garfield.com'},
  {'Date': new Date(performance3.year, performance3.month, performance3.day), 'Title': performance3.name + " " + performance3.place, 'Link': 'https://garfield.com'}
];


var settings = {};
var element = document.getElementById('caleandar');
caleandar(element, events, settings);
