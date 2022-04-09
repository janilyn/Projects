//updates the date everytime someone opens the file
function onOpen(e){
  UpdateConfirmationDL();
}

function UpdateConfirmationDL() {
  var body = DocumentApp.getActiveDocument().getBody();
  
  //searches the paragraph containing the phrase
  var search = body.findText("We would appreciate it if we could receive your response by ");
  var searchElement = search.getElement();

  //deletes the previous date
  var insertstartindex = search.getEndOffsetInclusive() + 1;
  var searchendex = searchElement.getText().length-2;
  searchElement.editAsText().deleteText(insertstartindex, searchendex);

  //inserts the new date in the place of the previous one
  var date2weeks = new Date(new Date().getTime() + 14 * 24 * 60 * 60 * 1000);
  var date = Utilities.formatDate(date2weeks, "GMT+8", "MMMM d, yyyy");
  searchElement.insertText(insertstartindex,date);
  
  //changes the style of the date
  var searchendex = searchElement.getText().length-2;
  searchElement.setBold(insertstartindex,searchendex,true);
}
