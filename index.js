classes = JSON.parse()
var fs = require("fs");

fs.readFile("classdata.json", function (err, data) {
    if (err) throw err;
    console.log(data.toString());
});

function createClassStrings() {
  classStrings = {};
  Object.keys(classes).forEach(quarter => {
    Object.keys(classes[quarter]).forEach(classId => {
      const classData = classes[quarter][classId];
      const prefix = quarter == 'current' ? '' : quarter + ' ';
      if (!classData.name) return console.log('Could not find name for class', classData);
      if (!classStrings[prefix + classData.name.toLowerCase()]) classStrings[prefix + classData.name.toLowerCase()] = classData;
      const nameArr = classData.fullName.split(' ').slice(0, 4);

      classStrings[prefix + nameArr.join(' ').toLowerCase()] = classData;
      classStrings[prefix + nameArr.join(' ').toLowerCase().replace(' -', '')] = classData;

      if (parseInt(nameArr[3]) < 10) {
        classStrings[prefix + classData.name.toLowerCase() + ' - ' + nameArr[3].slice(1)] = classData;
        classStrings[prefix + classData.name.toLowerCase() + ' ' + nameArr[3].slice(1)] = classData;
      }
    });
  });
console.log(classStrings)
}

createClassStrings();