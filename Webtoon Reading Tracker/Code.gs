//Accesses GSheets API to add a custom menu which will run the scripts
function onOpen(){
  var ui = SpreadsheetApp.getUi()
  var menu = ui.createMenu("Custom")
  var item = menu.addItem("Sort", "initSort")
  var item2 = menu.addItem("Format", "changeFormat")
  item.addToUi()
}

//Function that performs multi-parameter sorts to the active sheet
function initSort(){
  const currentSheet = SpreadsheetApp.getActiveSheet()
  const currentSheetName = currentSheet.getSheetName()
  
  const range = currentSheet.getRange(2,1,currentSheet.getLastRow()-1,currentSheet.getLastColumn())

  //types of sheet
  var sheettype1 = ["Favorites", "Romance", "Family"]
  var sheettype2 = ["Modern"]

  //sorting each sheet type
  if(sheettype1.indexOf(currentSheetName) != -1){
    range.sort(1)
    range.sort({column:7, ascending: false})
    range.sort({column:9, ascending: false})
    return
  }
  else if(sheettype2.indexOf(currentSheetName) != -1){
    range.sort(2)
    range.sort(1)
    range.sort({column:8, ascending: false})
    range.sort({column:10, ascending: false})
    return
  }
}

// Applies style to the table in the active sheet. Responsible for setting the borders of the table
function changeFormat(){
  const currentSheet = SpreadsheetApp.getActiveSheet()
  const currentSheetName = currentSheet.getSheetName()
  const header = currentSheet.getRange(1,1,1,currentSheet.getLastColumn())
  const whole = currentSheet.getRange("A1:NH")
  const range = currentSheet.getRange(2,1,currentSheet.getLastRow()-1,currentSheet.getLastColumn())

  whole.setBorder(false,false,false,false,false,false)
  range.setBorder(true,true,true,true,true,false)
  header.setBorder(true,true,true,true,true,false)
  
  //types of sheet
  var sheettype1 = ["Favorites", "Romance", "Family"]
  var sheettype2 = ["Modern"]

  //sorting each sheet type
  if(sheettype1.indexOf(currentSheetName) != -1){
    sheettype1Style(range,currentSheet)
  }
}

//A sub function of changeFormat() which fixes the font style and applies conditional formatting to all the rows in the rightmost column
function sheettype1Style(range,currentSheet){
  range.setBackground('white')
  range.setFontFamily('Arial')
  range.setFontSize('10')

  const info = currentSheet.getRange(2,1,currentSheet.getLastRow()-1,5)
  info.setFontColor('black')

  const chap = currentSheet.getRange(2,3,currentSheet.getLastRow()-1,2)
  chap.setHorizontalAlignment("center")

  const links = currentSheet.getRange(2,6,currentSheet.getLastRow()-1,1)
  links.setFontColor('#1155cc')

  const checkboxes = currentSheet.getRange(2,7,currentSheet.getLastRow()-1,2)
  checkboxes.setFontColor('#808080')

  currentSheet.clearConditionalFormatRules()

  var rules = [];
  rules.push(createRule(currentSheet, "Ongoing", "#b7e1cd"));
  rules.push(createRule(currentSheet, "Hiatus", "#fce8b2"));
  rules.push(createRule(currentSheet, "Finished", "#d9d9d9"));
  currentSheet.setConditionalFormatRules(rules);
}

// Creates the conditional format rule that sheettype1Style() is using
function createRule(currentSheet, text, color){
  const status = currentSheet.getRange(2,9,currentSheet.getLastRow()-1,1)
  var rule = SpreadsheetApp.newConditionalFormatRule()
      .whenTextContains(text)
      .setBackground(color)
      .setRanges([status])
      .build();
  return rule

}
